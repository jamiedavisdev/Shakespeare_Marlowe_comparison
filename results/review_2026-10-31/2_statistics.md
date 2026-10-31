# Independent review 2 of 4: statistical methodology (2026-10-31)

Brief: evaluate inferential logic and statistical validity. Reviewer re-implemented the project's feature pipeline (function words, 2,000-word chunks, LOO by play with family hold-out, LR C=0.1), reproduced the headline numbers exactly, then added play-level cluster bootstrap, a permutation null, extra splits, and size-matched / period-restricted impostors pools.

## Verdict
The study is well built for what it directly measures, but its decisive inference rests on a register-mismatched comparison (seven heroic verse plays vs a set that is three-fifths comedy), and the same classifier separates Shakespeare's own 1591-94 histories/tragedies from his own 1591-94 comedies at 0.78-0.83 accuracy, nearly matching the 0.85-0.86 reported for the question pair. When the comparison is register-matched (Marlowe's 1589-93 plays vs Titus and Richard III) the classifier is at chance (acc 0.52-0.54, AUC 0.50-0.51 on both corpora), and no method in the report has demonstrated power inside that register (Greene vs Peele 0.60 [0.43, 0.81]). The honest conclusion is therefore weaker than "the evidence does not support a single author": with these methods and sample sizes the data cannot distinguish two authors from one author who wrote in two registers, the report quantifies no uncertainty anywhere, and the bottom-line claim that early Shakespeare is "further from Marlowe than Marlowe's own imitators are" holds for the comedies only, not for the two tragedies, and depends on the feature set.

## Findings, ranked by threat to the conclusion

### 1. The decisive comparison is confounded with register, and the same-author register split reproduces it. (serious, borders on fatal for claim 1)
Function words, play-level cluster-bootstrap 95% CI in brackets; main / EP corpus:
- Question pair, Marlowe vs {Tit, R3, Shr, TGV, Err}: acc 0.85 [0.74, 0.95] / 0.86 [0.76, 0.95]; AUC 0.92 / 0.94.
- Same author, same years, register split: {1H6, 2H6, 3H6, Tit, R3} vs {Shr, TGV, Err}: acc 0.78 [0.71, 0.86] / 0.83 [0.77, 0.90]; AUC 0.83 / 0.87; play-level AUC 1.00 on both corpora.
- Marlowe vs comedies only: 0.79 / 0.83, AUC 0.91 / 0.93. Marlowe vs {Tit, R3} only: 0.68 / 0.67, AUC 0.60 [0.47, 0.76] / 0.58 [0.48, 0.70].
- Late Marlowe {Faustus, JoM, Ed2, MP} vs {Tit, R3}: acc 0.52 [0.42, 0.62] / 0.54 [0.46, 0.61]; AUC 0.51 / 0.50. Chance on both corpora. (One play on the B training side in each fold, so low power; but {Tit, R3} vs Greene gives the same 0.54 / 0.54, and vs Peele 0.71 / 0.65.)
- Per-play P(Marlowe) in the question pair: Tit 0.43, R3 0.35, Shr 0.34 sit next to the boundary; TGV 0.04 and Err 0.08 carry the accuracy. Prose share: Tit 4%, R3 5%, Marlowe plays 0-3% (Faustus 48%, MP 17%); Shr 21%, TGV 29%, Err 15%.
- Distance matrix: mean Marlowe to {Tit, R3} = 1.03; Henry VI to comedies (same author, same years) = 1.04; Marlowe to comedies = 1.15; R3 to its own sibling 3H6 = 0.97 vs R3 to Ed2 = 0.97.

The report's test logic assumes the method can see a hand across a register change. The report's own data show Shakespeare's hand is not visible across his own register change with this method.

What does survive: a permutation over all 792 seven/five relabellings of the 12 plays puts the actual Marlowe/Shakespeare split first (acc 0.85, AUC 0.92; null median 0.46 / 0.41; p = 0.001). But the second- and third-best splits move Faustus and JoM to the Shakespeare side at 0.81 / 0.91, and the fourth-best, {1Tam, 2Tam, Dido, Ed2, MP, Tit, R3} vs {Faustus, JoM, Shr, TGV, Err} at 0.76 / 0.87, is a pure register partition crossing the author line. For Marlowe vs Greene, the actual labelling is not distinguishable from random relabellings (acc p = 0.21, AUC p = 0.06).

