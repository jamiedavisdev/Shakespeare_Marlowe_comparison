# Pairwise distinguishability (leave-one-play-out logistic regression on 2000-word chunks)

Can a classifier trained on the *other* plays tell which set a held-out play's chunks belong to? For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; for different authors we expect values near 1. The question pair should be read against the two benchmarks.

| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |
|---|---|---|---|---|---|---|---|
| QUESTION  Marlowe vs Shakespeare early | 7 plays | 8 plays | 139 | 0.63 | 0.63 | 0.59 | 0.57 |
| QUESTION  Marlowe vs Shakespeare early, Henry VI excluded | 7 plays | 5 plays | 105 | 0.84 | 0.87 | 0.74 | 0.82 |
| QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched) | 7 plays | 4 plays | 99 | 0.41 | 0.34 | 0.34 | 0.13 |
| QUESTION  Marlowe vs Shakespeare later | 7 plays | 11 plays | 173 | 0.89 | 0.95 | 0.92 | 0.97 |
| QUESTION  Marlowe vs all Shakespeare | 7 plays | 19 plays | 257 | 0.79 | 0.79 | 0.85 | 0.84 |
| SAME-AUTHOR  Shakespeare early vs Shakespeare later | 8 plays | 11 plays | 202 | 0.69 | 0.75 | 0.69 | 0.75 |
| SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies | 4 plays | 4 plays | 84 | 0.75 | 0.82 | 0.67 | 0.76 |
| SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611 | 5 plays | 6 plays | 118 | 0.72 | 0.79 | 0.77 | 0.82 |
| SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93 | 3 plays | 4 plays | 55 | 0.58 | 0.68 | 0.53 | 0.57 |
| DIFFERENT  Marlowe vs Greene (same register, same years) | 7 plays | 4 plays | 83 | 0.69 | 0.78 | 0.75 | 0.76 |
| DIFFERENT  Marlowe vs Peele (same register, same years) | 7 plays | 4 plays | 82 | 0.63 | 0.70 | 0.62 | 0.51 |
| DIFFERENT  Marlowe vs anonymous heroic/history 1587-94 | 7 plays | 8 plays | 122 | 0.57 | 0.57 | 0.46 | 0.42 |
| DIFFERENT  Shakespeare early vs Greene | 8 plays | 4 plays | 112 | 0.70 | 0.60 | 0.71 | 0.72 |
| DIFFERENT  Shakespeare early vs Peele | 8 plays | 4 plays | 111 | 0.78 | 0.81 | 0.68 | 0.65 |
| DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94 | 8 plays | 8 plays | 151 | 0.50 | 0.57 | 0.48 | 0.50 |
| DIFFERENT  Greene vs Peele | 4 plays | 4 plays | 55 | 0.67 | 0.78 | 0.65 | 0.71 |
| DIFFERENT  Henry VI 1-3 + Titus vs Greene | 4 plays | 4 plays | 72 | 0.56 | 0.61 | 0.42 | 0.44 |
| QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison) | 4 plays | 7 plays | 99 | 0.41 | 0.34 | 0.35 | 0.13 |

# Per-play mean P(set A), words model


## QUESTION  Marlowe vs Shakespeare early

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.54 | 0.71 |
| 2Tam (Marlowe) | A | 0.66 | 0.79 |
| Dido (Marlowe) | A | 0.61 | 0.73 |
| DrFaust (Marlowe) | A | 0.39 | 0.30 |
| JoM (Marlowe) | A | 0.18 | 0.25 |
| Ed2 (Marlowe) | A | 0.62 | 0.32 |
| MP (Marlowe) | A | 0.64 | 0.74 |
| 2H6 (Shakespeare) | B | 0.57 | 0.73 |
| 3H6 (Shakespeare) | B | 0.64 | 0.71 |
| 1H6 (Shakespeare) | B | 0.68 | 0.82 |
| Tit (Shakespeare) | B | 0.35 | 0.43 |
| R3 (Shakespeare) | B | 0.28 | 0.40 |
| Shr (Shakespeare) | B | 0.23 | 0.16 |
| TGV (Shakespeare) | B | 0.10 | 0.10 |
| Err (Shakespeare) | B | 0.04 | 0.04 |

