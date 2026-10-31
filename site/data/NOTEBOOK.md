# Lab notebook: Marlowe / early Shakespeare authorship test

A running record of process, reasoning, dead ends and results. Newest entries at the bottom.
REPORT.md holds the distilled conclusions; this file holds the trail.

## 2026-10-30, session 1: framing

**Starting idea (Jamie):** train one language model per corpus and compare the weights.

**Why I argued against comparing weights, and where that argument is weaker than I first said:**
- Models trained *from scratch* on two corpora are not comparable parameter by parameter: random
  seeds, neuron permutation symmetry and many equivalent minima mean the distance between weight
  tensors is dominated by noise. With 100-200k words per author you could not train from scratch
  anyway.
- Models *fine-tuned from the same pretrained checkpoint* are a different matter. The weight deltas
  ("task vectors") live in one coordinate system, and the task-arithmetic literature shows they are
  meaningful. So the idea is testable in that form, with the obvious control: fine-tune twice on the
  same corpus with different seeds and see whether seed noise is smaller than author difference.
  Planned for session 2 (needs PyTorch).
- Either way, comparing what the models *predict* (held-out cross-entropy) is the more direct and
  better understood test, so it came first.

**Design decisions:**
- Controls are non-negotiable. Kyd, Peele, Lyly and two anonymous plays from the same years, later
  controls, and two multi-play authors (Fletcher, Ford) as known-different benchmarks.
- One editorial house for both sides: Folger Shakespeare (modern spelling) and Folger EMED
  regularised texts. Measured the residual edition effect with Gutenberg copies of two Marlowe plays:
  cosine delta 0.01-0.05 between editions of the same play, about 1.0 between different plays.
- Dialogue only. Speaker labels and stage directions are editorial and would be a trivial
  source-fingerprint.
- "Families" of plays sharing plot and characters (Henry VI 1-3 + Richard III, Tamburlaine 1+2,
  the two Shrews) are held out together. Without this, 2 Henry VI is "recognised" as Shakespeare
  because 3 Henry VI is in training, which proves nothing.

**Dead ends and bugs worth recording:**
- Folger's download page lists only some play codes; the rest live at predictable S3 slugs.
- First pass at the cross-entropy test truncated training text by taking plays in order, so the
  "Shakespeare-early" model was effectively the Henry VI trilogy plus Titus. Fixed by taking an equal
  share of characters from every training play. The affinity numbers changed materially.
- Proper-noun masking initially masked "I" (always capitalised). Caught by printing the mask list.
- A chunk-classifier benchmark with only two plays on one side (Ford) has no power; AUC sat at 0.5
  with accuracy 0.86 because the classifier labelled everything as the big class. Left in the table
  as a warning, not as evidence.
- Most-frequent-word features mostly measure period and genre. Kyd's Spanish Tragedy is attributed
  to Marlowe by every feature set. This is the central confound of the whole exercise.

**Results (see REPORT.md):** no support for a single author; Henry VI 1-3 lean Marlowe but so does Kyd.

## 2026-10-30, session 2: pushing further

**Plan:**
1. More 1587-92 history/tragedy controls, to attack the register confound directly. Candidate
   source: EarlyPrint (regularised EEBO-TCP texts, same lineage as EMED).
2. Scene-level scan of Henry VI 1-3 against the New Oxford Shakespeare scene attributions. If the
   Marlowe signal concentrates in the scenes scholars already give to Marlowe, that is a validation of
   the method; if it is uniform, it is register.
3. General Impostors verification (Koppel & Winter 2014): a calibrated "same author?" score per play.
4. Neural version: fine-tune GPT-2 per author, held-out perplexity, and the task-vector weight test.

### Session 2, step 1: scene-level scan of Henry VI (results/scene_scan/scene_scan.md)

Method: train Marlowe vs Shakespeare with the whole Henry VI / Richard III family excluded, then score
every scene with (a) a function-word classifier and (b) proper-noun-masked character models, reporting
ΔH = H(Marlowe) − H(Shakespeare) in bits/char (negative favours Marlowe).

Word-weighted results by published attribution:

