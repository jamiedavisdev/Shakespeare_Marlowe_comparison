# Are Marlowe's plays and early Shakespeare by the same hand? Report, version 2

Date: 2026-10-30. Version 1 is kept at `results/REPORT_v1_2026-10-30.md`; the lab notebook
(`NOTEBOOK.md`) records every step, bug and change of mind. All numbers are reproducible from the
scripts (README.md).

## Bottom line

The evidence does not support a single author, and version 2 makes that case on firmer ground than
version 1 did, because it now includes the controls that matter most: three authors who wrote the same
kind of play as Marlowe in the same years (Greene, Peele, and eight anonymous heroic/history plays),
and a second corpus in which every text comes from one editorial pipeline.

1. **Shakespeare's early plays outside Henry VI (Titus, Richard III, Shrew, Two Gentlemen, Errors) are
   further from Marlowe than Marlowe's own imitators are.** A function-word classifier separates
   Marlowe from these five plays at accuracy 0.85-0.86 (AUC 0.92-0.94) on both corpora, but separates
   Marlowe from Greene or Peele at only 0.57-0.60. Under a Marlowe character model those five plays
   cost +0.07 bits/char more than under a Shakespeare model; Greene's and Peele's plays cost −0.04 and
   −0.06 (they are *better* predicted by Marlowe than by Shakespeare). The impostors verification test
   gives the five plays 0.05-0.06 as Marlowe and 0.86-0.89 as Shakespeare, against calibrated
   same-author scores of 0.47-0.67 and different-author scores of 0.05-0.35.
2. **The Henry VI plays belong to the heroic register of 1587-92, which no method here can split by
   author.** Within that register, Marlowe, Greene, Peele, Kyd, the anonymous plays and Henry VI 1-3
   are mutually confusable: Marlowe's own plays verify as Peele (0.50-0.51) as readily as Marlowe
   (0.47-0.52); character models predict Tamburlaine best with a Peele model. Henry VI's "Marlowe
   affinity" in version 1 was register plus an editorial-source artefact; on the single-source corpus
   the Henry VI plays land nearest the anonymous heroic plays.
3. **Scene-level results agree with published co-authorship work on 2 Henry VI but cannot go beyond
   it.** Both scorers put the Jack Cade scenes (4.2-4.10) nearer Marlowe than the rest of the play, as
   Craig and Kinney found, and the lean survives when verse is compared only with verse. Nothing
   comparable appears in Richard III. A first-pass ordering of 1 Henry VI that matched Taylor's
   Nashe/Shakespeare division did not survive the verse-only control.
4. **Comparing fine-tuned model weights, the original idea, does not work, and the controls show why.**
   A model's weight delta is 0.75-0.78 similar to itself under another random seed and 0.21-0.28
   similar to every other model, with same-author pairs no closer than different-author pairs.

If one person had written both canons, Marlowe's hand should be visible across early Shakespeare,
more visible there than in Greene and Peele, and visible in the comedies and in Richard III, not only
in the plays scholars already consider collaborative. None of that holds.

## What changed since version 1

- **Version 1 overstated the character-model evidence.** Its claim that "Marlowe's plays recognise
  each other" rested on a single-source comparison. Measuring the edition effect directly showed that
  swapping a play's edition (EMED vs EarlyPrint) moves its cross-entropy by 0.04-0.07 bits/char, the
  same size as the author affinities. On an all-EarlyPrint corpus, Marlowe's plays are predicted as
  well or better by Peele and Greene models. The character-model test cannot separate authors inside
  the 1587-92 heroic register at this data size. Word-level tests were unaffected (edition effect
  0.01-0.05 cosine delta against ~1.0 between plays), and they replicate exactly on the second corpus.
- **A training-set leak in the first scene scan** (Titus was scored by a model that had seen Titus)
  was found and fixed; the Henry VI scene results were unaffected.
- **Budget truncation** in the first cross-entropy run took plays in order, so the early-Shakespeare
  model was effectively Henry VI plus Titus. Now every model draws an equal share from every play.

## Corpora

| | Folger/EMED corpus (`data/clean`) | all-EarlyPrint corpus (`data/clean_ep`) | quarto corpus (`data/clean_q`) |
|---|---|---|---|
| Shakespeare | Folger editions, modern spelling | 1623 Folio (TCP A11954) | 1594-1609 quartos only; reported texts of 2 and 3 Henry VI stand in for those plays; 1H6, Shrew, TGV, Errors absent |
| Marlowe | Folger EMED regularised | 1590-1633 quartos, EarlyPrint | same |
| controls 1587-94 | EMED (Kyd, Peele OWT, Lyly, 2 anon) + EarlyPrint (17 plays) | all EarlyPrint | same |
| later controls, Fletcher, Ford | EMED | not included | not included |
| plays | 57 | 48 | 43 |

The quarto corpus exists because the character models proved sensitive to printing era: the 1594
Titus and 1597 Richard III quartos sit 0.03-0.06 bits/char nearer the Marlowe model than the Folio
texts of the same plays do (`results/ep/crossentropy_masked/quarto_check.md`).

