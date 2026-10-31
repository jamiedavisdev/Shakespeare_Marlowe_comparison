# Pairwise distinguishability (leave-one-play-out logistic regression on 2000-word chunks)

Can a classifier trained on the *other* plays tell which set a held-out play's chunks belong to? For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; for different authors we expect values near 1. The question pair should be read against the two benchmarks.

| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |
|---|---|---|---|---|---|---|---|
| QUESTION  Marlowe vs Shakespeare early | 7 plays | 8 plays | 138 | 0.67 | 0.76 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, Henry VI excluded | 7 plays | 5 plays | 104 | 0.85 | 0.92 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched) | 7 plays | 4 plays | 99 | 0.43 | 0.36 | nan | nan |
| QUESTION  Marlowe vs Shakespeare later | 7 plays | 11 plays | 174 | 0.95 | 0.99 | nan | nan |
| QUESTION  Marlowe vs all Shakespeare | 7 plays | 19 plays | 257 | 0.88 | 0.92 | nan | nan |
| SAME-AUTHOR  Shakespeare early vs Shakespeare later | 8 plays | 11 plays | 202 | 0.79 | 0.85 | nan | nan |
| SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies | 4 plays | 4 plays | 83 | 0.66 | 0.78 | nan | nan |
| SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611 | 5 plays | 6 plays | 119 | 0.70 | 0.81 | nan | nan |
| SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93 | 3 plays | 4 plays | 55 | 0.56 | 0.59 | nan | nan |
| DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays) | 11 plays | 3 plays | 151 | 0.93 | 0.89 | nan | nan |
| DIFFERENT  Shakespeare early vs Fletcher | 8 plays | 3 plays | 115 | 0.93 | 0.91 | nan | nan |
| DIFFERENT  Marlowe vs Fletcher | 7 plays | 3 plays | 87 | 0.89 | 0.87 | nan | nan |
| DIFFERENT  Fletcher vs Ford | 3 plays | 2 plays | 51 | 0.51 | 0.46 | nan | nan |
| DIFFERENT  Shakespeare later vs Ford | 11 plays | 2 plays | 138 | 0.87 | 0.52 | nan | nan |
| DIFFERENT  Marlowe vs Ford | 7 plays | 2 plays | 74 | 0.80 | 0.88 | nan | nan |
| DIFFERENT  Marlowe vs Greene (same register, same years) | 7 plays | 4 plays | 83 | 0.59 | 0.68 | nan | nan |
| DIFFERENT  Marlowe vs Peele (same register, same years) | 7 plays | 4 plays | 82 | 0.60 | 0.62 | nan | nan |
| DIFFERENT  Marlowe vs anonymous heroic/history 1587-94 | 7 plays | 8 plays | 122 | 0.75 | 0.80 | nan | nan |
| DIFFERENT  Shakespeare early vs Greene | 8 plays | 4 plays | 111 | 0.70 | 0.70 | nan | nan |
| DIFFERENT  Shakespeare early vs Peele | 8 plays | 4 plays | 110 | 0.81 | 0.82 | nan | nan |
| DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94 | 8 plays | 8 plays | 150 | 0.65 | 0.76 | nan | nan |
| DIFFERENT  Greene vs Peele | 4 plays | 4 plays | 55 | 0.60 | 0.71 | nan | nan |
| DIFFERENT  Henry VI 1-3 + Titus vs Greene | 4 plays | 4 plays | 72 | 0.57 | 0.56 | nan | nan |
| QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison) | 4 plays | 7 plays | 99 | 0.43 | 0.36 | nan | nan |

# Per-play mean P(set A), words model


## QUESTION  Marlowe vs Shakespeare early

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.62 | nan |
| 2Tam (Marlowe) | A | 0.87 | nan |
| Dido (Marlowe) | A | 0.67 | nan |
| DrFaust (Marlowe) | A | 0.53 | nan |
| JoM (Marlowe) | A | 0.47 | nan |
| Ed2 (Marlowe) | A | 0.53 | nan |
| MP (Marlowe) | A | 0.72 | nan |
| 2H6 (Shakespeare) | B | 0.49 | nan |
| 3H6 (Shakespeare) | B | 0.62 | nan |
| 1H6 (Shakespeare) | B | 0.68 | nan |
| Tit (Shakespeare) | B | 0.20 | nan |
| R3 (Shakespeare) | B | 0.35 | nan |
| Shr (Shakespeare) | B | 0.14 | nan |
| TGV (Shakespeare) | B | 0.03 | nan |
| Err (Shakespeare) | B | 0.04 | nan |

