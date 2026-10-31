# Pairwise distinguishability (leave-one-play-out logistic regression on 2000-word chunks)

Can a classifier trained on the *other* plays tell which set a held-out play's chunks belong to? For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; for different authors we expect values near 1. The question pair should be read against the two benchmarks.

| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |
|---|---|---|---|---|---|---|---|
| QUESTION  Marlowe vs Shakespeare early | 7 plays | 8 plays | 138 | 0.54 | 0.60 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, Henry VI excluded | 7 plays | 5 plays | 104 | 0.82 | 0.90 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched) | 7 plays | 4 plays | 99 | 0.39 | 0.25 | nan | nan |
| QUESTION  Marlowe vs Shakespeare later | 7 plays | 11 plays | 174 | 0.97 | 0.99 | nan | nan |
| QUESTION  Marlowe vs all Shakespeare | 7 plays | 19 plays | 257 | 0.83 | 0.89 | nan | nan |
| SAME-AUTHOR  Shakespeare early vs Shakespeare later | 8 plays | 11 plays | 202 | 0.72 | 0.80 | nan | nan |
| SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies | 4 plays | 4 plays | 83 | 0.67 | 0.75 | nan | nan |
| SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611 | 5 plays | 6 plays | 119 | 0.75 | 0.85 | nan | nan |
| SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93 | 3 plays | 4 plays | 55 | 0.53 | 0.55 | nan | nan |
| DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays) | 11 plays | 3 plays | 151 | 0.89 | 0.93 | nan | nan |
| DIFFERENT  Shakespeare early vs Fletcher | 8 plays | 3 plays | 115 | 0.91 | 0.92 | nan | nan |
| DIFFERENT  Marlowe vs Fletcher | 7 plays | 3 plays | 87 | 0.89 | 0.96 | nan | nan |
| DIFFERENT  Fletcher vs Ford | 3 plays | 2 plays | 51 | 0.49 | 0.38 | nan | nan |
| DIFFERENT  Shakespeare later vs Ford | 11 plays | 2 plays | 138 | 0.86 | 0.58 | nan | nan |
| DIFFERENT  Marlowe vs Ford | 7 plays | 2 plays | 74 | 0.78 | 0.93 | nan | nan |
| DIFFERENT  Marlowe vs Greene (same register, same years) | 7 plays | 4 plays | 83 | 0.73 | 0.76 | nan | nan |
| DIFFERENT  Marlowe vs Peele (same register, same years) | 7 plays | 4 plays | 82 | 0.51 | 0.47 | nan | nan |
| DIFFERENT  Marlowe vs anonymous heroic/history 1587-94 | 7 plays | 8 plays | 122 | 0.63 | 0.65 | nan | nan |
| DIFFERENT  Shakespeare early vs Greene | 8 plays | 4 plays | 111 | 0.67 | 0.64 | nan | nan |
| DIFFERENT  Shakespeare early vs Peele | 8 plays | 4 plays | 110 | 0.76 | 0.74 | nan | nan |
| DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94 | 8 plays | 8 plays | 150 | 0.53 | 0.60 | nan | nan |
| DIFFERENT  Greene vs Peele | 4 plays | 4 plays | 55 | 0.69 | 0.74 | nan | nan |
| DIFFERENT  Henry VI 1-3 + Titus vs Greene | 4 plays | 4 plays | 72 | 0.49 | 0.54 | nan | nan |
| QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison) | 4 plays | 7 plays | 99 | 0.42 | 0.26 | nan | nan |

# Per-play mean P(set A), words model


## QUESTION  Marlowe vs Shakespeare early

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.64 | nan |
| 2Tam (Marlowe) | A | 0.83 | nan |
| Dido (Marlowe) | A | 0.65 | nan |
| DrFaust (Marlowe) | A | 0.38 | nan |
| JoM (Marlowe) | A | 0.26 | nan |
| Ed2 (Marlowe) | A | 0.34 | nan |
| MP (Marlowe) | A | 0.70 | nan |
| 2H6 (Shakespeare) | B | 0.68 | nan |
| 3H6 (Shakespeare) | B | 0.72 | nan |
| 1H6 (Shakespeare) | B | 0.77 | nan |
| Tit (Shakespeare) | B | 0.24 | nan |
| R3 (Shakespeare) | B | 0.41 | nan |
| Shr (Shakespeare) | B | 0.14 | nan |
| TGV (Shakespeare) | B | 0.07 | nan |
| Err (Shakespeare) | B | 0.13 | nan |

