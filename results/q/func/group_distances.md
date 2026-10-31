# Group-mean distances (cosine delta on z-scored word frequencies, features=func)

Lower = more similar. Diagonal = within-group (different plays by the same group).

| | Marlowe | Shakespeare early (<=1594) | Shakespeare later (1595-1611) | Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | Greene (4 plays, 1587-91) | Peele (4 plays, 1589-94) | Anonymous heroic/history 1587-94 (8 plays) |
|---|---|---|---|---|---|---|---|
| Marlowe | 0.938 ± 0.195 (n=42) | 1.024 ± 0.086 (n=28) | 1.129 ± 0.129 (n=70) | 1.046 ± 0.146 (n=35) | 1.024 ± 0.128 (n=28) | 0.950 ± 0.219 (n=28) | 0.995 ± 0.155 (n=56) |
| Shakespeare early (<=1594) | 1.024 ± 0.086 (n=28) | 0.861 ± 0.121 (n=12) | 1.025 ± 0.150 (n=40) | 0.995 ± 0.121 (n=20) | 1.050 ± 0.084 (n=16) | 1.017 ± 0.085 (n=16) | 1.000 ± 0.113 (n=32) |
| Shakespeare later (1595-1611) | 1.129 ± 0.129 (n=70) | 1.025 ± 0.150 (n=40) | 0.797 ± 0.123 (n=90) | 1.004 ± 0.137 (n=50) | 1.085 ± 0.110 (n=40) | 1.102 ± 0.163 (n=40) | 1.076 ± 0.111 (n=80) |
| Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | 1.046 ± 0.146 (n=35) | 0.995 ± 0.121 (n=20) | 1.004 ± 0.137 (n=50) | 0.999 ± 0.122 (n=20) | 1.042 ± 0.104 (n=20) | 1.154 ± 0.151 (n=19) | 1.005 ± 0.139 (n=40) |
| Greene (4 plays, 1587-91) | 1.024 ± 0.128 (n=28) | 1.050 ± 0.084 (n=16) | 1.085 ± 0.110 (n=40) | 1.042 ± 0.104 (n=20) | 0.942 ± 0.126 (n=12) | 0.987 ± 0.131 (n=16) | 1.012 ± 0.106 (n=32) |
| Peele (4 plays, 1589-94) | 0.950 ± 0.219 (n=28) | 1.017 ± 0.085 (n=16) | 1.102 ± 0.163 (n=40) | 1.154 ± 0.151 (n=19) | 0.987 ± 0.131 (n=16) | 0.885 ± 0.280 (n=12) | 1.000 ± 0.182 (n=32) |
| Anonymous heroic/history 1587-94 (8 plays) | 0.995 ± 0.155 (n=56) | 1.000 ± 0.113 (n=32) | 1.076 ± 0.111 (n=80) | 1.005 ± 0.139 (n=40) | 1.012 ± 0.106 (n=32) | 1.000 ± 0.182 (n=32) | 1.024 ± 0.139 (n=56) |

## Same table with classic Burrows Delta (mean |z| difference)

| | Marlowe | Shakespeare early (<=1594) | Shakespeare later (1595-1611) | Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | Greene (4 plays, 1587-91) | Peele (4 plays, 1589-94) | Anonymous heroic/history 1587-94 (8 plays) |
|---|---|---|---|---|---|---|---|
| Marlowe | 1.027 | 0.971 | 1.110 | 1.200 | 1.118 | 1.114 | 1.050 |
| Shakespeare early (<=1594) | 0.971 | 0.791 | 0.950 | 1.071 | 1.043 | 1.079 | 0.959 |
| Shakespeare later (1595-1611) | 1.110 | 0.950 | 0.877 | 1.131 | 1.149 | 1.198 | 1.069 |
| Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | 1.200 | 1.071 | 1.131 | 1.244 | 1.233 | 1.339 | 1.161 |
| Greene (4 plays, 1587-91) | 1.118 | 1.043 | 1.149 | 1.233 | 1.120 | 1.178 | 1.114 |
| Peele (4 plays, 1589-94) | 1.114 | 1.079 | 1.198 | 1.339 | 1.178 | 1.161 | 1.143 |
| Anonymous heroic/history 1587-94 (8 plays) | 1.050 | 0.959 | 1.069 | 1.161 | 1.114 | 1.143 | 1.068 |

## Nearest neighbours of each Marlowe play (cosine delta)

| Marlowe play | 1st | 2nd | 3rd | nearest Shakespeare play |
|---|---|---|---|---|
| 1Tam (Marlowe) | 2Tam (Marlowe) 0.340 | Alcazar (Peele) 0.502 | David (Peele) 0.587 | 3H6 (Shakespeare) 0.964 |
| 2Tam (Marlowe) | 1Tam (Marlowe) 0.340 | David (Peele) 0.532 | Alcazar (Peele) 0.538 | R2 (Shakespeare) 0.962 |
| Dido (Marlowe) | Orlando (Greene) 0.739 | ST (Kyd) 0.768 | EdwardI (Peele) 0.814 | 3H6 (Shakespeare) 0.958 |
| DrFaust (Marlowe) | JoM (Marlowe) 0.794 | Rom (Shakespeare) 0.819 | Dido (Marlowe) 0.829 | Rom (Shakespeare) 0.819 |
| JoM (Marlowe) | TTR3 (Anon-TTR3) 0.700 | Ed2 (Marlowe) 0.788 | DrFaust (Marlowe) 0.794 | Tro (Shakespeare) 0.893 |
| Ed2 (Marlowe) | MP (Marlowe) 0.737 | JoM (Marlowe) 0.788 | Arden (Anon-Arden) 0.789 | 3H6 (Shakespeare) 0.824 |
| MP (Marlowe) | Ed2 (Marlowe) 0.737 | Alcazar (Peele) 0.799 | David (Peele) 0.835 | 3H6 (Shakespeare) 0.973 |

## Nearest neighbours of each early Shakespeare play

| Play | 1st | 2nd | 3rd | nearest Marlowe play |
|---|---|---|---|---|
| 2H6 (Shakespeare) | 3H6 (Shakespeare) 0.612 | AShrew (Anon-AShrew) 0.776 | Arden (Anon-Arden) 0.822 | DrFaust (Marlowe) 0.876 |
| 3H6 (Shakespeare) | 2H6 (Shakespeare) 0.612 | ST (Kyd) 0.737 | Arden (Anon-Arden) 0.815 | Ed2 (Marlowe) 0.824 |
| Tit (Shakespeare) | 3H6 (Shakespeare) 0.821 | Lr (Shakespeare) 0.863 | ST (Kyd) 0.874 | JoM (Marlowe) 0.966 |
| R3 (Shakespeare) | R2 (Shakespeare) 0.763 | MV (Shakespeare) 0.771 | LLL (Shakespeare) 0.787 | Ed2 (Marlowe) 0.960 |