| play | scenes | P(Marlowe) | ΔH |
|---|---|---|---|
| 1H6 Act 1 (Nashe per Taylor/NOS) | 6 | 0.48 | +0.007 |
| 1H6 unattributed remainder | 14 | 0.50 | +0.069 |
| 1H6 2.4, 4.2-4.7 (Shakespeare per Taylor/NOS) | 7 | 0.47 | +0.117 |
| 2H6 4.2-4.10, the Cade scenes (Marlowe per Craig & Kinney) | 9 | 0.69 | +0.061 |
| 2H6 remainder | 15 | 0.36 | +0.126 |
| 3H6 all | 28 | 0.58 | +0.069 |
| Richard III | 25 | 0.15 | +0.163 |
| Titus | 14 | 0.13 | +0.336 |

Thoughts:
- The character model's ordering inside 1H6 matches Taylor's 1995 division: the Nashe act is least
  Shakespearean, the Talbot scenes most. The function-word classifier sees nothing in 1H6, which is
  expected for 300-1300-word scenes.
- In 2H6 both scorers put the Cade scenes nearer Marlowe than the rest of the play, agreeing with
  Craig & Kinney. Caveat I cannot yet remove: the Cade scenes are largely prose and the prose/verse
  balance of the training sets is not matched.
- Titus is strongly non-Marlowe throughout, but Acts 1-2 (ΔH +0.5 to +0.7) differ sharply from Acts
  3-5 (+0.1 to +0.3). Act 1 and 2.1-2.2 are the scenes usually given to Peele. ΔH only measures
  "Marlowe versus Shakespeare", so this is a hint, not an attribution. With Peele now at four plays a
  three-way Titus scan is possible.
- Richard III: nothing Marlowe-like anywhere, a useful negative control.

### Session 2, step 2: EarlyPrint controls

EarlyPrint (texts.earlyprint.org; raw files at
`bitbucket.org/eads004/<first 3 chars of TCP id>/raw/master/<TCP id>.xml`) gives linguistically
annotated EEBO-TCP texts with a `reg` attribute carrying standardised spelling. Added 17 plays of
1587-1594: Greene (Alphonsus, Orlando Furioso, Friar Bacon, James IV), Peele (Alcazar, Edward I, David
and Bethsabe), Lodge (Wounds of Civil War), Lyly (Endymion) and eight anonymous heroic/history plays
(Soliman and Perseda, Locrine, Selimus, Troublesome Reign of King John, Jack Straw, Edward III, Arden
of Faversham, True Tragedy of Richard III). Also fetched EarlyPrint copies of Spanish Tragedy, Faustus
and Edward II to measure the EarlyPrint-vs-EMED edition effect before trusting cross-source comparisons.
Greene and Peele now have four plays each: the first known-different authors in the corpus who wrote
the same kind of play in the same years as Marlowe.

Interruption: the disk filled (PyTorch install plus an already nearly full volume). Resumed after
Jamie freed space.

**Parser fix.** EarlyPrint's TCP transcriptions leave a speech without a speaker label outside any
`<sp>` element when the quarto printed none (the opening speech of Edward II, for instance). The first
parser dropped 2-5% of words that way, including Gaveston's opening soliloquy. Now any `<l>`/`<p>` not
inside a stage direction or heading is kept.

**Neural experiment design (scripts/finetune.py).** GPT-2 small (124M) fine-tuned from the same
checkpoint for 3 epochs on exactly the same number of tokens per model (the smaller of the Greene and
Peele corpora, about 79k GPT-2 tokens, drawn equally from each training play). Thirteen models:
Marlowe with two seeds, Marlowe split in two halves (Tamburlaine 1+2 + Dido vs Faustus, Jew, Edward II,
Massacre), later Shakespeare with two seeds and split in two halves, early Shakespeare without the Henry VI
family, Greene, Peele, the eight anonymous heroic plays, Fletcher.
(A) Behaviour: bits per token of every play under every model that did not train on it.
(B) Weights: cosine similarity between fine-tuning deltas, with the three controls that decide whether
the measurement means anything: seed-only pairs (same data), same-author-different-plays pairs, and
known-different pairs. If seed-only cosine is not clearly higher than different-author cosine, weight
comparison is uninformative at this scale, whatever it says about Marlowe and Shakespeare.

