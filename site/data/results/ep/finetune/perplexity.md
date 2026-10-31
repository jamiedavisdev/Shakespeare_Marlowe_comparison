# Held-out bits per token under fine-tuned GPT-2 author models

Rows = plays; columns = models. A play that was in a model's training set is marked "(train)". Marlowe plays are scored by the Marlowe model that did *not* train on them (Marlowe_A scores the B plays and vice versa). Base = pretrained GPT-2 without fine-tuning.

| play | author | base | Marlowe_s1 | ShEarlyNonH6 | ShLater_s1 | Greene | Peele | AnonHeroic |
|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | 6.373 | 6.163 | 6.097 | 6.050 | 6.264 | 6.243 | 6.110 |
| 3H6 | Shakespeare | 6.280 | 6.030 | 5.979 | 5.923 | 6.143 | 6.142 | 5.959 |
| 1H6 | Shakespeare | 6.390 | 6.172 | 6.137 | 6.100 | 6.260 | 6.263 | 6.140 |
| Tit | Shakespeare | 6.425 | 6.176 | (train) | 6.161 | 6.258 | 6.194 | 6.158 |
| R3 | Shakespeare | 6.259 | 6.101 | 5.953 | 5.872 | 6.194 | 6.155 | 6.016 |
| Shr | Shakespeare | 6.332 | 6.101 | (train) | 5.998 | 6.074 | 6.113 | 6.048 |
| TGV | Shakespeare | 6.129 | 5.883 | (train) | 5.717 | 5.936 | 5.964 | 5.873 |
| Err | Shakespeare | 6.211 | 6.005 | (train) | 5.916 | 6.043 | 6.062 | 5.948 |
| R2 | Shakespeare | 6.460 | 6.321 | 6.197 | (train) | 6.397 | 6.364 | 6.268 |
| MND | Shakespeare | 6.378 | 6.320 | 6.172 | (train) | 6.345 | 6.334 | 6.289 |
| Rom | Shakespeare | 6.421 | 6.255 | 6.075 | (train) | 6.282 | 6.286 | 6.208 |
| MV | Shakespeare | 6.324 | 6.170 | 6.007 | (train) | 6.232 | 6.218 | 6.135 |
| 1H4 | Shakespeare | 6.447 | 6.374 | 6.216 | (train) | 6.435 | 6.404 | 6.328 |
| JC | Shakespeare | 6.149 | 6.069 | 5.885 | (train) | 6.149 | 6.119 | 6.036 |
| Ham | Shakespeare | 6.552 | 6.494 | 6.327 | (train) | 6.553 | 6.532 | 6.464 |
| Mac | Shakespeare | 6.599 | 6.578 | 6.409 | (train) | 6.664 | 6.612 | 6.555 |
| Lr | Shakespeare | 6.619 | 6.522 | 6.353 | (train) | 6.608 | 6.574 | 6.495 |
| WT | Shakespeare | 6.718 | 6.670 | 6.445 | (train) | 6.754 | 6.725 | 6.661 |
| Tmp | Shakespeare | 6.745 | 6.659 | 6.501 | (train) | 6.756 | 6.714 | 6.683 |
| 1Tam | Marlowe | 6.521 | 6.260* | 6.388 | 6.426 | 6.220 | 6.177 | 6.189 |
| 2Tam | Marlowe | 6.423 | 6.129* | 6.279 | 6.320 | 6.126 | 6.061 | 6.090 |
| Dido | Marlowe | 6.374 | 6.081* | 6.127 | 6.216 | 6.071 | 6.081 | 6.081 |
| DrFaust | Marlowe | 6.158 | 5.999* | 5.999 | 6.053 | 5.872 | 5.925 | 5.906 |
| JoM | Marlowe | 6.242 | 6.071* | 5.941 | 6.004 | 6.071 | 6.042 | 5.988 |
| Ed2 | Marlowe | 6.170 | 5.887* | 5.947 | 6.008 | 5.856 | 5.789 | 5.779 |
| MP | Marlowe | 6.167 | 5.814* | 5.901 | 5.970 | 5.832 | 5.804 | 5.724 |
| ST | Kyd | 6.331 | 5.995 | 6.048 | 6.125 | 6.035 | 6.046 | 5.988 |
| OWT | Peele | 6.386 | 6.236 | 6.215 | 6.300 | 6.179 | (train) | 6.176 |
| Gal | Lyly | 6.271 | 6.162 | 6.141 | 6.131 | 6.128 | 6.167 | 6.147 |
| AShrew | Anon-AShrew | 6.169 | 5.777 | 5.762 | 5.957 | 5.760 | 5.812 | 5.744 |
| TCKL | Anon-Leir | 5.976 | 5.693 | 5.672 | 5.738 | 5.721 | 5.759 | 5.664 |
| Alphonsus | Greene | 6.493 | 6.111 | 6.267 | 6.345 | (train) | 6.145 | 6.063 |
| Orlando | Greene | 6.736 | 6.370 | 6.567 | 6.604 | (train) | 6.440 | 6.390 |
| FriarBacon | Greene | 6.839 | 6.602 | 6.688 | 6.785 | (train) | 6.550 | 6.561 |
| JamesIV | Greene | 6.660 | 6.402 | 6.433 | 6.505 | (train) | 6.414 | 6.321 |
| Alcazar | Peele | 6.507 | 6.214 | 6.458 | 6.540 | 6.306 | (train) | 6.215 |
| EdwardI | Peele | 6.786 | 6.547 | 6.665 | 6.730 | 6.493 | (train) | 6.470 |
| David | Peele | 6.176 | 5.969 | 6.138 | 6.172 | 6.078 | (train) | 6.006 |
| Wounds | Lodge | 6.796 | 6.501 | 6.569 | 6.676 | 6.437 | 6.504 | 6.496 |
| Soliman | Anon-Soliman | 6.326 | 6.005 | 6.070 | 6.162 | 6.029 | 6.050 | (train) |
| Locrine | Anon-Locrine | 6.412 | 6.183 | 6.372 | 6.429 | 6.190 | 6.164 | (train) |
| Selimus | Anon-Selimus | 6.427 | 6.089 | 6.301 | 6.356 | 6.183 | 6.188 | (train) |
| TRKJ | Anon-TRKJ | 6.694 | 6.431 | 6.461 | 6.507 | 6.450 | 6.448 | (train) |
| JackStraw | Anon-JackStraw | 6.352 | 6.089 | 6.138 | 6.172 | 6.100 | 6.041 | (train) |
| EdwardIII | Anon-EdwardIII | 6.509 | 6.223 | 6.331 | 6.353 | 6.276 | 6.260 | (train) |
| Arden | Anon-Arden | 6.365 | 6.054 | 6.078 | 6.191 | 6.084 | 6.126 | (train) |
| TTR3 | Anon-TTR3 | 6.326 | 6.095 | 6.177 | 6.209 | 6.090 | 6.081 | (train) |
| Endymion | Lyly | 6.381 | 6.322 | 6.305 | 6.313 | 6.296 | 6.319 | 6.285 |

\* scored by the Marlowe model trained on the other half of the canon.