## QUESTION  Marlowe vs Shakespeare early, Henry VI excluded

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.91 | nan |
| 2Tam (Marlowe) | A | 0.94 | nan |
| Dido (Marlowe) | A | 0.78 | nan |
| DrFaust (Marlowe) | A | 0.56 | nan |
| JoM (Marlowe) | A | 0.45 | nan |
| Ed2 (Marlowe) | A | 0.73 | nan |
| MP (Marlowe) | A | 0.82 | nan |
| Tit (Shakespeare) | B | 0.47 | nan |
| R3 (Shakespeare) | B | 0.41 | nan |
| Shr (Shakespeare) | B | 0.17 | nan |
| TGV (Shakespeare) | B | 0.14 | nan |
| Err (Shakespeare) | B | 0.08 | nan |

## QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.50 | nan |
| 2Tam (Marlowe) | A | 0.67 | nan |
| Dido (Marlowe) | A | 0.73 | nan |
| DrFaust (Marlowe) | A | 0.54 | nan |
| JoM (Marlowe) | A | 0.41 | nan |
| Ed2 (Marlowe) | A | 0.29 | nan |
| MP (Marlowe) | A | 0.65 | nan |
| 2H6 (Shakespeare) | B | 0.82 | nan |
| 3H6 (Shakespeare) | B | 0.76 | nan |
| 1H6 (Shakespeare) | B | 0.88 | nan |
| Tit (Shakespeare) | B | 0.42 | nan |

## QUESTION  Marlowe vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.93 | nan |
| 2Tam (Marlowe) | A | 0.89 | nan |
| Dido (Marlowe) | A | 0.87 | nan |
| DrFaust (Marlowe) | A | 0.75 | nan |
| JoM (Marlowe) | A | 0.54 | nan |
| Ed2 (Marlowe) | A | 0.85 | nan |
| MP (Marlowe) | A | 0.91 | nan |
| R2 (Shakespeare) | B | 0.33 | nan |
| MND (Shakespeare) | B | 0.07 | nan |
| Rom (Shakespeare) | B | 0.04 | nan |
| MV (Shakespeare) | B | 0.04 | nan |
| 1H4 (Shakespeare) | B | 0.09 | nan |
| JC (Shakespeare) | B | 0.05 | nan |
| Ham (Shakespeare) | B | 0.04 | nan |
| Mac (Shakespeare) | B | 0.02 | nan |
| Lr (Shakespeare) | B | 0.02 | nan |
| WT (Shakespeare) | B | 0.02 | nan |
| Tmp (Shakespeare) | B | 0.04 | nan |

## QUESTION  Marlowe vs all Shakespeare

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.72 | nan |
| 2Tam (Marlowe) | A | 0.80 | nan |
| Dido (Marlowe) | A | 0.63 | nan |
| DrFaust (Marlowe) | A | 0.32 | nan |
| JoM (Marlowe) | A | 0.28 | nan |
| Ed2 (Marlowe) | A | 0.40 | nan |
| MP (Marlowe) | A | 0.78 | nan |
| 2H6 (Shakespeare) | B | 0.41 | nan |
| 3H6 (Shakespeare) | B | 0.60 | nan |
| 1H6 (Shakespeare) | B | 0.55 | nan |
| Tit (Shakespeare) | B | 0.19 | nan |
| R3 (Shakespeare) | B | 0.13 | nan |
| Shr (Shakespeare) | B | 0.08 | nan |
| TGV (Shakespeare) | B | 0.02 | nan |
| Err (Shakespeare) | B | 0.03 | nan |
| R2 (Shakespeare) | B | 0.13 | nan |
| MND (Shakespeare) | B | 0.03 | nan |
| Rom (Shakespeare) | B | 0.01 | nan |
| MV (Shakespeare) | B | 0.02 | nan |
| 1H4 (Shakespeare) | B | 0.03 | nan |
| JC (Shakespeare) | B | 0.04 | nan |
| Ham (Shakespeare) | B | 0.02 | nan |
| Mac (Shakespeare) | B | 0.01 | nan |
| Lr (Shakespeare) | B | 0.01 | nan |
| WT (Shakespeare) | B | 0.01 | nan |
| Tmp (Shakespeare) | B | 0.02 | nan |