## QUESTION  Marlowe vs Shakespeare early, Henry VI excluded

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.84 | nan |
| 2Tam (Marlowe) | A | 0.96 | nan |
| Dido (Marlowe) | A | 0.87 | nan |
| DrFaust (Marlowe) | A | 0.64 | nan |
| JoM (Marlowe) | A | 0.48 | nan |
| Ed2 (Marlowe) | A | 0.71 | nan |
| MP (Marlowe) | A | 0.78 | nan |
| Tit (Shakespeare) | B | 0.43 | nan |
| R3 (Shakespeare) | B | 0.35 | nan |
| Shr (Shakespeare) | B | 0.34 | nan |
| TGV (Shakespeare) | B | 0.04 | nan |
| Err (Shakespeare) | B | 0.08 | nan |

## QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.44 | nan |
| 2Tam (Marlowe) | A | 0.72 | nan |
| Dido (Marlowe) | A | 0.62 | nan |
| DrFaust (Marlowe) | A | 0.51 | nan |
| JoM (Marlowe) | A | 0.45 | nan |
| Ed2 (Marlowe) | A | 0.51 | nan |
| MP (Marlowe) | A | 0.67 | nan |
| 2H6 (Shakespeare) | B | 0.68 | nan |
| 3H6 (Shakespeare) | B | 0.77 | nan |
| 1H6 (Shakespeare) | B | 0.87 | nan |
| Tit (Shakespeare) | B | 0.33 | nan |

## QUESTION  Marlowe vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.85 | nan |
| 2Tam (Marlowe) | A | 0.89 | nan |
| Dido (Marlowe) | A | 0.93 | nan |
| DrFaust (Marlowe) | A | 0.60 | nan |
| JoM (Marlowe) | A | 0.59 | nan |
| Ed2 (Marlowe) | A | 0.85 | nan |
| MP (Marlowe) | A | 0.92 | nan |
| R2 (Shakespeare) | B | 0.26 | nan |
| MND (Shakespeare) | B | 0.13 | nan |
| Rom (Shakespeare) | B | 0.11 | nan |
| MV (Shakespeare) | B | 0.07 | nan |
| 1H4 (Shakespeare) | B | 0.09 | nan |
| JC (Shakespeare) | B | 0.13 | nan |
| Ham (Shakespeare) | B | 0.05 | nan |
| Mac (Shakespeare) | B | 0.13 | nan |
| Lr (Shakespeare) | B | 0.03 | nan |
| WT (Shakespeare) | B | 0.04 | nan |
| Tmp (Shakespeare) | B | 0.06 | nan |

## QUESTION  Marlowe vs all Shakespeare

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.71 | nan |
| 2Tam (Marlowe) | A | 0.86 | nan |
| Dido (Marlowe) | A | 0.77 | nan |
| DrFaust (Marlowe) | A | 0.48 | nan |
| JoM (Marlowe) | A | 0.42 | nan |
| Ed2 (Marlowe) | A | 0.58 | nan |
| MP (Marlowe) | A | 0.77 | nan |
| 2H6 (Shakespeare) | B | 0.45 | nan |
| 3H6 (Shakespeare) | B | 0.60 | nan |
| 1H6 (Shakespeare) | B | 0.48 | nan |
| Tit (Shakespeare) | B | 0.17 | nan |
| R3 (Shakespeare) | B | 0.15 | nan |
| Shr (Shakespeare) | B | 0.07 | nan |
| TGV (Shakespeare) | B | 0.02 | nan |
| Err (Shakespeare) | B | 0.02 | nan |
| R2 (Shakespeare) | B | 0.10 | nan |
| MND (Shakespeare) | B | 0.08 | nan |
| Rom (Shakespeare) | B | 0.03 | nan |
| MV (Shakespeare) | B | 0.01 | nan |
| 1H4 (Shakespeare) | B | 0.07 | nan |
| JC (Shakespeare) | B | 0.11 | nan |
| Ham (Shakespeare) | B | 0.04 | nan |
| Mac (Shakespeare) | B | 0.15 | nan |
| Lr (Shakespeare) | B | 0.03 | nan |
| WT (Shakespeare) | B | 0.06 | nan |
| Tmp (Shakespeare) | B | 0.02 | nan |