### 2. No uncertainty is quantified anywhere; chunk dependence within plays is never acknowledged; the key gaps are inside the noise. (serious)
Effective n is 7 vs 5 plays (question), 8 vs 11 (same-author benchmark), 7 vs 4 (Greene, Peele), 4 vs 4 (Greene vs Peele). Play-level cluster bootstrap:
- Question 0.85 [0.74, 0.95] vs same-author Sh early/later 0.79 [0.70, 0.88]: not distinguishable.
- Question vs Marlowe-Greene 0.59 [0.45, 0.72] and Marlowe-Peele 0.60 [0.44, 0.76]: CIs barely clear, and finding 1 explains the gap.
- Greene vs Peele 0.60 [0.43, 0.81], AUC 0.71 [0.47, 0.99]: the "different-author same-register" benchmark is itself indistinguishable from chance.

### 3. The impostors (GI) scores are inflated by candidate-pool size and summarised in a way that hides a poorly calibrated per-play distribution. (serious)
Shakespeare has 18 candidates, Marlowe 5-6, Greene and Peele 3-4; the score takes the minimum distance over candidates. With a random 6-play Shakespeare pool (30 draws): Tit 0.76 to 0.52, Shr 0.86 to 0.47, TGV 0.85 to 0.68, R3 0.99 to 0.84, Err 0.91 to 0.80. The headline "0.89 as Shakespeare" becomes roughly 0.66 when size-matched, against Marlowe's own self-score of 0.52.
Per-play calibration: same-author scores for register-matched authors range 0.09-0.96 (1Tam as Marlowe 0.09); different-author scores range 0.01-0.99 (1Tam and 2Tam as Peele 0.99, Alcazar and David as Marlowe 0.81). Treating each play as one observation, same-vs-different AUC is 0.70 on both corpora. The report's "0.47-0.67" and "0.05-0.35" are ranges of group means, not of plays.
Edward II verifies as Shakespeare at 0.66 (main) / 0.47 (EP) and Faustus at 0.52 / 0.66, inside the report's own "same-author" band. 1H6 and 3H6 verify as Marlowe at 0.61 / 0.68 and as Shakespeare at 0.10 / 0.15.
Removing other Shakespeare plays from the impostor pool raises the five plays' "as Marlowe" scores only modestly (R3 0.05 to 0.17, Err 0.06 to 0.16, Tit 0.18 to 0.22), a fair point for the report's side; but 1Tam and 2Tam score 0.00 and 0.10 as Marlowe under the same conditions.

### 4. Feature-set selection: the "imitators are closer than Shakespeare" inequality holds for function words and reverses for mfw150. (serious)
From `results/mfw150/pairwise_distinguishability.md` (main): Marlowe vs Greene 0.83 / 0.93, Marlowe vs Peele 0.66 / 0.73, Greene vs Peele 0.75 / 0.78, question pair 0.79 / 0.87. Under mfw150 Greene is more separable from Marlowe than early Shakespeare is. mfw500 (main): Greene 0.73 / 0.76, Peele 0.51 / 0.47, question 0.82 / 0.90. The report sentence "separates Marlowe from Greene or Peele at only 0.57-0.60" is true of one of three feature sets.
The script pre-registers "Marlowe vs Shakespeare early, histories/Titus only (genre-matched)" (0.43 / 0.36 func main; 0.38 / 0.30 EP). The row never appears in REPORT.md or NOTEBOOK.md. It is degenerate (family rule leaves Titus alone on the B side), but silently dropping the one pre-registered register-matched test is the wrong way to handle a broken row.

### 5. The Zeta acceptance test is sound in spirit but applied selectively, and has almost no power. (serious as an argument)
Greene vs Peele: 4 vs 4 plays, 52 chunks; both canons mix heroic plays with comedies/romances and damaged texts. The function-word classifier, which the report treats as decisive, scores 0.60 [0.43, 0.81] on the same test. By the report's own criterion the decisive method also fails. The criterion is used to discount Zeta's Henry VI result but not the function-word five-play result, which rests on the same register-mismatched comparison.

### 6. "Replication on both corpora" is an edition-robustness check, not a replication. (minor)
The 17 EarlyPrint controls are byte-identical files in both corpora; Marlowe differs only in regularisation of the same quartos. Edition effect 0.01-0.1 cosine delta against ~1.0 between plays, so agreement is nearly guaranteed for word-level methods. The methods are not independent either (chunk classifier, GI, Zeta and word profiles are four summaries of the same word frequencies).

