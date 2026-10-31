# Chunk-level Marlowe probability for each Shakespeare play

Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-150 words, 2000-word chunks. Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.

| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |
|---|---|---|---|---|---|
| 2H6 (Shakespeare) | shakespeare_early | 12 | 0.45 | 5 | 0.78 |
| 3H6 (Shakespeare) | shakespeare_early | 12 | 0.60 | 6 | 0.98 |
| 1H6 (Shakespeare) | shakespeare_early | 10 | 0.48 | 3 | 0.93 |
| Tit (Shakespeare) | shakespeare_early | 10 | 0.17 | 0 | 0.49 |
| R3 (Shakespeare) | shakespeare_early | 14 | 0.15 | 0 | 0.46 |
| Shr (Shakespeare) | shakespeare_early | 10 | 0.07 | 0 | 0.23 |
| TGV (Shakespeare) | shakespeare_early | 8 | 0.02 | 0 | 0.04 |
| Err (Shakespeare) | shakespeare_early | 7 | 0.02 | 0 | 0.09 |
| R2 (Shakespeare) | shakespeare_later | 11 | 0.10 | 1 | 0.53 |
| MND (Shakespeare) | shakespeare_later | 8 | 0.08 | 0 | 0.27 |
| Rom (Shakespeare) | shakespeare_later | 12 | 0.03 | 0 | 0.13 |
| MV (Shakespeare) | shakespeare_later | 10 | 0.01 | 0 | 0.05 |
| 1H4 (Shakespeare) | shakespeare_later | 12 | 0.07 | 0 | 0.27 |
| JC (Shakespeare) | shakespeare_later | 10 | 0.11 | 0 | 0.49 |
| Ham (Shakespeare) | shakespeare_later | 15 | 0.04 | 0 | 0.15 |
| Mac (Shakespeare) | shakespeare_later | 8 | 0.15 | 0 | 0.43 |
| Lr (Shakespeare) | shakespeare_later | 13 | 0.03 | 0 | 0.18 |
| WT (Shakespeare) | shakespeare_later | 12 | 0.06 | 0 | 0.41 |
| Tmp (Shakespeare) | shakespeare_later | 8 | 0.02 | 0 | 0.06 |
| ST (Kyd) | control | 10 | 0.43 | 3 | 0.88 |
| OWT (Peele) | control | 4 | 0.23 | 1 | 0.70 |
| Gal (Lyly) | control | 7 | 0.22 | 1 | 0.99 |
| AShrew (Anon-AShrew) | control | 6 | 0.17 | 0 | 0.41 |
| TCKL (Anon-Leir) | control | 11 | 0.09 | 0 | 0.28 |
| ShoeHol (Dekker) | control | 9 | 0.30 | 3 | 0.72 |
| RT (Middleton) | control | 10 | 0.44 | 3 | 0.96 |
| KBP (Beaumont) | control | 10 | 0.21 | 1 | 0.72 |
| FS (Fletcher) | control_multi | 10 | 0.61 | 7 | 1.00 |
| Prize (Fletcher) | control_multi | 11 | 0.48 | 5 | 0.98 |
| IP (Fletcher) | control_multi | 11 | 0.98 | 11 | 1.00 |
| Perkin (Ford) | control_multi | 10 | 0.25 | 2 | 0.66 |
| TPSW (Ford) | control_multi | 9 | 0.08 | 0 | 0.34 |
| Alphonsus (Greene) | control_ep | 5 | 0.16 | 1 | 0.52 |
| Orlando (Greene) | control_ep | 5 | 0.82 | 5 | 0.99 |
| FriarBacon (Greene) | control_ep | 8 | 0.38 | 3 | 0.88 |
| JamesIV (Greene) | control_ep | 10 | 0.17 | 1 | 0.50 |
| Alcazar (Peele) | control_ep | 5 | 0.94 | 5 | 0.97 |
| EdwardI (Peele) | control_ep | 11 | 0.51 | 6 | 0.88 |
| David (Peele) | control_ep | 7 | 0.89 | 7 | 1.00 |
| Wounds (Lodge) | control_ep | 10 | 0.89 | 10 | 0.96 |
| Soliman (Anon-Soliman) | control_ep | 9 | 0.25 | 1 | 0.74 |
| Locrine (Anon-Locrine) | control_ep | 8 | 0.64 | 6 | 0.98 |
| Selimus (Anon-Selimus) | control_ep | 9 | 0.21 | 1 | 0.57 |
| TRKJ (Anon-TRKJ) | control_ep | 7 | 0.31 | 2 | 0.73 |
| JackStraw (Anon-JackStraw) | control_ep | 4 | 0.76 | 3 | 0.92 |
| EdwardIII (Anon-EdwardIII) | control_ep | 10 | 0.39 | 4 | 0.95 |
| Arden (Anon-Arden) | control_ep | 10 | 0.33 | 4 | 0.58 |
| TTR3 (Anon-TTR3) | control_ep | 10 | 0.42 | 5 | 0.93 |
| Endymion (Lyly) | control_ep | 9 | 0.11 | 0 | 0.30 |
| 1Tam (Marlowe) | marlowe (held out) | 9 | 0.71 | 7 | 0.97 |
| 2Tam (Marlowe) | marlowe (held out) | 9 | 0.86 | 9 | 1.00 |
| Dido (Marlowe) | marlowe (held out) | 7 | 0.77 | 6 | 0.99 |
| DrFaust (Marlowe) | marlowe (held out) | 6 | 0.48 | 2 | 0.90 |
| JoM (Marlowe) | marlowe (held out) | 9 | 0.42 | 4 | 0.92 |
| Ed2 (Marlowe) | marlowe (held out) | 10 | 0.58 | 6 | 0.96 |
| MP (Marlowe) | marlowe (held out) | 5 | 0.77 | 5 | 0.97 |