## SAME-AUTHOR  Shakespeare early vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.65 | nan |
| 3H6 (Shakespeare) | A | 0.76 | nan |
| 1H6 (Shakespeare) | A | 0.30 | nan |
| Tit (Shakespeare) | A | 0.77 | nan |
| R3 (Shakespeare) | A | 0.52 | nan |
| Shr (Shakespeare) | A | 0.67 | nan |
| TGV (Shakespeare) | A | 0.72 | nan |
| Err (Shakespeare) | A | 0.51 | nan |
| R2 (Shakespeare) | B | 0.51 | nan |
| MND (Shakespeare) | B | 0.35 | nan |
| Rom (Shakespeare) | B | 0.46 | nan |
| MV (Shakespeare) | B | 0.29 | nan |
| 1H4 (Shakespeare) | B | 0.18 | nan |
| JC (Shakespeare) | B | 0.20 | nan |
| Ham (Shakespeare) | B | 0.10 | nan |
| Mac (Shakespeare) | B | 0.03 | nan |
| Lr (Shakespeare) | B | 0.11 | nan |
| WT (Shakespeare) | B | 0.06 | nan |
| Tmp (Shakespeare) | B | 0.11 | nan |

## SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.58 | nan |
| 3H6 (Shakespeare) | A | 0.61 | nan |
| 1H6 (Shakespeare) | A | 0.50 | nan |
| Tit (Shakespeare) | A | 0.56 | nan |
| R3 (Shakespeare) | B | 0.41 | nan |
| Shr (Shakespeare) | B | 0.43 | nan |
| TGV (Shakespeare) | B | 0.09 | nan |
| Err (Shakespeare) | B | 0.17 | nan |

## SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.44 | nan |
| MND (Shakespeare) | A | 0.74 | nan |
| Rom (Shakespeare) | A | 0.76 | nan |
| MV (Shakespeare) | A | 0.53 | nan |
| 1H4 (Shakespeare) | A | 0.60 | nan |
| JC (Shakespeare) | B | 0.69 | nan |
| Ham (Shakespeare) | B | 0.29 | nan |
| Mac (Shakespeare) | B | 0.04 | nan |
| Lr (Shakespeare) | B | 0.36 | nan |
| WT (Shakespeare) | B | 0.15 | nan |
| Tmp (Shakespeare) | B | 0.21 | nan |

## SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.29 | nan |
| 2Tam (Marlowe) | A | 0.37 | nan |
| Dido (Marlowe) | A | 0.25 | nan |
| DrFaust (Marlowe) | B | 0.40 | nan |
| JoM (Marlowe) | B | 0.11 | nan |
| Ed2 (Marlowe) | B | 0.27 | nan |
| MP (Marlowe) | B | 0.30 | nan |

## DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.97 | nan |
| MND (Shakespeare) | A | 0.86 | nan |
| Rom (Shakespeare) | A | 0.94 | nan |
| MV (Shakespeare) | A | 0.98 | nan |
| 1H4 (Shakespeare) | A | 0.97 | nan |
| JC (Shakespeare) | A | 0.96 | nan |
| Ham (Shakespeare) | A | 0.98 | nan |
| Mac (Shakespeare) | A | 0.94 | nan |
| Lr (Shakespeare) | A | 0.94 | nan |
| WT (Shakespeare) | A | 0.90 | nan |
| Tmp (Shakespeare) | A | 0.96 | nan |
| FS (Fletcher) | B | 0.88 | nan |
| Prize (Fletcher) | B | 0.25 | nan |
| IP (Fletcher) | B | 0.06 | nan |

## DIFFERENT  Shakespeare early vs Fletcher

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.94 | nan |
| 3H6 (Shakespeare) | A | 0.96 | nan |
| 1H6 (Shakespeare) | A | 0.87 | nan |
| Tit (Shakespeare) | A | 0.93 | nan |
| R3 (Shakespeare) | A | 0.93 | nan |
| Shr (Shakespeare) | A | 0.89 | nan |
| TGV (Shakespeare) | A | 0.94 | nan |
| Err (Shakespeare) | A | 0.95 | nan |
| FS (Fletcher) | B | 0.79 | nan |
| Prize (Fletcher) | B | 0.13 | nan |
| IP (Fletcher) | B | 0.06 | nan |