### 7. Fine-tuned-weight cosines: the null is real for this metric, the generalisation is too broad, and one number is wrong. (minor)
- Seed-only cross-pair noise is about ±0.002, so same-author (0.270-0.272) equal to different-author-same-register (0.265-0.276) is a precise null.
- Centring (from the saved Gram matrix): seed pairs 0.60, every other pair in [-0.34, +0.05]; centring does not rescue an author signal.
- "The weights carry no detectable author signal" is not justified: embeddings and LM head were excluded, which is where lexical preference would live; no per-layer analysis, no linear probe.
- The diagonal of the cosine matrix is 1.013-1.015. A vector's cosine with itself is 1 by definition; norms and dot products were computed on different tensors (half vs float). Fix before citing.
- The question pair "sits with the cross-register pairs" (0.232, main) is not reproduced on EP (0.27).

### 8. Confounds
Handled: editorial source (strongest part of the study). Plot families. Proper nouns. Size matching (but see code audit).
Acknowledged but not removed: register/genre; prose/verse (only for 2H6); reported texts; collaboration in Titus.
Ignored: Edward III and Arden in the "anonymous heroic" set are widely attributed in part to Shakespeare; Dido's possible Nashe share; heterogeneity of control sets (Greene and Peele each mix comedy and heroic plays, lowering their benchmark accuracies, whereas the question pair's genre mix is aligned with the label); date overlap is a point the report could have used (TGV 1591, Shr 1592 overlap Ed2 1592 and MP 1593, so "one author who drifted" must be "one author who wrote in two registers at once").

### 9. Conclusion strength. (serious as framing)
"The evidence does not support a single author" is literally true. Bottom-line item 1 is overstated. Item 2 (Henry VI) and item 5 (Zeta) are fairly stated. Item 4 (weights) is right for the metric used and over-general beyond it. Understated: the permutation result (actual labelling is the best of 792 partitions) and the chronology-overlap argument are genuinely in the report's favour and are not made. Honest bottom line: no positive evidence for a single hand; the register-mismatched tests cannot bear on the question; the register-matched tests are at chance with CIs that include strong separation and no separation; the methods have no demonstrated power inside the 1587-93 heroic register, so the question is open on this evidence.

## Proposals, ranked by information gain per unit effort
1. Non-dramatic, same-genre, same-year texts. Hero and Leander (1593) against Venus and Adonis (1593) and Lucrece (1594). Controls: Chapman's continuation of Hero and Leander (1598; same poem, different hand: the ideal impostor), Lodge's Scilla's Metamorphosis, Drayton's Endimion and Phoebe, Heywood's Oenone and Paris, Marston's Pigmalion. Rolling 1,000-word chunks, function words plus MFW, GI with the epyllion impostors, bootstrap. If Hero and Leander chunks are nearer V&A/Lucrece than Chapman's continuation is, that is the first register-free support for one hand; if V&A/Lucrece are as far from Hero and Leander as Chapman's continuation is, the first register-free evidence against.
2. Report play-level uncertainty and the register-matched rows (low effort, high gain). Cluster bootstrap over plays for every row, play-level accuracy/AUC, the permutation over relabellings, and the four rows from finding 1.
3. Fix the GI method: size-matched candidate pools, per-play score distributions, held-out-pair calibration curve. If after size-matching Titus or R3 as Marlowe exceeds Marlowe's own median self-score (about 0.5), the five-play claim fails.
4. Positive control for scene-level power: run the scene scan on Henry VIII and Two Noble Kinsmen with Fletcher vs Shakespeare models. If the method recovers Fletcher's scenes at a stated accuracy, the 2H6 Cade result has a calibration; if not, drop the scene-level section.
5. Prose/verse stratification of the question pair: verse-only chunks of the five plays vs Marlowe's verse.
6. Word-adjacency networks (Segarra et al. 2016), with an acceptance check on a register-matched known-different pair first.
7. Chronological trajectory: project every play onto the Marlowe/later-Shakespeare axis and plot against date. Under one author who changed, late Marlowe, Tit, R3, R2 should form a continuum; under two authors, Ed2/MP and Tit/R3 should sit apart at the same date.
8. Equal-register benchmark set: Marlowe vs Greene-heroic and vs Peele-heroic; Shakespeare early histories vs later histories as the same-author register-matched benchmark.
9. Fine-tuning follow-up: include embeddings and LM head, per-module centred cosines, linear probe on deltas, fix the diagonal bug.

Scratch scripts (session-specific, may be gone): chunk_check.py, gi_check.py in the session scratchpad.
