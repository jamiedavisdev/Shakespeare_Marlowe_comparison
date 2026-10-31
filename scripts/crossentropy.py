"""Language-model cross-entropy test.

For each held-out play, build a character n-gram language model (Witten-Bell interpolation,
order 6) for every candidate author from that author's *other* plays, and measure the held-out
play's cross-entropy (bits per character) under each model.  Lower = the model finds the text
less surprising.  This is the behavioural version of "train one model per author and compare":
we compare what the models predict rather than their parameters.

Training data for Marlowe, Shakespeare-early, Shakespeare-later and Shakespeare-all is truncated to
the same character budget so that model size does not drive the result.
"""
import json, re, pathlib, collections, math, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
CORPUS = os.environ.get('CORPUS', 'main')   # main = Folger/EMED corpus; ep = all-EarlyPrint corpus
CLEAN = ROOT / 'data' / ('clean' if CORPUS == 'main' else 'clean_' + CORPUS)
RESROOT = ROOT / 'results' / ('' if CORPUS == 'main' else CORPUS)
VARIANT = sys.argv[1] if len(sys.argv) > 1 else 'plain'      # plain | masked
RES = RESROOT / ('crossentropy' if VARIANT == 'plain' else 'crossentropy_masked')
RES.mkdir(parents=True, exist_ok=True)
FAMILIES = [{'1H6', '2H6', '3H6', 'R3', 'TTR3'}, {'1Tam', '2Tam'}, {'Shr', 'AShrew'}, {'ST', 'Soliman'}]
def related(wid):
    if VARIANT == 'plain':
        return {wid}
    for f in FAMILIES:
        if wid in f:
            return f
    return {wid}
ORDER = 6                       # context length 5 -> 6-grams
WORD_RE = re.compile(r"[a-z]+(?:['\-][a-z]+)*")

manifest = json.loads((CLEAN / 'manifest.json').read_text())
WORKS = {w['id']: w for w in manifest if w['group'] != 'altsource'}
IDS = list(WORKS)

CAP_RE = re.compile(r"[A-Za-z]+(?:['\-][A-Za-z]+)*")
def proper_nouns(raw):
    """Token types that are capitalised in >=90% of their non-line-initial occurrences (>=3 of them)."""
    cap = collections.Counter(); tot = collections.Counter()
    for line in raw.splitlines():
        toks = CAP_RE.findall(line)
        for t in toks[1:]:
            tot[t.lower()] += 1
            if t[0].isupper():
                cap[t.lower()] += 1
    return {w for w, n in tot.items() if n >= 3 and cap[w] / n >= 0.9 and not (w == 'i' or w.startswith("i'"))}

def text_of(wid):
    raw = (CLEAN / f'{wid}.txt').read_text()
    if VARIANT == 'masked':
        names = proper_nouns(raw)
        toks = ['~' if t in names else t for t in WORD_RE.findall(raw.lower())]
    else:
        toks = WORD_RE.findall(raw.lower())
    return ' ' + ' '.join(toks) + ' '

TEXT = {w: text_of(w) for w in IDS}
ALPHABET = sorted(set(''.join(TEXT.values())))
V = len(ALPHABET)

def ngram_counts(s):
    """counts[k] : Counter of (context, char) for context length k, k=0..ORDER-1"""
    counts = [collections.Counter() for _ in range(ORDER)]
    for k in range(ORDER):
        c = counts[k]
        for i in range(k, len(s)):
            c[s[i - k:i + 1]] += 1
    return counts

PLAY_COUNTS = {}
def play_counts(wid):
    if wid not in PLAY_COUNTS:
        PLAY_COUNTS[wid] = ngram_counts(TEXT[wid])
    return PLAY_COUNTS[wid]

class WBModel:
    """Witten-Bell interpolated char model built from summed n-gram counters."""
    def __init__(self, counts):
        self.counts = counts
        # per context: total count and number of distinct continuations
        self.ctx_total = [collections.Counter() for _ in range(ORDER)]
        self.ctx_types = [collections.Counter() for _ in range(ORDER)]
        for k in range(ORDER):
            for g, n in counts[k].items():
                self.ctx_total[k][g[:-1]] += n
                self.ctx_types[k][g[:-1]] += 1
    def prob(self, s, i):
        p = 1.0 / V
        for k in range(ORDER):
            if i - k < 0:
                break
            ctx = s[i - k:i]
            tot = self.ctx_total[k].get(ctx, 0)
            if tot == 0:
                break
            typ = self.ctx_types[k][ctx]
            c = self.counts[k].get(s[i - k:i + 1], 0)
            lam = tot / (tot + typ)
            p = lam * c / tot + (1 - lam) * p
        return p
    def cross_entropy(self, s):
        return -sum(math.log2(self.prob(s, i)) for i in range(len(s))) / len(s)

