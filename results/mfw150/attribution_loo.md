# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-150 words)

Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.

| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |
|---|---|---|---|---|---|---|---|---|
| 1Tam | Marlowe | **Peele** | 0.877 | 1.467 | 1.292 | 1.410 | Peele 0.517 | NO |
| 2Tam | Marlowe | **Lodge** | 0.854 | 1.435 | 1.306 | 1.365 | Lodge 0.504 | NO |
| Dido | Marlowe | **Lodge** | 0.798 | 1.152 | 0.960 | 1.207 | Lodge 0.716 | NO |
| DrFaust | Marlowe | **Anon-Arden** | 1.007 | 0.979 | 0.887 | 1.033 | Anon-Arden 0.811 | NO |
| JoM | Marlowe | **Anon-Arden** | 1.082 | 0.934 | 0.857 | 0.992 | Anon-Arden 0.684 | NO |
| Ed2 | Marlowe | **Marlowe** | 0.620 | 1.149 | 0.986 | 1.189 | Kyd 0.696 | yes |
| MP | Marlowe | **Marlowe** | 0.585 | 1.309 | 1.138 | 1.308 | Anon-TTR3 0.706 | yes |
| 2H6 | Shakespeare | **Marlowe** | 0.731 | 1.083 | 1.127 | 1.043 | Anon-Selimus 0.787 | NO |
| 3H6 | Shakespeare | **Anon-EdwardIII** | 0.708 | 1.123 | 1.040 | 1.131 | Anon-EdwardIII 0.666 | NO |
| 1H6 | Shakespeare | **Anon-EdwardIII** | 0.861 | 1.127 | 1.217 | 1.055 | Anon-EdwardIII 0.615 | NO |
| Tit | Shakespeare | **Kyd** | 0.852 | 0.861 | 0.867 | 0.895 | Kyd 0.834 | NO |
| R3 | Shakespeare | **Shakespeare** | 0.976 | 0.830 | 0.949 | 0.816 | Kyd 0.832 | yes |
| Shr | Shakespeare | **Dekker** | 1.288 | 0.781 | 0.816 | 0.824 | Dekker 0.662 | NO |
| TGV | Shakespeare | **Shakespeare** | 1.433 | 0.647 | 0.790 | 0.684 | Anon-Leir 0.719 | yes |
| Err | Shakespeare | **Shakespeare** | 1.338 | 0.649 | 0.769 | 0.693 | Anon-Arden 0.744 | yes |
| R2 | Shakespeare | **Anon-EdwardIII** | 0.916 | 0.890 | 0.984 | 0.871 | Anon-EdwardIII 0.756 | NO |
| MND | Shakespeare | **Shakespeare** | 1.185 | 0.703 | 0.840 | 0.715 | Fletcher 0.800 | yes |
| Rom | Shakespeare | **Shakespeare** | 1.322 | 0.560 | 0.635 | 0.653 | Beaumont 0.845 | yes |
| MV | Shakespeare | **Shakespeare** | 1.478 | 0.531 | 0.707 | 0.574 | Anon-Leir 0.770 | yes |
| 1H4 | Shakespeare | **Shakespeare** | 1.265 | 0.637 | 0.849 | 0.626 | Beaumont 0.802 | yes |
| JC | Shakespeare | **Shakespeare** | 1.189 | 0.584 | 0.902 | 0.524 | Anon-Arden 0.790 | yes |
| Ham | Shakespeare | **Shakespeare** | 1.261 | 0.542 | 0.871 | 0.486 | Ford 0.773 | yes |
| Mac | Shakespeare | **Shakespeare** | 1.125 | 0.663 | 0.991 | 0.577 | Middleton 0.829 | yes |
| Lr | Shakespeare | **Shakespeare** | 1.242 | 0.535 | 0.800 | 0.524 | Beaumont 0.748 | yes |
| WT | Shakespeare | **Shakespeare** | 1.495 | 0.513 | 0.820 | 0.483 | Ford 0.614 | yes |
| Tmp | Shakespeare | **Shakespeare** | 1.336 | 0.433 | 0.672 | 0.469 | Fletcher 0.783 | yes |
| ST | Kyd | **Anon-TTR3** | 0.676 | 1.195 | 0.869 | 1.308 | Anon-TTR3 0.630 | NO |
| OWT | Peele | **Anon-AShrew** | 1.205 | 0.821 | 0.888 | 0.837 | Anon-AShrew 0.763 | NO |
| Gal | Lyly | **Lyly** | 1.086 | 1.009 | 1.006 | 1.008 | Lyly 0.358 | yes |
| AShrew | Anon-AShrew | **Beaumont** | 0.921 | 0.954 | 0.901 | 0.991 | Beaumont 0.624 | NO |
| TCKL | Anon-Leir | **Anon-AShrew** | 1.206 | 0.863 | 0.833 | 0.917 | Anon-AShrew 0.740 | NO |
| ShoeHol | Dekker | **Beaumont** | 1.077 | 0.778 | 0.780 | 0.838 | Beaumont 0.675 | NO |
| RT | Middleton | **Ford** | 1.032 | 0.850 | 1.030 | 0.801 | Ford 0.751 | NO |
| KBP | Beaumont | **Fletcher** | 1.169 | 0.735 | 0.859 | 0.747 | Fletcher 0.537 | NO |
| FS | Fletcher | **Beaumont** | 0.948 | 1.020 | 1.066 | 0.991 | Beaumont 0.790 | NO |
| Prize | Fletcher | **Fletcher** | 1.360 | 0.716 | 0.914 | 0.694 | Fletcher 0.481 | yes |
| IP | Fletcher | **Fletcher** | 1.174 | 0.846 | 1.132 | 0.746 | Fletcher 0.565 | yes |
| Perkin | Ford | **Anon-Locrine** | 1.007 | 1.032 | 1.216 | 0.931 | Anon-Locrine 0.798 | NO |
| TPSW | Ford | **Fletcher** | 1.382 | 0.702 | 0.830 | 0.719 | Fletcher 0.630 | NO |
| Alphonsus | Greene | **Anon-Leir** | 1.007 | 1.121 | 1.125 | 1.085 | Anon-Leir 0.697 | NO |
| Orlando | Greene | **Lodge** | 0.881 | 1.215 | 1.058 | 1.233 | Lodge 0.695 | NO |
| FriarBacon | Greene | **Greene** | 0.984 | 1.255 | 1.108 | 1.256 | Greene 0.580 | yes |
| JamesIV | Greene | **Lodge** | 1.162 | 1.117 | 0.968 | 1.160 | Lodge 0.798 | NO |
| Alcazar | Peele | **Anon-Locrine** | 0.539 | 1.404 | 1.236 | 1.369 | Anon-Locrine 0.442 | NO |
| EdwardI | Peele | **Peele** | 0.829 | 1.268 | 1.056 | 1.299 | Peele 0.586 | yes |
| David | Peele | **Anon-Locrine** | 0.548 | 1.327 | 1.077 | 1.356 | Anon-Locrine 0.517 | NO |
| Wounds | Lodge | **Marlowe** | 0.537 | 1.535 | 1.295 | 1.496 | Anon-Locrine 0.541 | NO |
| Soliman | Anon-Soliman | **Anon-Arden** | 0.941 | 1.089 | 0.790 | 1.220 | Anon-Arden 0.723 | NO |
| Locrine | Anon-Locrine | **Peele** | 0.682 | 1.375 | 1.184 | 1.360 | Peele 0.497 | NO |
| Selimus | Anon-Selimus | **Anon-Locrine** | 0.754 | 1.305 | 1.157 | 1.293 | Anon-Locrine 0.656 | NO |
| TRKJ | Anon-TRKJ | **Peele** | 0.852 | 1.205 | 1.037 | 1.232 | Peele 0.565 | NO |
| JackStraw | Anon-JackStraw | **Anon-Leir** | 0.829 | 1.151 | 1.232 | 1.067 | Anon-Leir 0.785 | NO |
| EdwardIII | Anon-EdwardIII | **Anon-Selimus** | 0.842 | 1.044 | 0.981 | 1.064 | Anon-Selimus 0.719 | NO |
| Arden | Anon-Arden | **Anon-TTR3** | 0.937 | 0.944 | 0.822 | 1.023 | Anon-TTR3 0.734 | NO |
| TTR3 | Anon-TTR3 | **Kyd** | 0.828 | 1.165 | 1.042 | 1.182 | Kyd 0.644 | NO |
| Endymion | Lyly | **Lyly** | 1.156 | 1.055 | 1.134 | 1.000 | Lyly 0.366 | yes |

Accuracy: 21/56

