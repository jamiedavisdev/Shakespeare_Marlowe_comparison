# Pairwise distinguishability (leave-one-play-out logistic regression on 2000-word chunks)

Can a classifier trained on the *other* plays tell which set a held-out play's chunks belong to? For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; for different authors we expect values near 1. The question pair should be read against the two benchmarks.

| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |
|---|---|---|---|---|---|---|---|
| QUESTION  Marlowe vs Shakespeare early | 7 plays | 8 plays | 138 | 0.57 | 0.62 | 0.59 | 0.58 |
| QUESTION  Marlowe vs Shakespeare early, Henry VI excluded | 7 plays | 5 plays | 104 | 0.79 | 0.87 | 0.74 | 0.82 |
| QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched) | 7 plays | 4 plays | 99 | 0.44 | 0.35 | 0.38 | 0.13 |
| QUESTION  Marlowe vs Shakespeare later | 7 plays | 11 plays | 174 | 0.90 | 0.98 | 0.94 | 0.98 |
| QUESTION  Marlowe vs all Shakespeare | 7 plays | 19 plays | 257 | 0.85 | 0.85 | 0.85 | 0.87 |
| SAME-AUTHOR  Shakespeare early vs Shakespeare later | 8 plays | 11 plays | 202 | 0.69 | 0.79 | 0.67 | 0.75 |
| SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies | 4 plays | 4 plays | 83 | 0.72 | 0.82 | 0.65 | 0.76 |
| SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611 | 5 plays | 6 plays | 119 | 0.74 | 0.82 | 0.79 | 0.85 |
| SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93 | 3 plays | 4 plays | 55 | 0.58 | 0.60 | 0.53 | 0.54 |
| DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays) | 11 plays | 3 plays | 151 | 0.90 | 0.90 | 0.89 | 0.86 |
| DIFFERENT  Shakespeare early vs Fletcher | 8 plays | 3 plays | 115 | 0.92 | 0.89 | 0.90 | 0.90 |
| DIFFERENT  Marlowe vs Fletcher | 7 plays | 3 plays | 87 | 0.85 | 0.88 | 0.89 | 0.91 |
| DIFFERENT  Fletcher vs Ford | 3 plays | 2 plays | 51 | 0.55 | 0.52 | 0.51 | 0.44 |
| DIFFERENT  Shakespeare later vs Ford | 11 plays | 2 plays | 138 | 0.86 | 0.44 | 0.86 | 0.32 |
| DIFFERENT  Marlowe vs Ford | 7 plays | 2 plays | 74 | 0.77 | 0.79 | 0.76 | 0.74 |
| DIFFERENT  Marlowe vs Greene (same register, same years) | 7 plays | 4 plays | 83 | 0.83 | 0.93 | 0.80 | 0.87 |
| DIFFERENT  Marlowe vs Peele (same register, same years) | 7 plays | 4 plays | 82 | 0.66 | 0.73 | 0.61 | 0.55 |
| DIFFERENT  Marlowe vs anonymous heroic/history 1587-94 | 7 plays | 8 plays | 122 | 0.75 | 0.86 | 0.59 | 0.63 |
| DIFFERENT  Shakespeare early vs Greene | 8 plays | 4 plays | 111 | 0.75 | 0.78 | 0.80 | 0.82 |
| DIFFERENT  Shakespeare early vs Peele | 8 plays | 4 plays | 110 | 0.77 | 0.81 | 0.72 | 0.69 |
| DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94 | 8 plays | 8 plays | 150 | 0.73 | 0.85 | 0.58 | 0.65 |
| DIFFERENT  Greene vs Peele | 4 plays | 4 plays | 55 | 0.75 | 0.78 | 0.67 | 0.73 |
| DIFFERENT  Henry VI 1-3 + Titus vs Greene | 4 plays | 4 plays | 72 | 0.67 | 0.78 | 0.50 | 0.55 |
| QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison) | 4 plays | 7 plays | 99 | 0.44 | 0.36 | 0.38 | 0.13 |

# Per-play mean P(set A), words model


