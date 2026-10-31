"""Word-level comparisons: (1) which words separate two sets of plays, (2) Burrows's Zeta.

Part 1, word profiles: for each pair of play sets, the rate per 1,000 words of every function word
and every common word (present in >= 60% of plays, proper nouns removed) is computed per play, and
words are ranked by the standardised difference between the two sets (Cohen's d over play-level
rates). This answers "what does Marlowe-like actually mean".

Part 2, Zeta (Burrows 2007; Craig & Kinney 2009 variant): plays are cut into 2,000-word chunks;
for every word, zeta = share of A-chunks containing it minus share of B-chunks containing it.
The top K words each way are "markers". A chunk is placed by the share of A-markers and of
B-markers it contains. Markers are chosen with the scored play (and its family) held out, so every
plotted point is out of sample. Chunks are classified by the nearest training centroid; accuracy and
AUC are reported per pair, with the same same-author / different-author benchmarks as the other
tests. Greene vs Peele is the acceptance test: if Zeta cannot separate those two, it has no business
pronouncing on Henry VI.

Usage: CORPUS=main|ep python scripts/word_profiles.py
Outputs results/[ep/]words/{word_profiles.md,json, zeta.md,json}
"""
import json, re, pathlib, collections, os, sys
import numpy as np
from sklearn.metrics import roc_auc_score

ROOT = pathlib.Path(__file__).resolve().parents[1]
CORPUS = os.environ.get('CORPUS', 'main')
CLEAN = ROOT / 'data' / ('clean' if CORPUS == 'main' else 'clean_' + CORPUS)
RES = ROOT / 'results' / ('' if CORPUS == 'main' else CORPUS) / 'words'
RES.mkdir(parents=True, exist_ok=True)
WORD_RE = re.compile(r"[a-z]+(?:['\-][a-z]+)*")
CAP_RE = re.compile(r"[A-Za-z]+(?:['\-][A-Za-z]+)*")
CHUNK = 2000
K_MARKERS = 150      # marker words per side
MIN_PLAYS = 5        # a Zeta candidate word must occur in at least this many plays corpus-wide
FUNCTION_WORDS = """a about above after again against all am among an and any are art as at ay be because been before
being both but by can cannot could did do does doth dost done down each either else ere even ever every few for forth from
had has hast hath have having he hence her here hers herself him himself his hither how i if in into is it its itself let
many may me might mine more most much must my myself nay neither never no none nor not nothing now of off oft often on once
one only or other our ours out over own same shall shalt she should since so some still such than that the thee their them
themselves then thence there therefore these they thine this thither those thou though through thus thy thyself till tis to
too under until unto up upon us very was we well were wert what when whence where wherefore whether which while whilst who
whom whose why will wilt with within without would ye yea yet yonder you your yours yourself""".split()
FW = set(FUNCTION_WORDS)

manifest = json.loads((CLEAN / 'manifest.json').read_text())
WORKS = {w['id']: w for w in manifest if w['group'] != 'altsource'}
def present(L): return [w for w in L if w in WORKS]
FAMILIES = [{'1H6', '2H6', '3H6', 'R3', 'TTR3'}, {'1Tam', '2Tam'}, {'Shr', 'AShrew'}, {'ST', 'Soliman'}]
def related(wid):
    for f in FAMILIES:
        if wid in f: return f
    return {wid}

# ---------------------------------------------------------------- tokens, proper nouns
def cap_counts(text):
    """Per word: (capitalised, total) over non-line-initial occurrences."""
    cap = collections.Counter(); tot = collections.Counter()
    for line in text.split('\n'):
        ws = CAP_RE.findall(line)
        for w in ws[1:]:
            lw = w.lower()
            if lw == 'i' or lw.startswith("i'"): continue
            tot[lw] += 1
            if w[0].isupper(): cap[lw] += 1
    return cap, tot