**Bug found in the scene scan.** The Shakespeare side of the scene scorers excluded the Henry VI
family but not Titus or any other scanned play, so the Titus scan was scoring Titus against a model
that had seen Titus. Every Titus ΔH was inflated towards Shakespeare (Act 1 at +0.94 was the giveaway:
too good to be true). Fixed by training the scorers per scanned play with its family excluded. The
Henry VI numbers were unaffected (that family was already excluded) but are re-run anyway.

### Session 2, step 4: the edition effect is as large as the author effect for character models

Measured directly (results/crossentropy_masked/edition_effect.md): the same play in its EarlyPrint
edition instead of its EMED edition scores about +0.04 bits/char worse under models trained on EMED or
Folger text, and about −0.06 bits/char better under models trained on EarlyPrint text. Gutenberg's
Dyce edition is worse still (+0.12). The author affinities I have been reading are 0.03-0.10 bits/char.
So in the six-model cross-entropy table, "Henry VI prefers Marlowe (EMED) to Greene (EarlyPrint)" is
contaminated by "Folger text is nearer EMED text than EarlyPrint text". Word-frequency features are much
less affected (the earlier cosine-delta check gave 0.01-0.05 against ~1.0 between plays), but the
character model sees spelling and tokenisation conventions that editors leave behind.

Consequence: every cross-source comparison with character models is suspect, including some I
reported in REPORT.md v1 (Marlowe EMED vs Shakespeare Folger). Fix: build a second corpus in which
every text comes from the same pipeline. EarlyPrint has the 1623 Folio (TCP A11954), all seven Marlowe
plays and all the 1587-94 controls. Replicating on that corpus is the right test; the Folger/EMED corpus
keeps its value for the word-level tests and for scene boundaries.

### Session 2, step 5: register-matched benchmarks (function-word chunk classifiers, results/func)

| pair | type | acc | AUC |
|---|---|---|---|
| Marlowe vs Shakespeare early, Henry VI excluded | question | 0.85 | 0.92 |
| Marlowe vs Greene | different author, same register and years | 0.59 | 0.68 |
| Marlowe vs Peele | different author, same register and years | 0.60 | 0.62 |
| Greene vs Peele | different, same register | 0.60 | 0.71 |
| Marlowe vs anonymous heroic 1587-94 | different | 0.75 | 0.80 |
| Shakespeare early vs Greene | different | 0.70 | 0.70 |
| Shakespeare early vs Peele | different | 0.81 | 0.82 |

Two readings, and I think both are right:
- Function-word classifiers at 2000 words with 4-7 plays a side can barely tell Greene from Peele or
  either from Marlowe. The register swamps the author. Anyone who reports "Marlowe is distinguishable
  from Shakespeare" with these tools and no register-matched control is reporting the register.
- And yet early Shakespeare outside Henry VI is *more* distinguishable from Marlowe (0.85) than Greene
  or Peele are (0.6). If one hand wrote both, it would have to have changed more between Edward II and
  Titus/Richard III than Marlowe differs from his imitators. Not impossible, but the pattern runs the
  wrong way for the hypothesis.

### Session 2, step 6: all-EarlyPrint replication corpus (data/clean_ep, results/ep)

Every text from one pipeline: Shakespeare from the 1623 Folio (TCP A11954, split by play), Marlowe from
the early quartos (Tamburlaine 1590 split into its two parts), Kyd, Peele, Lyly, the two anonymous
plays and the 17 added controls all from EarlyPrint. Same play ids as the main corpus so every script
runs unchanged with `CORPUS=ep`. Word counts agree with the Folger/EMED corpus within about 1%, which
is a useful check that both pipelines extract the same dialogue. Fletcher, Ford and the three later
controls are absent (not needed for the register question; they are in the main corpus).

What this corpus can and cannot settle: cross-entropy and classifier comparisons between any two
authors are now free of editorial-source effects. The price is Folio text for Shakespeare, which is a
1623 printing of plays written in 1590-1594, with compositors' spellings regularised by MorphAdorner
rather than by an editor; the character models will see more printing-house noise than before.

