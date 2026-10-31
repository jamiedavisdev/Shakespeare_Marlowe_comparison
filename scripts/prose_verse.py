"""Verse-only (and prose-only) rescoring of the Henry VI scenes.

Marlowe's verse/prose lines come from EMED's line milestones (ana="#verse" / "#prose").
Shakespeare's come from the Folger layout: prose speeches carry the speaker label inline
("CADE  We, John Cade..."), verse speeches put the label on its own line. One-line inline speeches are
ambiguous and are dropped from training.
"""
import json, re, pathlib, collections, math, sys
import numpy as np
import xml.etree.ElementTree as ET
from sklearn.linear_model import LogisticRegression
sys.argv = ['x']
import importlib.util
ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ss', ROOT / 'scripts' / 'scene_scan.py'); ss = importlib.util.module_from_spec(spec); spec.loader.exec_module(ss)
RES = ROOT / 'results' / 'scene_scan'
manifest = ss.manifest
local = lambda t: t.split('}', 1)[-1]

# ---------------- EMED: words on verse vs prose lines
def emed_by_mode(wid):
    root = ET.parse(ROOT / manifest[wid]['file']).getroot()
    mode_of = {}
    for m in root.iter():
        if local(m.tag) == 'milestone' and m.get('unit') == 'wln':
            mode = 'prose' if '#prose' in (m.get('ana') or '') else 'verse'
            for ref in (m.get('corresp') or '').split():
                mode_of[ref.lstrip('#')] = mode
    out = {'verse': [], 'prose': []}
    body = next(e for e in root.iter() if local(e.tag) == 'body')
    for sp in body.iter():
        if local(sp.tag) != 'sp': continue
        for el in sp.iter():
            t = local(el.tag)
            if t == 'w':
                anc = False
                mode = mode_of.get(el.get('{http://www.w3.org/XML/1998/namespace}id'), 'verse')
                # pick EMED regularised form
                regs = [(r.get('resp', ''), ''.join(r.itertext())) for r in el.iter() if local(r.tag) == 'reg']
                txt = next((x for resp, x in regs if 'EMED' in resp), regs[0][1] if regs else ''.join(el.itertext()))
                out[mode].append(txt)
    return {k: ' '.join(v) for k, v in out.items()}

# ---------------- Folger: speeches with prose/verse flag, by scene
SPEAKER_INLINE = re.compile(r"^([A-Z][A-Z0-9' .,\-]*[A-Z0-9.])\s{2,}(\S.*)$")
SPEAKER_ALONE = re.compile(r"^([A-Z][A-Z0-9' .,\-]*[A-Z0-9.])\s*$")
def folger_speeches(wid):
    raw = (ROOT / manifest[wid]['file']).read_text(encoding='utf-8')
    lines = raw.splitlines()
    start = next(i for i, l in enumerate(lines) if ss.START_RE.match(l))
    text = re.sub(r'\[[^\]]*\]', ' ', '\n'.join(lines[start:]), flags=re.S)
    speeches = []; act = sc = 0; key = None; cur = None
    def flush():
        nonlocal cur
        if cur and cur['lines']:
            n = len(cur['lines'])
            if cur['inline'] and n == 1 and len(cur['lines'][0].split()) < 12:
                cur['mode'] = 'ambiguous'
            else:
                cur['mode'] = 'prose' if cur['inline'] else 'verse'
            speeches.append(cur)
        cur = None
    for line in text.splitlines():
        s = line.strip()
        if not s or re.fullmatch(r'=+', s):
            continue
        m = re.match(r'^ACT (\d+)$', s)
        if m: flush(); act = int(m.group(1)); continue
        m = re.match(r'^Scene (\d+)$', s)
        if m: flush(); sc = int(m.group(1)); key = f'{act}.{sc}'; continue
        if s in ('INDUCTION', 'PROLOGUE', 'EPILOGUE', 'CHORUS', 'FINIS'):
            flush(); key = s.lower(); continue
        m = SPEAKER_INLINE.match(line.rstrip())
        if m: flush(); cur = {'scene': key, 'inline': True, 'lines': [m.group(2).strip()]}; continue
        m = SPEAKER_ALONE.match(line.rstrip())
        if m: flush(); cur = {'scene': key, 'inline': False, 'lines': []}; continue
        if cur is None: cur = {'scene': key, 'inline': False, 'lines': []}
        cur['lines'].append(s)
    flush()
    return speeches