TOK, PN = {}, {}
POOL_CAP = collections.Counter(); POOL_TOT = collections.Counter()
for wid in WORKS:
    text = (CLEAN / f'{wid}.txt').read_text()
    cap, tot = cap_counts(text)
    # names: capitalised in >= 90% of non-line-initial uses within a play (>= 3 uses) ...
    PN[wid] = {w for w, n in tot.items() if n >= 3 and cap[w] / n >= 0.9}
    POOL_CAP.update(cap); POOL_TOT.update(tot)
    # single letters other than a / I / O are edition artefacts (Folger prints "in 's" for "in his")
    TOK[wid] = [t for t in WORD_RE.findall(text.lower()) if len(t) > 1 or t in ('a', 'i', 'o')]
# ... or capitalised in >= 60% of uses corpus-wide (>= 5 uses): catches names the EMED regulariser lower-cases half the time (tamburlaine)
ALL_PN = set().union(*PN.values()) | {w for w, n in POOL_TOT.items() if n >= 5 and POOL_CAP[w] / n >= 0.6}
def masked(wid): return [t for t in TOK[wid] if t not in ALL_PN]
print(f'{len(ALL_PN)} name-like words masked')

# ---------------------------------------------------------------- sets
by_author = collections.defaultdict(list)
for wid, w in WORKS.items(): by_author[w['author']].append(wid)
MARLOWE = present(['1Tam', '2Tam', 'Dido', 'DrFaust', 'JoM', 'Ed2', 'MP'])
H6 = present(['1H6', '2H6', '3H6'])
SH_NONH6 = present(['Tit', 'R3', 'Shr', 'TGV', 'Err'])
SH_EARLY = H6 + SH_NONH6
SH_LATER = [w for w, x in WORKS.items() if x['group'] == 'shakespeare_later']
SH_LATER_A = present(['R2', 'MND', 'Rom', 'MV', '1H4']); SH_LATER_B = present(['JC', 'Ham', 'Mac', 'Lr', 'WT', 'Tmp'])
GREENE = present(['Alphonsus', 'Orlando', 'FriarBacon', 'JamesIV'])
PEELE = present(['OWT', 'Alcazar', 'EdwardI', 'David'])
ANON = present(['Soliman', 'Locrine', 'Selimus', 'TRKJ', 'JackStraw', 'EdwardIII', 'Arden', 'TTR3'])
FLETCHER = present(['FS', 'Prize', 'IP'])
MARLOWE_A = present(['1Tam', '2Tam', 'Dido']); MARLOWE_B = present(['DrFaust', 'JoM', 'Ed2', 'MP'])
SETS = {'Marlowe': MARLOWE, 'Shakespeare early, Henry VI excluded': SH_NONH6, 'Henry VI 1-3': H6,
        'Shakespeare early (all 8)': SH_EARLY, 'Shakespeare later': SH_LATER, 'Greene': GREENE, 'Peele': PEELE,
        'Anonymous heroic': ANON, 'Fletcher': FLETCHER, 'Marlowe 1587-89': MARLOWE_A, 'Marlowe 1589-93': MARLOWE_B,
        'Shakespeare 1595-97': SH_LATER_A, 'Shakespeare 1599-1611': SH_LATER_B}
