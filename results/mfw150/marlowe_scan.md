# Chunk-level Marlowe probability for each Shakespeare play

Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-150 words, 2000-word chunks. Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.

| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |
|---|---|---|---|---|---|
| 2H6 (Shakespeare) | shakespeare_early | 12 | 0.40 | 4 | 0.94 |
| 3H6 (Shakespeare) | shakespeare_early | 12 | 0.64 | 6 | 0.99 |
| 1H6 (Shakespeare) | shakespeare_early | 10 | 0.45 | 3 | 0.83 |
| Tit (Shakespeare) | shakespeare_early | 10 | 0.28 | 2 | 0.92 |
| R3 (Shakespeare) | shakespeare_early | 14 | 0.08 | 0 | 0.28 |
| Shr (Shakespeare) | shakespeare_early | 10 | 0.15 | 1 | 0.56 |
| TGV (Shakespeare) | shakespeare_early | 8 | 0.06 | 0 | 0.33 |
| Err (Shakespeare) | shakespeare_early | 7 | 0.05 | 0 | 0.16 |
| R2 (Shakespeare) | shakespeare_later | 11 | 0.14 | 0 | 0.42 |
| MND (Shakespeare) | shakespeare_later | 8 | 0.09 | 0 | 0.31 |
| Rom (Shakespeare) | shakespeare_later | 12 | 0.04 | 0 | 0.16 |
| MV (Shakespeare) | shakespeare_later | 10 | 0.05 | 0 | 0.40 |
| 1H4 (Shakespeare) | shakespeare_later | 12 | 0.12 | 1 | 0.66 |
| JC (Shakespeare) | shakespeare_later | 10 | 0.02 | 0 | 0.07 |
| Ham (Shakespeare) | shakespeare_later | 15 | 0.06 | 0 | 0.27 |
| Mac (Shakespeare) | shakespeare_later | 8 | 0.06 | 0 | 0.17 |
| Lr (Shakespeare) | shakespeare_later | 13 | 0.04 | 0 | 0.17 |
| WT (Shakespeare) | shakespeare_later | 12 | 0.03 | 0 | 0.07 |
| Tmp (Shakespeare) | shakespeare_later | 8 | 0.05 | 0 | 0.15 |
| ST (Kyd) | control | 10 | 0.80 | 10 | 0.90 |
| OWT (Peele) | control | 4 | 0.29 | 1 | 0.87 |
| Gal (Lyly) | control | 7 | 0.35 | 2 | 0.93 |
| AShrew (Anon-AShrew) | control | 6 | 0.84 | 5 | 0.99 |
| TCKL (Anon-Leir) | control | 11 | 0.12 | 1 | 0.66 |
| ShoeHol (Dekker) | control | 9 | 0.22 | 1 | 0.53 |
| RT (Middleton) | control | 10 | 0.35 | 3 | 0.97 |
| KBP (Beaumont) | control | 10 | 0.19 | 0 | 0.49 |
| FS (Fletcher) | control_multi | 10 | 0.39 | 3 | 0.91 |
| Prize (Fletcher) | control_multi | 11 | 0.13 | 0 | 0.24 |
| IP (Fletcher) | control_multi | 11 | 0.56 | 7 | 0.99 |
| Perkin (Ford) | control_multi | 10 | 0.15 | 1 | 0.58 |
| TPSW (Ford) | control_multi | 9 | 0.15 | 0 | 0.46 |
| Alphonsus (Greene) | control_ep | 5 | 0.15 | 0 | 0.32 |
| Orlando (Greene) | control_ep | 5 | 0.66 | 3 | 0.99 |
| FriarBacon (Greene) | control_ep | 8 | 0.38 | 2 | 0.82 |
| JamesIV (Greene) | control_ep | 10 | 0.16 | 1 | 0.62 |
| Alcazar (Peele) | control_ep | 5 | 0.71 | 3 | 0.91 |
| EdwardI (Peele) | control_ep | 11 | 0.36 | 4 | 0.84 |
| David (Peele) | control_ep | 7 | 0.61 | 5 | 0.94 |
| Wounds (Lodge) | control_ep | 10 | 0.85 | 9 | 1.00 |
| Soliman (Anon-Soliman) | control_ep | 9 | 0.43 | 4 | 0.95 |
| Locrine (Anon-Locrine) | control_ep | 8 | 0.53 | 4 | 0.96 |
| Selimus (Anon-Selimus) | control_ep | 9 | 0.34 | 2 | 0.58 |
| TRKJ (Anon-TRKJ) | control_ep | 7 | 0.28 | 2 | 0.80 |
| JackStraw (Anon-JackStraw) | control_ep | 4 | 0.38 | 2 | 0.73 |
| EdwardIII (Anon-EdwardIII) | control_ep | 10 | 0.19 | 1 | 0.52 |
| Arden (Anon-Arden) | control_ep | 10 | 0.50 | 6 | 0.80 |
| TTR3 (Anon-TTR3) | control_ep | 10 | 0.26 | 1 | 0.53 |
| Endymion (Lyly) | control_ep | 9 | 0.24 | 2 | 0.70 |
| 1Tam (Marlowe) | marlowe (held out) | 9 | 0.63 | 7 | 0.95 |
| 2Tam (Marlowe) | marlowe (held out) | 9 | 0.69 | 7 | 0.94 |
| Dido (Marlowe) | marlowe (held out) | 7 | 0.66 | 5 | 0.96 |
| DrFaust (Marlowe) | marlowe (held out) | 6 | 0.23 | 1 | 0.70 |
| JoM (Marlowe) | marlowe (held out) | 9 | 0.33 | 3 | 0.88 |
| Ed2 (Marlowe) | marlowe (held out) | 10 | 0.58 | 6 | 0.88 |
| MP (Marlowe) | marlowe (held out) | 5 | 0.80 | 5 | 0.96 |