## SAME-AUTHOR  Shakespeare early vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.36 | nan |
| 3H6 (Shakespeare) | A | 0.54 | nan |
| 1H6 (Shakespeare) | A | 0.23 | nan |
| Tit (Shakespeare) | A | 0.77 | nan |
| R3 (Shakespeare) | A | 0.27 | nan |
| Shr (Shakespeare) | A | 0.61 | nan |
| TGV (Shakespeare) | A | 0.57 | nan |
| Err (Shakespeare) | A | 0.66 | nan |
| R2 (Shakespeare) | B | 0.56 | nan |
| MND (Shakespeare) | B | 0.20 | nan |
| Rom (Shakespeare) | B | 0.26 | nan |
| MV (Shakespeare) | B | 0.22 | nan |
| 1H4 (Shakespeare) | B | 0.30 | nan |
| JC (Shakespeare) | B | 0.18 | nan |
| Ham (Shakespeare) | B | 0.10 | nan |
| Mac (Shakespeare) | B | 0.03 | nan |
| Lr (Shakespeare) | B | 0.08 | nan |
| WT (Shakespeare) | B | 0.07 | nan |
| Tmp (Shakespeare) | B | 0.08 | nan |

## SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.58 | nan |
| 3H6 (Shakespeare) | A | 0.66 | nan |
| 1H6 (Shakespeare) | A | 0.57 | nan |
| Tit (Shakespeare) | A | 0.60 | nan |
| R3 (Shakespeare) | B | 0.63 | nan |
| Shr (Shakespeare) | B | 0.32 | nan |
| TGV (Shakespeare) | B | 0.17 | nan |
| Err (Shakespeare) | B | 0.11 | nan |

## SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.56 | nan |
| MND (Shakespeare) | A | 0.69 | nan |
| Rom (Shakespeare) | A | 0.79 | nan |
| MV (Shakespeare) | A | 0.51 | nan |
| 1H4 (Shakespeare) | A | 0.63 | nan |
| JC (Shakespeare) | B | 0.68 | nan |
| Ham (Shakespeare) | B | 0.34 | nan |
| Mac (Shakespeare) | B | 0.06 | nan |
| Lr (Shakespeare) | B | 0.18 | nan |
| WT (Shakespeare) | B | 0.12 | nan |
| Tmp (Shakespeare) | B | 0.17 | nan |

## SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.22 | nan |
| 2Tam (Marlowe) | A | 0.26 | nan |
| Dido (Marlowe) | A | 0.23 | nan |
| DrFaust (Marlowe) | B | 0.35 | nan |
| JoM (Marlowe) | B | 0.17 | nan |
| Ed2 (Marlowe) | B | 0.25 | nan |
| MP (Marlowe) | B | 0.15 | nan |

## DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.98 | nan |
| MND (Shakespeare) | A | 0.93 | nan |
| Rom (Shakespeare) | A | 0.97 | nan |
| MV (Shakespeare) | A | 0.97 | nan |
| 1H4 (Shakespeare) | A | 0.97 | nan |
| JC (Shakespeare) | A | 0.97 | nan |
| Ham (Shakespeare) | A | 0.99 | nan |
| Mac (Shakespeare) | A | 0.92 | nan |
| Lr (Shakespeare) | A | 0.97 | nan |
| WT (Shakespeare) | A | 0.96 | nan |
| Tmp (Shakespeare) | A | 0.95 | nan |
| FS (Fletcher) | B | 0.91 | nan |
| Prize (Fletcher) | B | 0.34 | nan |
| IP (Fletcher) | B | 0.40 | nan |

## DIFFERENT  Shakespeare early vs Fletcher

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.90 | nan |
| 3H6 (Shakespeare) | A | 0.95 | nan |
| 1H6 (Shakespeare) | A | 0.83 | nan |
| Tit (Shakespeare) | A | 0.97 | nan |
| R3 (Shakespeare) | A | 0.95 | nan |
| Shr (Shakespeare) | A | 0.90 | nan |
| TGV (Shakespeare) | A | 0.91 | nan |
| Err (Shakespeare) | A | 0.95 | nan |
| FS (Fletcher) | B | 0.86 | nan |
| Prize (Fletcher) | B | 0.19 | nan |
| IP (Fletcher) | B | 0.21 | nan |

