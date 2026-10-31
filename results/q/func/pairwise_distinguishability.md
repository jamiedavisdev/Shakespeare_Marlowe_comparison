# Pairwise distinguishability (leave-one-play-out logistic regression on 2000-word chunks)

Can a classifier trained on the *other* plays tell which set a held-out play's chunks belong to? For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; for different authors we expect values near 1. The question pair should be read against the two benchmarks.

| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |
|---|---|---|---|---|---|---|---|
| QUESTION  Marlowe vs Shakespeare early | 7 plays | 4 plays | 94 | 0.52 | 0.54 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, Henry VI excluded | 7 plays | 2 plays | 78 | 0.64 | 0.62 | nan | nan |
| QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched) | 7 plays | 3 plays | 81 | 0.65 | 0.55 | nan | nan |
| QUESTION  Marlowe vs Shakespeare later | 7 plays | 10 plays | 160 | 0.93 | 0.98 | nan | nan |
| QUESTION  Marlowe vs all Shakespeare | 7 plays | 14 plays | 199 | 0.88 | 0.93 | nan | nan |
| SAME-AUTHOR  Shakespeare early vs Shakespeare later | 4 plays | 10 plays | 144 | 0.71 | 0.73 | nan | nan |
| SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93 | 3 plays | 4 plays | 55 | 0.55 | 0.60 | nan | nan |
| DIFFERENT  Marlowe vs Greene (same register, same years) | 7 plays | 4 plays | 83 | 0.57 | 0.60 | nan | nan |
| DIFFERENT  Marlowe vs Peele (same register, same years) | 7 plays | 4 plays | 82 | 0.57 | 0.61 | nan | nan |
| DIFFERENT  Marlowe vs anonymous heroic/history 1587-94 | 7 plays | 8 plays | 122 | 0.63 | 0.65 | nan | nan |
| DIFFERENT  Shakespeare early vs Greene | 4 plays | 4 plays | 67 | 0.49 | 0.50 | nan | nan |
| DIFFERENT  Shakespeare early vs Peele | 4 plays | 4 plays | 66 | 0.56 | 0.65 | nan | nan |
| DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94 | 4 plays | 8 plays | 106 | 0.55 | 0.47 | nan | nan |
| DIFFERENT  Greene vs Peele | 4 plays | 4 plays | 55 | 0.60 | 0.71 | nan | nan |
| DIFFERENT  Henry VI 1-3 + Titus vs Greene | 3 plays | 4 plays | 54 | 0.61 | 0.63 | nan | nan |
| QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison) | 3 plays | 7 plays | 81 | 0.65 | 0.55 | nan | nan |

# Per-play mean P(set A), words model


## QUESTION  Marlowe vs Shakespeare early

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.49 | nan |
| 2Tam (Marlowe) | A | 0.76 | nan |
| Dido (Marlowe) | A | 0.83 | nan |
| DrFaust (Marlowe) | A | 0.59 | nan |
| JoM (Marlowe) | A | 0.62 | nan |
| Ed2 (Marlowe) | A | 0.65 | nan |
| MP (Marlowe) | A | 0.63 | nan |
| 2H6 (Shakespeare) | B | 0.76 | nan |
| 3H6 (Shakespeare) | B | 0.67 | nan |
| Tit (Shakespeare) | B | 0.36 | nan |
| R3 (Shakespeare) | B | 0.67 | nan |

## QUESTION  Marlowe vs Shakespeare early, Henry VI excluded

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.60 | nan |
| 2Tam (Marlowe) | A | 0.78 | nan |
| Dido (Marlowe) | A | 0.88 | nan |
| DrFaust (Marlowe) | A | 0.75 | nan |
| JoM (Marlowe) | A | 0.63 | nan |
| Ed2 (Marlowe) | A | 0.72 | nan |
| MP (Marlowe) | A | 0.70 | nan |
| Tit (Shakespeare) | B | 0.59 | nan |
| R3 (Shakespeare) | B | 0.67 | nan |

## QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.53 | nan |
| 2Tam (Marlowe) | A | 0.72 | nan |
| Dido (Marlowe) | A | 0.83 | nan |
| DrFaust (Marlowe) | A | 0.63 | nan |
| JoM (Marlowe) | A | 0.66 | nan |
| Ed2 (Marlowe) | A | 0.73 | nan |
| MP (Marlowe) | A | 0.69 | nan |
| 2H6 (Shakespeare) | B | 0.76 | nan |
| 3H6 (Shakespeare) | B | 0.67 | nan |
| Tit (Shakespeare) | B | 0.56 | nan |

## QUESTION  Marlowe vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.75 | nan |
| 2Tam (Marlowe) | A | 0.79 | nan |
| Dido (Marlowe) | A | 0.91 | nan |
| DrFaust (Marlowe) | A | 0.67 | nan |
| JoM (Marlowe) | A | 0.67 | nan |
| Ed2 (Marlowe) | A | 0.84 | nan |
| MP (Marlowe) | A | 0.94 | nan |
| R2 (Shakespeare) | B | 0.37 | nan |
| Rom (Shakespeare) | B | 0.11 | nan |
| 1H4 (Shakespeare) | B | 0.17 | nan |
| LLL (Shakespeare) | B | 0.02 | nan |
| MND (Shakespeare) | B | 0.16 | nan |
| MV (Shakespeare) | B | 0.07 | nan |
| Ado (Shakespeare) | B | 0.01 | nan |
| 2H4 (Shakespeare) | B | 0.07 | nan |
| Lr (Shakespeare) | B | 0.07 | nan |
| Tro (Shakespeare) | B | 0.09 | nan |