**GI verification replicates on the all-EarlyPrint corpus (results/ep/gi_verify):** early Shakespeare
outside Henry VI 0.06 as Marlowe / 0.86 as Shakespeare (main corpus 0.05 / 0.89); Henry VI 0.41 as
Marlowe, 0.56 as anonymous-heroic, 0.29 as Shakespeare (main 0.55 / 0.53 / 0.38); Marlowe's own plays
0.47 as Marlowe, 0.50 as Peele (main 0.52 / 0.51). Function-word results are not an artefact of the
editions. The Folio text, if anything, pulls Henry VI slightly further from Marlowe and towards the
anonymous heroic plays.

### Session 2, step 7: character models on the all-EarlyPrint corpus (results/ep/crossentropy_masked)

Six size-matched models (about 290k characters each, equal share from every training play, proper
nouns masked, families excluded). Double-centred affinities, group means:

| held-out group | Marlowe | Sh-early | Sh-later | Greene | Peele | Anon-heroic |
|---|---|---|---|---|---|---|
| Marlowe plays | -0.021 | +0.030 | +0.057 | -0.022 | **-0.047** | +0.002 |
| Henry VI 1-3 | -0.010 | +0.027 | -0.016 | +0.019 | +0.009 | **-0.029** |
| Tit, R3, Shr, TGV, Err | +0.033 | -0.033 | **-0.044** | +0.015 | +0.025 | +0.004 |
| Shakespeare later | +0.035 | -0.040 | **-0.090** | +0.035 | +0.040 | +0.020 |
| Greene plays | **-0.031** | +0.019 | +0.063 | -0.010 | -0.029 | -0.011 |
| Peele plays | **-0.040** | +0.029 | +0.058 | -0.032 | -0.007 | -0.008 |

What this says, honestly:
- Within the 1587-92 heroic group the character models do not identify authors at all. Marlowe's own
  plays are best predicted by the Peele model (Tamburlaine 1 and 2, Edward II) or the Greene model
  (Dido, Faustus); Greene's and Peele's plays are best predicted by the Marlowe model. With ~55k words
  of training text, a 6-gram character model learns the register, not the writer. The earlier,
  single-source result "Marlowe's plays recognise each other" was partly the register plus the
  Folger/EMED-versus-EarlyPrint edition offset that step 4 measured. I was wrong to lean on it in
  REPORT.md v1, and the report is corrected.
- What survives, now source-fair: Shakespeare outside Henry VI is best predicted by Shakespeare
  (early or later) and worst by Marlowe, and the raw gap H(Marlowe) − H(Sh-early) for those plays is
  +0.072 bits/char, while Greene's and Peele's plays sit at −0.044 and −0.063. Shakespeare's early
  comedies, Titus and Richard III are far more alien to a Marlowe model than Marlowe's imitators are.
- Henry VI 1-3 land on the anonymous-heroic model, with Marlowe second. Nothing specific to Marlowe.

Function-word benchmarks replicate on this corpus (Marlowe vs non-H6 early Shakespeare 0.86 / 0.94;
Marlowe vs Greene 0.57 / 0.60; Marlowe vs Peele 0.57 / 0.61; Greene vs Peele 0.60 / 0.71).

Idea not yet tested: the Cade scenes of 2H6 are mostly prose; none of the scorers controls for
prose/verse balance. A prose-only and verse-only split of the training sets would settle whether the
"Marlowe-ward" Cade result is a prose effect. Folger text does not mark prose explicitly, but line
length and capitalisation at line start would separate it well enough.

### Session 2, step 8: is the Cade-scene result a prose effect? (results/scene_scan/prose_verse.md)

Marlowe's verse and prose separated with EMED's line markup (104k verse words, 9k prose); Shakespeare's
with the Folger layout convention that prose speeches carry the speaker label inline (191k verse, 109k
prose, Henry VI family excluded). Verse scenes are then judged only by verse-trained models.

| 2 Henry VI | verse words | P(Marlowe) verse-only | ΔH verse-only |
|---|---|---|---|
| Cade scenes 4.2-4.10 | 2041 | 0.71 | +0.085 |
| all other scenes | 17176 | 0.33 | +0.164 |