## DIFFERENT  Marlowe vs Fletcher

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.94 | nan |
| 2Tam (Marlowe) | A | 0.95 | nan |
| Dido (Marlowe) | A | 0.96 | nan |
| DrFaust (Marlowe) | A | 0.87 | nan |
| JoM (Marlowe) | A | 0.80 | nan |
| Ed2 (Marlowe) | A | 0.98 | nan |
| MP (Marlowe) | A | 0.98 | nan |
| FS (Fletcher) | B | 0.79 | nan |
| Prize (Fletcher) | B | 0.11 | nan |
| IP (Fletcher) | B | 0.16 | nan |

## DIFFERENT  Fletcher vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| FS (Fletcher) | A | 0.32 | nan |
| Prize (Fletcher) | A | 0.69 | nan |
| IP (Fletcher) | A | 0.72 | nan |
| Perkin (Ford) | B | 0.58 | nan |
| TPSW (Ford) | B | 0.79 | nan |

## DIFFERENT  Shakespeare later vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.92 | nan |
| MND (Shakespeare) | A | 0.98 | nan |
| Rom (Shakespeare) | A | 0.98 | nan |
| MV (Shakespeare) | A | 0.94 | nan |
| 1H4 (Shakespeare) | A | 0.96 | nan |
| JC (Shakespeare) | A | 0.99 | nan |
| Ham (Shakespeare) | A | 0.96 | nan |
| Mac (Shakespeare) | A | 0.97 | nan |
| Lr (Shakespeare) | A | 0.97 | nan |
| WT (Shakespeare) | A | 0.92 | nan |
| Tmp (Shakespeare) | A | 0.97 | nan |
| Perkin (Ford) | B | 0.92 | nan |
| TPSW (Ford) | B | 0.96 | nan |

## DIFFERENT  Marlowe vs Ford

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.93 | nan |
| 2Tam (Marlowe) | A | 0.97 | nan |
| Dido (Marlowe) | A | 0.98 | nan |
| DrFaust (Marlowe) | A | 0.88 | nan |
| JoM (Marlowe) | A | 0.81 | nan |
| Ed2 (Marlowe) | A | 0.93 | nan |
| MP (Marlowe) | A | 0.97 | nan |
| Perkin (Ford) | B | 0.69 | nan |
| TPSW (Ford) | B | 0.69 | nan |

## DIFFERENT  Marlowe vs Greene (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.75 | nan |
| 2Tam (Marlowe) | A | 0.87 | nan |
| Dido (Marlowe) | A | 0.73 | nan |
| DrFaust (Marlowe) | A | 0.67 | nan |
| JoM (Marlowe) | A | 0.64 | nan |
| Ed2 (Marlowe) | A | 0.85 | nan |
| MP (Marlowe) | A | 0.83 | nan |
| Alphonsus (Greene) | B | 0.79 | nan |
| Orlando (Greene) | B | 0.51 | nan |
| FriarBacon (Greene) | B | 0.35 | nan |
| JamesIV (Greene) | B | 0.58 | nan |

## DIFFERENT  Marlowe vs Peele (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.33 | nan |
| 2Tam (Marlowe) | A | 0.37 | nan |
| Dido (Marlowe) | A | 0.60 | nan |
| DrFaust (Marlowe) | A | 0.79 | nan |
| JoM (Marlowe) | A | 0.87 | nan |
| Ed2 (Marlowe) | A | 0.75 | nan |
| MP (Marlowe) | A | 0.70 | nan |
| OWT (Peele) | B | 0.61 | nan |
| Alcazar (Peele) | B | 0.60 | nan |
| EdwardI (Peele) | B | 0.75 | nan |
| David (Peele) | B | 0.67 | nan |

## DIFFERENT  Marlowe vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.37 | nan |
| 2Tam (Marlowe) | A | 0.66 | nan |
| Dido (Marlowe) | A | 0.78 | nan |
| DrFaust (Marlowe) | A | 0.43 | nan |
| JoM (Marlowe) | A | 0.22 | nan |
| Ed2 (Marlowe) | A | 0.46 | nan |
| MP (Marlowe) | A | 0.68 | nan |
| Soliman (Anon-Soliman) | B | 0.19 | nan |
| Locrine (Anon-Locrine) | B | 0.52 | nan |
| Selimus (Anon-Selimus) | B | 0.17 | nan |
| TRKJ (Anon-TRKJ) | B | 0.55 | nan |
| JackStraw (Anon-JackStraw) | B | 0.31 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.44 | nan |
| Arden (Anon-Arden) | B | 0.44 | nan |
| TTR3 (Anon-TTR3) | B | 0.29 | nan |