## QUESTION  Marlowe vs Shakespeare early, Henry VI excluded

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.84 | 0.88 |
| 2Tam (Marlowe) | A | 0.87 | 0.94 |
| Dido (Marlowe) | A | 0.70 | 0.87 |
| DrFaust (Marlowe) | A | 0.47 | 0.40 |
| JoM (Marlowe) | A | 0.25 | 0.34 |
| Ed2 (Marlowe) | A | 0.88 | 0.64 |
| MP (Marlowe) | A | 0.78 | 0.92 |
| Tit (Shakespeare) | B | 0.55 | 0.62 |
| R3 (Shakespeare) | B | 0.28 | 0.40 |
| Shr (Shakespeare) | B | 0.26 | 0.28 |
| TGV (Shakespeare) | B | 0.08 | 0.11 |
| Err (Shakespeare) | B | 0.11 | 0.05 |

## QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.54 | 0.65 |
| 2Tam (Marlowe) | A | 0.56 | 0.69 |
| Dido (Marlowe) | A | 0.62 | 0.72 |
| DrFaust (Marlowe) | A | 0.41 | 0.44 |
| JoM (Marlowe) | A | 0.31 | 0.38 |
| Ed2 (Marlowe) | A | 0.52 | 0.30 |
| MP (Marlowe) | A | 0.61 | 0.59 |
| 2H6 (Shakespeare) | B | 0.65 | 0.91 |
| 3H6 (Shakespeare) | B | 0.66 | 0.84 |
| 1H6 (Shakespeare) | B | 0.74 | 0.95 |
| Tit (Shakespeare) | B | 0.52 | 0.67 |

## QUESTION  Marlowe vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.82 | 0.85 |
| 2Tam (Marlowe) | A | 0.82 | 0.80 |
| Dido (Marlowe) | A | 0.73 | 0.83 |
| DrFaust (Marlowe) | A | 0.49 | 0.45 |
| JoM (Marlowe) | A | 0.46 | 0.39 |
| Ed2 (Marlowe) | A | 0.87 | 0.59 |
| MP (Marlowe) | A | 0.87 | 0.93 |
| R2 (Shakespeare) | B | 0.41 | 0.26 |
| MND (Shakespeare) | B | 0.17 | 0.08 |
| Rom (Shakespeare) | B | 0.09 | 0.05 |
| MV (Shakespeare) | B | 0.06 | 0.03 |
| 1H4 (Shakespeare) | B | 0.21 | 0.10 |
| JC (Shakespeare) | B | 0.06 | 0.05 |
| Ham (Shakespeare) | B | 0.11 | 0.05 |
| Mac (Shakespeare) | B | 0.03 | 0.02 |
| Lr (Shakespeare) | B | 0.09 | 0.03 |
| WT (Shakespeare) | B | 0.03 | 0.01 |
| Tmp (Shakespeare) | B | 0.08 | 0.08 |