def build(train_ids, budget=None):
    """Sum per-play counters; if budget (chars) given, truncate concatenated text instead."""
    if budget is None:
        total = [collections.Counter() for _ in range(ORDER)]
        for w in train_ids:
            pc = play_counts(w)
            for k in range(ORDER):
                total[k].update(pc[k])
        return WBModel(total), sum(len(TEXT[w]) for w in train_ids)
    # budget: equal share of characters from every training play (so no play or sub-period dominates)
    share = budget // len(train_ids)
    s = ''.join(TEXT[w][:share] for w in train_ids)
    return WBModel(ngram_counts(s)), len(s)

AUTHORS = collections.defaultdict(list)
for w in IDS:
    AUTHORS[WORKS[w]['author']].append(w)
SH_EARLY = [w for w in IDS if WORKS[w]['group'] == 'shakespeare_early']
SH_LATER = [w for w in IDS if WORKS[w]['group'] == 'shakespeare_later']
MARLOWE = AUTHORS['Marlowe']
GREENE = AUTHORS['Greene']
PEELE = AUTHORS['Peele']
ANON = [w for w in ['Soliman', 'Locrine', 'Selimus', 'TRKJ', 'JackStraw', 'EdwardIII', 'Arden', 'TTR3'] if w in WORKS]
MATCHED = ['Marlowe', 'Sh-early', 'Sh-later', 'Sh-all', 'Greene', 'Peele', 'Anon-heroic']

# character budget = Marlowe corpus minus its largest play (the smallest Marlowe training set we'll ever use)
BUDGET = min(sum(len(TEXT[w]) for w in GREENE), sum(len(TEXT[w]) for w in PEELE))

