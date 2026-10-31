# Shakespeare / Marlowe authorship comparison

Stylometric and language-model tests of whether the early plays attributed to Shakespeare
(up to 1594) are distinguishable from the plays of Christopher Marlowe, measured against
control authors of the same period.

## Layout

```
scripts/works.json        corpus definition: id, title, author, group, date, source, notes
scripts/build_corpus.py   downloads are in data/raw; this strips speaker labels, stage directions,
                          apparatus and produces data/clean/<id>.txt (dialogue only) + manifest.json
scripts/stylometry.py     distances, clustering, PCA, leave-one-play-out attribution,
                          chunk classifiers, Marlowe-probability scan, source-confound check
                          arg: mfw150 | mfw500 | func   (feature set)  -> results/<feature set>/
scripts/crossentropy.py   character 6-gram author models, cross-entropy of each held-out play
                          arg: plain | masked  -> results/crossentropy[_masked]/
scripts/ce_report.py      double-centred affinity table from a crossentropy run
scripts/gi_verify.py      General Impostors verification scores, calibrated with known pairs
scripts/scene_scan.py     four-way (Marlowe/Shakespeare/Peele/Greene) scene-level scan of 1-3 Henry VI, Titus, R3
scripts/prose_verse.py    verse-only / prose-only rescoring of the Henry VI scenes
scripts/edition_effect.py how much an edition change moves cross-entropy under fixed models
scripts/quarto_check.py   Folio vs 1590s-quarto text of Titus and Richard III under the author models
scripts/finetune.py       GPT-2 fine-tune per author: held-out bits/token and weight-delta cosines
REPORT.md                 findings and caveats (v1 archived in results/)
NOTEBOOK.md               dated lab notebook: process, thoughts, bugs, results
```

Three corpora share play ids and are selected with the `CORPUS` environment variable:
`main` (default; Folger Shakespeare + Folger EMED + EarlyPrint controls, `data/clean`),
`ep` (everything from EarlyPrint incl. the 1623 Folio, `data/clean_ep`, results in `results/ep`),
`q` (Shakespeare from early quartos only, `data/clean_q`, results in `results/q`).
Corpus definitions: `scripts/works.json`, `works_ep.json`, `works_q.json`.

## Corpus

| group | plays | source |
|---|---|---|
| Marlowe | 1 & 2 Tamburlaine, Dido, Doctor Faustus (A-text), Jew of Malta, Edward II, Massacre at Paris | Folger EMED, regularised-spelling XML |
| Shakespeare early (≤1594) | 1-3 Henry VI, Titus, Richard III, Shrew, Two Gentlemen, Errors | Folger Shakespeare TXT |
| Shakespeare later | R2, MND, Rom, MV, 1H4, JC, Ham, Mac, Lr, WT, Tmp | Folger Shakespeare TXT |
| early controls | Kyd *Spanish Tragedy*, Peele *Old Wives Tale*, Lyly *Gallathea*, anon. *Taming of a Shrew*, anon. *King Leir* | Folger EMED |
| later controls | Dekker *Shoemakers' Holiday*, Middleton *Revenger's Tragedy*, Beaumont *Knight of the Burning Pestle* | Folger EMED |
| multi-play benchmark authors | Fletcher (3 plays), Ford (2 plays) | Folger EMED |
| alternate-source check | Faustus and Jew of Malta from Project Gutenberg (Dyce edition) | Gutenberg |

Both Folger products modernise spelling, so the only systematic source difference is punctuation,
which no feature set here uses. The alternate-source check quantifies the residual effect.

## Run

```
python3 -m venv .venv && .venv/bin/pip install numpy scipy scikit-learn matplotlib
.venv/bin/python scripts/build_corpus.py
for f in func mfw150 mfw500; do .venv/bin/python scripts/stylometry.py $f; done
.venv/bin/python scripts/crossentropy.py plain && .venv/bin/python scripts/ce_report.py plain
.venv/bin/python scripts/crossentropy.py masked && .venv/bin/python scripts/ce_report.py masked
.venv/bin/python scripts/gi_verify.py
.venv/bin/python scripts/scene_scan.py && .venv/bin/python scripts/prose_verse.py
CORPUS=ep .venv/bin/python scripts/build_corpus.py && CORPUS=ep .venv/bin/python scripts/stylometry.py func   # etc.
.venv/bin/pip install torch transformers && .venv/bin/python scripts/finetune.py   # ~1 h on an M3 Pro
```

EarlyPrint raw files: `https://bitbucket.org/eads004/<first 3 chars of TCP id>/raw/master/<TCP id>.xml`.

Raw downloads (data/raw) are re-fetched with the curl commands recorded in REPORT.md if missing.
