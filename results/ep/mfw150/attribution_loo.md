# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-150 words)

Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.

| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |
|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | **Anon-EdwardIII** | 0.831 | 1.048 | 1.098 | 1.014 | Anon-EdwardIII 0.819 | NO |
| 3H6 | Shakespeare | **Anon-EdwardIII** | 0.800 | 1.119 | 1.079 | 1.112 | Anon-EdwardIII 0.689 | NO |
| 1H6 | Shakespeare | **Anon-EdwardIII** | 0.973 | 1.104 | 1.188 | 1.042 | Anon-EdwardIII 0.668 | NO |
| Tit | Shakespeare | **Anon-EdwardIII** | 0.946 | 0.897 | 0.893 | 0.923 | Anon-EdwardIII 0.869 | NO |
| R3 | Shakespeare | **Shakespeare** | 1.125 | 0.816 | 0.957 | 0.792 | Kyd 0.901 | yes |
| Shr | Shakespeare | **Shakespeare** | 1.284 | 0.677 | 0.719 | 0.733 | Anon-Arden 0.702 | yes |
| TGV | Shakespeare | **Shakespeare** | 1.455 | 0.597 | 0.708 | 0.649 | Anon-Leir 0.690 | yes |
| Err | Shakespeare | **Shakespeare** | 1.398 | 0.563 | 0.683 | 0.617 | Anon-Arden 0.712 | yes |
| R2 | Shakespeare | **Peele** | 0.976 | 0.899 | 1.002 | 0.873 | Peele 0.817 | NO |
| MND | Shakespeare | **Shakespeare** | 1.194 | 0.734 | 0.832 | 0.750 | Lyly 0.810 | yes |
| Rom | Shakespeare | **Shakespeare** | 1.355 | 0.553 | 0.646 | 0.622 | Anon-AShrew 0.927 | yes |
| MV | Shakespeare | **Shakespeare** | 1.450 | 0.519 | 0.648 | 0.573 | Anon-Leir 0.711 | yes |
| 1H4 | Shakespeare | **Shakespeare** | 1.285 | 0.608 | 0.837 | 0.585 | Anon-Arden 0.823 | yes |
| JC | Shakespeare | **Shakespeare** | 1.203 | 0.559 | 0.861 | 0.507 | Anon-Arden 0.795 | yes |
| Ham | Shakespeare | **Shakespeare** | 1.243 | 0.471 | 0.736 | 0.461 | Anon-Leir 0.920 | yes |
| Mac | Shakespeare | **Shakespeare** | 1.106 | 0.624 | 0.949 | 0.546 | Anon-EdwardIII 0.932 | yes |
| Lr | Shakespeare | **Shakespeare** | 1.152 | 0.498 | 0.743 | 0.491 | Anon-AShrew 0.921 | yes |
| WT | Shakespeare | **Shakespeare** | 1.385 | 0.388 | 0.611 | 0.421 | Anon-Leir 0.655 | yes |
| Tmp | Shakespeare | **Shakespeare** | 1.272 | 0.400 | 0.602 | 0.443 | Anon-Arden 0.915 | yes |
| 1Tam | Marlowe | **Peele** | 0.960 | 1.527 | 1.429 | 1.433 | Peele 0.532 | NO |
| 2Tam | Marlowe | **Lodge** | 0.930 | 1.480 | 1.425 | 1.378 | Lodge 0.552 | NO |
| Dido | Marlowe | **Lodge** | 0.860 | 1.172 | 1.088 | 1.170 | Lodge 0.759 | NO |
| DrFaust | Marlowe | **Anon-Arden** | 1.045 | 0.941 | 0.938 | 0.956 | Anon-Arden 0.725 | NO |
| JoM | Marlowe | **Anon-Arden** | 1.132 | 0.790 | 0.760 | 0.854 | Anon-Arden 0.625 | NO |
| Ed2 | Marlowe | **Anon-TTR3** | 0.690 | 1.118 | 1.022 | 1.135 | Anon-TTR3 0.687 | NO |
| MP | Marlowe | **Marlowe** | 0.668 | 1.312 | 1.205 | 1.286 | Anon-TTR3 0.700 | yes |
| ST | Kyd | **Anon-TTR3** | 0.781 | 1.215 | 1.003 | 1.265 | Anon-TTR3 0.676 | NO |
| OWT | Peele | **Anon-Arden** | 1.231 | 0.772 | 0.853 | 0.786 | Anon-Arden 0.766 | NO |
| Gal | Lyly | **Lyly** | 1.077 | 0.973 | 0.979 | 0.977 | Lyly 0.346 | yes |
| AShrew | Anon-AShrew | **Anon-Arden** | 0.930 | 0.862 | 0.865 | 0.893 | Anon-Arden 0.609 | NO |
| TCKL | Anon-Leir | **Anon-AShrew** | 1.192 | 0.826 | 0.804 | 0.878 | Anon-AShrew 0.749 | NO |
| Alphonsus | Greene | **Anon-Leir** | 1.075 | 1.150 | 1.149 | 1.113 | Anon-Leir 0.717 | NO |
| Orlando | Greene | **Lodge** | 0.905 | 1.233 | 1.108 | 1.236 | Lodge 0.735 | NO |
| FriarBacon | Greene | **Greene** | 1.012 | 1.252 | 1.081 | 1.272 | Greene 0.620 | yes |
| JamesIV | Greene | **Lodge** | 1.160 | 1.025 | 0.918 | 1.071 | Lodge 0.815 | NO |
| Alcazar | Peele | **Anon-Locrine** | 0.575 | 1.482 | 1.340 | 1.427 | Anon-Locrine 0.451 | NO |
| EdwardI | Peele | **Peele** | 0.874 | 1.217 | 1.045 | 1.247 | Peele 0.611 | yes |
| David | Peele | **Anon-Locrine** | 0.622 | 1.442 | 1.226 | 1.432 | Anon-Locrine 0.535 | NO |
| Wounds | Lodge | **Anon-Locrine** | 0.578 | 1.526 | 1.371 | 1.469 | Anon-Locrine 0.550 | NO |
| Soliman | Anon-Soliman | **Anon-Arden** | 0.918 | 1.103 | 0.824 | 1.215 | Anon-Arden 0.775 | NO |
| Locrine | Anon-Locrine | **Peele** | 0.722 | 1.412 | 1.306 | 1.361 | Peele 0.508 | NO |
| Selimus | Anon-Selimus | **Anon-Locrine** | 0.812 | 1.294 | 1.202 | 1.266 | Anon-Locrine 0.702 | NO |
| TRKJ | Anon-TRKJ | **Peele** | 0.916 | 1.235 | 1.118 | 1.233 | Peele 0.611 | NO |
| JackStraw | Anon-JackStraw | **Anon-Leir** | 0.823 | 1.128 | 1.190 | 1.068 | Anon-Leir 0.780 | NO |
| EdwardIII | Anon-EdwardIII | **Anon-Selimus** | 0.906 | 1.110 | 1.040 | 1.117 | Anon-Selimus 0.790 | NO |
| Arden | Anon-Arden | **Anon-AShrew** | 0.898 | 0.804 | 0.723 | 0.891 | Anon-AShrew 0.628 | NO |
| TTR3 | Anon-TTR3 | **Kyd** | 0.883 | 1.165 | 1.018 | 1.196 | Kyd 0.699 | NO |
| Endymion | Lyly | **Lyly** | 1.135 | 1.045 | 1.100 | 1.008 | Lyly 0.338 | yes |

Accuracy: 19/48

