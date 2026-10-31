# Chunk-level Marlowe probability for each Shakespeare play

Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-150 words, 2000-word chunks. Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.

| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |
|---|---|---|---|---|---|
| 2H6 (Shakespeare) | shakespeare_early | 8 | 0.63 | 5 | 0.89 |
| 3H6 (Shakespeare) | shakespeare_early | 8 | 0.54 | 4 | 0.98 |
| Tit (Shakespeare) | shakespeare_early | 10 | 0.22 | 1 | 0.71 |
| R3 (Shakespeare) | shakespeare_early | 13 | 0.18 | 1 | 0.66 |
| R2 (Shakespeare) | shakespeare_later | 10 | 0.14 | 0 | 0.46 |
| Rom (Shakespeare) | shakespeare_later | 9 | 0.05 | 0 | 0.16 |
| 1H4 (Shakespeare) | shakespeare_later | 12 | 0.09 | 0 | 0.33 |
| LLL (Shakespeare) | shakespeare_later | 9 | 0.01 | 0 | 0.03 |
| MND (Shakespeare) | shakespeare_later | 8 | 0.12 | 0 | 0.25 |
| MV (Shakespeare) | shakespeare_later | 10 | 0.05 | 0 | 0.33 |
| Ado (Shakespeare) | shakespeare_later | 10 | 0.01 | 0 | 0.02 |
| 2H4 (Shakespeare) | shakespeare_later | 12 | 0.06 | 0 | 0.25 |
| Lr (Shakespeare) | shakespeare_later | 12 | 0.06 | 0 | 0.23 |
| Tro (Shakespeare) | shakespeare_later | 13 | 0.13 | 1 | 0.60 |
| ST (Kyd) | control | 10 | 0.54 | 4 | 0.92 |
| OWT (Peele) | control | 4 | 0.15 | 0 | 0.30 |
| Gal (Lyly) | control | 7 | 0.45 | 2 | 0.99 |
| AShrew (Anon-AShrew) | control | 6 | 0.21 | 1 | 0.56 |
| TCKL (Anon-Leir) | control | 11 | 0.29 | 2 | 0.76 |
| Alphonsus (Greene) | control_ep | 5 | 0.22 | 1 | 0.60 |
| Orlando (Greene) | control_ep | 5 | 0.79 | 4 | 0.99 |
| FriarBacon (Greene) | control_ep | 8 | 0.40 | 3 | 0.92 |
| JamesIV (Greene) | control_ep | 10 | 0.22 | 1 | 0.91 |
| Alcazar (Peele) | control_ep | 5 | 0.84 | 5 | 0.97 |
| EdwardI (Peele) | control_ep | 11 | 0.41 | 4 | 0.85 |
| David (Peele) | control_ep | 7 | 0.79 | 6 | 0.98 |
| Wounds (Lodge) | control_ep | 10 | 0.83 | 9 | 0.93 |
| Soliman (Anon-Soliman) | control_ep | 9 | 0.43 | 4 | 0.83 |
| Locrine (Anon-Locrine) | control_ep | 8 | 0.66 | 5 | 0.98 |
| Selimus (Anon-Selimus) | control_ep | 9 | 0.39 | 3 | 0.70 |
| TRKJ (Anon-TRKJ) | control_ep | 7 | 0.40 | 2 | 0.69 |
| JackStraw (Anon-JackStraw) | control_ep | 4 | 0.79 | 3 | 0.96 |
| EdwardIII (Anon-EdwardIII) | control_ep | 10 | 0.41 | 5 | 0.92 |
| Arden (Anon-Arden) | control_ep | 10 | 0.27 | 1 | 0.77 |
| TTR3 (Anon-TTR3) | control_ep | 10 | 0.55 | 6 | 0.96 |
| Endymion (Lyly) | control_ep | 9 | 0.44 | 3 | 0.80 |
| 1Tam (Marlowe) | marlowe (held out) | 9 | 0.53 | 4 | 0.92 |
| 2Tam (Marlowe) | marlowe (held out) | 9 | 0.72 | 8 | 0.92 |
| Dido (Marlowe) | marlowe (held out) | 7 | 0.88 | 7 | 0.99 |
| DrFaust (Marlowe) | marlowe (held out) | 6 | 0.57 | 4 | 0.80 |
| JoM (Marlowe) | marlowe (held out) | 9 | 0.61 | 7 | 0.96 |
| Ed2 (Marlowe) | marlowe (held out) | 10 | 0.72 | 8 | 0.98 |
| MP (Marlowe) | marlowe (held out) | 5 | 0.82 | 5 | 0.97 |
