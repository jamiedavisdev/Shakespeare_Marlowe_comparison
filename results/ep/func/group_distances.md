# Group-mean distances (cosine delta on z-scored word frequencies, features=func)

Lower = more similar. Diagonal = within-group (different plays by the same group).

| | Marlowe | Shakespeare early (<=1594) | Shakespeare later (1595-1611) | Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | Greene (4 plays, 1587-91) | Peele (4 plays, 1589-94) | Anonymous heroic/history 1587-94 (8 plays) |
|---|---|---|---|---|---|---|---|
| Marlowe | 0.928 ± 0.194 (n=42) | 1.064 ± 0.150 (n=56) | 1.112 ± 0.128 (n=77) | 1.045 ± 0.141 (n=35) | 1.008 ± 0.133 (n=28) | 0.925 ± 0.220 (n=28) | 0.985 ± 0.156 (n=56) |
| Shakespeare early (<=1594) | 1.064 ± 0.150 (n=56) | 0.959 ± 0.128 (n=56) | 0.977 ± 0.140 (n=88) | 0.980 ± 0.126 (n=40) | 1.046 ± 0.090 (n=32) | 1.053 ± 0.183 (n=32) | 1.022 ± 0.139 (n=64) |
| Shakespeare later (1595-1611) | 1.112 ± 0.128 (n=77) | 0.977 ± 0.140 (n=88) | 0.823 ± 0.132 (n=110) | 1.025 ± 0.116 (n=55) | 1.109 ± 0.106 (n=44) | 1.128 ± 0.157 (n=44) | 1.087 ± 0.104 (n=88) |
| Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | 1.045 ± 0.141 (n=35) | 0.980 ± 0.126 (n=40) | 1.025 ± 0.116 (n=55) | 1.012 ± 0.121 (n=20) | 1.032 ± 0.106 (n=20) | 1.136 ± 0.145 (n=19) | 1.005 ± 0.137 (n=40) |
| Greene (4 plays, 1587-91) | 1.008 ± 0.133 (n=28) | 1.046 ± 0.090 (n=32) | 1.109 ± 0.106 (n=44) | 1.032 ± 0.106 (n=20) | 0.925 ± 0.124 (n=12) | 0.954 ± 0.132 (n=16) | 0.996 ± 0.108 (n=32) |
| Peele (4 plays, 1589-94) | 0.925 ± 0.220 (n=28) | 1.053 ± 0.183 (n=32) | 1.128 ± 0.157 (n=44) | 1.136 ± 0.145 (n=19) | 0.954 ± 0.132 (n=16) | 0.853 ± 0.279 (n=12) | 0.974 ± 0.181 (n=32) |
| Anonymous heroic/history 1587-94 (8 plays) | 0.985 ± 0.156 (n=56) | 1.022 ± 0.139 (n=64) | 1.087 ± 0.104 (n=88) | 1.005 ± 0.137 (n=40) | 0.996 ± 0.108 (n=32) | 0.974 ± 0.181 (n=32) | 1.014 ± 0.138 (n=56) |

## Same table with classic Burrows Delta (mean |z| difference)

| | Marlowe | Shakespeare early (<=1594) | Shakespeare later (1595-1611) | Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | Greene (4 plays, 1587-91) | Peele (4 plays, 1589-94) | Anonymous heroic/history 1587-94 (8 plays) |
|---|---|---|---|---|---|---|---|
| Marlowe | 1.034 | 1.027 | 1.119 | 1.208 | 1.129 | 1.121 | 1.057 |
| Shakespeare early (<=1594) | 1.027 | 0.871 | 0.944 | 1.071 | 1.083 | 1.138 | 0.997 |
| Shakespeare later (1595-1611) | 1.119 | 0.944 | 0.914 | 1.153 | 1.186 | 1.242 | 1.094 |
| Controls early (Kyd, Peele, Lyly, A Shrew, Leir) | 1.208 | 1.071 | 1.153 | 1.253 | 1.242 | 1.348 | 1.169 |
| Greene (4 plays, 1587-91) | 1.129 | 1.083 | 1.186 | 1.242 | 1.135 | 1.188 | 1.125 |
| Peele (4 plays, 1589-94) | 1.121 | 1.138 | 1.242 | 1.348 | 1.188 | 1.168 | 1.149 |
| Anonymous heroic/history 1587-94 (8 plays) | 1.057 | 0.997 | 1.094 | 1.169 | 1.125 | 1.149 | 1.075 |