## DIFFERENT  Shakespeare early vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.53 | nan |
| 3H6 (Shakespeare) | A | 0.56 | nan |
| 1H6 (Shakespeare) | A | 0.42 | nan |
| Tit (Shakespeare) | A | 0.95 | nan |
| R3 (Shakespeare) | A | 0.69 | nan |
| Shr (Shakespeare) | A | 0.90 | nan |
| TGV (Shakespeare) | A | 0.90 | nan |
| Err (Shakespeare) | A | 0.95 | nan |
| Alphonsus (Greene) | B | 0.72 | nan |
| Orlando (Greene) | B | 0.32 | nan |
| FriarBacon (Greene) | B | 0.42 | nan |
| JamesIV (Greene) | B | 0.80 | nan |

## DIFFERENT  Shakespeare early vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.53 | nan |
| 3H6 (Shakespeare) | A | 0.64 | nan |
| 1H6 (Shakespeare) | A | 0.56 | nan |
| Tit (Shakespeare) | A | 0.76 | nan |
| R3 (Shakespeare) | A | 0.74 | nan |
| Shr (Shakespeare) | A | 0.90 | nan |
| TGV (Shakespeare) | A | 0.97 | nan |
| Err (Shakespeare) | A | 0.97 | nan |
| OWT (Peele) | B | 0.72 | nan |
| Alcazar (Peele) | B | 0.21 | nan |
| EdwardI (Peele) | B | 0.70 | nan |
| David (Peele) | B | 0.21 | nan |

## DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.25 | nan |
| 3H6 (Shakespeare) | A | 0.19 | nan |
| 1H6 (Shakespeare) | A | 0.20 | nan |
| Tit (Shakespeare) | A | 0.88 | nan |
| R3 (Shakespeare) | A | 0.53 | nan |
| Shr (Shakespeare) | A | 0.80 | nan |
| TGV (Shakespeare) | A | 0.84 | nan |
| Err (Shakespeare) | A | 0.64 | nan |
| Soliman (Anon-Soliman) | B | 0.44 | nan |
| Locrine (Anon-Locrine) | B | 0.27 | nan |
| Selimus (Anon-Selimus) | B | 0.30 | nan |
| TRKJ (Anon-TRKJ) | B | 0.53 | nan |
| JackStraw (Anon-JackStraw) | B | 0.17 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.55 | nan |
| Arden (Anon-Arden) | B | 0.69 | nan |
| TTR3 (Anon-TTR3) | B | 0.19 | nan |

## DIFFERENT  Greene vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| Alphonsus (Greene) | A | 0.74 | nan |
| Orlando (Greene) | A | 0.66 | nan |
| FriarBacon (Greene) | A | 0.58 | nan |
| JamesIV (Greene) | A | 0.57 | nan |
| OWT (Peele) | B | 0.62 | nan |
| Alcazar (Peele) | B | 0.15 | nan |
| EdwardI (Peele) | B | 0.57 | nan |
| David (Peele) | B | 0.14 | nan |

## DIFFERENT  Henry VI 1-3 + Titus vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.43 | nan |
| 3H6 (Shakespeare) | A | 0.50 | nan |
| 1H6 (Shakespeare) | A | 0.37 | nan |
| Tit (Shakespeare) | A | 0.86 | nan |
| Alphonsus (Greene) | B | 0.70 | nan |
| Orlando (Greene) | B | 0.31 | nan |
| FriarBacon (Greene) | B | 0.29 | nan |
| JamesIV (Greene) | B | 0.63 | nan |

## QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.18 | nan |
| 3H6 (Shakespeare) | A | 0.23 | nan |
| 1H6 (Shakespeare) | A | 0.12 | nan |
| Tit (Shakespeare) | A | 0.59 | nan |
| 1Tam (Marlowe) | B | 0.47 | nan |
| 2Tam (Marlowe) | B | 0.31 | nan |
| Dido (Marlowe) | B | 0.27 | nan |
| DrFaust (Marlowe) | B | 0.46 | nan |
| JoM (Marlowe) | B | 0.60 | nan |
| Ed2 (Marlowe) | B | 0.71 | nan |
| MP (Marlowe) | B | 0.36 | nan |