## QUESTION  Marlowe vs Shakespeare early

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.57 | 0.75 |
| 2Tam (Marlowe) | A | 0.64 | 0.82 |
| Dido (Marlowe) | A | 0.59 | 0.73 |
| DrFaust (Marlowe) | A | 0.33 | 0.32 |
| JoM (Marlowe) | A | 0.29 | 0.29 |
| Ed2 (Marlowe) | A | 0.54 | 0.34 |
| MP (Marlowe) | A | 0.67 | 0.76 |
| 2H6 (Shakespeare) | B | 0.58 | 0.73 |
| 3H6 (Shakespeare) | B | 0.68 | 0.74 |
| 1H6 (Shakespeare) | B | 0.68 | 0.81 |
| Tit (Shakespeare) | B | 0.30 | 0.43 |
| R3 (Shakespeare) | B | 0.34 | 0.42 |
| Shr (Shakespeare) | B | 0.25 | 0.15 |
| TGV (Shakespeare) | B | 0.10 | 0.07 |
| Err (Shakespeare) | B | 0.07 | 0.04 |

## QUESTION  Marlowe vs Shakespeare early, Henry VI excluded

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.87 | 0.88 |
| 2Tam (Marlowe) | A | 0.87 | 0.94 |
| Dido (Marlowe) | A | 0.71 | 0.85 |
| DrFaust (Marlowe) | A | 0.42 | 0.43 |
| JoM (Marlowe) | A | 0.35 | 0.38 |
| Ed2 (Marlowe) | A | 0.83 | 0.61 |
| MP (Marlowe) | A | 0.79 | 0.93 |
| Tit (Shakespeare) | B | 0.51 | 0.63 |
| R3 (Shakespeare) | B | 0.34 | 0.42 |
| Shr (Shakespeare) | B | 0.29 | 0.29 |
| TGV (Shakespeare) | B | 0.06 | 0.08 |
| Err (Shakespeare) | B | 0.11 | 0.05 |

## QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.57 | 0.68 |
| 2Tam (Marlowe) | A | 0.62 | 0.73 |
| Dido (Marlowe) | A | 0.69 | 0.77 |
| DrFaust (Marlowe) | A | 0.36 | 0.52 |
| JoM (Marlowe) | A | 0.40 | 0.44 |
| Ed2 (Marlowe) | A | 0.54 | 0.32 |
| MP (Marlowe) | A | 0.67 | 0.59 |
| 2H6 (Shakespeare) | B | 0.63 | 0.90 |
| 3H6 (Shakespeare) | B | 0.69 | 0.85 |
| 1H6 (Shakespeare) | B | 0.76 | 0.96 |
| Tit (Shakespeare) | B | 0.57 | 0.69 |

## QUESTION  Marlowe vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.86 | 0.88 |
| 2Tam (Marlowe) | A | 0.83 | 0.85 |
| Dido (Marlowe) | A | 0.80 | 0.84 |
| DrFaust (Marlowe) | A | 0.49 | 0.48 |
| JoM (Marlowe) | A | 0.54 | 0.44 |
| Ed2 (Marlowe) | A | 0.86 | 0.61 |
| MP (Marlowe) | A | 0.92 | 0.91 |
| R2 (Shakespeare) | B | 0.42 | 0.27 |
| MND (Shakespeare) | B | 0.14 | 0.06 |
| Rom (Shakespeare) | B | 0.08 | 0.05 |
| MV (Shakespeare) | B | 0.04 | 0.03 |
| 1H4 (Shakespeare) | B | 0.17 | 0.09 |
| JC (Shakespeare) | B | 0.04 | 0.06 |
| Ham (Shakespeare) | B | 0.10 | 0.03 |
| Mac (Shakespeare) | B | 0.05 | 0.02 |
| Lr (Shakespeare) | B | 0.06 | 0.02 |
| WT (Shakespeare) | B | 0.03 | 0.01 |
| Tmp (Shakespeare) | B | 0.07 | 0.07 |