## QUESTION  Marlowe vs all Shakespeare

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.58 | 0.67 |
| 2Tam (Marlowe) | A | 0.68 | 0.68 |
| Dido (Marlowe) | A | 0.57 | 0.62 |
| DrFaust (Marlowe) | A | 0.29 | 0.28 |
| JoM (Marlowe) | A | 0.19 | 0.24 |
| Ed2 (Marlowe) | A | 0.57 | 0.26 |
| MP (Marlowe) | A | 0.71 | 0.75 |
| 2H6 (Shakespeare) | B | 0.50 | 0.38 |
| 3H6 (Shakespeare) | B | 0.64 | 0.46 |
| 1H6 (Shakespeare) | B | 0.52 | 0.40 |
| Tit (Shakespeare) | B | 0.29 | 0.38 |
| R3 (Shakespeare) | B | 0.07 | 0.03 |
| Shr (Shakespeare) | B | 0.16 | 0.08 |
| TGV (Shakespeare) | B | 0.07 | 0.04 |
| Err (Shakespeare) | B | 0.04 | 0.01 |
| R2 (Shakespeare) | B | 0.20 | 0.08 |
| MND (Shakespeare) | B | 0.07 | 0.05 |
| Rom (Shakespeare) | B | 0.04 | 0.02 |
| MV (Shakespeare) | B | 0.07 | 0.03 |
| 1H4 (Shakespeare) | B | 0.15 | 0.04 |
| JC (Shakespeare) | B | 0.05 | 0.01 |
| Ham (Shakespeare) | B | 0.11 | 0.05 |
| Mac (Shakespeare) | B | 0.03 | 0.02 |
| Lr (Shakespeare) | B | 0.07 | 0.01 |
| WT (Shakespeare) | B | 0.04 | 0.00 |
| Tmp (Shakespeare) | B | 0.06 | 0.03 |

## SAME-AUTHOR  Shakespeare early vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.27 | 0.20 |
| 3H6 (Shakespeare) | A | 0.53 | 0.43 |
| 1H6 (Shakespeare) | A | 0.23 | 0.11 |
| Tit (Shakespeare) | A | 0.66 | 0.88 |
| R3 (Shakespeare) | A | 0.26 | 0.21 |
| Shr (Shakespeare) | A | 0.76 | 0.71 |
| TGV (Shakespeare) | A | 0.70 | 0.41 |
| Err (Shakespeare) | A | 0.65 | 0.60 |
| R2 (Shakespeare) | B | 0.68 | 0.53 |
| MND (Shakespeare) | B | 0.28 | 0.22 |
| Rom (Shakespeare) | B | 0.28 | 0.30 |
| MV (Shakespeare) | B | 0.33 | 0.20 |
| 1H4 (Shakespeare) | B | 0.22 | 0.12 |
| JC (Shakespeare) | B | 0.11 | 0.11 |
| Ham (Shakespeare) | B | 0.23 | 0.06 |
| Mac (Shakespeare) | B | 0.02 | 0.02 |
| Lr (Shakespeare) | B | 0.13 | 0.15 |
| WT (Shakespeare) | B | 0.12 | 0.09 |
| Tmp (Shakespeare) | B | 0.10 | 0.12 |

## SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.66 | 0.55 |
| 3H6 (Shakespeare) | A | 0.71 | 0.64 |
| 1H6 (Shakespeare) | A | 0.77 | 0.57 |
| Tit (Shakespeare) | A | 0.47 | 0.41 |
| R3 (Shakespeare) | B | 0.53 | 0.48 |
| Shr (Shakespeare) | B | 0.40 | 0.37 |
| TGV (Shakespeare) | B | 0.06 | 0.04 |
| Err (Shakespeare) | B | 0.20 | 0.14 |

## SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.56 | 0.49 |
| MND (Shakespeare) | A | 0.81 | 0.85 |
| Rom (Shakespeare) | A | 0.70 | 0.81 |
| MV (Shakespeare) | A | 0.60 | 0.45 |
| 1H4 (Shakespeare) | A | 0.52 | 0.63 |
| JC (Shakespeare) | B | 0.80 | 0.70 |
| Ham (Shakespeare) | B | 0.40 | 0.37 |
| Mac (Shakespeare) | B | 0.12 | 0.14 |
| Lr (Shakespeare) | B | 0.20 | 0.12 |
| WT (Shakespeare) | B | 0.15 | 0.14 |
| Tmp (Shakespeare) | B | 0.21 | 0.20 |

## SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.34 | 0.23 |
| 2Tam (Marlowe) | A | 0.33 | 0.21 |
| Dido (Marlowe) | A | 0.22 | 0.23 |
| DrFaust (Marlowe) | B | 0.30 | 0.30 |
| JoM (Marlowe) | B | 0.10 | 0.16 |
| Ed2 (Marlowe) | B | 0.23 | 0.15 |
| MP (Marlowe) | B | 0.25 | 0.21 |

## DIFFERENT  Marlowe vs Greene (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.59 | 0.76 |
| 2Tam (Marlowe) | A | 0.73 | 0.81 |
| Dido (Marlowe) | A | 0.55 | 0.62 |
| DrFaust (Marlowe) | A | 0.48 | 0.58 |
| JoM (Marlowe) | A | 0.73 | 0.80 |
| Ed2 (Marlowe) | A | 0.90 | 0.82 |
| MP (Marlowe) | A | 0.86 | 0.88 |
| Alphonsus (Greene) | B | 0.51 | 0.77 |
| Orlando (Greene) | B | 0.51 | 0.40 |
| FriarBacon (Greene) | B | 0.35 | 0.40 |
| JamesIV (Greene) | B | 0.48 | 0.63 |

## DIFFERENT  Marlowe vs Peele (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.36 | 0.42 |
| 2Tam (Marlowe) | A | 0.37 | 0.54 |
| Dido (Marlowe) | A | 0.59 | 0.71 |
| DrFaust (Marlowe) | A | 0.76 | 0.73 |
| JoM (Marlowe) | A | 0.88 | 0.89 |
| Ed2 (Marlowe) | A | 0.84 | 0.70 |
| MP (Marlowe) | A | 0.69 | 0.78 |
| OWT (Peele) | B | 0.43 | 0.85 |
| Alcazar (Peele) | B | 0.33 | 0.37 |
| EdwardI (Peele) | B | 0.57 | 0.74 |
| David (Peele) | B | 0.36 | 0.67 |

## DIFFERENT  Marlowe vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.26 | 0.29 |
| 2Tam (Marlowe) | A | 0.39 | 0.41 |
| Dido (Marlowe) | A | 0.49 | 0.34 |
| DrFaust (Marlowe) | A | 0.30 | 0.30 |
| JoM (Marlowe) | A | 0.17 | 0.16 |
| Ed2 (Marlowe) | A | 0.70 | 0.34 |
| MP (Marlowe) | A | 0.64 | 0.49 |
| Soliman (Anon-Soliman) | B | 0.18 | 0.42 |
| Locrine (Anon-Locrine) | B | 0.40 | 0.51 |
| Selimus (Anon-Selimus) | B | 0.18 | 0.25 |
| TRKJ (Anon-TRKJ) | B | 0.39 | 0.38 |
| JackStraw (Anon-JackStraw) | B | 0.58 | 0.44 |
| EdwardIII (Anon-EdwardIII) | B | 0.35 | 0.34 |
| Arden (Anon-Arden) | B | 0.71 | 0.78 |
| TTR3 (Anon-TTR3) | B | 0.20 | 0.22 |

## DIFFERENT  Shakespeare early vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.56 | 0.56 |
| 3H6 (Shakespeare) | A | 0.53 | 0.58 |
| 1H6 (Shakespeare) | A | 0.35 | 0.40 |
| Tit (Shakespeare) | A | 0.91 | 0.92 |
| R3 (Shakespeare) | A | 0.61 | 0.75 |
| Shr (Shakespeare) | A | 0.84 | 0.93 |
| TGV (Shakespeare) | A | 0.86 | 0.90 |
| Err (Shakespeare) | A | 0.88 | 0.98 |
| Alphonsus (Greene) | B | 0.73 | 0.67 |
| Orlando (Greene) | B | 0.42 | 0.23 |
| FriarBacon (Greene) | B | 0.31 | 0.38 |
| JamesIV (Greene) | B | 0.76 | 0.73 |

