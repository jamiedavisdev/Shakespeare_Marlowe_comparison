# Chunk-level Marlowe probability for each Shakespeare play

Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-500 words, 2000-word chunks. Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.

| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |
|---|---|---|---|---|---|
| 2H6 (Shakespeare) | shakespeare_early | 12 | 0.41 | 4 | 0.98 |
| 3H6 (Shakespeare) | shakespeare_early | 12 | 0.60 | 7 | 0.99 |
| 1H6 (Shakespeare) | shakespeare_early | 10 | 0.55 | 6 | 0.77 |
| Tit (Shakespeare) | shakespeare_early | 10 | 0.19 | 1 | 0.54 |
| R3 (Shakespeare) | shakespeare_early | 14 | 0.13 | 0 | 0.24 |
| Shr (Shakespeare) | shakespeare_early | 10 | 0.08 | 0 | 0.29 |
| TGV (Shakespeare) | shakespeare_early | 8 | 0.02 | 0 | 0.07 |
| Err (Shakespeare) | shakespeare_early | 7 | 0.03 | 0 | 0.07 |
| R2 (Shakespeare) | shakespeare_later | 11 | 0.13 | 1 | 0.55 |
| MND (Shakespeare) | shakespeare_later | 8 | 0.03 | 0 | 0.13 |
| Rom (Shakespeare) | shakespeare_later | 12 | 0.01 | 0 | 0.08 |
| MV (Shakespeare) | shakespeare_later | 10 | 0.02 | 0 | 0.10 |
| 1H4 (Shakespeare) | shakespeare_later | 12 | 0.03 | 0 | 0.08 |
| JC (Shakespeare) | shakespeare_later | 10 | 0.04 | 0 | 0.18 |
| Ham (Shakespeare) | shakespeare_later | 15 | 0.02 | 0 | 0.04 |
| Mac (Shakespeare) | shakespeare_later | 8 | 0.01 | 0 | 0.05 |
| Lr (Shakespeare) | shakespeare_later | 13 | 0.01 | 0 | 0.02 |
| WT (Shakespeare) | shakespeare_later | 12 | 0.01 | 0 | 0.07 |
| Tmp (Shakespeare) | shakespeare_later | 8 | 0.02 | 0 | 0.09 |
| ST (Kyd) | control | 10 | 0.53 | 5 | 0.91 |
| OWT (Peele) | control | 4 | 0.26 | 1 | 0.76 |
| Gal (Lyly) | control | 7 | 0.20 | 1 | 0.76 |
| AShrew (Anon-AShrew) | control | 6 | 0.55 | 3 | 0.87 |
| TCKL (Anon-Leir) | control | 11 | 0.08 | 0 | 0.15 |
| ShoeHol (Dekker) | control | 9 | 0.10 | 0 | 0.31 |
| RT (Middleton) | control | 10 | 0.13 | 1 | 0.76 |
| KBP (Beaumont) | control | 10 | 0.03 | 0 | 0.08 |
| FS (Fletcher) | control_multi | 10 | 0.10 | 0 | 0.21 |
| Prize (Fletcher) | control_multi | 11 | 0.02 | 0 | 0.05 |
| IP (Fletcher) | control_multi | 11 | 0.14 | 1 | 0.68 |
| Perkin (Ford) | control_multi | 10 | 0.06 | 0 | 0.20 |
| TPSW (Ford) | control_multi | 9 | 0.04 | 0 | 0.23 |
| Alphonsus (Greene) | control_ep | 5 | 0.43 | 2 | 0.68 |
| Orlando (Greene) | control_ep | 5 | 0.80 | 4 | 0.98 |
| FriarBacon (Greene) | control_ep | 8 | 0.55 | 6 | 0.76 |
| JamesIV (Greene) | control_ep | 10 | 0.21 | 1 | 0.56 |
| Alcazar (Peele) | control_ep | 5 | 0.81 | 5 | 0.89 |
| EdwardI (Peele) | control_ep | 11 | 0.36 | 5 | 0.84 |
| David (Peele) | control_ep | 7 | 0.75 | 6 | 0.99 |
| Wounds (Lodge) | control_ep | 10 | 0.74 | 8 | 0.97 |
| Soliman (Anon-Soliman) | control_ep | 9 | 0.32 | 2 | 0.67 |
| Locrine (Anon-Locrine) | control_ep | 8 | 0.51 | 4 | 0.96 |
| Selimus (Anon-Selimus) | control_ep | 9 | 0.36 | 2 | 0.76 |
| TRKJ (Anon-TRKJ) | control_ep | 7 | 0.46 | 3 | 0.90 |
| JackStraw (Anon-JackStraw) | control_ep | 4 | 0.33 | 1 | 0.85 |
| EdwardIII (Anon-EdwardIII) | control_ep | 10 | 0.28 | 2 | 0.92 |
| Arden (Anon-Arden) | control_ep | 10 | 0.31 | 3 | 0.81 |
| TTR3 (Anon-TTR3) | control_ep | 10 | 0.31 | 2 | 0.80 |
| Endymion (Lyly) | control_ep | 9 | 0.20 | 1 | 0.71 |
| 1Tam (Marlowe) | marlowe (held out) | 9 | 0.72 | 8 | 0.99 |
| 2Tam (Marlowe) | marlowe (held out) | 9 | 0.80 | 8 | 0.95 |
| Dido (Marlowe) | marlowe (held out) | 7 | 0.63 | 5 | 0.95 |
| DrFaust (Marlowe) | marlowe (held out) | 6 | 0.32 | 1 | 0.68 |
| JoM (Marlowe) | marlowe (held out) | 9 | 0.28 | 2 | 0.82 |
| Ed2 (Marlowe) | marlowe (held out) | 10 | 0.40 | 2 | 0.91 |
| MP (Marlowe) | marlowe (held out) | 5 | 0.78 | 5 | 0.95 |
