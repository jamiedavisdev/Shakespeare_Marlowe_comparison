# Group-mean distances (cosine delta on z-scored word frequencies, features=mfw150)

Lower = more similar. Diagonal = within-group (different plays by the same group).

| | Marlowe | Shakespeare early (<=1594) | Shakespeare later (1595-1611) | Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | Greene (4 plays, 1587-91) | Peele (4 plays, 1589-94) | Anonymous heroic/history 1587-94 (8 plays) |
|---|---|---|---|---|---|---|---|
| Marlowe | 0.945 ± 0.238 (n=42) | 1.055 ± 0.186 (n=56) | 1.116 ± 0.166 (n=77) | 1.040 ± 0.154 (n=35) | 1.038 ± 0.131 (n=28) | 0.954 ± 0.252 (n=28) | 0.965 ± 0.181 (n=56) |
| Shakespeare early (<=1594) | 1.055 ± 0.186 (n=56) | 0.982 ± 0.181 (n=56) | 0.950 ± 0.165 (n=88) | 1.003 ± 0.165 (n=40) | 1.059 ± 0.091 (n=32) | 1.054 ± 0.215 (n=32) | 1.019 ± 0.170 (n=64) |
| Shakespeare later (1595-1611) | 1.116 ± 0.166 (n=77) | 0.950 ± 0.165 (n=88) | 0.782 ± 0.154 (n=110) | 1.015 ± 0.149 (n=55) | 1.124 ± 0.104 (n=44) | 1.139 ± 0.208 (n=44) | 1.111 ± 0.129 (n=88) |
| Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | 1.040 ± 0.154 (n=35) | 1.003 ± 0.165 (n=40) | 1.015 ± 0.149 (n=55) | 1.002 ± 0.144 (n=20) | 1.001 ± 0.124 (n=20) | 1.125 ± 0.182 (n=19) | 1.038 ± 0.176 (n=40) |
| Greene (4 plays, 1587-91) | 1.038 ± 0.131 (n=28) | 1.059 ± 0.091 (n=32) | 1.124 ± 0.104 (n=44) | 1.001 ± 0.124 (n=20) | 0.918 ± 0.146 (n=12) | 0.957 ± 0.117 (n=16) | 0.989 ± 0.107 (n=32) |
| Peele (4 plays, 1589-94) | 0.954 ± 0.252 (n=28) | 1.054 ± 0.215 (n=32) | 1.139 ± 0.208 (n=44) | 1.125 ± 0.182 (n=19) | 0.957 ± 0.117 (n=16) | 0.857 ± 0.284 (n=12) | 0.958 ± 0.219 (n=32) |
| Anonymous heroic/history 1587-94 (8 plays) | 0.965 ± 0.181 (n=56) | 1.019 ± 0.170 (n=64) | 1.111 ± 0.129 (n=88) | 1.038 ± 0.176 (n=40) | 0.989 ± 0.107 (n=32) | 0.958 ± 0.219 (n=32) | 0.997 ± 0.160 (n=56) |

## Same table with classic Burrows Delta (mean |z| difference)

| | Marlowe | Shakespeare early (<=1594) | Shakespeare later (1595-1611) | Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | Greene (4 plays, 1587-91) | Peele (4 plays, 1589-94) | Anonymous heroic/history 1587-94 (8 plays) |
|---|---|---|---|---|---|---|---|
| Marlowe | 1.101 | 1.079 | 1.156 | 1.249 | 1.162 | 1.210 | 1.070 |
| Shakespeare early (<=1594) | 1.079 | 0.908 | 0.942 | 1.103 | 1.088 | 1.218 | 1.004 |
| Shakespeare later (1595-1611) | 1.156 | 0.942 | 0.891 | 1.167 | 1.178 | 1.312 | 1.094 |
| Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | 1.249 | 1.103 | 1.167 | 1.276 | 1.212 | 1.412 | 1.189 |
| Greene (4 plays, 1587-91) | 1.162 | 1.088 | 1.178 | 1.212 | 1.107 | 1.221 | 1.105 |
| Peele (4 plays, 1589-94) | 1.210 | 1.218 | 1.312 | 1.412 | 1.221 | 1.256 | 1.182 |
| Anonymous heroic/history 1587-94 (8 plays) | 1.070 | 1.004 | 1.094 | 1.189 | 1.105 | 1.182 | 1.052 |