## QUESTION  Marlowe vs all Shakespeare

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.63 | 0.76 |
| 2Tam (Marlowe) | A | 0.69 | 0.76 |
| Dido (Marlowe) | A | 0.66 | 0.67 |
| DrFaust (Marlowe) | A | 0.23 | 0.29 |
| JoM (Marlowe) | A | 0.33 | 0.29 |
| Ed2 (Marlowe) | A | 0.58 | 0.28 |
| MP (Marlowe) | A | 0.80 | 0.72 |
| 2H6 (Shakespeare) | B | 0.40 | 0.35 |
| 3H6 (Shakespeare) | B | 0.64 | 0.47 |
| 1H6 (Shakespeare) | B | 0.45 | 0.35 |
| Tit (Shakespeare) | B | 0.28 | 0.39 |
| R3 (Shakespeare) | B | 0.08 | 0.04 |
| Shr (Shakespeare) | B | 0.15 | 0.08 |
| TGV (Shakespeare) | B | 0.06 | 0.03 |
| Err (Shakespeare) | B | 0.05 | 0.01 |
| R2 (Shakespeare) | B | 0.14 | 0.06 |
| MND (Shakespeare) | B | 0.09 | 0.04 |
| Rom (Shakespeare) | B | 0.04 | 0.02 |
| MV (Shakespeare) | B | 0.05 | 0.03 |
| 1H4 (Shakespeare) | B | 0.12 | 0.04 |
| JC (Shakespeare) | B | 0.02 | 0.01 |
| Ham (Shakespeare) | B | 0.06 | 0.03 |
| Mac (Shakespeare) | B | 0.06 | 0.02 |
| Lr (Shakespeare) | B | 0.04 | 0.01 |
| WT (Shakespeare) | B | 0.03 | 0.00 |
| Tmp (Shakespeare) | B | 0.05 | 0.03 |

## SAME-AUTHOR  Shakespeare early vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.39 | 0.19 |
| 3H6 (Shakespeare) | A | 0.64 | 0.44 |
| 1H6 (Shakespeare) | A | 0.25 | 0.10 |
| Tit (Shakespeare) | A | 0.73 | 0.87 |
| R3 (Shakespeare) | A | 0.37 | 0.23 |
| Shr (Shakespeare) | A | 0.69 | 0.70 |
| TGV (Shakespeare) | A | 0.70 | 0.36 |
| Err (Shakespeare) | A | 0.59 | 0.50 |
| R2 (Shakespeare) | B | 0.68 | 0.58 |
| MND (Shakespeare) | B | 0.22 | 0.15 |
| Rom (Shakespeare) | B | 0.29 | 0.32 |
| MV (Shakespeare) | B | 0.31 | 0.16 |
| 1H4 (Shakespeare) | B | 0.26 | 0.12 |
| JC (Shakespeare) | B | 0.11 | 0.13 |
| Ham (Shakespeare) | B | 0.19 | 0.06 |
| Mac (Shakespeare) | B | 0.03 | 0.02 |
| Lr (Shakespeare) | B | 0.19 | 0.19 |
| WT (Shakespeare) | B | 0.07 | 0.06 |
| Tmp (Shakespeare) | B | 0.15 | 0.12 |

## SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.65 | 0.56 |
| 3H6 (Shakespeare) | A | 0.68 | 0.64 |
| 1H6 (Shakespeare) | A | 0.68 | 0.51 |
| Tit (Shakespeare) | A | 0.48 | 0.41 |
| R3 (Shakespeare) | B | 0.47 | 0.47 |
| Shr (Shakespeare) | B | 0.41 | 0.36 |
| TGV (Shakespeare) | B | 0.04 | 0.05 |
| Err (Shakespeare) | B | 0.20 | 0.12 |

## SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.54 | 0.50 |
| MND (Shakespeare) | A | 0.78 | 0.83 |
| Rom (Shakespeare) | A | 0.72 | 0.86 |
| MV (Shakespeare) | A | 0.61 | 0.46 |
| 1H4 (Shakespeare) | A | 0.53 | 0.64 |
| JC (Shakespeare) | B | 0.73 | 0.67 |
| Ham (Shakespeare) | B | 0.36 | 0.34 |
| Mac (Shakespeare) | B | 0.11 | 0.12 |
| Lr (Shakespeare) | B | 0.22 | 0.13 |
| WT (Shakespeare) | B | 0.13 | 0.15 |
| Tmp (Shakespeare) | B | 0.22 | 0.20 |

## SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.33 | 0.21 |
| 2Tam (Marlowe) | A | 0.32 | 0.19 |
| Dido (Marlowe) | A | 0.20 | 0.21 |
| DrFaust (Marlowe) | B | 0.31 | 0.31 |
| JoM (Marlowe) | B | 0.16 | 0.16 |
| Ed2 (Marlowe) | B | 0.24 | 0.16 |
| MP (Marlowe) | B | 0.26 | 0.22 |

## DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.98 | 1.00 |
| MND (Shakespeare) | A | 0.78 | 0.86 |
| Rom (Shakespeare) | A | 0.91 | 0.96 |
| MV (Shakespeare) | A | 0.97 | 0.98 |
| 1H4 (Shakespeare) | A | 0.96 | 0.98 |
| JC (Shakespeare) | A | 0.96 | 0.95 |
| Ham (Shakespeare) | A | 0.99 | 1.00 |
| Mac (Shakespeare) | A | 0.94 | 0.97 |
| Lr (Shakespeare) | A | 0.93 | 0.97 |
| WT (Shakespeare) | A | 0.91 | 0.95 |
| Tmp (Shakespeare) | A | 0.93 | 0.96 |
| FS (Fletcher) | B | 0.91 | 0.97 |
| Prize (Fletcher) | B | 0.31 | 0.45 |
| IP (Fletcher) | B | 0.32 | 0.30 |

## DIFFERENT  Shakespeare early vs Fletcher

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.91 | 0.88 |
| 3H6 (Shakespeare) | A | 0.93 | 0.94 |
| 1H6 (Shakespeare) | A | 0.81 | 0.89 |
| Tit (Shakespeare) | A | 0.90 | 0.96 |
| R3 (Shakespeare) | A | 0.94 | 0.96 |
| Shr (Shakespeare) | A | 0.85 | 0.88 |
| TGV (Shakespeare) | A | 0.86 | 0.83 |
| Err (Shakespeare) | A | 0.92 | 0.97 |
| FS (Fletcher) | B | 0.83 | 0.87 |
| Prize (Fletcher) | B | 0.19 | 0.24 |
| IP (Fletcher) | B | 0.18 | 0.18 |

## DIFFERENT  Marlowe vs Fletcher

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.90 | 0.97 |
| 2Tam (Marlowe) | A | 0.87 | 0.97 |
| Dido (Marlowe) | A | 0.84 | 0.94 |
| DrFaust (Marlowe) | A | 0.70 | 0.84 |
| JoM (Marlowe) | A | 0.66 | 0.77 |
| Ed2 (Marlowe) | A | 0.96 | 0.98 |
| MP (Marlowe) | A | 0.98 | 0.99 |
| FS (Fletcher) | B | 0.78 | 0.87 |
| Prize (Fletcher) | B | 0.09 | 0.13 |
| IP (Fletcher) | B | 0.19 | 0.15 |

## DIFFERENT  Fletcher vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| FS (Fletcher) | A | 0.33 | 0.43 |
| Prize (Fletcher) | A | 0.79 | 0.82 |
| IP (Fletcher) | A | 0.82 | 0.80 |
| Perkin (Ford) | B | 0.53 | 0.64 |
| TPSW (Ford) | B | 0.80 | 0.89 |

## DIFFERENT  Shakespeare later vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.91 | 0.98 |
| MND (Shakespeare) | A | 0.93 | 0.98 |
| Rom (Shakespeare) | A | 0.98 | 0.99 |
| MV (Shakespeare) | A | 0.95 | 0.96 |
| 1H4 (Shakespeare) | A | 0.90 | 0.94 |
| JC (Shakespeare) | A | 0.98 | 0.99 |
| Ham (Shakespeare) | A | 0.93 | 0.97 |
| Mac (Shakespeare) | A | 0.93 | 0.99 |
| Lr (Shakespeare) | A | 0.95 | 0.94 |
| WT (Shakespeare) | A | 0.83 | 0.90 |
| Tmp (Shakespeare) | A | 0.96 | 0.98 |
| Perkin (Ford) | B | 0.94 | 0.98 |
| TPSW (Ford) | B | 0.97 | 0.99 |