Dialogue only, speaker labels and stage directions removed, proper nouns masked for character models.
"Families" (Henry VI 1-3 + Richard III + True Tragedy of Richard III; Tamburlaine 1+2; the two Shrews;
Spanish Tragedy + Soliman) are always held out together.

## Methods

- Word-frequency distances (cosine delta), clustering, PCA; three feature sets.
- Leave-one-play-out nearest-centroid attribution.
- Chunk classifiers (logistic regression, 2000-word chunks, leave-one-play-out) for pairs of sets,
  with same-author and different-author benchmark pairs.
- General Impostors verification (Koppel & Winter 2014), 200 rounds, random half of the features and
  12 random impostors per round.
- Character 6-gram Witten-Bell models per author, size-matched, proper nouns masked; raw
  cross-entropy gaps and double-centred affinities.
- Scene-level four-way scan (Marlowe / Shakespeare / Peele / Greene) of 1-3 Henry VI, Titus,
  Richard III.
- GPT-2 small fine-tuned per author with equal token budgets: held-out bits per token, and cosine
  similarity of weight deltas with seed-only and same-author controls.

## Results

### Chunk classifiers, function words (`results/func`, `results/ep/func`)

| pair | type | Folger/EMED acc / AUC | EarlyPrint acc / AUC |
|---|---|---|---|
| Marlowe vs Shakespeare early, Henry VI excluded | question | 0.85 / 0.92 | 0.86 / 0.94 |
| Marlowe vs Shakespeare later | question | 0.95 / 0.99 | 0.93 / 0.98 |
| Shakespeare early vs later | same author | 0.79 / 0.85 | 0.73 / 0.81 |
| Marlowe 1587-89 vs 1589-93 | same author | 0.56 / 0.59 | 0.55 / 0.60 |
| Marlowe vs Greene | different, same register | 0.59 / 0.68 | 0.57 / 0.60 |
| Marlowe vs Peele | different, same register | 0.60 / 0.62 | 0.57 / 0.61 |
| Greene vs Peele | different, same register | 0.60 / 0.71 | 0.60 / 0.71 |
| Shakespeare early vs Peele | different | 0.81 / 0.82 | 0.72 / 0.74 |
| Shakespeare later vs Fletcher | different, same period | 0.93 / 0.89 | n/a |

### Impostors verification (`results/gi_verify`, `results/ep/gi_verify`), mean score by target group

| target | as Marlowe | as Shakespeare | as Greene | as Peele | as Anon-heroic |
|---|---|---|---|---|---|
| Marlowe plays | 0.52 / 0.47 | 0.22 / 0.20 | 0.21 / 0.19 | 0.51 / 0.50 | 0.42 / 0.43 |
| Shakespeare early, Henry VI excluded | 0.05 / 0.06 | 0.89 / 0.86 | 0.04 / 0.03 | 0.19 / 0.21 | 0.21 / 0.26 |
| Henry VI 1-3 | 0.55 / 0.41 | 0.38 / 0.29 | 0.18 / 0.14 | 0.33 / 0.29 | 0.53 / 0.56 |
| Shakespeare later | 0.07 / 0.05 | 0.97 / 0.97 | 0.02 / 0.01 | 0.06 / 0.05 | 0.11 / 0.09 |
| Greene | 0.35 / 0.30 | 0.16 / 0.17 | 0.58 / 0.55 | 0.39 / 0.36 | 0.49 / 0.41 |
| Peele | 0.52 / 0.52 | 0.20 / 0.23 | 0.19 / 0.16 | 0.67 / 0.66 | 0.43 / 0.41 |

(Folger/EMED / EarlyPrint.)

### Character models (`results/ep/crossentropy_masked`, `results/q/crossentropy_masked`)

Raw gap H(Marlowe model) − H(later-Shakespeare model), bits/char, negative = the Marlowe model
predicts the text better:

| held-out | Folio corpus | quarto corpus |
|---|---|---|
| Marlowe's own plays | −0.078 | −0.084 |
| Greene's plays | −0.094 | −0.086 |
| Peele's plays | −0.097 | −0.088 |
| Titus | −0.014 | −0.066 |
| Richard III | +0.087 | +0.044 |
| 2, 3 Henry VI (Folio / reported texts) | +0.030, −0.005 | −0.029, −0.053 |
| Shrew, Two Gentlemen, Errors (Folio only) | +0.05 to +0.06 | n/a |
| later Shakespeare | +0.13 | +0.11 |

Two things follow. The character models are register detectors, not author detectors: Greene's and
Peele's plays are predicted *better* by the Marlowe model than Marlowe's own are, and better than by
their own authors' models. And within that limit, Shakespeare's early tragedies sit between the heroic
register and his later work (Titus nearer the register, Richard III nearer later Shakespeare), which
is what chronology plus genre predicts for a different author and is also compatible with one author
changing. The character models therefore do not decide the question; the calibrated function-word
tests do, and the quarto corpus replicates them (Titus and Richard III verify as Shakespeare at 0.91
and as Marlowe at 0.07).

