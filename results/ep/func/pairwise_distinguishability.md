# Pairwise distinguishability (leave-one-play-out logistic regression on 2000-word chunks)

Can a classifier trained on the *other* plays tell which set a held-out play's chunks belong to? For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; for different authors we expect values near 1. The question pair should be read against the two benchmarks.

| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |
|---|---|---|---|---|---|---|---|
| QUESTION  Marlowe vs Shakespeare early | 7 plays | 8 plays | 139 | 0.68 | 0.76 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, Henry VI excluded | 7 plays | 5 plays | 105 | 0.86 | 0.94 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched) | 7 plays | 4 plays | 99 | 0.38 | 0.30 | nan | nan |
| QUESTION  Marlowe vs Shakespeare later | 7 plays | 11 plays | 173 | 0.93 | 0.98 | nan | nan |
| QUESTION  Marlowe vs all Shakespeare | 7 plays | 19 plays | 257 | 0.86 | 0.92 | nan | nan |
| SAME-AUTHOR  Shakespeare early vs Shakespeare later | 8 plays | 11 plays | 202 | 0.73 | 0.81 | nan | nan |
| SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies | 4 plays | 4 plays | 84 | 0.71 | 0.82 | nan | nan |
| SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611 | 5 plays | 6 plays | 118 | 0.67 | 0.76 | nan | nan |
| SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93 | 3 plays | 4 plays | 55 | 0.55 | 0.60 | nan | nan |
| DIFFERENT  Marlowe vs Greene (same register, same years) | 7 plays | 4 plays | 83 | 0.57 | 0.60 | nan | nan |
| DIFFERENT  Marlowe vs Peele (same register, same years) | 7 plays | 4 plays | 82 | 0.57 | 0.61 | nan | nan |
| DIFFERENT  Marlowe vs anonymous heroic/history 1587-94 | 7 plays | 8 plays | 122 | 0.63 | 0.65 | nan | nan |
| DIFFERENT  Shakespeare early vs Greene | 8 plays | 4 plays | 112 | 0.64 | 0.61 | nan | nan |
| DIFFERENT  Shakespeare early vs Peele | 8 plays | 4 plays | 111 | 0.72 | 0.74 | nan | nan |
| DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94 | 8 plays | 8 plays | 151 | 0.58 | 0.63 | nan | nan |
| DIFFERENT  Greene vs Peele | 4 plays | 4 plays | 55 | 0.60 | 0.71 | nan | nan |
| DIFFERENT  Henry VI 1-3 + Titus vs Greene | 4 plays | 4 plays | 72 | 0.42 | 0.42 | nan | nan |
| QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison) | 4 plays | 7 plays | 99 | 0.38 | 0.30 | nan | nan |

# Per-play mean P(set A), words model


## QUESTION  Marlowe vs Shakespeare early

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.45 | nan |
| 2Tam (Marlowe) | A | 0.71 | nan |
| Dido (Marlowe) | A | 0.64 | nan |
| DrFaust (Marlowe) | A | 0.58 | nan |
| JoM (Marlowe) | A | 0.60 | nan |
| Ed2 (Marlowe) | A | 0.55 | nan |
| MP (Marlowe) | A | 0.74 | nan |
| 2H6 (Shakespeare) | B | 0.55 | nan |
| 3H6 (Shakespeare) | B | 0.58 | nan |
| 1H6 (Shakespeare) | B | 0.69 | nan |
| Tit (Shakespeare) | B | 0.20 | nan |
| R3 (Shakespeare) | B | 0.32 | nan |
| Shr (Shakespeare) | B | 0.10 | nan |
| TGV (Shakespeare) | B | 0.02 | nan |
| Err (Shakespeare) | B | 0.03 | nan |

## QUESTION  Marlowe vs Shakespeare early, Henry VI excluded

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.77 | nan |
| 2Tam (Marlowe) | A | 0.94 | nan |
| Dido (Marlowe) | A | 0.88 | nan |
| DrFaust (Marlowe) | A | 0.66 | nan |
| JoM (Marlowe) | A | 0.55 | nan |
| Ed2 (Marlowe) | A | 0.74 | nan |
| MP (Marlowe) | A | 0.78 | nan |
| Tit (Shakespeare) | B | 0.43 | nan |
| R3 (Shakespeare) | B | 0.32 | nan |
| Shr (Shakespeare) | B | 0.28 | nan |
| TGV (Shakespeare) | B | 0.03 | nan |
| Err (Shakespeare) | B | 0.08 | nan |

## QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.30 | nan |
| 2Tam (Marlowe) | A | 0.46 | nan |
| Dido (Marlowe) | A | 0.54 | nan |
| DrFaust (Marlowe) | A | 0.56 | nan |
| JoM (Marlowe) | A | 0.51 | nan |
| Ed2 (Marlowe) | A | 0.51 | nan |
| MP (Marlowe) | A | 0.67 | nan |
| 2H6 (Shakespeare) | B | 0.70 | nan |
| 3H6 (Shakespeare) | B | 0.74 | nan |
| 1H6 (Shakespeare) | B | 0.87 | nan |
| Tit (Shakespeare) | B | 0.35 | nan |

## QUESTION  Marlowe vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.78 | nan |
| 2Tam (Marlowe) | A | 0.82 | nan |
| Dido (Marlowe) | A | 0.92 | nan |
| DrFaust (Marlowe) | A | 0.57 | nan |
| JoM (Marlowe) | A | 0.64 | nan |
| Ed2 (Marlowe) | A | 0.82 | nan |
| MP (Marlowe) | A | 0.92 | nan |
| R2 (Shakespeare) | B | 0.27 | nan |
| MND (Shakespeare) | B | 0.16 | nan |
| Rom (Shakespeare) | B | 0.10 | nan |
| MV (Shakespeare) | B | 0.06 | nan |
| 1H4 (Shakespeare) | B | 0.18 | nan |
| JC (Shakespeare) | B | 0.14 | nan |
| Ham (Shakespeare) | B | 0.04 | nan |
| Mac (Shakespeare) | B | 0.11 | nan |
| Lr (Shakespeare) | B | 0.05 | nan |
| WT (Shakespeare) | B | 0.03 | nan |
| Tmp (Shakespeare) | B | 0.05 | nan |

## QUESTION  Marlowe vs all Shakespeare

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.50 | nan |
| 2Tam (Marlowe) | A | 0.68 | nan |
| Dido (Marlowe) | A | 0.74 | nan |
| DrFaust (Marlowe) | A | 0.54 | nan |
| JoM (Marlowe) | A | 0.64 | nan |
| Ed2 (Marlowe) | A | 0.61 | nan |
| MP (Marlowe) | A | 0.82 | nan |
| 2H6 (Shakespeare) | B | 0.48 | nan |
| 3H6 (Shakespeare) | B | 0.54 | nan |
| 1H6 (Shakespeare) | B | 0.51 | nan |
| Tit (Shakespeare) | B | 0.15 | nan |
| R3 (Shakespeare) | B | 0.13 | nan |
| Shr (Shakespeare) | B | 0.03 | nan |
| TGV (Shakespeare) | B | 0.01 | nan |
| Err (Shakespeare) | B | 0.02 | nan |
| R2 (Shakespeare) | B | 0.09 | nan |
| MND (Shakespeare) | B | 0.08 | nan |
| Rom (Shakespeare) | B | 0.03 | nan |
| MV (Shakespeare) | B | 0.01 | nan |
| 1H4 (Shakespeare) | B | 0.11 | nan |
| JC (Shakespeare) | B | 0.10 | nan |
| Ham (Shakespeare) | B | 0.03 | nan |
| Mac (Shakespeare) | B | 0.08 | nan |
| Lr (Shakespeare) | B | 0.03 | nan |
| WT (Shakespeare) | B | 0.04 | nan |
| Tmp (Shakespeare) | B | 0.03 | nan |

## SAME-AUTHOR  Shakespeare early vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.57 | nan |
| 3H6 (Shakespeare) | A | 0.73 | nan |
| 1H6 (Shakespeare) | A | 0.25 | nan |
| Tit (Shakespeare) | A | 0.76 | nan |
| R3 (Shakespeare) | A | 0.45 | nan |
| Shr (Shakespeare) | A | 0.63 | nan |
| TGV (Shakespeare) | A | 0.73 | nan |
| Err (Shakespeare) | A | 0.47 | nan |
| R2 (Shakespeare) | B | 0.50 | nan |
| MND (Shakespeare) | B | 0.42 | nan |
| Rom (Shakespeare) | B | 0.46 | nan |
| MV (Shakespeare) | B | 0.37 | nan |
| 1H4 (Shakespeare) | B | 0.26 | nan |
| JC (Shakespeare) | B | 0.25 | nan |
| Ham (Shakespeare) | B | 0.09 | nan |
| Mac (Shakespeare) | B | 0.02 | nan |
| Lr (Shakespeare) | B | 0.13 | nan |
| WT (Shakespeare) | B | 0.07 | nan |
| Tmp (Shakespeare) | B | 0.09 | nan |

## SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.59 | nan |
| 3H6 (Shakespeare) | A | 0.64 | nan |
| 1H6 (Shakespeare) | A | 0.60 | nan |
| Tit (Shakespeare) | A | 0.61 | nan |
| R3 (Shakespeare) | B | 0.43 | nan |
| Shr (Shakespeare) | B | 0.40 | nan |
| TGV (Shakespeare) | B | 0.13 | nan |
| Err (Shakespeare) | B | 0.15 | nan |

## SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| R2 (Shakespeare) | A | 0.42 | nan |
| MND (Shakespeare) | A | 0.73 | nan |
| Rom (Shakespeare) | A | 0.74 | nan |
| MV (Shakespeare) | A | 0.50 | nan |
| 1H4 (Shakespeare) | A | 0.53 | nan |
| JC (Shakespeare) | B | 0.69 | nan |
| Ham (Shakespeare) | B | 0.34 | nan |
| Mac (Shakespeare) | B | 0.07 | nan |
| Lr (Shakespeare) | B | 0.37 | nan |
| WT (Shakespeare) | B | 0.13 | nan |
| Tmp (Shakespeare) | B | 0.21 | nan |

## SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.30 | nan |
| 2Tam (Marlowe) | A | 0.38 | nan |
| Dido (Marlowe) | A | 0.25 | nan |
| DrFaust (Marlowe) | B | 0.38 | nan |
| JoM (Marlowe) | B | 0.08 | nan |
| Ed2 (Marlowe) | B | 0.29 | nan |
| MP (Marlowe) | B | 0.32 | nan |

## DIFFERENT  Marlowe vs Greene (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.51 | nan |
| 2Tam (Marlowe) | A | 0.73 | nan |
| Dido (Marlowe) | A | 0.46 | nan |
| DrFaust (Marlowe) | A | 0.53 | nan |
| JoM (Marlowe) | A | 0.81 | nan |
| Ed2 (Marlowe) | A | 0.88 | nan |
| MP (Marlowe) | A | 0.69 | nan |
| Alphonsus (Greene) | B | 0.64 | nan |
| Orlando (Greene) | B | 0.66 | nan |
| FriarBacon (Greene) | B | 0.46 | nan |
| JamesIV (Greene) | B | 0.67 | nan |

## DIFFERENT  Marlowe vs Peele (same register, same years)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.33 | nan |
| 2Tam (Marlowe) | A | 0.38 | nan |
| Dido (Marlowe) | A | 0.62 | nan |
| DrFaust (Marlowe) | A | 0.77 | nan |
| JoM (Marlowe) | A | 0.87 | nan |
| Ed2 (Marlowe) | A | 0.86 | nan |
| MP (Marlowe) | A | 0.69 | nan |
| OWT (Peele) | B | 0.63 | nan |
| Alcazar (Peele) | B | 0.47 | nan |
| EdwardI (Peele) | B | 0.69 | nan |
| David (Peele) | B | 0.38 | nan |

## DIFFERENT  Marlowe vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.34 | nan |
| 2Tam (Marlowe) | A | 0.57 | nan |
| Dido (Marlowe) | A | 0.54 | nan |
| DrFaust (Marlowe) | A | 0.44 | nan |
| JoM (Marlowe) | A | 0.52 | nan |
| Ed2 (Marlowe) | A | 0.58 | nan |
| MP (Marlowe) | A | 0.58 | nan |
| Soliman (Anon-Soliman) | B | 0.21 | nan |
| Locrine (Anon-Locrine) | B | 0.64 | nan |
| Selimus (Anon-Selimus) | B | 0.25 | nan |
| TRKJ (Anon-TRKJ) | B | 0.35 | nan |
| JackStraw (Anon-JackStraw) | B | 0.49 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.37 | nan |
| Arden (Anon-Arden) | B | 0.55 | nan |
| TTR3 (Anon-TTR3) | B | 0.19 | nan |

