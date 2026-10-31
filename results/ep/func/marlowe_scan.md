# Chunk-level Marlowe probability for each Shakespeare play

Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-150 words, 2000-word chunks. Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.

| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |
|---|---|---|---|---|---|
| 2H6 (Shakespeare) | shakespeare_early | 12 | 0.48 | 5 | 0.84 |
| 3H6 (Shakespeare) | shakespeare_early | 12 | 0.54 | 7 | 0.97 |
| 1H6 (Shakespeare) | shakespeare_early | 10 | 0.51 | 6 | 0.95 |
| Tit (Shakespeare) | shakespeare_early | 10 | 0.15 | 1 | 0.56 |
| R3 (Shakespeare) | shakespeare_early | 14 | 0.13 | 0 | 0.41 |
| Shr (Shakespeare) | shakespeare_early | 10 | 0.03 | 0 | 0.11 |
| TGV (Shakespeare) | shakespeare_early | 9 | 0.01 | 0 | 0.03 |
| Err (Shakespeare) | shakespeare_early | 7 | 0.02 | 0 | 0.10 |
| R2 (Shakespeare) | shakespeare_later | 11 | 0.09 | 0 | 0.33 |
| MND (Shakespeare) | shakespeare_later | 8 | 0.08 | 0 | 0.22 |
| Rom (Shakespeare) | shakespeare_later | 12 | 0.03 | 0 | 0.21 |
| MV (Shakespeare) | shakespeare_later | 11 | 0.01 | 0 | 0.03 |
| 1H4 (Shakespeare) | shakespeare_later | 12 | 0.11 | 0 | 0.49 |
| JC (Shakespeare) | shakespeare_later | 10 | 0.10 | 1 | 0.53 |
| Ham (Shakespeare) | shakespeare_later | 14 | 0.03 | 0 | 0.15 |
| Mac (Shakespeare) | shakespeare_later | 8 | 0.08 | 0 | 0.28 |
| Lr (Shakespeare) | shakespeare_later | 12 | 0.03 | 0 | 0.13 |
| WT (Shakespeare) | shakespeare_later | 12 | 0.04 | 0 | 0.34 |
| Tmp (Shakespeare) | shakespeare_later | 8 | 0.03 | 0 | 0.18 |
| ST (Kyd) | control | 10 | 0.48 | 4 | 0.89 |
| OWT (Peele) | control | 4 | 0.17 | 0 | 0.38 |
| Gal (Lyly) | control | 7 | 0.25 | 2 | 0.98 |
| AShrew (Anon-AShrew) | control | 6 | 0.27 | 1 | 0.75 |
| TCKL (Anon-Leir) | control | 11 | 0.19 | 1 | 0.87 |
| Alphonsus (Greene) | control_ep | 5 | 0.18 | 1 | 0.52 |
| Orlando (Greene) | control_ep | 5 | 0.71 | 4 | 1.00 |
| FriarBacon (Greene) | control_ep | 8 | 0.38 | 3 | 0.84 |
| JamesIV (Greene) | control_ep | 10 | 0.19 | 1 | 0.99 |
| Alcazar (Peele) | control_ep | 5 | 0.84 | 5 | 0.94 |
| EdwardI (Peele) | control_ep | 11 | 0.40 | 3 | 0.93 |
| David (Peele) | control_ep | 7 | 0.78 | 6 | 0.98 |
| Wounds (Lodge) | control_ep | 10 | 0.90 | 10 | 0.97 |
| Soliman (Anon-Soliman) | control_ep | 9 | 0.40 | 3 | 0.72 |
| Locrine (Anon-Locrine) | control_ep | 8 | 0.70 | 7 | 0.99 |
| Selimus (Anon-Selimus) | control_ep | 9 | 0.25 | 1 | 0.69 |
| TRKJ (Anon-TRKJ) | control_ep | 7 | 0.25 | 1 | 0.55 |
| JackStraw (Anon-JackStraw) | control_ep | 4 | 0.61 | 3 | 0.88 |
| EdwardIII (Anon-EdwardIII) | control_ep | 10 | 0.29 | 2 | 0.78 |
| Arden (Anon-Arden) | control_ep | 10 | 0.30 | 2 | 0.80 |
| TTR3 (Anon-TTR3) | control_ep | 10 | 0.43 | 3 | 0.98 |
| Endymion (Lyly) | control_ep | 9 | 0.12 | 0 | 0.31 |
| 1Tam (Marlowe) | marlowe (held out) | 9 | 0.50 | 5 | 0.91 |
| 2Tam (Marlowe) | marlowe (held out) | 9 | 0.68 | 8 | 0.81 |
| Dido (Marlowe) | marlowe (held out) | 7 | 0.74 | 6 | 1.00 |
| DrFaust (Marlowe) | marlowe (held out) | 6 | 0.54 | 3 | 0.76 |
| JoM (Marlowe) | marlowe (held out) | 9 | 0.64 | 6 | 0.99 |
| Ed2 (Marlowe) | marlowe (held out) | 10 | 0.61 | 7 | 0.97 |
| MP (Marlowe) | marlowe (held out) | 5 | 0.82 | 5 | 0.99 |