## Nearest neighbours of each Marlowe play (cosine delta)

| Marlowe play | 1st | 2nd | 3rd | nearest Shakespeare play |
|---|---|---|---|---|
| 1Tam (Marlowe) | 2Tam (Marlowe) 0.198 | Alcazar (Peele) 0.431 | David (Peele) 0.569 | 1H6 (Shakespeare) 0.876 |
| 2Tam (Marlowe) | 1Tam (Marlowe) 0.198 | Alcazar (Peele) 0.466 | David (Peele) 0.540 | 1H6 (Shakespeare) 0.861 |
| Dido (Marlowe) | Orlando (Greene) 0.749 | Wounds (Lodge) 0.780 | 3H6 (Shakespeare) 0.803 | 3H6 (Shakespeare) 0.803 |
| DrFaust (Marlowe) | Arden (Anon-Arden) 0.749 | 1H4 (Shakespeare) 0.783 | Rom (Shakespeare) 0.793 | 1H4 (Shakespeare) 0.783 |
| JoM (Marlowe) | Arden (Anon-Arden) 0.687 | Shr (Shakespeare) 0.756 | WT (Shakespeare) 0.762 | Shr (Shakespeare) 0.756 |
| Ed2 (Marlowe) | MP (Marlowe) 0.532 | TTR3 (Anon-TTR3) 0.704 | 2H6 (Shakespeare) 0.748 | 2H6 (Shakespeare) 0.748 |
| MP (Marlowe) | Ed2 (Marlowe) 0.532 | David (Peele) 0.722 | TTR3 (Anon-TTR3) 0.723 | R3 (Shakespeare) 0.925 |

## Nearest neighbours of each early Shakespeare play

| Play | 1st | 2nd | 3rd | nearest Marlowe play |
|---|---|---|---|---|
| 2H6 (Shakespeare) | Ed2 (Marlowe) 0.748 | 3H6 (Shakespeare) 0.785 | 1H6 (Shakespeare) 0.835 | Ed2 (Marlowe) 0.748 |
| 3H6 (Shakespeare) | EdwardIII (Anon-EdwardIII) 0.712 | Ed2 (Marlowe) 0.771 | ST (Kyd) 0.784 | Ed2 (Marlowe) 0.771 |
| 1H6 (Shakespeare) | EdwardIII (Anon-EdwardIII) 0.687 | Locrine (Anon-Locrine) 0.734 | Alcazar (Peele) 0.743 | 2Tam (Marlowe) 0.861 |
| Tit (Shakespeare) | R2 (Shakespeare) 0.804 | 3H6 (Shakespeare) 0.822 | JoM (Marlowe) 0.838 | JoM (Marlowe) 0.838 |
| R3 (Shakespeare) | R2 (Shakespeare) 0.728 | TTR3 (Anon-TTR3) 0.788 | Mac (Shakespeare) 0.799 | MP (Marlowe) 0.925 |
| Shr (Shakespeare) | TGV (Shakespeare) 0.530 | AShrew (Anon-AShrew) 0.555 | OWT (Peele) 0.624 | JoM (Marlowe) 0.756 |
| TGV (Shakespeare) | Shr (Shakespeare) 0.530 | WT (Shakespeare) 0.558 | Rom (Shakespeare) 0.619 | JoM (Marlowe) 0.818 |
| Err (Shakespeare) | TGV (Shakespeare) 0.656 | MV (Shakespeare) 0.659 | Rom (Shakespeare) 0.708 | JoM (Marlowe) 0.813 |
