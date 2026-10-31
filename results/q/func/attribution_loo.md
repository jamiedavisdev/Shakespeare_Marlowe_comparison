# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-150 words)

Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.

| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |
|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | **Anon-Arden** | 0.921 | 1.044 | 0.848 | 1.069 | Anon-Arden 0.746 | NO |
| 3H6 | Shakespeare | **Kyd** | 0.866 | 1.207 | 0.772 | 1.246 | Kyd 0.709 | NO |
| Tit | Shakespeare | **Kyd** | 1.055 | 0.866 | 0.782 | 0.938 | Kyd 0.854 | NO |
| R3 | Shakespeare | **Shakespeare** | 1.164 | 0.758 | 0.889 | 0.772 | Anon-EdwardIII 0.861 | yes |
| R2 | Shakespeare | **Shakespeare** | 1.066 | 0.767 | 0.752 | 0.861 | Anon-Selimus 0.817 | yes |
| Rom | Shakespeare | **Shakespeare** | 1.214 | 0.647 | 0.882 | 0.684 | Anon-Arden 0.788 | yes |
| 1H4 | Shakespeare | **Shakespeare** | 1.191 | 0.581 | 0.884 | 0.614 | Anon-Selimus 0.895 | yes |
| LLL | Shakespeare | **Shakespeare** | 1.412 | 0.589 | 1.172 | 0.495 | Lyly 0.868 | yes |
| MND | Shakespeare | **Shakespeare** | 1.121 | 0.768 | 1.078 | 0.725 | Anon-Arden 0.841 | yes |
| MV | Shakespeare | **Shakespeare** | 1.373 | 0.541 | 1.119 | 0.466 | Anon-Leir 0.721 | yes |
| Ado | Shakespeare | **Shakespeare** | 1.411 | 0.501 | 1.104 | 0.425 | Lyly 0.664 | yes |
| 2H4 | Shakespeare | **Shakespeare** | 1.220 | 0.493 | 1.012 | 0.465 | Anon-AShrew 0.912 | yes |
| Lr | Shakespeare | **Shakespeare** | 1.238 | 0.516 | 0.959 | 0.513 | Anon-Arden 0.940 | yes |
| Tro | Shakespeare | **Shakespeare** | 1.245 | 0.657 | 1.156 | 0.573 | Anon-Arden 0.895 | yes |
| 1Tam | Marlowe | **Peele** | 1.027 | 1.338 | 1.009 | 1.339 | Peele 0.560 | NO |
| 2Tam | Marlowe | **Peele** | 0.889 | 1.344 | 1.082 | 1.315 | Peele 0.515 | NO |
| Dido | Marlowe | **Kyd** | 0.828 | 1.329 | 1.061 | 1.313 | Kyd 0.725 | NO |
| DrFaust | Marlowe | **Anon-Arden** | 0.931 | 1.012 | 0.973 | 1.023 | Anon-Arden 0.826 | NO |
| JoM | Marlowe | **Anon-TTR3** | 0.973 | 0.917 | 0.951 | 0.934 | Anon-TTR3 0.712 | NO |
| Ed2 | Marlowe | **Anon-Arden** | 0.746 | 1.088 | 0.842 | 1.153 | Anon-Arden 0.739 | NO |
| MP | Marlowe | **Marlowe** | 0.743 | 1.275 | 0.962 | 1.297 | Anon-JackStraw 0.831 | yes |
| ST | Kyd | **Anon-TTR3** | 0.848 | 1.162 | 0.729 | 1.279 | Anon-TTR3 0.772 | NO |
| OWT | Peele | **Anon-Arden** | 1.136 | 0.787 | 1.028 | 0.770 | Anon-Arden 0.731 | NO |
| Gal | Lyly | **Lyly** | 1.119 | 0.933 | 1.135 | 0.880 | Lyly 0.298 | yes |
| AShrew | Anon-AShrew | **Anon-Leir** | 1.019 | 0.798 | 0.732 | 0.896 | Anon-Leir 0.691 | NO |
| TCKL | Anon-Leir | **Anon-AShrew** | 1.123 | 0.869 | 1.002 | 0.865 | Anon-AShrew 0.723 | NO |
| Alphonsus | Greene | **Anon-Leir** | 1.139 | 1.004 | 1.002 | 1.003 | Anon-Leir 0.694 | NO |
| Orlando | Greene | **Lodge** | 0.772 | 1.218 | 1.072 | 1.196 | Lodge 0.751 | NO |
| FriarBacon | Greene | **Greene** | 0.945 | 1.232 | 1.034 | 1.225 | Greene 0.707 | yes |
| JamesIV | Greene | **Lodge** | 1.154 | 0.949 | 1.049 | 0.929 | Lodge 0.759 | NO |
| Alcazar | Peele | **Lodge** | 0.669 | 1.329 | 0.952 | 1.355 | Lodge 0.612 | NO |
| EdwardI | Peele | **Peele** | 0.842 | 1.114 | 1.012 | 1.113 | Peele 0.657 | yes |
| David | Peele | **Peele** | 0.641 | 1.320 | 0.889 | 1.372 | Peele 0.588 | yes |
| Wounds | Lodge | **Peele** | 0.692 | 1.307 | 0.962 | 1.330 | Peele 0.661 | NO |
| Soliman | Anon-Soliman | **Anon-Arden** | 0.974 | 1.044 | 0.765 | 1.142 | Anon-Arden 0.719 | NO |
| Locrine | Anon-Locrine | **Peele** | 0.815 | 1.206 | 1.065 | 1.186 | Peele 0.652 | NO |
| Selimus | Anon-Selimus | **Anon-TRKJ** | 0.990 | 1.098 | 0.934 | 1.127 | Anon-TRKJ 0.828 | NO |
| TRKJ | Anon-TRKJ | **Peele** | 0.933 | 1.211 | 0.941 | 1.240 | Peele 0.709 | NO |
| JackStraw | Anon-JackStraw | **Marlowe** | 0.800 | 1.141 | 1.197 | 1.067 | Anon-TTR3 0.832 | NO |
| EdwardIII | Anon-EdwardIII | **Anon-Locrine** | 0.942 | 1.100 | 0.911 | 1.139 | Anon-Locrine 0.852 | NO |
| Arden | Anon-Arden | **Anon-Soliman** | 1.002 | 0.770 | 0.789 | 0.844 | Anon-Soliman 0.735 | NO |
| TTR3 | Anon-TTR3 | **Anon-Soliman** | 1.003 | 1.044 | 1.060 | 1.036 | Anon-Soliman 0.741 | NO |
| Endymion | Lyly | **Lyly** | 1.165 | 0.950 | 1.375 | 0.807 | Lyly 0.323 | yes |

Accuracy: 17/43