## DIFFERENT  Marlowe vs Fletcher

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.95 | nan |
| 2Tam (Marlowe) | A | 0.92 | nan |
| Dido (Marlowe) | A | 0.95 | nan |
| DrFaust (Marlowe) | A | 0.78 | nan |
| JoM (Marlowe) | A | 0.79 | nan |
| Ed2 (Marlowe) | A | 0.96 | nan |
| MP (Marlowe) | A | 0.95 | nan |
| FS (Fletcher) | B | 0.86 | nan |
| Prize (Fletcher) | B | 0.04 | nan |
| IP (Fletcher) | B | 0.21 | nan |

## DIFFERENT  Fletcher vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| FS (Fletcher) | A | 0.18 | nan |
| Prize (Fletcher) | A | 0.76 | nan |
| IP (Fletcher) | A | 0.81 | nan |
| Perkin (Ford) | B | 0.58 | nan |
| TPSW (Ford) | B | 0.82 | nan |

## DIFFERENT  Shakespeare later vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.93 | nan |
| MND (Shakespeare) | A | 0.96 | nan |
| Rom (Shakespeare) | A | 0.95 | nan |
| MV (Shakespeare) | A | 0.97 | nan |
| 1H4 (Shakespeare) | A | 0.94 | nan |
| JC (Shakespeare) | A | 0.98 | nan |
| Ham (Shakespeare) | A | 0.91 | nan |
| Mac (Shakespeare) | A | 0.97 | nan |
| Lr (Shakespeare) | A | 0.93 | nan |
| WT (Shakespeare) | A | 0.83 | nan |
| Tmp (Shakespeare) | A | 0.95 | nan |
| Perkin (Ford) | B | 0.81 | nan |
| TPSW (Ford) | B | 0.96 | nan |

## DIFFERENT  Marlowe vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.90 | nan |
| 2Tam (Marlowe) | A | 0.93 | nan |
| Dido (Marlowe) | A | 0.96 | nan |
| DrFaust (Marlowe) | A | 0.87 | nan |
| JoM (Marlowe) | A | 0.77 | nan |
| Ed2 (Marlowe) | A | 0.95 | nan |
| MP (Marlowe) | A | 0.95 | nan |
| Perkin (Ford) | B | 0.65 | nan |
| TPSW (Ford) | B | 0.75 | nan |

## DIFFERENT  Marlowe vs Greene (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.59 | nan |
| 2Tam (Marlowe) | A | 0.75 | nan |
| Dido (Marlowe) | A | 0.49 | nan |
| DrFaust (Marlowe) | A | 0.53 | nan |
| JoM (Marlowe) | A | 0.83 | nan |
| Ed2 (Marlowe) | A | 0.91 | nan |
| MP (Marlowe) | A | 0.70 | nan |
| Alphonsus (Greene) | B | 0.59 | nan |
| Orlando (Greene) | B | 0.64 | nan |
| FriarBacon (Greene) | B | 0.43 | nan |
| JamesIV (Greene) | B | 0.63 | nan |

## DIFFERENT  Marlowe vs Peele (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.38 | nan |
| 2Tam (Marlowe) | A | 0.39 | nan |
| Dido (Marlowe) | A | 0.59 | nan |
| DrFaust (Marlowe) | A | 0.72 | nan |
| JoM (Marlowe) | A | 0.90 | nan |
| Ed2 (Marlowe) | A | 0.88 | nan |
| MP (Marlowe) | A | 0.70 | nan |
| OWT (Peele) | B | 0.56 | nan |
| Alcazar (Peele) | B | 0.48 | nan |
| EdwardI (Peele) | B | 0.69 | nan |
| David (Peele) | B | 0.38 | nan |

## DIFFERENT  Marlowe vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.39 | nan |
| 2Tam (Marlowe) | A | 0.60 | nan |
| Dido (Marlowe) | A | 0.58 | nan |
| DrFaust (Marlowe) | A | 0.51 | nan |
| JoM (Marlowe) | A | 0.69 | nan |
| Ed2 (Marlowe) | A | 0.76 | nan |
| MP (Marlowe) | A | 0.63 | nan |
| Soliman (Anon-Soliman) | B | 0.16 | nan |
| Locrine (Anon-Locrine) | B | 0.58 | nan |
| Selimus (Anon-Selimus) | B | 0.22 | nan |
| TRKJ (Anon-TRKJ) | B | 0.30 | nan |
| JackStraw (Anon-JackStraw) | B | 0.40 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.29 | nan |
| Arden (Anon-Arden) | B | 0.43 | nan |
| TTR3 (Anon-TTR3) | B | 0.15 | nan |