## DIFFERENT  Shakespeare early vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.64 | 0.50 |
| 3H6 (Shakespeare) | A | 0.66 | 0.55 |
| 1H6 (Shakespeare) | A | 0.58 | 0.47 |
| Tit (Shakespeare) | A | 0.69 | 0.77 |
| R3 (Shakespeare) | A | 0.66 | 0.69 |
| Shr (Shakespeare) | A | 0.86 | 0.93 |
| TGV (Shakespeare) | A | 0.98 | 1.00 |
| Err (Shakespeare) | A | 0.98 | 0.99 |
| OWT (Peele) | B | 0.51 | 0.94 |
| Alcazar (Peele) | B | 0.18 | 0.14 |
| EdwardI (Peele) | B | 0.64 | 0.78 |
| David (Peele) | B | 0.09 | 0.25 |

## DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.26 | 0.13 |
| 3H6 (Shakespeare) | A | 0.15 | 0.13 |
| 1H6 (Shakespeare) | A | 0.22 | 0.09 |
| Tit (Shakespeare) | A | 0.50 | 0.56 |
| R3 (Shakespeare) | A | 0.43 | 0.44 |
| Shr (Shakespeare) | A | 0.80 | 0.88 |
| TGV (Shakespeare) | A | 0.80 | 0.71 |
| Err (Shakespeare) | A | 0.79 | 0.85 |
| Soliman (Anon-Soliman) | B | 0.46 | 0.28 |
| Locrine (Anon-Locrine) | B | 0.16 | 0.28 |
| Selimus (Anon-Selimus) | B | 0.21 | 0.17 |
| TRKJ (Anon-TRKJ) | B | 0.63 | 0.65 |
| JackStraw (Anon-JackStraw) | B | 0.50 | 0.43 |
| EdwardIII (Anon-EdwardIII) | B | 0.47 | 0.53 |
| Arden (Anon-Arden) | B | 0.80 | 0.96 |
| TTR3 (Anon-TTR3) | B | 0.11 | 0.12 |

## DIFFERENT  Greene vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| Alphonsus (Greene) | A | 0.89 | 0.81 |
| Orlando (Greene) | A | 0.72 | 0.74 |
| FriarBacon (Greene) | A | 0.58 | 0.63 |
| JamesIV (Greene) | A | 0.49 | 0.50 |
| OWT (Peele) | B | 0.77 | 0.81 |
| Alcazar (Peele) | B | 0.13 | 0.09 |
| EdwardI (Peele) | B | 0.47 | 0.58 |
| David (Peele) | B | 0.10 | 0.12 |

## DIFFERENT  Henry VI 1-3 + Titus vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.51 | 0.28 |
| 3H6 (Shakespeare) | A | 0.53 | 0.42 |
| 1H6 (Shakespeare) | A | 0.43 | 0.21 |
| Tit (Shakespeare) | A | 0.68 | 0.72 |
| Alphonsus (Greene) | B | 0.60 | 0.61 |
| Orlando (Greene) | B | 0.36 | 0.23 |
| FriarBacon (Greene) | B | 0.27 | 0.34 |
| JamesIV (Greene) | B | 0.54 | 0.57 |

## QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.35 | 0.09 |
| 3H6 (Shakespeare) | A | 0.34 | 0.15 |
| 1H6 (Shakespeare) | A | 0.26 | 0.05 |
| Tit (Shakespeare) | A | 0.48 | 0.33 |
| 1Tam (Marlowe) | B | 0.46 | 0.36 |
| 2Tam (Marlowe) | B | 0.44 | 0.31 |
| Dido (Marlowe) | B | 0.38 | 0.29 |
| DrFaust (Marlowe) | B | 0.59 | 0.56 |
| JoM (Marlowe) | B | 0.70 | 0.62 |
| Ed2 (Marlowe) | B | 0.48 | 0.70 |
| MP (Marlowe) | B | 0.39 | 0.42 |