## QUESTION  Marlowe vs all Shakespeare

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 1Tam (Marlowe) | A | 0.53 | nan |
| 2Tam (Marlowe) | A | 0.72 | nan |
| Dido (Marlowe) | A | 0.88 | nan |
| DrFaust (Marlowe) | A | 0.57 | nan |
| JoM (Marlowe) | A | 0.61 | nan |
| Ed2 (Marlowe) | A | 0.72 | nan |
| MP (Marlowe) | A | 0.82 | nan |
| 2H6 (Shakespeare) | B | 0.63 | nan |
| 3H6 (Shakespeare) | B | 0.54 | nan |
| Tit (Shakespeare) | B | 0.22 | nan |
| R3 (Shakespeare) | B | 0.18 | nan |
| R2 (Shakespeare) | B | 0.14 | nan |
| Rom (Shakespeare) | B | 0.05 | nan |
| 1H4 (Shakespeare) | B | 0.09 | nan |
| LLL (Shakespeare) | B | 0.01 | nan |
| MND (Shakespeare) | B | 0.12 | nan |
| MV (Shakespeare) | B | 0.05 | nan |
| Ado (Shakespeare) | B | 0.01 | nan |
| 2H4 (Shakespeare) | B | 0.06 | nan |
| Lr (Shakespeare) | B | 0.06 | nan |
| Tro (Shakespeare) | B | 0.13 | nan |

## SAME-AUTHOR  Shakespeare early vs Shakespeare later

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.41 | nan |
| 3H6 (Shakespeare) | A | 0.55 | nan |
| Tit (Shakespeare) | A | 0.51 | nan |
| R3 (Shakespeare) | A | 0.12 | nan |
| R2 (Shakespeare) | B | 0.69 | nan |
| Rom (Shakespeare) | B | 0.30 | nan |
| 1H4 (Shakespeare) | B | 0.20 | nan |
| LLL (Shakespeare) | B | 0.10 | nan |
| MND (Shakespeare) | B | 0.15 | nan |
| MV (Shakespeare) | B | 0.17 | nan |
| Ado (Shakespeare) | B | 0.05 | nan |
| 2H4 (Shakespeare) | B | 0.11 | nan |
| Lr (Shakespeare) | B | 0.15 | nan |
| Tro (Shakespeare) | B | 0.06 | nan |

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
| 2H6 (Shakespeare) | A | 0.45 | nan |
| 3H6 (Shakespeare) | A | 0.52 | nan |
| Tit (Shakespeare) | A | 0.83 | nan |
| R3 (Shakespeare) | A | 0.40 | nan |
| Alphonsus (Greene) | B | 0.78 | nan |
| Orlando (Greene) | B | 0.33 | nan |
| FriarBacon (Greene) | B | 0.34 | nan |
| JamesIV (Greene) | B | 0.66 | nan |

## DIFFERENT  Shakespeare early vs Peele

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.41 | nan |
| 3H6 (Shakespeare) | A | 0.48 | nan |
| Tit (Shakespeare) | A | 0.59 | nan |
| R3 (Shakespeare) | A | 0.54 | nan |
| OWT (Peele) | B | 0.45 | nan |
| Alcazar (Peele) | B | 0.22 | nan |
| EdwardI (Peele) | B | 0.61 | nan |
| David (Peele) | B | 0.18 | nan |

## DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.26 | nan |
| 3H6 (Shakespeare) | A | 0.22 | nan |
| Tit (Shakespeare) | A | 0.60 | nan |
| R3 (Shakespeare) | A | 0.20 | nan |
| Soliman (Anon-Soliman) | B | 0.28 | nan |
| Locrine (Anon-Locrine) | B | 0.38 | nan |
| Selimus (Anon-Selimus) | B | 0.32 | nan |
| TRKJ (Anon-TRKJ) | B | 0.36 | nan |
| JackStraw (Anon-JackStraw) | B | 0.05 | nan |
| EdwardIII (Anon-EdwardIII) | B | 0.56 | nan |
| Arden (Anon-Arden) | B | 0.64 | nan |
| TTR3 (Anon-TTR3) | B | 0.07 | nan |

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
| 2H6 (Shakespeare) | A | 0.45 | nan |
| 3H6 (Shakespeare) | A | 0.52 | nan |
| Tit (Shakespeare) | A | 0.66 | nan |
| Alphonsus (Greene) | B | 0.65 | nan |
| Orlando (Greene) | B | 0.29 | nan |
| FriarBacon (Greene) | B | 0.36 | nan |
| JamesIV (Greene) | B | 0.50 | nan |

## QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)

| play | set | P(A) words | P(A) chars |
|---|---|---|---|
| 2H6 (Shakespeare) | A | 0.24 | nan |
| 3H6 (Shakespeare) | A | 0.33 | nan |
| Tit (Shakespeare) | A | 0.44 | nan |
| 1Tam (Marlowe) | B | 0.47 | nan |
| 2Tam (Marlowe) | B | 0.28 | nan |
| Dido (Marlowe) | B | 0.17 | nan |
| DrFaust (Marlowe) | B | 0.37 | nan |
| JoM (Marlowe) | B | 0.34 | nan |
| Ed2 (Marlowe) | B | 0.27 | nan |
| MP (Marlowe) | B | 0.31 | nan |