The impostors test on the quarto corpus also replicates for the reported Henry VI texts: 0.30 as
Marlowe, 0.31 as Shakespeare, 0.60 as anonymous-heroic.

### Scene scan (`results/scene_scan/scene_scan.md`)

Word-weighted ΔH = H(Marlowe) − H(Shakespeare), bits/char, models trained without the scanned family:

| scenes | P(Marlowe) | ΔH |
|---|---|---|
| 1H6 Act 1 (Nashe) | 0.32 | +0.156 |
| 1H6 unattributed | 0.34 | +0.211 |
| 1H6 2.4, 4.2-4.7 (Shakespeare) | 0.30 | +0.239 |
| 2H6 Cade scenes 4.2-4.10 (Marlowe per Craig & Kinney) | 0.56 | +0.216 |
| 2H6 remainder | 0.23 | +0.243 |
| 3H6 | 0.46 | +0.191 |
| Titus | 0.08 | +0.240 |
| Richard III | 0.10 | +0.298 |

Titus with Peele as a candidate: P(Peele) 0.23 over the play; Act 1 (usually given to Peele) is
scored 0.18 Peele by function words, which is too weak to confirm or deny the attribution.

Verse-only check (`results/scene_scan/prose_verse.md`): with Marlowe's and Shakespeare's prose removed
from training and from the scenes, the Cade scenes still lean Marlowe-ward (P 0.71, ΔH +0.085) against
the rest of 2 Henry VI (0.33, +0.164). The result is not a prose artefact. The 1 Henry VI ordering, by
contrast, weakens in verse-only scoring and should not be leaned on.

## Neural models (`results/finetune`)

Thirteen GPT-2 small models fine-tuned from one checkpoint on identical token budgets (78,818
tokens each, equal share per play, 3 epochs); `results/finetune/taskvectors.md`, `perplexity.md`.

**Comparing the weights, with controls.** Cosine similarity between fine-tuning deltas:

| pair | type | cosine |
|---|---|---|
| same text, two seeds (Marlowe; Shakespeare-later) | seed noise | 0.78; 0.75 |
| same author, different plays (Marlowe A/B; Shakespeare-later A/B) | same author | 0.27; 0.27 |
| Shakespeare early vs later | same author, different period | 0.27 |
| Marlowe vs Greene; vs Peele; vs anonymous heroic | different author, same register | 0.27; 0.27; 0.27 |
| Greene vs Peele | different author, same register | 0.28 |
| **Marlowe vs Shakespeare early (non-Henry VI)** | the question | **0.23** |
| Marlowe vs Fletcher; Shakespeare early vs Peele | different author and register | 0.22; 0.21 |

A fine-tuned model's weight delta is 0.75-0.78 similar to itself under a new seed and 0.21-0.28
similar to anything else, with same-author pairs (0.27) indistinguishable from different-author pairs
in the same register (0.27). The weights record which text the model saw and which register it is in;
they carry no detectable author signal at this scale. The Marlowe-Shakespeare pair sits with the
cross-register pairs. This is the measured answer to the original proposal: comparing weights cannot
answer the question, and the control pairs show why.

**Comparing behaviour.** Held-out bits per token, all-EarlyPrint corpus (`results/ep/finetune/perplexity.md`),
so no edition offset: Marlowe's plays are predicted best by a Peele, Greene or anonymous-heroic model in
six of seven cases, not by the Marlowe model trained on the other half of his canon. Henry VI 1-3 and
Richard III are predicted best by Shakespeare models, and for Henry VI the Marlowe model is the worst of
the heroic-register models (2 Henry VI: Shakespeare-later 6.05, anonymous 6.11, Marlowe 6.16). The
same holds on the Folger/EMED corpus. The weight-delta cosines replicate on both corpora (seed-only
0.76-0.78, everything else 0.21-0.30, same-author pairs no closer than different-author pairs).

## Limits

- Seven Marlowe plays, two of them damaged texts. Eight early Shakespeare plays, three of them
  probably collaborative. Four plays each for Greene and Peele. Every test above is weak at this size;
  the strength of the conclusion comes from the same pattern appearing in every method on both corpora.
- Register and genre dominate every feature set. The register-matched controls expose this; they do
  not remove it. A method that separates Greene from Peele reliably would be needed to say anything
  author-specific about Henry VI.
- Prose/verse balance is controlled only in the 2 Henry VI check; the Marlowe prose corpus (9k words) is too small for prose-mode conclusions.
- The Folio is a 1623 printing of 1590s plays; the EarlyPrint regularisation is automatic, not
  editorial. The two corpora agree, which is reassuring, but neither is a critical edition of the
  original manuscripts, which do not exist.

## Next steps that would add real information

1. A method with demonstrated power inside the heroic register: word-adjacency networks (Segarra et
   al. 2016) or Burrows's Zeta on the same corpus, with Greene vs Peele as the acceptance test.
2. Early quartos of Titus (1594) and Richard III (1597) from EarlyPrint in place of the Folio text, to
   check that the Folio printing is not what separates them from Marlowe.
3. Larger neural models, or longer fine-tuning, if the task-vector test below shows seed noise is
   small enough to make weight comparison meaningful.
