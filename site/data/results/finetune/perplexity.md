# Held-out bits per token under fine-tuned GPT-2 author models

Rows = plays; columns = models. A play that was in a model's training set is marked "(train)". Marlowe plays are scored by the Marlowe model that did *not* train on them (Marlowe_A scores the B plays and vice versa). Base = pretrained GPT-2 without fine-tuning.

| play | author | base | Marlowe_s1 | ShEarlyNonH6 | ShLater_s1 | Greene | Peele | AnonHeroic | Fletcher |
|---|---|---|---|---|---|---|---|---|---|
| 1Tam | Marlowe | 6.471 | 6.199* | 6.436 | 6.462 | 6.229 | 6.172 | 6.192 | 6.492 |
| 2Tam | Marlowe | 6.372 | 6.078* | 6.326 | 6.325 | 6.132 | 6.057 | 6.104 | 6.363 |
| Dido | Marlowe | 6.294 | 6.018* | 6.171 | 6.222 | 6.065 | 6.045 | 6.048 | 6.276 |
| DrFaust | Marlowe | 6.058 | 5.891* | 6.027 | 6.033 | 5.896 | 5.861 | 5.923 | 6.058 |
| JoM | Marlowe | 6.186 | 6.032* | 6.051 | 6.123 | 6.102 | 6.028 | 6.041 | 6.080 |
| Ed2 | Marlowe | 6.110 | 5.858* | 5.924 | 5.933 | 5.898 | 5.783 | 5.813 | 6.081 |
| MP | Marlowe | 6.155 | 5.788* | 6.017 | 6.045 | 5.932 | 5.815 | 5.821 | 6.105 |
| 2H6 | Shakespeare | 6.124 | 6.010 | 5.873 | 5.856 | 6.182 | 6.099 | 6.076 | 6.297 |
| 3H6 | Shakespeare | 6.058 | 5.874 | 5.782 | 5.788 | 6.054 | 5.985 | 5.904 | 6.208 |
| 1H6 | Shakespeare | 6.135 | 6.000 | 5.925 | 5.929 | 6.133 | 6.087 | 6.049 | 6.269 |
| Tit | Shakespeare | 6.108 | 5.985 | (train) | 5.878 | 6.141 | 6.028 | 6.051 | 6.239 |
| R3 | Shakespeare | 6.045 | 5.980 | 5.772 | 5.739 | 6.102 | 6.019 | 5.972 | 6.194 |
| Shr | Shakespeare | 6.005 | 5.968 | (train) | 5.693 | 6.035 | 5.974 | 6.014 | 6.032 |
| TGV | Shakespeare | 5.876 | 5.787 | (train) | 5.557 | 5.898 | 5.841 | 5.859 | 5.912 |
| Err | Shakespeare | 5.915 | 5.853 | (train) | 5.630 | 5.967 | 5.891 | 5.876 | 5.973 |
| R2 | Shakespeare | 6.268 | 6.207 | 6.031 | (train) | 6.305 | 6.232 | 6.200 | 6.382 |
| MND | Shakespeare | 6.148 | 6.219 | 5.941 | (train) | 6.299 | 6.221 | 6.275 | 6.289 |
| Rom | Shakespeare | 6.077 | 6.077 | 5.768 | (train) | 6.176 | 6.085 | 6.120 | 6.174 |
| MV | Shakespeare | 6.063 | 6.070 | 5.763 | (train) | 6.193 | 6.085 | 6.118 | 6.155 |
| 1H4 | Shakespeare | 6.178 | 6.176 | 5.968 | (train) | 6.310 | 6.175 | 6.244 | 6.295 |
| JC | Shakespeare | 5.852 | 5.858 | 5.641 | (train) | 5.978 | 5.909 | 5.898 | 5.967 |
| Ham | Shakespeare | 6.258 | 6.296 | 6.052 | (train) | 6.405 | 6.298 | 6.378 | 6.330 |
| Mac | Shakespeare | 6.410 | 6.478 | 6.261 | (train) | 6.585 | 6.478 | 6.539 | 6.445 |
| Lr | Shakespeare | 6.350 | 6.413 | 6.138 | (train) | 6.540 | 6.409 | 6.493 | 6.412 |
| WT | Shakespeare | 6.400 | 6.470 | 6.203 | (train) | 6.585 | 6.465 | 6.546 | 6.406 |
| Tmp | Shakespeare | 6.389 | 6.460 | 6.195 | (train) | 6.597 | 6.473 | 6.568 | 6.414 |
| ST | Kyd | 6.237 | 5.946 | 6.098 | 6.160 | 6.025 | 6.011 | 5.968 | 6.219 |
| OWT | Peele | 6.301 | 6.096 | 6.228 | 6.255 | 6.238 | (train) | 6.208 | 6.242 |
| Gal | Lyly | 6.204 | 6.028 | 6.157 | 6.091 | 6.170 | 6.030 | 6.188 | 6.151 |
| AShrew | Anon-AShrew | 6.120 | 5.750 | 5.850 | 5.963 | 5.824 | 5.809 | 5.790 | 5.990 |
| TCKL | Anon-Leir | 5.930 | 5.672 | 5.748 | 5.804 | 5.765 | 5.773 | 5.706 | 5.844 |
| ShoeHol | Dekker | 6.483 | 6.327 | 6.451 | 6.408 | 6.434 | 6.330 | 6.394 | 6.422 |
| RT | Middleton | 6.692 | 6.522 | 6.670 | 6.594 | 6.699 | 6.630 | 6.628 | 6.428 |
| KBP | Beaumont | 6.326 | 6.155 | 6.267 | 6.239 | 6.282 | 6.143 | 6.226 | 6.078 |
| FS | Fletcher | 6.634 | 6.547 | 6.672 | 6.595 | 6.546 | 6.532 | 6.558 | (train) |
| Prize | Fletcher | 6.372 | 6.260 | 6.307 | 6.244 | 6.385 | 6.302 | 6.333 | (train) |
| IP | Fletcher | 6.329 | 6.227 | 6.335 | 6.266 | 6.384 | 6.292 | 6.317 | (train) |
| Perkin | Ford | 6.856 | 6.805 | 6.950 | 6.813 | 6.957 | 6.872 | 6.881 | 6.737 |
| TPSW | Ford | 6.444 | 6.269 | 6.374 | 6.359 | 6.424 | 6.336 | 6.380 | 6.153 |
| Alphonsus | Greene | 6.493 | 6.162 | 6.419 | 6.455 | (train) | 6.157 | 6.054 | 6.474 |
| Orlando | Greene | 6.736 | 6.453 | 6.748 | 6.767 | (train) | 6.449 | 6.393 | 6.757 |
| FriarBacon | Greene | 6.839 | 6.687 | 6.865 | 6.899 | (train) | 6.557 | 6.557 | 6.948 |
| JamesIV | Greene | 6.660 | 6.498 | 6.660 | 6.666 | (train) | 6.410 | 6.321 | 6.637 |
| Alcazar | Peele | 6.507 | 6.276 | 6.491 | 6.516 | 6.305 | (train) | 6.202 | 6.633 |
| EdwardI | Peele | 6.786 | 6.651 | 6.861 | 6.862 | 6.502 | (train) | 6.465 | 6.883 |
| David | Peele | 6.176 | 6.024 | 6.202 | 6.210 | 6.069 | (train) | 6.001 | 6.289 |
| Wounds | Lodge | 6.796 | 6.570 | 6.739 | 6.793 | 6.433 | 6.506 | 6.483 | 6.834 |
| Soliman | Anon-Soliman | 6.326 | 6.078 | 6.249 | 6.303 | 6.028 | 6.064 | (train) | 6.326 |
| Locrine | Anon-Locrine | 6.412 | 6.233 | 6.456 | 6.462 | 6.192 | 6.171 | (train) | 6.549 |
| Selimus | Anon-Selimus | 6.427 | 6.135 | 6.410 | 6.420 | 6.184 | 6.197 | (train) | 6.504 |
| TRKJ | Anon-TRKJ | 6.694 | 6.516 | 6.707 | 6.741 | 6.442 | 6.449 | (train) | 6.780 |
| JackStraw | Anon-JackStraw | 6.352 | 6.206 | 6.361 | 6.369 | 6.100 | 6.051 | (train) | 6.363 |
| EdwardIII | Anon-EdwardIII | 6.509 | 6.289 | 6.470 | 6.442 | 6.277 | 6.263 | (train) | 6.505 |
| Arden | Anon-Arden | 6.365 | 6.165 | 6.292 | 6.347 | 6.081 | 6.131 | (train) | 6.327 |
| TTR3 | Anon-TTR3 | 6.326 | 6.201 | 6.416 | 6.380 | 6.091 | 6.094 | (train) | 6.478 |
| Endymion | Lyly | 6.381 | 6.415 | 6.542 | 6.542 | 6.291 | 6.331 | 6.285 | 6.478 |

\* scored by the Marlowe model trained on the other half of the canon.