The Marlowe-ward lean of the Cade scenes survives when verse is compared only with verse, on both
scorers. So it is not a prose artefact. It remains a register-level statement (the verse models cannot
tell Marlowe from Greene or Peele either), but it is the same statement Craig and Kinney made with
different tools, and it does not appear in Richard III or in the rest of 2 Henry VI. In 1 Henry VI the
verse-only scan no longer orders the scenes as Taylor does (Shakespeare scenes 0.53 Marlowe, Nashe act
0.44): the earlier ordering was partly carried by the prose share of Act 1. One more reason to treat
scene-level numbers on 300-1000-word scenes as suggestive only.

### Session 2, step 9: Folio vs quarto, and a third corpus (results/q)

Checked whether the Folio printing itself separates Titus and Richard III from Marlowe
(results/ep/crossentropy_masked/quarto_check.md). Same models, same masking:

| text | H(Marlowe) − H(Sh-early) |
|---|---|
| Titus, Folio 1623 | +0.037 |
| Titus, Q1 1594 | +0.011 |
| Richard III, Folio 1623 | +0.042 |
| Richard III, Q1 1597 | −0.014 |

The 1590s quartos sit measurably nearer the Marlowe model than the Folio texts do. Part of what the
character models call "Marlowe" is 1590s printing-house spelling that MorphAdorner's regularisation
does not fully remove, and the Shakespeare models, trained on Folio text, carry 1623 habits. The
right comparison for character models is quarto against quarto.

Built corpus `q`: Shakespeare only from early quartos (Titus 1594, Richard III 1597, the reported
texts of 2 and 3 Henry VI from 1594-5 standing in for those plays, and R2, Rom Q1, 1H4, LLL, MND, MV,
Ado, 2H4, Lr, Tro from 1597-1609); Marlowe and all controls as in the EarlyPrint corpus. 1 Henry VI,
Shrew, Two Gentlemen and Errors have no early quarto and drop out. The two reported Henry VI texts are
memorial reconstructions, shorter and rougher than the Folio versions, so they are a test of the
reporters' memory of the plays as much as of the plays; flagged accordingly.


### Session 2, step 10: quarto-only corpus results (results/q)

Caveat first: with only four early plays and three of them one family (the two reported Henry VI texts
and Richard III), the "Sh-early" character model in this corpus is a single play whenever a family
member is held out. Its numbers are meaningless; the fair Shakespeare comparator here is the
ten-quarto Sh-later model. Function-word results are unaffected by this.

Function words (GI verification): Titus and Richard III quartos score 0.07 as Marlowe and 0.91 as
Shakespeare; later-quarto Shakespeare 0.04 / 0.98; Marlowe's plays 0.49 / 0.13; the reported Henry VI
texts 0.30 Marlowe / 0.31 Shakespeare / 0.60 anonymous-heroic. The chunk classifier separates Marlowe
from the ten later quartos at 0.93 / 0.98. Function-word conclusions survive the change of printing.

Character models (raw gaps, bits/char; negative = Marlowe model predicts the text better):

| corpus | play / group | H(Marlowe) − H(Sh-later) | H(Marlowe) − H(Greene) | H(Marlowe) − H(Peele) |
|---|---|---|---|---|
| ep (Folio) | Tit | -0.014 | -0.109 | -0.061 |
| ep (Folio) | R3 | +0.087 | -0.083 | -0.074 |
| ep (Folio) | 2H6 | +0.030 | -0.092 | -0.092 |
| ep (Folio) | 3H6 | -0.005 | -0.096 | -0.090 |
| ep (Folio) | Greene plays | -0.094 | -0.086 | -0.080 |
| ep (Folio) | Peele plays | -0.097 | -0.074 | -0.111 |
| ep (Folio) | Marlowe plays | -0.078 | -0.064 | -0.052 |
| q (quartos) | Tit | -0.066 | -0.120 | -0.062 |
| q (quartos) | R3 | +0.044 | -0.081 | -0.064 |
| q (quartos) | 2H6 | -0.029 | -0.087 | -0.068 |
| q (quartos) | 3H6 | -0.053 | -0.084 | -0.072 |
| q (quartos) | Greene plays | -0.086 | -0.086 | -0.080 |
| q (quartos) | Peele plays | -0.088 | -0.074 | -0.111 |
| q (quartos) | Marlowe plays | -0.084 | -0.064 | -0.052 |