def main():
    print(f'variant={VARIANT} alphabet={V} order={ORDER} budget={BUDGET} chars', flush=True)
    if VARIANT == 'masked':
        print('masked names in 2H6:', sorted(proper_nouns((CLEAN / '2H6.txt').read_text()))[:40], flush=True)
    model_names = MATCHED + ['Fletcher', 'Ford', 'Kyd', 'Lodge', 'Lyly', 'Anon-AShrew', 'Anon-Leir', 'Dekker', 'Middleton', 'Beaumont']
    rows = {}
    for held in IDS:
        row = {}
        def tr(ids):
            return [w for w in ids if w not in related(held)]
        sets = {
            'Marlowe': (tr(MARLOWE), BUDGET), 'Sh-early': (tr(SH_EARLY), BUDGET), 'Sh-later': (tr(SH_LATER), BUDGET),
            'Sh-all': (tr(SH_EARLY + SH_LATER), BUDGET), 'Greene': (tr(GREENE), BUDGET), 'Peele': (tr(PEELE), BUDGET), 'Anon-heroic': (tr(ANON), BUDGET),
            'Fletcher': (tr(AUTHORS['Fletcher']), None), 'Ford': (tr(AUTHORS['Ford']), None),
        }
        for a in ['Kyd', 'Lodge', 'Lyly', 'Anon-AShrew', 'Anon-Leir', 'Dekker', 'Middleton', 'Beaumont']:
            sets[a] = (tr(AUTHORS.get(a, [])), None)
        for name, (ids, budget) in sets.items():
            if not ids:
                row[name] = (float('nan'), 0); continue
            m, n = build(ids, budget)
            row[name] = (m.cross_entropy(TEXT[held]), n)
        rows[held] = row
        print(f"{held:8s} " + ' '.join(f"{name}={row[name][0]:.3f}" for name in ['Marlowe', 'Sh-early', 'Sh-later', 'Greene', 'Peele', 'Anon-heroic']), flush=True)

    # ---- write results
    out = ['# Cross-entropy of each play under character-level author models (bits/char, lower = more predictable)\n',
           f'Order-{ORDER} Witten-Bell character models. Variant: {VARIANT} (masked = proper nouns replaced by a placeholder, and plays sharing plot/characters excluded from training together). The held-out play is never in training. '
           f'Marlowe, Sh-early, Sh-later, Sh-all, Greene, Peele and Anon-heroic models are truncated to {BUDGET:,} characters (= the smaller of the Greene and Peele corpora) '
           'so they are the same size, drawing an equal share of characters from each training play; Fletcher (3 plays), Ford (2) and the single-play controls are smaller, so their entropies are biased upward and are listed for reference only.\n',
           '| held-out play | author | ' + ' | '.join(model_names) + ' | best size-matched model | Marlowe − Sh-all |',
           '|---|---|' + '---|' * len(model_names) + '---|---|']
    matched = MATCHED
    for held in IDS:
        r = rows[held]
        if any(math.isnan(r[m][0]) for m in model_names): pass
        cands = {k: r[k][0] for k in matched if not math.isnan(r[k][0])}
        best = min(cands, key=cands.get)
        diff = r['Marlowe'][0] - r['Sh-all'][0]
        out.append(f"| {held} | {WORKS[held]['author']} | " + ' | '.join(('-' if math.isnan(r[m][0]) else f'{r[m][0]:.3f}') for m in model_names) + f' | **{best}** | {diff:+.3f} |')

    # ---- benchmark summary
    def mean_diff(ids, a, b):
        return np.mean([rows[w][a][0] - rows[w][b][0] for w in ids])
    out.append('\n## Summary: mean cross-entropy gap (bits/char) for groups of held-out plays\n')
    out.append('Positive = the Marlowe model finds these plays *more* surprising than the Shakespeare model does.\n')
    out.append('| held-out group | H(Marlowe) − H(Sh-all) | H(Marlowe) − H(Sh-early) | H(Marlowe) − H(Sh-later) | H(Sh-early) − H(Sh-later) |')
    out.append('|---|---|---|---|---|')
    groups = [('Marlowe plays', MARLOWE), ('Shakespeare early', SH_EARLY), ('Shakespeare early, Henry VI excluded', [w for w in SH_EARLY if 'H6' not in w]),
              ('Henry VI 1-3', [w for w in ['1H6', '2H6', '3H6'] if w in WORKS]), ('Shakespeare later', SH_LATER),
              ('early controls (Kyd, Peele, Lyly, A Shrew, Leir)', [w for w in ['ST', 'OWT', 'Gal', 'AShrew', 'TCKL'] if w in WORKS]),
              ('later controls (Dekker, Middleton, Beaumont)', [w for w in ['ShoeHol', 'RT', 'KBP'] if w in WORKS]), ('Fletcher', AUTHORS.get('Fletcher', [])), ('Ford', AUTHORS.get('Ford', [])),
              ('Greene', GREENE), ('Peele', PEELE), ('Lodge', AUTHORS.get('Lodge', [])), ('anonymous heroic/history 1587-94', ANON)]
    groups = [(n, ids) for n, ids in groups if ids]
    for name, ids in groups:
        out.append(f"| {name} | {mean_diff(ids, 'Marlowe', 'Sh-all'):+.3f} | {mean_diff(ids, 'Marlowe', 'Sh-early'):+.3f} | {mean_diff(ids, 'Marlowe', 'Sh-later'):+.3f} | {mean_diff(ids, 'Sh-early', 'Sh-later'):+.3f} |")

    out.append('\n## Reading guide\n')
    out.append('* Same-author benchmark: how much lower is H under the author\'s own (other-plays) model than under a different author\'s? '
               'For Shakespeare-early plays, compare H(Sh-later) [same author, different period] with H(Marlowe) [the hypothesis]. '
               'If Marlowe wrote early Shakespeare, H(Marlowe) should be about as low as H(Sh-later) for those plays, and lower than it is for the control plays.\n')
    (RES / 'crossentropy.md').write_text('\n'.join(out) + '\n')
    json.dump({'matched': MATCHED, 'rows': {h: {k: v[0] for k, v in r.items()} for h, r in rows.items()}}, open(RES / 'crossentropy.json', 'w'), indent=1)
    print('done')

if __name__ == '__main__':
    main()
