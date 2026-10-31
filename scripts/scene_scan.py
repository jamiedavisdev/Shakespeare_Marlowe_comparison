"""Scene-level Marlowe/Shakespeare scan of the Henry VI plays (and any Folger play).

Two independent scorers, both trained with the scanned play's whole family (1H6, 2H6, 3H6, R3) excluded:
  1. function-word logistic regression, Marlowe chunks vs Shakespeare chunks  -> P(Marlowe) per scene
  2. character 6-gram Witten-Bell models (proper nouns masked, size-matched)   -> H(Marlowe) - H(Shakespeare) per scene, bits/char
Scenes are compared with the published attributions recorded in SCENE_PRIORS.
"""
import json, re, pathlib, collections, math, sys
import numpy as np
from sklearn.linear_model import LogisticRegression

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLEAN = ROOT / 'data' / 'clean'
RES = ROOT / 'results' / 'scene_scan'
RES.mkdir(parents=True, exist_ok=True)
WORD_RE = re.compile(r"[a-z]+(?:['\-][a-z]+)*")
CAP_RE = re.compile(r"[A-Za-z]+(?:['\-][A-Za-z]+)*")
CHUNK = 2000
ORDER = 6
FUNCTION_WORDS = """a about above after again against all am among an and any are art as at ay be because been before
being both but by can cannot could did do does doth dost done down each either else ere even ever every few for forth from
had has hast hath have having he hence her here hers herself him himself his hither how i if in into is it its itself let
many may me might mine more most much must my myself nay neither never no none nor not nothing now of off oft often on once
one only or other our ours out over own same shall shalt she should since so some still such than that the thee their them
themselves then thence there therefore these they thine this thither those thou though through thus thy thyself till tis to
too under until unto up upon us very was we well were wert what when whence where wherefore whether which while whilst who
whom whose why will wilt with within without would ye yea yet yonder you your yours yourself""".split()
FAMILY = {'1H6', '2H6', '3H6', 'R3', 'TTR3'}
GREENE = ['Alphonsus', 'Orlando', 'FriarBacon', 'JamesIV']
PEELE = ['OWT', 'Alcazar', 'EdwardI', 'David']

# Published attributions (scene -> author) used only for comparison, never for training.
#  1H6: Taylor 1995 / New Oxford Shakespeare: Act 1 Nashe; 2.4 and 4.2-4.7 Shakespeare; the rest Marlowe (NOS) / unknown.
#  2H6: Craig & Kinney 2009: Marlowe in the Cade scenes 4.2-4.10 (strongest 4.3-4.10); NOS credits Marlowe more widely.
#  3H6: Craig & Burrows (NOS Authorship Companion) argue Marlowe involvement; no scene list recovered here.
SCENE_PRIORS = {
    '1H6': {**{f'1.{i}': 'Nashe' for i in range(1, 7)}, '2.4': 'Shakespeare', **{f'4.{i}': 'Shakespeare' for i in range(2, 8)}},
    '2H6': {**{f'4.{i}': 'Marlowe?' for i in range(2, 11)}},
    '3H6': {},
}

manifest = {w['id']: w for w in json.loads((CLEAN / 'manifest.json').read_text())}

# ---------------- Folger scene parser (same cleaning rules as build_corpus.parse_folger)
START_RE = re.compile(r'^(ACT \d+|INDUCTION|PROLOGUE|Scene \d+)\s*$')
SPEAKER_RE = re.compile(r"^([A-Z][A-Z0-9' .,\-]*[A-Z0-9.])(?:\s{2,}(.*))?$")
def folger_scenes(wid):
    raw = (ROOT / manifest[wid]['file']).read_text(encoding='utf-8')
    lines = raw.splitlines()
    start = next(i for i, l in enumerate(lines) if START_RE.match(l))
    text = re.sub(r'\[[^\]]*\]', ' ', '\n'.join(lines[start:]), flags=re.S)
    scenes = collections.OrderedDict(); act = 0; sc = 0; key = None
    for line in text.splitlines():
        s = line.strip()
        if not s or re.fullmatch(r'=+', s):
            continue
        m = re.match(r'^ACT (\d+)$', s)
        if m: act = int(m.group(1)); continue
        m = re.match(r'^Scene (\d+)$', s)
        if m: sc = int(m.group(1)); key = f'{act}.{sc}'; scenes.setdefault(key, []); continue
        if s in ('INDUCTION', 'PROLOGUE', 'EPILOGUE', 'CHORUS', 'FINIS'):
            key = s.lower(); scenes.setdefault(key, []); continue
        if key is None: continue
        m = SPEAKER_RE.match(line.rstrip())
        if m:
            if m.group(2) and m.group(2).strip(): scenes[key].append(m.group(2).strip())
            continue
        scenes[key].append(s)
    return {k: '\n'.join(v) for k, v in scenes.items() if v}

