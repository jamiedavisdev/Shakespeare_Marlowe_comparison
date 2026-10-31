# Chunk-level Marlowe probability for each Shakespeare play

Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-150 words, 2000-word chunks. Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.

| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |
|---|---|---|---|---|---|
| 2H6 (Shakespeare) | shakespeare_early | 12 | 0.50 | 7 | 0.91 |
| 3H6 (Shakespeare) | shakespeare_early | 12 | 0.64 | 8 | 0.99 |
| 1H6 (Shakespeare) | shakespeare_early | 10 | 0.52 | 5 | 0.91 |
| Tit (Shakespeare) | shakespeare_early | 10 | 0.29 | 2 | 0.96 |
| R3 (Shakespeare) | shakespeare_early | 14 | 0.07 | 0 | 0.20 |
| Shr (Shakespeare) | shakespeare_early | 10 | 0.16 | 0 | 0.39 |
| TGV (Shakespeare) | shakespeare_early | 9 | 0.07 | 0 | 0.47 |
| Err (Shakespeare) | shakespeare_early | 7 | 0.04 | 0 | 0.11 |
| R2 (Shakespeare) | shakespeare_later | 11 | 0.20 | 3 | 0.60 |
| MND (Shakespeare) | shakespeare_later | 8 | 0.07 | 0 | 0.27 |
| Rom (Shakespeare) | shakespeare_later | 12 | 0.04 | 0 | 0.19 |
| MV (Shakespeare) | shakespeare_later | 11 | 0.07 | 1 | 0.57 |
| 1H4 (Shakespeare) | shakespeare_later | 12 | 0.15 | 1 | 0.80 |
| JC (Shakespeare) | shakespeare_later | 10 | 0.05 | 0 | 0.32 |
| Ham (Shakespeare) | shakespeare_later | 14 | 0.11 | 1 | 0.67 |
| Mac (Shakespeare) | shakespeare_later | 8 | 0.03 | 0 | 0.07 |
| Lr (Shakespeare) | shakespeare_later | 12 | 0.07 | 0 | 0.47 |
| WT (Shakespeare) | shakespeare_later | 12 | 0.04 | 0 | 0.14 |
| Tmp (Shakespeare) | shakespeare_later | 8 | 0.06 | 0 | 0.29 |
| ST (Kyd) | control | 10 | 0.71 | 9 | 0.88 |
| OWT (Peele) | control | 4 | 0.27 | 1 | 0.86 |
| Gal (Lyly) | control | 7 | 0.54 | 3 | 0.95 |
| AShrew (Anon-AShrew) | control | 6 | 0.84 | 5 | 0.99 |
| TCKL (Anon-Leir) | control | 11 | 0.19 | 1 | 0.87 |
| Alphonsus (Greene) | control_ep | 5 | 0.21 | 0 | 0.44 |
| Orlando (Greene) | control_ep | 5 | 0.70 | 3 | 0.99 |
| FriarBacon (Greene) | control_ep | 8 | 0.43 | 4 | 0.83 |
| JamesIV (Greene) | control_ep | 10 | 0.15 | 0 | 0.42 |
| Alcazar (Peele) | control_ep | 5 | 0.62 | 3 | 0.86 |
| EdwardI (Peele) | control_ep | 11 | 0.35 | 2 | 0.93 |
| David (Peele) | control_ep | 7 | 0.58 | 4 | 0.97 |
| Wounds (Lodge) | control_ep | 10 | 0.84 | 9 | 1.00 |
| Soliman (Anon-Soliman) | control_ep | 9 | 0.51 | 4 | 0.97 |
| Locrine (Anon-Locrine) | control_ep | 8 | 0.57 | 5 | 0.97 |
| Selimus (Anon-Selimus) | control_ep | 9 | 0.35 | 2 | 0.78 |
| TRKJ (Anon-TRKJ) | control_ep | 7 | 0.25 | 2 | 0.77 |
| JackStraw (Anon-JackStraw) | control_ep | 4 | 0.47 | 2 | 0.89 |
| EdwardIII (Anon-EdwardIII) | control_ep | 10 | 0.22 | 1 | 0.63 |
| Arden (Anon-Arden) | control_ep | 10 | 0.61 | 6 | 0.91 |
| TTR3 (Anon-TTR3) | control_ep | 10 | 0.26 | 0 | 0.49 |
| Endymion (Lyly) | control_ep | 9 | 0.36 | 3 | 0.86 |
| 1Tam (Marlowe) | marlowe (held out) | 9 | 0.58 | 5 | 0.97 |
| 2Tam (Marlowe) | marlowe (held out) | 9 | 0.68 | 7 | 0.96 |
| Dido (Marlowe) | marlowe (held out) | 7 | 0.57 | 3 | 0.97 |
| DrFaust (Marlowe) | marlowe (held out) | 6 | 0.29 | 2 | 0.70 |
| JoM (Marlowe) | marlowe (held out) | 9 | 0.19 | 2 | 0.72 |
| Ed2 (Marlowe) | marlowe (held out) | 10 | 0.57 | 7 | 0.83 |
| MP (Marlowe) | marlowe (held out) | 5 | 0.71 | 3 | 0.98 |
