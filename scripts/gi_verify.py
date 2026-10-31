"""General Impostors authorship verification (Koppel & Winter 2014), calibrated with known pairs.

For a target play T and a candidate author C: repeat N times, each time with a random half of the
features and a random sample of impostor plays (by authors other than C and T's own author being
irrelevant: impostors are simply every play not by C, outside T's family). Score = fraction of rounds
in which T's nearest candidate play is closer than T's nearest impostor play. Near 1 = consistent with
C; near 0 = some impostor is reliably closer. Features: function words; distance: cosine on z-scores.
"""
import json, re, pathlib, collections, random, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
CORPUS = os.environ.get('CORPUS', 'main')   # main = Folger/EMED corpus; ep = all-EarlyPrint corpus
CLEAN = ROOT / 'data' / ('clean' if CORPUS == 'main' else 'clean_' + CORPUS)
RESROOT = ROOT / 'results' / ('' if CORPUS == 'main' else CORPUS)
RES = RESROOT / 'gi_verify'; RES.mkdir(parents=True, exist_ok=True)
WORD_RE = re.compile(r"[a-z]+(?:['\-][a-z]+)*")
N_ROUNDS = 200; FEAT_FRAC = 0.5; N_IMP = 12; random.seed(0); np.random.seed(0)
FUNCTION_WORDS = """a about above after again against all am among an and any are art as at ay be because been before
being both but by can cannot could did do does doth dost done down each either else ere even ever every few for forth from
had has hast hath have having he hence her here hers herself him himself his hither how i if in into is it its itself let
many may me might mine more most much must my myself nay neither never no none nor not nothing now of off oft often on once
one only or other our ours out over own same shall shalt she should since so some still such than that the thee their them
themselves then thence there therefore these they thine this thither those thou though through thus thy thyself till tis to
too under until unto up upon us very was we well were wert what when whence where wherefore whether which while whilst who
whom whose why will wilt with within without would ye yea yet yonder you your yours yourself""".split()
FAMILIES = [{'1H6', '2H6', '3H6', 'R3', 'TTR3'}, {'1Tam', '2Tam'}, {'Shr', 'AShrew'}, {'ST', 'Soliman'}]
def related(w):
    for f in FAMILIES:
        if w in f: return f
    return {w}
manifest = {w['id']: w for w in json.loads((CLEAN / 'manifest.json').read_text()) if w['group'] != 'altsource'}
IDS = list(manifest)
ANON = ['Soliman', 'Locrine', 'Selimus', 'TRKJ', 'JackStraw', 'EdwardIII', 'Arden', 'TTR3']
def author(w):
    a = manifest[w]['author']
    return 'Anon-heroic' if w in ANON else a
TOK = {w: WORD_RE.findall((CLEAN / f'{w}.txt').read_text().lower()) for w in IDS}
def vec(toks):
    c = collections.Counter(toks); n = len(toks)
    return np.array([c[f] / n * 1000 for f in FUNCTION_WORDS])
X = np.array([vec(TOK[w]) for w in IDS]); mu = X.mean(0); sd = X.std(0); sd[sd == 0] = 1
Z = (X - mu) / sd; idx = {w: i for i, w in enumerate(IDS)}
def cos(a, b): return 1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12)

CANDS = [c for c in ['Marlowe', 'Shakespeare', 'Greene', 'Peele', 'Anon-heroic', 'Fletcher'] if any(author(w) == c for w in IDS)]
def gi(T, C):
    cand = [w for w in IDS if author(w) == C and w not in related(T)]
    imps = [w for w in IDS if author(w) != C and w not in related(T)]
    if not cand: return float('nan')
    wins = 0
    for _ in range(N_ROUNDS):
        f = np.random.rand(Z.shape[1]) < FEAT_FRAC
        if f.sum() < 10: continue
        zt = Z[idx[T], f]
        dc = min(cos(zt, Z[idx[w], f]) for w in cand)
        di = min(cos(zt, Z[idx[w], f]) for w in random.sample(imps, min(N_IMP, len(imps))))
        wins += dc < di
    return wins / N_ROUNDS

rows = {}
for T in IDS:
    rows[T] = {C: gi(T, C) for C in CANDS}
json.dump(rows, open(RES / 'gi_scores.json', 'w'), indent=1)
out = ['# General Impostors verification scores (function words, %d rounds)\n' % N_ROUNDS,
       'Score = share of rounds in which the target play is nearer to some play by the candidate author than to every sampled impostor. '
       'The target\'s own author\'s plays count as impostors when they are not the candidate, so a play by a known author should score high '
       'only in its own column. Plays sharing plot/characters with the target are excluded from both sides.\n',
       '| play | author | ' + ' | '.join(f'as {c}' for c in CANDS) + ' |', '|---|---|' + '---|' * len(CANDS)]
for T in IDS:
    out.append(f"| {T} | {author(T)} | " + ' | '.join(f"{rows[T][C]:.2f}" if not np.isnan(rows[T][C]) else '-' for C in CANDS) + ' |')
# calibration summary
out.append('\n## Calibration\n'); out.append('| target group | ' + ' | '.join(f'as {c}' for c in CANDS) + ' |'); out.append('|---|' + '---|' * len(CANDS))
groups = [('Marlowe plays', [w for w in IDS if author(w) == 'Marlowe']), ('Shakespeare early (≤1594)', [w for w in IDS if manifest[w]['group'] == 'shakespeare_early']),
          ('  Henry VI 1-3', [w for w in ['1H6', '2H6', '3H6'] if w in IDS]), ('  Tit, R3, Shr, TGV, Err', [w for w in ['Tit', 'R3', 'Shr', 'TGV', 'Err'] if w in IDS]),
          ('Shakespeare later', [w for w in IDS if manifest[w]['group'] == 'shakespeare_later']), ('Greene', [w for w in IDS if author(w) == 'Greene']),
          ('Peele', [w for w in IDS if author(w) == 'Peele']), ('Anon heroic', ANON), ('Fletcher', [w for w in IDS if author(w) == 'Fletcher']),
          ('Kyd ST', ['ST']), ('other single-play controls', ['Gal', 'Endymion', 'Wounds', 'AShrew', 'TCKL', 'ShoeHol', 'RT', 'KBP', 'Perkin', 'TPSW'])]
groups = [(g, [w for w in ids if w in IDS]) for g, ids in groups]; groups = [(g, ids) for g, ids in groups if ids]
for g, ids in groups:
    out.append(f'| {g} | ' + ' | '.join(f"{np.nanmean([rows[w][C] for w in ids]):.2f}" for C in CANDS) + ' |')
(RES / 'gi_verify.md').write_text('\n'.join(out) + '\n')
print('\n'.join(out[-13:]))
