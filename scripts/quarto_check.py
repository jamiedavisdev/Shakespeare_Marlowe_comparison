"""Does Folio vs quarto text change how Titus and Richard III relate to Marlowe? (all-EarlyPrint corpus)"""
import os, sys, json, re, collections, math, pathlib
os.environ['CORPUS'] = 'ep'; sys.argv = ['x', 'masked']
import importlib.util, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ce', ROOT / 'scripts' / 'crossentropy.py'); ce = importlib.util.module_from_spec(spec); spec.loader.exec_module(ce)
spec2 = importlib.util.spec_from_file_location('gi', ROOT / 'scripts' / 'gi_verify.py')
manifest = {w['id']: w for w in json.loads((ROOT / 'data/clean_ep/manifest.json').read_text())}
def masked(w):
    raw = (ROOT / 'data/clean_ep' / f'{w}.txt').read_text(); names = ce.proper_nouns(raw)
    return ' ' + ' '.join('~' if t in names else t for t in ce.WORD_RE.findall(raw.lower())) + ' '
out = ['# Folio vs quarto check (all-EarlyPrint corpus, masked char models, size-matched)\n',
       '| play | text | H(Marlowe) | H(Sh-early) | H(Sh-later) | H(Greene) | H(Peele) | H(Marlowe) − H(Sh-early) |', '|---|---|---|---|---|---|---|---|']
for base, q in (('Tit', 'Tit_Q'), ('R3', 'R3_Q')):
    excl = ce.related(base)
    models = {n: ce.build([w for w in ids if w not in excl], ce.BUDGET)[0] for n, ids in
              (('Marlowe', ce.MARLOWE), ('Sh-early', ce.SH_EARLY), ('Sh-later', ce.SH_LATER), ('Greene', ce.GREENE), ('Peele', ce.PEELE))}
    for t in (base, q):
        s = ce.TEXT[t] if t in ce.TEXT else masked(t)
        H = {n: m.cross_entropy(s) for n, m in models.items()}
        out.append(f"| {base} | {manifest[t]['title']} | " + ' | '.join(f"{H[n]:.3f}" for n in models) + f" | {H['Marlowe'] - H['Sh-early']:+.3f} |")
        print(out[-1], flush=True)
(ROOT / 'results/ep/crossentropy_masked/quarto_check.md').write_text('\n'.join(out) + '\n')
