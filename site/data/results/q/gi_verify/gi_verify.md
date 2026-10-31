# General Impostors verification scores (function words, 200 rounds)

Score = share of rounds in which the target play is nearer to some play by the candidate author than to every sampled impostor. The target's own author's plays count as impostors when they are not the candidate, so a play by a known author should score high only in its own column. Plays sharing plot/characters with the target are excluded from both sides.

| play | author | as Marlowe | as Shakespeare | as Greene | as Peele | as Anon-heroic |
|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | 0.32 | 0.35 | 0.07 | 0.05 | 0.61 |
| 3H6 | Shakespeare | 0.29 | 0.28 | 0.04 | 0.04 | 0.58 |
| Tit | Shakespeare | 0.10 | 0.85 | 0.01 | 0.29 | 0.20 |
| R3 | Shakespeare | 0.04 | 0.97 | 0.08 | 0.00 | 0.14 |
| R2 | Shakespeare | 0.05 | 0.93 | 0.01 | 0.20 | 0.27 |
| Rom | Shakespeare | 0.27 | 0.91 | 0.04 | 0.06 | 0.23 |
| 1H4 | Shakespeare | 0.01 | 1.00 | 0.01 | 0.04 | 0.06 |
| LLL | Shakespeare | 0.00 | 1.00 | 0.03 | 0.00 | 0.01 |
| MND | Shakespeare | 0.01 | 0.94 | 0.03 | 0.16 | 0.12 |
| MV | Shakespeare | 0.01 | 1.00 | 0.04 | 0.01 | 0.01 |
| Ado | Shakespeare | 0.00 | 1.00 | 0.00 | 0.03 | 0.01 |
| 2H4 | Shakespeare | 0.01 | 0.99 | 0.00 | 0.04 | 0.01 |
| Lr | Shakespeare | 0.01 | 1.00 | 0.00 | 0.06 | 0.01 |
| Tro | Shakespeare | 0.03 | 1.00 | 0.01 | 0.10 | 0.00 |
| 1Tam | Marlowe | 0.03 | 0.00 | 0.07 | 0.98 | 0.40 |
| 2Tam | Marlowe | 0.14 | 0.00 | 0.09 | 0.99 | 0.22 |
| Dido | Marlowe | 0.33 | 0.01 | 0.63 | 0.41 | 0.39 |
| DrFaust | Marlowe | 0.72 | 0.48 | 0.17 | 0.19 | 0.28 |
| JoM | Marlowe | 0.52 | 0.11 | 0.00 | 0.07 | 0.80 |
| Ed2 | Marlowe | 0.86 | 0.30 | 0.01 | 0.01 | 0.55 |
| MP | Marlowe | 0.83 | 0.03 | 0.14 | 0.53 | 0.40 |
| ST | Kyd | 0.72 | 0.58 | 0.15 | 0.04 | 0.42 |
| OWT | Peele | 0.20 | 0.69 | 0.01 | 0.04 | 0.69 |
| Gal | Lyly | 0.32 | 0.56 | 0.07 | 0.04 | 0.14 |
| AShrew | Anon-AShrew | 0.32 | 0.50 | 0.01 | 0.21 | 0.46 |
| TCKL | Anon-Leir | 0.04 | 0.64 | 0.47 | 0.00 | 0.09 |
| Alphonsus | Greene | 0.14 | 0.08 | 0.25 | 0.04 | 0.70 |
| Orlando | Greene | 0.60 | 0.02 | 0.72 | 0.36 | 0.37 |
| FriarBacon | Greene | 0.24 | 0.05 | 0.83 | 0.73 | 0.24 |
| JamesIV | Greene | 0.07 | 0.56 | 0.27 | 0.09 | 0.25 |
| Alcazar | Peele | 0.74 | 0.00 | 0.07 | 0.91 | 0.18 |
| EdwardI | Peele | 0.27 | 0.06 | 0.43 | 0.59 | 0.41 |
| David | Peele | 0.69 | 0.00 | 0.04 | 0.96 | 0.17 |
| Wounds | Lodge | 0.57 | 0.02 | 0.24 | 0.86 | 0.09 |
| Soliman | Anon-heroic | 0.38 | 0.39 | 0.06 | 0.12 | 0.86 |
| Locrine | Anon-heroic | 0.64 | 0.01 | 0.21 | 0.92 | 0.04 |
| Selimus | Anon-heroic | 0.49 | 0.49 | 0.46 | 0.25 | 0.39 |
| TRKJ | Anon-heroic | 0.17 | 0.21 | 0.23 | 0.96 | 0.20 |
| JackStraw | Anon-heroic | 0.86 | 0.07 | 0.17 | 0.28 | 0.32 |
| EdwardIII | Anon-heroic | 0.73 | 0.40 | 0.23 | 0.53 | 0.23 |
| Arden | Anon-heroic | 0.54 | 0.43 | 0.00 | 0.44 | 0.44 |
| TTR3 | Anon-heroic | 0.86 | 0.11 | 0.02 | 0.01 | 0.51 |
| Endymion | Lyly | 0.14 | 0.57 | 0.03 | 0.04 | 0.08 |

## Calibration

| target group | as Marlowe | as Shakespeare | as Greene | as Peele | as Anon-heroic |
|---|---|---|---|---|---|
| Marlowe plays | 0.49 | 0.13 | 0.16 | 0.45 | 0.43 |
| Shakespeare early (≤1594) | 0.18 | 0.61 | 0.05 | 0.10 | 0.38 |
|   Henry VI 1-3 | 0.30 | 0.31 | 0.06 | 0.04 | 0.60 |
|   Tit, R3, Shr, TGV, Err | 0.07 | 0.91 | 0.05 | 0.14 | 0.17 |
| Shakespeare later | 0.04 | 0.98 | 0.02 | 0.07 | 0.07 |
| Greene | 0.27 | 0.18 | 0.52 | 0.30 | 0.39 |
| Peele | 0.47 | 0.19 | 0.14 | 0.62 | 0.36 |
| Anon heroic | 0.58 | 0.27 | 0.17 | 0.44 | 0.37 |
| Kyd ST | 0.72 | 0.58 | 0.15 | 0.04 | 0.42 |
| other single-play controls | 0.28 | 0.46 | 0.16 | 0.23 | 0.17 |