## DIFFERENT  Marlowe vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.88 | 0.94 |
| 2Tam (Marlowe) | A | 0.92 | 0.97 |
| Dido (Marlowe) | A | 0.95 | 0.98 |
| DrFaust (Marlowe) | A | 0.81 | 0.85 |
| JoM (Marlowe) | A | 0.77 | 0.78 |
| Ed2 (Marlowe) | A | 0.92 | 0.88 |
| MP (Marlowe) | A | 0.97 | 0.98 |
| Perkin (Ford) | B | 0.72 | 0.79 |
| TPSW (Ford) | B | 0.76 | 0.87 |

## DIFFERENT  Marlowe vs Greene (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.69 | 0.81 |
| 2Tam (Marlowe) | A | 0.80 | 0.85 |
| Dido (Marlowe) | A | 0.69 | 0.70 |
| DrFaust (Marlowe) | A | 0.64 | 0.65 |
| JoM (Marlowe) | A | 0.77 | 0.87 |
| Ed2 (Marlowe) | A | 0.90 | 0.85 |
| MP (Marlowe) | A | 0.88 | 0.88 |
| Alphonsus (Greene) | B | 0.43 | 0.75 |
| Orlando (Greene) | B | 0.43 | 0.33 |
| FriarBacon (Greene) | B | 0.27 | 0.36 |
| JamesIV (Greene) | B | 0.41 | 0.53 |

## DIFFERENT  Marlowe vs Peele (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.43 | 0.45 |
| 2Tam (Marlowe) | A | 0.40 | 0.56 |
| Dido (Marlowe) | A | 0.61 | 0.74 |
| DrFaust (Marlowe) | A | 0.75 | 0.77 |
| JoM (Marlowe) | A | 0.86 | 0.89 |
| Ed2 (Marlowe) | A | 0.83 | 0.70 |
| MP (Marlowe) | A | 0.67 | 0.75 |
| OWT (Peele) | B | 0.45 | 0.86 |
| Alcazar (Peele) | B | 0.38 | 0.43 |
| EdwardI (Peele) | B | 0.54 | 0.71 |
| David (Peele) | B | 0.34 | 0.65 |

## DIFFERENT  Marlowe vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.43 | 0.34 |
| 2Tam (Marlowe) | A | 0.52 | 0.48 |
| Dido (Marlowe) | A | 0.79 | 0.50 |
| DrFaust (Marlowe) | A | 0.70 | 0.45 |
| JoM (Marlowe) | A | 0.38 | 0.30 |
| Ed2 (Marlowe) | A | 0.75 | 0.47 |
| MP (Marlowe) | A | 0.73 | 0.55 |
| Soliman (Anon-Soliman) | B | 0.14 | 0.27 |
| Locrine (Anon-Locrine) | B | 0.47 | 0.51 |
| Selimus (Anon-Selimus) | B | 0.13 | 0.22 |
| TRKJ (Anon-TRKJ) | B | 0.30 | 0.34 |
| JackStraw (Anon-JackStraw) | B | 0.44 | 0.37 |
| EdwardIII (Anon-EdwardIII) | B | 0.22 | 0.25 |
| Arden (Anon-Arden) | B | 0.22 | 0.50 |
| TTR3 (Anon-TTR3) | B | 0.21 | 0.18 |

## DIFFERENT  Shakespeare early vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.60 | 0.63 |
| 3H6 (Shakespeare) | A | 0.63 | 0.64 |
| 1H6 (Shakespeare) | A | 0.51 | 0.50 |
| Tit (Shakespeare) | A | 0.92 | 0.94 |
| R3 (Shakespeare) | A | 0.69 | 0.76 |
| Shr (Shakespeare) | A | 0.90 | 0.95 |
| TGV (Shakespeare) | A | 0.90 | 0.90 |
| Err (Shakespeare) | A | 0.88 | 0.98 |
| Alphonsus (Greene) | B | 0.58 | 0.63 |
| Orlando (Greene) | B | 0.32 | 0.16 |
| FriarBacon (Greene) | B | 0.22 | 0.30 |
| JamesIV (Greene) | B | 0.67 | 0.64 |