Reading: on quarto text, Titus and Richard III are predicted about equally by the Marlowe model and by
the later-Shakespeare model (gap ≈ 0), whereas on Folio text they were clearly Shakespeare's
(+0.04 to +0.08). Greene's and Peele's plays, and Marlowe's own, stay at −0.08 to −0.09. So with
printing matched, Titus and Richard III sit halfway between the heroic-register plays and later
Shakespeare, which is what chronological drift plus genre would predict for 1592-93 tragedies by a
different author, and is also what a Marlowe who changed his style would produce. The character
models cannot adjudicate; the function-word tests can, and they do not put these plays with Marlowe.
The reported Henry VI texts behave like the anonymous heroic plays (Peele/anonymous models best).

Correction to the paragraph above, on re-reading the table: the two plays differ. Titus is nearer the
Marlowe model than the later-Shakespeare model on both printings (−0.014 Folio, −0.066 quarto);
Richard III is nearer later Shakespeare on both (+0.087, +0.044). Neither is as Marlowe-like as
Greene's or Peele's plays (−0.09). And the Greene model is weak in general: Greene's own plays are
predicted better by the Marlowe model than by the Greene model (−0.086), which says the Marlowe model
is the best general model of the heroic register, not that Greene wrote like Marlowe in particular.
Character models at this scale are register detectors. I will say so in the report and lean on the
function-word tests, which have calibrated known-same and known-different behaviour.

### Session 2, step 11: GPT-2 fine-tunes, and the answer to the original question (results/finetune)

Thirteen GPT-2 small models, each fine-tuned from the same checkpoint on 78,818 tokens (equal share
from every training play), 3 epochs. The experiment Jamie first proposed, with the controls that
decide whether it can mean anything.

**(B) Comparing the weights.** Cosine similarity between fine-tuning deltas (all non-embedding
parameters):

| pair | type | cosine |
|---|---|---|
| Marlowe seed 1 vs seed 2 (same text) | seed noise only | 0.777 |
| Shakespeare-later seed 1 vs seed 2 (same text) | seed noise only | 0.750 |
| Marlowe plays A vs Marlowe plays B | same author, different plays | 0.272 |
| Shakespeare-later A vs B | same author, different plays | 0.270 |
| Shakespeare early (non-H6) vs later | same author, different period | 0.271 |
| Marlowe vs Greene / Peele / anonymous heroic | different author, same register | 0.270 / 0.265 / 0.273 |
| Greene vs Peele | different author, same register | 0.276 |
| **Marlowe vs Shakespeare early (non-H6)** | the question | **0.232** |
| Marlowe vs Shakespeare later | different period | 0.213 |
| Shakespeare early vs Greene / Peele | different author, different register | 0.211 / 0.205 |
| Marlowe vs Fletcher | different author, different period | 0.224 |

Reading: the delta is 0.75-0.78 similar to itself across seeds and 0.21-0.28 similar to anything
else. Same author on different plays (0.27) is indistinguishable from different authors in the same
register (0.27). So at this scale the weights encode *which text* the model saw, then *which
register*, and nothing detectable about *which author*. The pair in question, 0.232, lands with the
cross-register pairs (0.21-0.22), not with the same-register pairs (0.27), which is the same thing the
other methods say about register, and says nothing about authorship. Comparing weights was not a way
to answer the question. It is nice to have the measurement rather than the argument.

**(A) Comparing behaviour.** Bits per token of held-out plays. Marlowe's own plays (scored by the
Marlowe model trained on the other half of his canon) are predicted slightly *better* by the Peele
model in five cases of seven (e.g. Tamburlaine 1: Peele 6.17, Marlowe 6.20, anonymous 6.19). Every
Shakespeare play, Henry VI included, is best predicted by a Shakespeare model, by 0.1-0.2 bits.
Caveat that applies to the Shakespeare comparisons here: this run used the Folger/EMED corpus, so the
Marlowe-vs-Shakespeare gap includes the edition offset measured in step 4. The Marlowe-vs-Peele/Greene
comparison is EMED vs EarlyPrint and suffers the same way, in the other direction, yet Peele still
wins. A rerun on the all-EarlyPrint corpus is in progress to remove the offset.