## DIFFERENT  Shakespeare early vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.63 | nan |
| 3H6 (Shakespeare) | A | 0.60 | nan |
| 1H6 (Shakespeare) | A | 0.42 | nan |
| Tit (Shakespeare) | A | 0.95 | nan |
| R3 (Shakespeare) | A | 0.68 | nan |
| Shr (Shakespeare) | A | 0.87 | nan |
| TGV (Shakespeare) | A | 0.93 | nan |
| Err (Shakespeare) | A | 0.96 | nan |
| Alphonsus (Greene) | B | 0.63 | nan |
| Orlando (Greene) | B | 0.13 | nan |
| FriarBacon (Greene) | B | 0.46 | nan |
| JamesIV (Greene) | B | 0.75 | nan |

## DIFFERENT  Shakespeare early vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.65 | nan |
| 3H6 (Shakespeare) | A | 0.69 | nan |
| 1H6 (Shakespeare) | A | 0.49 | nan |
| Tit (Shakespeare) | A | 0.72 | nan |
| R3 (Shakespeare) | A | 0.77 | nan |
| Shr (Shakespeare) | A | 0.85 | nan |
| TGV (Shakespeare) | A | 0.99 | nan |
| Err (Shakespeare) | A | 0.98 | nan |
| OWT (Peele) | B | 0.69 | nan |
| Alcazar (Peele) | B | 0.12 | nan |
| EdwardI (Peele) | B | 0.60 | nan |
| David (Peele) | B | 0.10 | nan |

## DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.53 | nan |
| 3H6 (Shakespeare) | A | 0.39 | nan |
| 1H6 (Shakespeare) | A | 0.33 | nan |
| Tit (Shakespeare) | A | 0.88 | nan |
| R3 (Shakespeare) | A | 0.56 | nan |
| Shr (Shakespeare) | A | 0.90 | nan |
| TGV (Shakespeare) | A | 0.85 | nan |
| Err (Shakespeare) | A | 0.81 | nan |
| Soliman (Anon-Soliman) | B | 0.40 | nan |
| Locrine (Anon-Locrine) | B | 0.42 | nan |
| Selimus (Anon-Selimus) | B | 0.32 | nan |
| TRKJ (Anon-TRKJ) | B | 0.41 | nan |
| JackStraw (Anon-JackStraw) | B | 0.15 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.36 | nan |
| Arden (Anon-Arden) | B | 0.51 | nan |
| TTR3 (Anon-TTR3) | B | 0.16 | nan |

## DIFFERENT  Greene vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| Alphonsus (Greene) | A | 0.86 | nan |
| Orlando (Greene) | A | 0.57 | nan |
| FriarBacon (Greene) | A | 0.53 | nan |
| JamesIV (Greene) | A | 0.53 | nan |
| OWT (Peele) | B | 0.65 | nan |
| Alcazar (Peele) | B | 0.12 | nan |
| EdwardI (Peele) | B | 0.59 | nan |
| David (Peele) | B | 0.11 | nan |

## DIFFERENT  Henry VI 1-3 + Titus vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.55 | nan |
| 3H6 (Shakespeare) | A | 0.52 | nan |
| 1H6 (Shakespeare) | A | 0.36 | nan |
| Tit (Shakespeare) | A | 0.88 | nan |
| Alphonsus (Greene) | B | 0.65 | nan |
| Orlando (Greene) | B | 0.23 | nan |
| FriarBacon (Greene) | B | 0.45 | nan |
| JamesIV (Greene) | B | 0.63 | nan |

## QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.32 | nan |
| 3H6 (Shakespeare) | A | 0.23 | nan |
| 1H6 (Shakespeare) | A | 0.13 | nan |
| Tit (Shakespeare) | A | 0.67 | nan |
| 1Tam (Marlowe) | B | 0.56 | nan |
| 2Tam (Marlowe) | B | 0.28 | nan |
| Dido (Marlowe) | B | 0.38 | nan |
| DrFaust (Marlowe) | B | 0.49 | nan |
| JoM (Marlowe) | B | 0.55 | nan |
| Ed2 (Marlowe) | B | 0.49 | nan |
| MP (Marlowe) | B | 0.33 | nan |