# ---------------- text helpers
def proper_nouns(raw):
    cap = collections.Counter(); tot = collections.Counter()
    for line in raw.splitlines():
        toks = CAP_RE.findall(line)
        for t in toks[1:]:
            tot[t.lower()] += 1
            if t[0].isupper(): cap[t.lower()] += 1
    return {w for w, n in tot.items() if n >= 3 and cap[w] / n >= 0.9 and not (w == 'i' or w.startswith("i'"))}
def tokens(raw): return WORD_RE.findall(raw.lower())
def masked_chars(raw, names):
    return ' ' + ' '.join('~' if t in names else t for t in WORD_RE.findall(raw.lower())) + ' '
def chunks(toks, size=CHUNK):
    out = [toks[i:i + size] for i in range(0, len(toks), size)]
    if len(out) > 1 and len(out[-1]) < size // 2: out[-2] += out[-1]; out.pop()
    return out
def fw_vec(toks):
    c = collections.Counter(toks); n = max(len(toks), 1)
    return np.array([c[w] / n * 1000 for w in FUNCTION_WORDS])

# ---------------- char model
class WB:
    def __init__(self, s):
        self.counts = [collections.Counter() for _ in range(ORDER)]
        self.tot = [collections.Counter() for _ in range(ORDER)]
        self.typ = [collections.Counter() for _ in range(ORDER)]
        for k in range(ORDER):
            c = self.counts[k]
            for i in range(k, len(s)): c[s[i - k:i + 1]] += 1
            for g, n in c.items(): self.tot[k][g[:-1]] += n; self.typ[k][g[:-1]] += 1
        self.V = 30
    def prob(self, s, i):
        p = 1.0 / self.V
        for k in range(ORDER):
            if i - k < 0: break
            ctx = s[i - k:i]; tot = self.tot[k].get(ctx, 0)
            if tot == 0: break
            lam = tot / (tot + self.typ[k][ctx])
            p = lam * self.counts[k].get(s[i - k:i + 1], 0) / tot + (1 - lam) * p
        return p
    def H(self, s): return -sum(math.log2(self.prob(s, i)) for i in range(len(s))) / len(s)

FAMILIES = [{'1H6', '2H6', '3H6', 'R3', 'TTR3'}, {'1Tam', '2Tam'}, {'Shr', 'AShrew'}, {'ST', 'Soliman'}]
def related(w):
    for f in FAMILIES:
        if w in f: return f
    return {w}