## Nearest neighbours of each Marlowe play (cosine delta)

| Marlowe play | 1st | 2nd | 3rd | nearest Shakespeare play |
|---|---|---|---|---|
| 1Tam (Marlowe) | 2Tam (Marlowe) 0.329 | Alcazar (Peele) 0.480 | David (Peele) 0.559 | 1H6 (Shakespeare) 0.877 |
| 2Tam (Marlowe) | 1Tam (Marlowe) 0.329 | David (Peele) 0.513 | Alcazar (Peele) 0.519 | 2H6 (Shakespeare) 0.910 |
| Dido (Marlowe) | Orlando (Greene) 0.727 | ST (Kyd) 0.775 | David (Peele) 0.783 | 3H6 (Shakespeare) 0.886 |
| DrFaust (Marlowe) | Rom (Shakespeare) 0.794 | JoM (Marlowe) 0.819 | Tmp (Shakespeare) 0.821 | Rom (Shakespeare) 0.794 |
| JoM (Marlowe) | TTR3 (Anon-TTR3) 0.698 | ST (Kyd) 0.792 | Ed2 (Marlowe) 0.794 | Shr (Shakespeare) 0.871 |
| Ed2 (Marlowe) | MP (Marlowe) 0.725 | 3H6 (Shakespeare) 0.764 | JoM (Marlowe) 0.794 | 3H6 (Shakespeare) 0.764 |
| MP (Marlowe) | Ed2 (Marlowe) 0.725 | Alcazar (Peele) 0.764 | David (Peele) 0.802 | 1H6 (Shakespeare) 0.936 |

## Nearest neighbours of each early Shakespeare play

| Play | 1st | 2nd | 3rd | nearest Marlowe play |
|---|---|---|---|---|
| 2H6 (Shakespeare) | 1H4 (Shakespeare) 0.793 | 3H6 (Shakespeare) 0.797 | FriarBacon (Greene) 0.857 | 2Tam (Marlowe) 0.910 |
| 3H6 (Shakespeare) | ST (Kyd) 0.729 | Soliman (Anon-Soliman) 0.751 | Ed2 (Marlowe) 0.764 | Ed2 (Marlowe) 0.764 |
| 1H6 (Shakespeare) | Alcazar (Peele) 0.819 | David (Peele) 0.838 | EdwardI (Peele) 0.850 | Ed2 (Marlowe) 0.864 |
| Tit (Shakespeare) | 2H6 (Shakespeare) 0.860 | ST (Kyd) 0.862 | EdwardI (Peele) 0.865 | JoM (Marlowe) 0.922 |
| R3 (Shakespeare) | Err (Shakespeare) 0.773 | R2 (Shakespeare) 0.783 | Mac (Shakespeare) 0.808 | MP (Marlowe) 1.002 |
| Shr (Shakespeare) | TGV (Shakespeare) 0.597 | AShrew (Anon-AShrew) 0.684 | MV (Shakespeare) 0.746 | JoM (Marlowe) 0.871 |
| TGV (Shakespeare) | Shr (Shakespeare) 0.597 | Rom (Shakespeare) 0.628 | WT (Shakespeare) 0.645 | JoM (Marlowe) 0.955 |
| Err (Shakespeare) | Arden (Anon-Arden) 0.698 | TGV (Shakespeare) 0.736 | Rom (Shakespeare) 0.748 | JoM (Marlowe) 0.942 |