PAIRS = [
    ('QUESTION', 'Marlowe', 'Shakespeare early, Henry VI excluded'),
    ('QUESTION', 'Marlowe', 'Henry VI 1-3'),
    ('QUESTION', 'Marlowe', 'Shakespeare early (all 8)'),
    ('QUESTION', 'Marlowe', 'Shakespeare later'),
    ('SAME-AUTHOR', 'Shakespeare early (all 8)', 'Shakespeare later'),
    ('SAME-AUTHOR', 'Shakespeare early, Henry VI excluded', 'Shakespeare later'),
    ('SAME-AUTHOR', 'Marlowe 1587-89', 'Marlowe 1589-93'),
    ('SAME-AUTHOR', 'Shakespeare 1595-97', 'Shakespeare 1599-1611'),
    ('SAME-AUTHOR?', 'Henry VI 1-3', 'Shakespeare early, Henry VI excluded'),
    ('DIFFERENT', 'Greene', 'Peele'),
    ('DIFFERENT', 'Marlowe', 'Greene'),
    ('DIFFERENT', 'Marlowe', 'Peele'),
    ('DIFFERENT', 'Marlowe', 'Anonymous heroic'),
    ('DIFFERENT', 'Henry VI 1-3', 'Greene'),
    ('DIFFERENT', 'Henry VI 1-3', 'Peele'),
    ('DIFFERENT', 'Shakespeare early, Henry VI excluded', 'Greene'),
    ('DIFFERENT', 'Shakespeare early, Henry VI excluded', 'Peele'),
    ('DIFFERENT', 'Shakespeare later', 'Fletcher'),
]
PAIRS = [p for p in PAIRS if len(SETS[p[1]]) >= 2 and len(SETS[p[2]]) >= 2]

# ---------------------------------------------------------------- part 1: word profiles
play_df = collections.Counter()
for wid in WORKS: play_df.update(set(masked(wid)))
COMMON = sorted(w for w, n in play_df.items() if n >= 0.6 * len(WORKS))
VOCAB = sorted(set(FUNCTION_WORDS) | set(COMMON))
VIDX = {w: i for i, w in enumerate(VOCAB)}
RATES = {}
for wid in WORKS:
    c = collections.Counter(masked(wid)); n = sum(c.values())
    RATES[wid] = np.array([c[w] / n * 1000 for w in VOCAB])

def cohen_d(A, B):
    a = np.array([RATES[w] for w in A]); b = np.array([RATES[w] for w in B])
    ma, mb = a.mean(0), b.mean(0)
    va = a.var(0, ddof=1) if len(A) > 1 else np.zeros(len(VOCAB))
    vb = b.var(0, ddof=1) if len(B) > 1 else np.zeros(len(VOCAB))
    sp = np.sqrt(((len(A) - 1) * va + (len(B) - 1) * vb) / max(1, len(A) + len(B) - 2))
    sp[sp == 0] = np.nan
    d = (ma - mb) / sp
    d[np.isnan(d)] = 0
    # consistency: share of A plays above the B median, and of B plays below the A median
    medB = np.median(b, 0); medA = np.median(a, 0)
    consA = (a > medB).mean(0); consB = (b < medA).mean(0)
    return ma, mb, d, consA, consB

profiles = []
md = ['# Which words separate two sets of plays?', '',
      'Rate per 1,000 words, averaged over plays; d = Cohen\'s d of the play-level rates (positive = commoner in set A). "A>" = share of A plays above the B median. Function words and words present in >= 60% of plays; proper nouns removed. Top 20 each way.', '']