## DIFFERENT  Shakespeare early vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.67 | 0.54 |
| 3H6 (Shakespeare) | A | 0.67 | 0.58 |
| 1H6 (Shakespeare) | A | 0.60 | 0.53 |
| Tit (Shakespeare) | A | 0.72 | 0.79 |
| R3 (Shakespeare) | A | 0.73 | 0.71 |
| Shr (Shakespeare) | A | 0.83 | 0.93 |
| TGV (Shakespeare) | A | 0.99 | 0.99 |
| Err (Shakespeare) | A | 0.95 | 0.99 |
| OWT (Peele) | B | 0.60 | 0.93 |
| Alcazar (Peele) | B | 0.14 | 0.13 |
| EdwardI (Peele) | B | 0.64 | 0.76 |
| David (Peele) | B | 0.10 | 0.23 |

## DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.40 | 0.19 |
| 3H6 (Shakespeare) | A | 0.38 | 0.18 |
| 1H6 (Shakespeare) | A | 0.43 | 0.13 |
| Tit (Shakespeare) | A | 0.82 | 0.68 |
| R3 (Shakespeare) | A | 0.58 | 0.46 |
| Shr (Shakespeare) | A | 0.87 | 0.95 |
| TGV (Shakespeare) | A | 0.90 | 0.81 |
| Err (Shakespeare) | A | 0.87 | 0.90 |
| Soliman (Anon-Soliman) | B | 0.26 | 0.11 |
| Locrine (Anon-Locrine) | B | 0.26 | 0.31 |
| Selimus (Anon-Selimus) | B | 0.15 | 0.16 |
| TRKJ (Anon-TRKJ) | B | 0.44 | 0.49 |
| JackStraw (Anon-JackStraw) | B | 0.27 | 0.22 |
| EdwardIII (Anon-EdwardIII) | B | 0.23 | 0.32 |
| Arden (Anon-Arden) | B | 0.40 | 0.77 |
| TTR3 (Anon-TTR3) | B | 0.10 | 0.13 |

## DIFFERENT  Greene vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| Alphonsus (Greene) | A | 0.88 | 0.81 |
| Orlando (Greene) | A | 0.72 | 0.76 |
| FriarBacon (Greene) | A | 0.62 | 0.66 |
| JamesIV (Greene) | A | 0.51 | 0.52 |
| OWT (Peele) | B | 0.74 | 0.77 |
| Alcazar (Peele) | B | 0.11 | 0.09 |
| EdwardI (Peele) | B | 0.50 | 0.59 |
| David (Peele) | B | 0.10 | 0.12 |

## DIFFERENT  Henry VI 1-3 + Titus vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.51 | 0.31 |
| 3H6 (Shakespeare) | A | 0.56 | 0.43 |
| 1H6 (Shakespeare) | A | 0.49 | 0.22 |
| Tit (Shakespeare) | A | 0.76 | 0.75 |
| Alphonsus (Greene) | B | 0.50 | 0.54 |
| Orlando (Greene) | B | 0.27 | 0.19 |
| FriarBacon (Greene) | B | 0.18 | 0.27 |
| JamesIV (Greene) | B | 0.44 | 0.46 |

## QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.37 | 0.10 |
| 3H6 (Shakespeare) | A | 0.31 | 0.15 |
| 1H6 (Shakespeare) | A | 0.24 | 0.04 |
| Tit (Shakespeare) | A | 0.43 | 0.30 |
| 1Tam (Marlowe) | B | 0.43 | 0.32 |
| 2Tam (Marlowe) | B | 0.38 | 0.27 |
| Dido (Marlowe) | B | 0.31 | 0.23 |
| DrFaust (Marlowe) | B | 0.64 | 0.48 |
| JoM (Marlowe) | B | 0.60 | 0.56 |
| Ed2 (Marlowe) | B | 0.46 | 0.68 |
| MP (Marlowe) | B | 0.32 | 0.40 |