def main():
    marlowe = [w for w in manifest if manifest[w]['author'] == 'Marlowe']
    shakes_all = [w for w in manifest if manifest[w]['author'] == 'Shakespeare']
    RAW = {w: (CLEAN / f'{w}.txt').read_text() for w in marlowe + shakes_all + PEELE + GREENE}
    NAMES = {w: proper_nouns(RAW[w]) for w in RAW}
    labels = ['Marlowe', 'Shakespeare', 'Peele', 'Greene']
    cache = {}
    def scorers(play):
        """Classifier + char models trained with the scanned play's family excluded from every author."""
        excl = frozenset(related(play))
        if excl in cache: return cache[excl]
        AUTH = {'Marlowe': [w for w in marlowe if w not in excl], 'Shakespeare': [w for w in shakes_all if w not in excl],
                'Peele': [w for w in PEELE if w not in excl], 'Greene': [w for w in GREENE if w not in excl]}
        X, y = [], []
        for li, a in enumerate(labels):
            for w in AUTH[a]:
                for c in chunks(tokens(RAW[w])): X.append(fw_vec(c)); y.append(li)
        X = np.array(X); mu = X.mean(0); sd = X.std(0); sd[sd == 0] = 1
        clf = LogisticRegression(C=0.1, class_weight='balanced', max_iter=5000).fit((X - mu) / sd, np.array(y))
        budget = min(sum(len(masked_chars(RAW[w], NAMES[w])) for w in ids) for ids in AUTH.values())
        def build(ids):
            share = budget // len(ids)
            return WB(''.join(masked_chars(RAW[w], NAMES[w])[:share] for w in ids))
        print(f'building models excluding {sorted(excl)} (budget {budget} chars)...', flush=True)
        CM = {a: build(ids) for a, ids in AUTH.items()}
        cache[excl] = (clf, mu, sd, CM)
        return cache[excl]

    out = ['# Scene-level scan: Marlowe / Shakespeare / Peele / Greene\n',
           'For each scanned play the models are trained with that play and any play sharing its plot/characters excluded from every author. '
           'P(·): multinomial function-word logistic regression (trained on 2000-word chunks, applied to the whole scene). '
           'ΔH(·) = H under that author\'s char model minus H under the Shakespeare char model, bits/char, proper nouns masked; negative = that author predicts the scene better than Shakespeare does. '
           'Scenes under ~400 words are weak evidence.\n']
    summary = []
    for play in ['1H6', '2H6', '3H6', 'Tit', 'R3']:
        scenes = folger_scenes(play)
        names = proper_nouns((CLEAN / f'{play}.txt').read_text())
        clf, mu, sd, CM = scorers(play)
        out.append(f'\n## {manifest[play]["title"]}\n')
        out.append('| scene | words | P(Marlowe) | P(Shakespeare) | P(Peele) | P(Greene) | ΔH(Marlowe) | ΔH(Peele) | ΔH(Greene) | published attribution |')
        out.append('|---|---|---|---|---|---|---|---|---|---|')
        rows = []
        for sc, txt in scenes.items():
            toks = tokens(txt)
            if len(toks) < 80: continue
            pr = clf.predict_proba(((fw_vec(toks) - mu) / sd).reshape(1, -1))[0]
            s_ = masked_chars(txt, names)
            H = {a: CM[a].H(s_) for a in labels}
            dh = {a: H[a] - H['Shakespeare'] for a in ('Marlowe', 'Peele', 'Greene')}
            prior = SCENE_PRIORS.get(play, {}).get(sc, '')
            rows.append({'scene': sc, 'words': len(toks), 'P': dict(zip(labels, map(float, pr))), 'dH': dh, 'prior': prior})
            out.append(f"| {sc} | {len(toks)} | " + ' | '.join(f'{pr[labels.index(a)]:.2f}' for a in ('Marlowe', 'Shakespeare', 'Peele', 'Greene')) + ' | ' + ' | '.join(f"{dh[a]:+.3f}" for a in ('Marlowe', 'Peele', 'Greene')) + f' | {prior} |')
        by = collections.defaultdict(list)
        for r in rows: by[r['prior'] or '(none)'].append(r)
        out.append('')
        for prior, v in by.items():
            n = sum(r['words'] for r in v)
            wp = {a: sum(r['words'] * r['P'][a] for r in v) / n for a in labels}
            wdh = {a: sum(r['words'] * r['dH'][a] for r in v) / n for a in ('Marlowe', 'Peele', 'Greene')}
            out.append(f"* scenes labelled **{prior}**: {len(v)} scenes, {n} words; word-weighted P = " + ', '.join(f'{a} {wp[a]:.2f}' for a in labels) + '; ΔH = ' + ', '.join(f'{a} {wdh[a]:+.3f}' for a in wdh))
            summary.append((play, prior, n, wp, wdh))
        json.dump(rows, open(RES / f'{play}_scenes.json', 'w'), indent=1)
    (RES / 'scene_scan.md').write_text('\n'.join(out) + '\n')
    for s_ in summary: print(s_)

if __name__ == '__main__':
    main()