### Session 2, step 12: GPT-2 replication on the all-EarlyPrint corpus (results/ep/finetune)

Weights: seed-only cosines 0.78 / 0.76; every other pair 0.25-0.30; same-author pairs 0.27-0.30;
Marlowe vs early Shakespeare 0.27, now inside the same-register band. Same verdict: no author signal.

Behaviour, now source-fair (bits per token, lower is better):

| play | Marlowe (other half) | Sh-early non-H6 | Sh-later | Greene | Peele | Anon-heroic |
|---|---|---|---|---|---|---|
| 1 Tamburlaine | 6.26 | 6.39 | 6.43 | 6.22 | **6.18** | 6.19 |
| Edward II | 5.89 | 5.95 | 6.01 | 5.86 | 5.79 | **5.78** |
| Faustus | 6.00 | 6.00 | 6.05 | **5.87** | 5.93 | 5.91 |
| 2 Henry VI | 6.16 | 6.10 | **6.05** | 6.26 | 6.24 | 6.11 |
| 3 Henry VI | 6.03 | 5.98 | **5.92** | 6.14 | 6.14 | 5.96 |
| 1 Henry VI | 6.17 | 6.14 | **6.10** | 6.26 | 6.26 | 6.14 |
| Titus | 6.18 | (train) | 6.16 | 6.26 | 6.19 | **6.16** |
| Richard III | 6.10 | 5.95 | **5.87** | 6.19 | 6.16 | 6.02 |

Marlowe's plays are predicted best by Peele, Greene or the anonymous model in six of seven cases; the
Henry VI plays and Richard III are predicted best by Shakespeare models, with the Marlowe model the
worst of the register models for Henry VI. A 124M-parameter model with 78k tokens per author sees
register first, and within register it does not pick out Marlowe; but it does pick out Shakespeare for
Henry VI, which the character n-grams did not. I would not build on that last point without a larger
token budget, because the Shakespeare models here are trained on text printed in 1623 like the Henry VI
plays themselves, and the quarto corpus is too thin to repeat the neural run.

Closing thought for the day: five methods, three corpora, and the same shape every time. Shakespeare
outside Henry VI is not Marlowe. Henry VI and Marlowe both sit in a crowded room with Greene, Peele,
Kyd and a dozen anonymous hands, and nothing here can tell those occupants apart.


## Session 3 (2026-10-31): word-level tests

**Prompt.** Jamie asked whether any word-frequency analysis had been done. The honest answer was: the
function-word and MFW features *are* word frequencies, but no per-word comparison had ever been
reported, and Zeta sat in "next steps". Both are now implemented in `scripts/word_profiles.py`, run on
the main and EP corpora, and shown on the site.

**Step 13: per-word profiles.** 190 function words plus every word present in >= 60% of plays, names
masked, rates per 1,000 words per play, ranked by Cohen's d across plays. The Marlowe-vs-early-Shakespeare
list is readable at a glance: Marlowe has *shall, whether, about, die, live, might, now*; Shakespeare has
*you, her, say, very, indeed, marry, fool, patience, tongue*. The second list is comic prose. I had
expected function words to dominate the top of a d-ranked list and they do, but content words from the
60%-presence set are right behind them.

**Step 14: Zeta.** Implemented per Burrows 2007 with the Craig/Kinney scoring (share of A-markers vs
share of B-markers per chunk, nearest centroid). Three bugs in sequence:

1. Sets consisting of one plot family (Henry VI 1-3) could never be scored: holding out one part removed
   all three from training. Fixed by holding out only the play on its own side when the family rule would
   empty the side, and recording in the report that this flatters Henry VI's cohesion.
2. *tamburlaine* appeared as a Marlowe marker. The EMED regulariser lower-cases the name in about half its
   occurrences, so the per-play capitalisation rule (>= 90%) missed it. Added a corpus-wide pooled rule
   (>= 60% capitalised over >= 5 uses). 1,691 name-like words are now masked.
3. *s* appeared as a Shakespeare marker: the Folger editions print "in 's" for "in his", and the
   tokeniser produced a bare *s*. Single-letter tokens other than a/I/O are now dropped. This artefact
   does not touch the function-word results (no single-letter feature) and the MFW runs replicate on the
   EP corpus, which has no such tokens, so I did not rerun them.

