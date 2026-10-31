"""How much does the edition (EMED vs EarlyPrint vs Gutenberg) change a play's cross-entropy under a fixed char model?"""
import json, re, pathlib, collections, math
ROOT = pathlib.Path(__file__).resolve().parents[1]; CLEAN = ROOT / 'data' / 'clean'
import importlib.util, sys
spec = importlib.util.spec_from_file_location('ce', ROOT / 'scripts' / 'crossentropy.py')
sys.argv = ['x', 'masked']; ce = importlib.util.module_from_spec(spec); spec.loader.exec_module(ce)
manifest = {w['id']: w for w in json.loads((CLEAN / 'manifest.json').read_text())}
alts = [w for w in manifest if manifest[w]['group'] == 'altsource']
def text(w): return ce.text_of.__wrapped__(w) if hasattr(ce.text_of, '__wrapped__') else None
# reuse ce's masked text builder for alt texts
ALT = {}
for a in alts:
    raw = (CLEAN / f'{a}.txt').read_text(); names = ce.proper_nouns(raw)
    ALT[a] = ' ' + ' '.join('~' if t in names else t for t in ce.WORD_RE.findall(raw.lower())) + ' '
models = {}
for name, ids in [('Marlowe', ce.MARLOWE), ('Sh-later', ce.SH_LATER), ('Greene', ce.GREENE), ('Anon-heroic', ce.ANON)]:
    pass
out = ['# Edition effect on character-model cross-entropy (bits/char)\n',
       'Same play, different edition, scored by the same models (models never contain the play in question).\n',
       '| play | edition pair | model | H(main edition) | H(alternate) | difference |', '|---|---|---|---|---|---|']
for a in alts:
    base = a.rsplit('_', 1)[0]
    for name, ids in [('Marlowe', ce.MARLOWE), ('Sh-later', ce.SH_LATER), ('Greene', ce.GREENE), ('Anon-heroic', ce.ANON)]:
        tr = [w for w in ids if w not in ce.related(base)]
        m, n = ce.build(tr, ce.BUDGET)
        h0 = m.cross_entropy(ce.TEXT[base]); h1 = m.cross_entropy(ALT[a])
        out.append(f"| {base} | {manifest[base]['source']} vs {manifest[a]['source']} | {name} | {h0:.3f} | {h1:.3f} | {h1-h0:+.3f} |")
        print(out[-1], flush=True)
(ROOT / 'results' / 'crossentropy_masked' / 'edition_effect.md').write_text('\n'.join(out) + '\n')