def main():
    marlowe = [w for w in manifest if manifest[w]['group'] == 'marlowe']
    shakes = [w for w in manifest if manifest[w]['author'] == 'Shakespeare' and manifest[w]['group'] != 'altsource' and w not in ss.FAMILY]
    M = {w: emed_by_mode(w) for w in marlowe}
    S = {}
    for w in shakes:
        sp = folger_speeches(w)
        S[w] = {m: '\n'.join(' '.join(x['lines']) for x in sp if x['mode'] == m) for m in ('verse', 'prose')}
    stats = ['| set | verse words | prose words |', '|---|---|---|']
    for name, D in (('Marlowe', M), ('Shakespeare (non-H6 family)', S)):
        stats.append(f"| {name} | {sum(len(ss.tokens(D[w]['verse'])) for w in D)} | {sum(len(ss.tokens(D[w]['prose'])) for w in D)} |")
    print('\n'.join(stats), flush=True)

    def build_scorers(mode):
        MT = {w: M[w][mode] for w in marlowe if len(ss.tokens(M[w][mode])) > 300}
        ST = {w: S[w][mode] for w in shakes if len(ss.tokens(S[w][mode])) > 300}
        NAMES = {w: ss.proper_nouns(t) for w, t in {**MT, **ST}.items()}
        X, y = [], []
        for w, t in MT.items():
            for c in ss.chunks(ss.tokens(t), 1500): X.append(ss.fw_vec(c)); y.append(1)
        for w, t in ST.items():
            for c in ss.chunks(ss.tokens(t), 1500): X.append(ss.fw_vec(c)); y.append(0)
        X = np.array(X); mu = X.mean(0); sd = X.std(0); sd[sd == 0] = 1
        clf = LogisticRegression(C=0.1, class_weight='balanced', max_iter=5000).fit((X - mu) / sd, np.array(y))
        mc = {w: ss.masked_chars(t, NAMES[w]) for w, t in MT.items()}; sc_ = {w: ss.masked_chars(t, NAMES[w]) for w, t in ST.items()}
        budget = min(sum(len(v) for v in mc.values()), sum(len(v) for v in sc_.values()))
        def build(D):
            share = budget // len(D); return ss.WB(''.join(v[:share] for v in D.values()))
        print(f'{mode}: Marlowe {len(MT)} plays, Shakespeare {len(ST)} plays, char budget {budget}', flush=True)
        return clf, mu, sd, build(mc), build(sc_)

    scorers = {m: build_scorers(m) for m in ('verse', 'prose')}
    out = ['# Henry VI scenes rescored with verse-only and prose-only models\n',
           'Marlowe verse/prose from EMED line markup; Shakespeare verse/prose from Folger speech layout. '
           'Models trained on Marlowe vs Shakespeare (Henry VI family excluded) *within one mode*, so a prose scene is judged against prose models and a verse scene against verse models. '
           'ΔH = H(Marlowe) − H(Shakespeare) bits/char, negative favours Marlowe. The Marlowe prose corpus is small (mostly Faustus and the Jew of Malta), so prose-mode numbers are weak.\n', '\n'.join(stats), '']
    summary = []
    for play in ['1H6', '2H6', '3H6']:
        sp = folger_speeches(play); names = ss.proper_nouns((ROOT / 'data' / 'clean' / f'{play}.txt').read_text())
        out.append(f'\n## {manifest[play]["title"]}\n')
        out.append('| scene | verse words | P(M) verse | ΔH verse | prose words | P(M) prose | ΔH prose | published |'); out.append('|---|---|---|---|---|---|---|---|')
        rows = []
        for scene in dict.fromkeys(x['scene'] for x in sp):
            if scene is None: continue
            row = {'scene': scene, 'prior': ss.SCENE_PRIORS.get(play, {}).get(scene, '')}
            for mode in ('verse', 'prose'):
                t = '\n'.join(' '.join(x['lines']) for x in sp if x['scene'] == scene and x['mode'] == mode)
                toks = ss.tokens(t); row[mode + '_n'] = len(toks)
                if len(toks) >= 150:
                    clf, mu, sd, Mm, Sm = scorers[mode]
                    row[mode + '_p'] = float(clf.predict_proba(((ss.fw_vec(toks) - mu) / sd).reshape(1, -1))[0, 1])
                    s_ = ss.masked_chars(t, names); row[mode + '_dh'] = Mm.H(s_) - Sm.H(s_)
                else:
                    row[mode + '_p'] = row[mode + '_dh'] = float('nan')
            rows.append(row)
            f = lambda v, fmt: '-' if (isinstance(v, float) and math.isnan(v)) else format(v, fmt)
            out.append(f"| {scene} | {row['verse_n']} | {f(row['verse_p'], '.2f')} | {f(row['verse_dh'], '+.3f')} | {row['prose_n']} | {f(row['prose_p'], '.2f')} | {f(row['prose_dh'], '+.3f')} | {row['prior']} |")
        by = collections.defaultdict(list)
        for r in rows: by[r['prior'] or '(none)'].append(r)
        out.append('')
        for prior, v in by.items():
            for mode in ('verse', 'prose'):
                vv = [r for r in v if not math.isnan(r[mode + '_p'])]
                if not vv: continue
                n = sum(r[mode + '_n'] for r in vv)
                wp = sum(r[mode + '_n'] * r[mode + '_p'] for r in vv) / n; wdh = sum(r[mode + '_n'] * r[mode + '_dh'] for r in vv) / n
                out.append(f'* **{prior}**, {mode} only: {len(vv)} scenes, {n} words, P(Marlowe) = {wp:.2f}, ΔH = {wdh:+.3f}')
                summary.append((play, prior, mode, n, round(wp, 2), round(wdh, 3)))
    (RES / 'prose_verse.md').write_text('\n'.join(out) + '\n')
    for s_ in summary: print(s_)

if __name__ == '__main__':
    main()