**Result.** Zeta fails the acceptance test. Greene vs Peele 0.44 / 0.43 (main / EP), Marlowe vs Peele
0.49 / 0.54, Marlowe vs anonymous heroic 0.70 / 0.57. It does separate Marlowe from non-Henry VI early
Shakespeare (0.79 / 0.85), but it separates Shakespeare 1595-97 from 1599-1611 almost as well
(0.74 / 0.72), and the marker lists are transparently genre vocabulary (war words vs conversation words).
Projected onto Marlowe-vs-Shakespeare markers, 1 and 3 Henry VI fall on Marlowe's side, and so does
every Greene, Peele and anonymous heroic play. Same conclusion as every other method, with the mechanism
now visible word by word.

**Thought.** This closes the "try Zeta" item honestly: it was the method most likely to split the
register, and it does not. Word-adjacency networks are the remaining published candidate. The per-word
tables are probably the most useful thing on the site for a non-specialist reader, because they turn
"Marlowe-like" into a list of words one can check against a page of text.

## Session 4 (2026-10-31): relative embedding geometry

**Idea (Jamie):** the weight comparison looked at the whole parameter delta, and it excluded the token
embeddings. What about the embeddings, and specifically the *relative* positions of words: even if two
models put a word in different places, is the vector between two words the same, and is that meaningful?

**My assessment before running it.** Distances between words are scalars and survive any rotation of
the space, so they are the right thing to compare across models; difference vectors are not, unless the
spaces share coordinates (ours do, by shared initialisation, so both can be reported). Expectations
written down before the run: (1) the raw pairwise distances will be near-identical across all thirteen
models, because 78,818 tokens cannot move a pretrained geometry, so the test has to use the *change* in
distance; (2) the words that move are the frequent ones, so this risks being a noisier function-word
test; (3) register will dominate again. Acceptance bar unchanged: same-author pairs must sit above
different-author same-register pairs.

**Step 15: implementation.** `finetune.py` part (C), run with `EMB_ONLY=1` so the perplexity and
task-vector files from 30 October are not overwritten by a re-run with slightly different numbers. Word
list fixed before training: 400 whole-word, lower-case GPT-2 tokens with at least three uses in every
model's training text, ranked by the smallest count across sets (*the, and, to, of, my, a, in, that, be,
with ... mad, beauty, horse, lies*). Names and sentence-initial forms are excluded by the lower-case
rule. Per model pair, three numbers: correlation of the raw pairwise-cosine matrices; correlation of the
change in pairwise cosine from pretrained (the relative test, coordinate-free); cosine of the embedding
deltas over those rows (the embedding-layer twin of the task-vector cosine). Same thirteen models, seeds
and budget. Raw rows saved to `embeddings.npz` so the analysis can be redone without retraining. About 40
minutes per corpus.

**Result, Folger/EMED corpus.** Raw geometry: 0.9999 for every pair, mean absolute change in a pair's
cosine 0.0005 (expectation 1 confirmed). Change in geometry: seed-only 0.94 / 0.93; same author, other
plays 0.46 (Marlowe) / 0.40 (Shakespeare later); same author, other period 0.39; Marlowe vs Greene /
Peele / anonymous heroic 0.43 / 0.45 / 0.46; Greene vs Peele 0.38; the question 0.41; Marlowe vs
Fletcher 0.31. Embedding-delta cosine gives the same ordering at lower values (seed 0.90, everything
else 0.23 to 0.34).

**Thought.** Two things I did not expect. The seed ceiling is 0.93, far above the 0.78 of the full weight
delta, so the embedding geometry is a much less noisy measurement than the task vector; expectation (2)
was too pessimistic about noise. And yet the author gap is still absent: Marlowe against his own other
plays equals Marlowe against the anonymous heroic plays, and the ordering of every pair is the register
and period ordering (inside the 1587-92 register mid 0.40s, across periods 0.31-0.39, Fletcher the
floor). A cleaner instrument that finds nothing is stronger evidence than a noisy one. What the
geometry records is which words co-occur in the training text, which is register and period. This is the
coordinate-free version of the original idea, and it closes it on the same grounds as the weight delta.
EP replication: see below.
