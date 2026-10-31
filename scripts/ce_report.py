"""Double-centred affinity table from crossentropy.json.

H[p, m] = cross-entropy of play p under model m.  Models differ in overall predictiveness and plays
differ in overall predictability, so we remove both main effects:
    A[p, m] = H[p, m] - mean_m H[p, .] - mean_p H[., m] + grand mean
over the three size-matched author models (Marlowe, Sh-early, Sh-later).  Negative A = this play is
*specifically* well predicted by this model, relative to how the model does on every other play.
"""
import json, pathlib, sys, collections
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
CORPUS = os.environ.get('CORPUS', 'main')
CLEAN = ROOT / 'data' / ('clean' if CORPUS == 'main' else 'clean_' + CORPUS)
RESROOT = ROOT / 'results' / ('' if CORPUS == 'main' else CORPUS)
variant = sys.argv[1] if len(sys.argv) > 1 else 'plain'
d = RESROOT / ('crossentropy' if variant == 'plain' else 'crossentropy_masked')
J = json.load(open(d / 'crossentropy.json')); H = J['rows']
manifest = {w['id']: w for w in json.load(open(CLEAN / 'manifest.json'))}
plays = list(H); models = [m for m in J['matched'] if m != 'Sh-all']
M = np.array([[H[p][m] for m in models] for p in plays])
A = M - M.mean(1, keepdims=True) - M.mean(0, keepdims=True) + M.mean()
out = [f'# Affinity (double-centred cross-entropy, bits/char), variant = {variant}\n',
       'Negative = the play is specifically well predicted by that author model, after removing each model\'s overall '
       'predictiveness and each play\'s overall predictability. Each row sums to zero.\n',
       '| play | author | group | ' + ' | '.join(f'A({m})' for m in models) + ' | strongest affinity |', '|---|---|---|' + '---|' * len(models) + '---|']
for i, p in enumerate(plays):
    best = models[int(np.argmin(A[i]))]
    out.append(f"| {p} | {manifest[p]['author']} | {manifest[p]['group']} | " + ' | '.join(f'{a:+.3f}' for a in A[i]) + f" | **{best}** |")
groups = collections.OrderedDict([
    ('Marlowe plays', [p for p in plays if manifest[p]['author'] == 'Marlowe']),
    ('Shakespeare early', [p for p in plays if manifest[p]['group'] == 'shakespeare_early']),
    ('  of which Henry VI 1-3', [p for p in ['1H6', '2H6', '3H6'] if p in plays]),
    ('  of which Tit, R3, Shr, TGV, Err', [p for p in ['Tit', 'R3', 'Shr', 'TGV', 'Err'] if p in plays]),
    ('Shakespeare later', [p for p in plays if manifest[p]['group'] == 'shakespeare_later']),
    ('early controls', [p for p in ['ST', 'OWT', 'Gal', 'AShrew', 'TCKL'] if p in plays]),
    ('later controls', [p for p in ['ShoeHol', 'RT', 'KBP'] if p in plays]),
    ('Fletcher', [p for p in plays if manifest[p]['author'] == 'Fletcher']), ('Ford', [p for p in plays if manifest[p]['author'] == 'Ford']),
    ('Greene', [p for p in plays if manifest[p]['author'] == 'Greene']), ('Peele', [p for p in plays if manifest[p]['author'] == 'Peele']),
    ('anonymous heroic 1587-94', [p for p in ['Soliman', 'Locrine', 'Selimus', 'TRKJ', 'JackStraw', 'EdwardIII', 'Arden', 'TTR3'] if p in plays]),
    ('Lodge, Lyly Endymion', [p for p in ['Wounds', 'Endymion'] if p in plays])])
groups = collections.OrderedDict((g, ids) for g, ids in groups.items() if ids)
out.append('\n## Group means\n'); out.append('| group | ' + ' | '.join(f'A({m})' for m in models) + ' |'); out.append('|---|' + '---|' * len(models))
idx = {p: i for i, p in enumerate(plays)}
for g, ids in groups.items():
    a = A[[idx[p] for p in ids]].mean(0)
    out.append(f'| {g} | ' + ' | '.join(f'{x:+.3f}' for x in a) + ' |')
(d / 'affinity.md').write_text('\n'.join(out) + '\n')
print('\n'.join(out[-12:]))