## DIFFERENT  Shakespeare early vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.55 | nan |
| 3H6 (Shakespeare) | A | 0.57 | nan |
| 1H6 (Shakespeare) | A | 0.38 | nan |
| Tit (Shakespeare) | A | 0.95 | nan |
| R3 (Shakespeare) | A | 0.67 | nan |
| Shr (Shakespeare) | A | 0.85 | nan |
| TGV (Shakespeare) | A | 0.94 | nan |
| Err (Shakespeare) | A | 0.95 | nan |
| Alphonsus (Greene) | B | 0.70 | nan |
| Orlando (Greene) | B | 0.44 | nan |
| FriarBacon (Greene) | B | 0.47 | nan |
| JamesIV (Greene) | B | 0.78 | nan |

## DIFFERENT  Shakespeare early vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.57 | nan |
| 3H6 (Shakespeare) | A | 0.67 | nan |
| 1H6 (Shakespeare) | A | 0.46 | nan |
| Tit (Shakespeare) | A | 0.66 | nan |
| R3 (Shakespeare) | A | 0.77 | nan |
| Shr (Shakespeare) | A | 0.80 | nan |
| TGV (Shakespeare) | A | 0.99 | nan |
| Err (Shakespeare) | A | 0.98 | nan |
| OWT (Peele) | B | 0.77 | nan |
| Alcazar (Peele) | B | 0.15 | nan |
| EdwardI (Peele) | B | 0.66 | nan |
| David (Peele) | B | 0.14 | nan |

## DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.41 | nan |
| 3H6 (Shakespeare) | A | 0.25 | nan |
| 1H6 (Shakespeare) | A | 0.29 | nan |
| Tit (Shakespeare) | A | 0.78 | nan |
| R3 (Shakespeare) | A | 0.52 | nan |
| Shr (Shakespeare) | A | 0.89 | nan |
| TGV (Shakespeare) | A | 0.79 | nan |
| Err (Shakespeare) | A | 0.76 | nan |
| Soliman (Anon-Soliman) | B | 0.37 | nan |
| Locrine (Anon-Locrine) | B | 0.33 | nan |
| Selimus (Anon-Selimus) | B | 0.34 | nan |
| TRKJ (Anon-TRKJ) | B | 0.53 | nan |
| JackStraw (Anon-JackStraw) | B | 0.20 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.68 | nan |
| Arden (Anon-Arden) | B | 0.71 | nan |
| TTR3 (Anon-TTR3) | B | 0.18 | nan |

## DIFFERENT  Greene vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| Alphonsus (Greene) | A | 0.85 | nan |
| Orlando (Greene) | A | 0.57 | nan |
| FriarBacon (Greene) | A | 0.51 | nan |
| JamesIV (Greene) | A | 0.52 | nan |
| OWT (Peele) | B | 0.67 | nan |
| Alcazar (Peele) | B | 0.13 | nan |
| EdwardI (Peele) | B | 0.57 | nan |
| David (Peele) | B | 0.11 | nan |

## DIFFERENT  Henry VI 1-3 + Titus vs Greene

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.46 | nan |
| 3H6 (Shakespeare) | A | 0.46 | nan |
| 1H6 (Shakespeare) | A | 0.35 | nan |
| Tit (Shakespeare) | A | 0.86 | nan |
| Alphonsus (Greene) | B | 0.72 | nan |
| Orlando (Greene) | B | 0.44 | nan |
| FriarBacon (Greene) | B | 0.48 | nan |
| JamesIV (Greene) | B | 0.68 | nan |

## QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.30 | nan |
| 3H6 (Shakespeare) | A | 0.26 | nan |
| 1H6 (Shakespeare) | A | 0.13 | nan |
| Tit (Shakespeare) | A | 0.65 | nan |
| 1Tam (Marlowe) | B | 0.70 | nan |
| 2Tam (Marlowe) | B | 0.54 | nan |
| Dido (Marlowe) | B | 0.46 | nan |
| DrFaust (Marlowe) | B | 0.44 | nan |
| JoM (Marlowe) | B | 0.49 | nan |
| Ed2 (Marlowe) | B | 0.49 | nan |
| MP (Marlowe) | B | 0.33 | nan |