for typ, a, b in PAIRS:
    A, B = SETS[a], SETS[b]
    ma, mb, d, cA, cB = cohen_d(A, B)
    order = np.argsort(-d)
    top = [dict(w=VOCAB[i], rateA=round(float(ma[i]), 2), rateB=round(float(mb[i]), 2), d=round(float(d[i]), 2), cons=round(float(cA[i]), 2), func=VOCAB[i] in FW) for i in order[:25]]
    bot = [dict(w=VOCAB[i], rateA=round(float(ma[i]), 2), rateB=round(float(mb[i]), 2), d=round(float(d[i]), 2), cons=round(float(cB[i]), 2), func=VOCAB[i] in FW) for i in order[::-1][:25]]
    per_play = {wid: {VOCAB[i]: round(float(RATES[wid][i]), 2) for i in list(order[:25]) + list(order[::-1][:25])} for wid in A + B}
    profiles.append(dict(type=typ, A=a, B=b, playsA=A, playsB=B, topA=top, topB=bot, per_play=per_play,
                         mean_abs_d_top20=round(float(np.mean(np.abs(d[order[:20]])) + np.mean(np.abs(d[order[::-1][:20]]))) / 2, 2)))
    md += [f'## {typ}: {a} (A, {len(A)} plays) vs {b} (B, {len(B)} plays)', '',
           '| commoner in A | A | B | d | A> | | commoner in B | A | B | d | B< |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for x, y in zip(top[:20], bot[:20]):
        md.append(f"| {x['w']} | {x['rateA']} | {x['rateB']} | {x['d']:+.2f} | {x['cons']:.2f} | | {y['w']} | {y['rateA']} | {y['rateB']} | {y['d']:+.2f} | {y['cons']:.2f} |")
    md.append('')
(RES / 'word_profiles.md').write_text('\n'.join(md))
json.dump(dict(vocab_size=len(VOCAB), pairs=profiles), open(RES / 'word_profiles.json', 'w'))
print('word profiles written', len(VOCAB), 'words')

# ---------------------------------------------------------------- part 2: Zeta
def chunks(toks, size=CHUNK):
    out = [toks[i:i + size] for i in range(0, len(toks), size)]
    if len(out) > 1 and len(out[-1]) < size // 2:
        out[-2] = out[-2] + out[-1]; out.pop()
    return out
ZVOCAB = sorted(w for w, n in play_df.items() if n >= MIN_PLAYS)
ZIDX = {w: i for i, w in enumerate(ZVOCAB)}
CH = {}      # wid -> binary matrix chunks x vocab
for wid in WORKS:
    rows = []
    for ch in chunks(masked(wid)):
        v = np.zeros(len(ZVOCAB), dtype=np.uint8)
        for t in set(ch):
            j = ZIDX.get(t)
            if j is not None: v[j] = 1
        rows.append(v)
    CH[wid] = np.array(rows)

def markers(A, B):
    """Top-K marker words for A and for B, from the training plays only."""
    ma = np.vstack([CH[w] for w in A]); mb = np.vstack([CH[w] for w in B])
    dfa = ma.mean(0); dfb = mb.mean(0)
    z = dfa - dfb
    ok = (ma.sum(0) + mb.sum(0)) >= 2
    z[~ok] = 0
    ia = np.argsort(-z)[:K_MARKERS]; ib = np.argsort(z)[:K_MARKERS]
    return ia, ib, z

def score(M, ia, ib):
    return M[:, ia].mean(1), M[:, ib].mean(1)

def zeta_pair(typ, a, b):
    A, B = SETS[a], SETS[b]
    pts = []   # out-of-sample chunk scores
    for held in A + B:
        side = 'A' if held in A else 'B'
        fam = related(held)
        # the held-out play leaves training; its plot-family leaves the *other* side always, and its own
        # side too unless that would empty the side (Henry VI 1-3 are then scored with their sibling parts in
        # training, which flatters that set's cohesion; noted in the report)
        own = A if side == 'A' else B; other = B if side == 'A' else A
        tr_own = [w for w in own if w not in fam] or [w for w in own if w != held]
        tr_other = [w for w in other if w not in fam]
        trA, trB = (tr_own, tr_other) if side == 'A' else (tr_other, tr_own)
        if len(trA) < 1 or len(trB) < 1: continue
        ia, ib, _ = markers(trA, trB)
        ta = score(np.vstack([CH[w] for w in trA]), ia, ib); tb = score(np.vstack([CH[w] for w in trB]), ia, ib)
        cA = np.array([ta[0].mean(), ta[1].mean()]); cB = np.array([tb[0].mean(), tb[1].mean()])
        sa, sb = score(CH[held], ia, ib)
        for k in range(len(sa)):
            p = np.array([sa[k], sb[k]])
            pred = 'A' if np.linalg.norm(p - cA) < np.linalg.norm(p - cB) else 'B'
            pts.append(dict(play=held, side=side, sA=round(float(sa[k]), 4), sB=round(float(sb[k]), 4), pred=pred,
                            margin=float(sa[k] - sb[k]) - float((cA[0] - cA[1] + cB[0] - cB[1]) / 2)))
    acc = np.mean([p['pred'] == p['side'] for p in pts])
    y = [1 if p['side'] == 'A' else 0 for p in pts]; s = [p['margin'] for p in pts]
    auc = roc_auc_score(y, s) if 0 < sum(y) < len(y) else float('nan')
    # per-play majority
    per_play = {}
    for w in A + B:
        ps = [p for p in pts if p['play'] == w]
        if ps: per_play[w] = dict(side=ps[0]['side'], chunks=len(ps), shareA_pred=round(float(np.mean([p['pred'] == 'A' for p in ps])), 2),
                                  sA=round(float(np.mean([p['sA'] for p in ps])), 3), sB=round(float(np.mean([p['sB'] for p in ps])), 3))
    # marker lists from the full pair, for display
    ia, ib, z = markers(A, B)
    ta = score(np.vstack([CH[w] for w in A]), ia, ib); tb = score(np.vstack([CH[w] for w in B]), ia, ib)
    return dict(type=typ, A=a, B=b, playsA=A, playsB=B, chunks=len(pts), acc=round(float(acc), 3), auc=round(float(auc), 3),
                markersA=[dict(w=ZVOCAB[i], z=round(float(z[i]), 2)) for i in ia[:40]],
                markersB=[dict(w=ZVOCAB[i], z=round(float(z[i]), 2)) for i in ib[:40]],
                centroidA=[round(float(ta[0].mean()), 3), round(float(ta[1].mean()), 3)], centroidB=[round(float(tb[0].mean()), 3), round(float(tb[1].mean()), 3)],
                points=pts, per_play=per_play)

zeta = [zeta_pair(*p) for p in PAIRS]
md = ['# Burrows\'s Zeta: marker-word tests', '',
      f'2,000-word chunks, proper nouns removed, candidate words present in >= {MIN_PLAYS} plays, {K_MARKERS} markers per side. Markers are chosen with the scored play and its family held out. Chunks are classified by nearest training centroid in (share of A-markers, share of B-markers). Read the question pairs against the benchmarks.', '',
      '| pair | type | plays | chunks | accuracy | AUC |', '|---|---|---|---|---|---|']
for zp in zeta:
    md.append(f"| {zp['A']} vs {zp['B']} | {zp['type']} | {len(zp['playsA'])} vs {len(zp['playsB'])} | {zp['chunks']} | {zp['acc']:.2f} | {zp['auc']:.2f} |")
md += ['', '## Per-play results (share of chunks placed with set A)', '']
for zp in zeta:
    md += [f"### {zp['A']} (A) vs {zp['B']} (B)", '', '| play | set | chunks | placed as A | A-marker share | B-marker share |', '|---|---|---|---|---|---|']
    for w, r in zp['per_play'].items():
        md.append(f"| {w} ({WORKS[w]['author']}) | {r['side']} | {r['chunks']} | {r['shareA_pred']:.2f} | {r['sA']:.3f} | {r['sB']:.3f} |")
    md += ['', f"Markers for A: {', '.join(m['w'] for m in zp['markersA'][:30])}", '', f"Markers for B: {', '.join(m['w'] for m in zp['markersB'][:30])}", '']

# projection: Marlowe vs Shakespeare (Henry VI family excluded from Shakespeare) applied to Henry VI, R3 and the register controls
SH_REF = [w for w in SH_NONH6 + SH_LATER if w not in {'R3'}]
ia, ib, z = markers(MARLOWE, SH_REF)
proj = dict(A='Marlowe', B='Shakespeare, Henry VI family excluded', playsA=MARLOWE, playsB=SH_REF,
            markersA=[dict(w=ZVOCAB[i], z=round(float(z[i]), 2)) for i in ia[:40]], markersB=[dict(w=ZVOCAB[i], z=round(float(z[i]), 2)) for i in ib[:40]], points=[])
# training points (in-sample, shown faint) and out-of-sample scored plays
for w in MARLOWE + SH_REF:
    sa, sb = score(CH[w], ia, ib)
    for k in range(len(sa)): proj['points'].append(dict(play=w, group='train-A' if w in MARLOWE else 'train-B', sA=round(float(sa[k]), 4), sB=round(float(sb[k]), 4)))
for w in H6 + present(['R3']) + GREENE + PEELE + ANON + present(['ST']):
    sa, sb = score(CH[w], ia, ib)
    for k in range(len(sa)): proj['points'].append(dict(play=w, group=WORKS[w]['author'] if w not in H6 + ['R3'] else w, sA=round(float(sa[k]), 4), sB=round(float(sb[k]), 4)))
ta = score(np.vstack([CH[w] for w in MARLOWE]), ia, ib); tb = score(np.vstack([CH[w] for w in SH_REF]), ia, ib)
proj['centroidA'] = [round(float(ta[0].mean()), 3), round(float(ta[1].mean()), 3)]; proj['centroidB'] = [round(float(tb[0].mean()), 3), round(float(tb[1].mean()), 3)]
md += ['## Projection: Marlowe vs Shakespeare markers applied to Henry VI, Richard III and the register controls', '',
       'Markers trained on all Marlowe vs all Shakespeare outside the Henry VI family (so Henry VI 1-3 and Richard III are out of sample; Greene, Peele, the anonymous plays and Kyd are never in training). Mean marker shares per play; the Marlowe centroid is at '
       f"({proj['centroidA'][0]:.3f}, {proj['centroidA'][1]:.3f}) and the Shakespeare centroid at ({proj['centroidB'][0]:.3f}, {proj['centroidB'][1]:.3f}).", '',
       '| play | author | chunks | Marlowe-marker share | Shakespeare-marker share | nearer |', '|---|---|---|---|---|---|']
cA = np.array(proj['centroidA']); cB = np.array(proj['centroidB'])
proj['per_play'] = {}
for w in H6 + present(['R3']) + GREENE + PEELE + ANON + present(['ST']):
    ps = [p for p in proj['points'] if p['play'] == w]
    m = np.array([np.mean([p['sA'] for p in ps]), np.mean([p['sB'] for p in ps])])
    near = 'Marlowe' if np.linalg.norm(m - cA) < np.linalg.norm(m - cB) else 'Shakespeare'
    share = float(np.mean([np.linalg.norm(np.array([p['sA'], p['sB']]) - cA) < np.linalg.norm(np.array([p['sA'], p['sB']]) - cB) for p in ps]))
    proj['per_play'][w] = dict(sA=round(float(m[0]), 3), sB=round(float(m[1]), 3), nearer=near, chunks=len(ps), share_marlowe=round(share, 2))
    md.append(f"| {w} | {WORKS[w]['author']} | {len(ps)} | {m[0]:.3f} | {m[1]:.3f} | {near} ({share:.0%} of chunks) |")
md += ['', f"Marlowe markers: {', '.join(m['w'] for m in proj['markersA'][:40])}", '', f"Shakespeare markers: {', '.join(m['w'] for m in proj['markersB'][:40])}", '']
(RES / 'zeta.md').write_text('\n'.join(md))
json.dump(dict(k=K_MARKERS, min_plays=MIN_PLAYS, chunk=CHUNK, vocab=len(ZVOCAB), pairs=zeta, projection=proj), open(RES / 'zeta.json', 'w'))
print('zeta written')
for zp in zeta: print(f"{zp['type']:13s} {zp['A']} vs {zp['B']}: acc {zp['acc']:.2f} auc {zp['auc']:.2f} ({zp['chunks']} chunks)")
