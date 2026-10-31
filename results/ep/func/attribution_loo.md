# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-150 words)

Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.

| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |
|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | **Anon-Selimus** | 0.934 | 1.025 | 0.982 | 1.039 | Anon-Selimus 0.852 | NO |
| 3H6 | Shakespeare | **Kyd** | 0.884 | 1.138 | 0.974 | 1.179 | Kyd 0.698 | NO |
| 1H6 | Shakespeare | **Peele** | 0.857 | 1.153 | 1.128 | 1.126 | Peele 0.809 | NO |
| Tit | Shakespeare | **Peele** | 1.024 | 0.939 | 0.855 | 0.998 | Peele 0.821 | NO |
| R3 | Shakespeare | **Shakespeare** | 1.190 | 0.761 | 0.794 | 0.805 | Anon-Leir 0.846 | yes |
| Shr | Shakespeare | **Shakespeare** | 1.261 | 0.722 | 0.716 | 0.807 | Anon-Arden 0.728 | yes |
| TGV | Shakespeare | **Shakespeare** | 1.432 | 0.583 | 0.661 | 0.674 | Anon-Leir 0.749 | yes |
| Err | Shakespeare | **Shakespeare** | 1.295 | 0.622 | 0.708 | 0.698 | Anon-Arden 0.652 | yes |
| R2 | Shakespeare | **Shakespeare** | 1.083 | 0.789 | 0.948 | 0.770 | Anon-Selimus 0.832 | yes |
| MND | Shakespeare | **Shakespeare** | 1.120 | 0.807 | 0.894 | 0.823 | Anon-Arden 0.837 | yes |
| Rom | Shakespeare | **Shakespeare** | 1.267 | 0.653 | 0.627 | 0.786 | Anon-Arden 0.917 | yes |
| MV | Shakespeare | **Shakespeare** | 1.407 | 0.567 | 0.725 | 0.622 | Lyly 0.752 | yes |
| 1H4 | Shakespeare | **Shakespeare** | 1.198 | 0.673 | 0.883 | 0.662 | Anon-Selimus 0.930 | yes |
| JC | Shakespeare | **Shakespeare** | 1.113 | 0.621 | 0.917 | 0.574 | Anon-Arden 0.698 | yes |
| Ham | Shakespeare | **Shakespeare** | 1.280 | 0.539 | 0.964 | 0.445 | Anon-Arden 0.952 | yes |
| Mac | Shakespeare | **Shakespeare** | 1.028 | 0.689 | 1.035 | 0.591 | Anon-EdwardIII 0.900 | yes |
| Lr | Shakespeare | **Shakespeare** | 1.267 | 0.476 | 0.844 | 0.437 | Anon-Arden 0.985 | yes |
| WT | Shakespeare | **Shakespeare** | 1.305 | 0.479 | 0.822 | 0.449 | Anon-Leir 0.772 | yes |
| Tmp | Shakespeare | **Shakespeare** | 1.248 | 0.515 | 0.775 | 0.527 | Anon-Leir 0.897 | yes |
| 1Tam | Marlowe | **Peele** | 0.971 | 1.412 | 1.296 | 1.331 | Peele 0.532 | NO |
| 2Tam | Marlowe | **Peele** | 0.863 | 1.368 | 1.344 | 1.255 | Peele 0.492 | NO |
| Dido | Marlowe | **Kyd** | 0.809 | 1.292 | 1.134 | 1.280 | Kyd 0.739 | NO |
| DrFaust | Marlowe | **Lyly** | 0.943 | 1.033 | 1.091 | 0.992 | Lyly 0.814 | NO |
| JoM | Marlowe | **Anon-TTR3** | 0.989 | 0.910 | 0.931 | 0.927 | Anon-TTR3 0.687 | NO |
| Ed2 | Marlowe | **Anon-Arden** | 0.760 | 1.072 | 0.922 | 1.128 | Anon-Arden 0.757 | NO |
| MP | Marlowe | **Marlowe** | 0.708 | 1.316 | 1.199 | 1.273 | Lodge 0.802 | yes |
| ST | Kyd | **Anon-TTR3** | 0.839 | 1.165 | 0.870 | 1.272 | Anon-TTR3 0.769 | NO |
| OWT | Peele | **Anon-Arden** | 1.127 | 0.856 | 0.948 | 0.854 | Anon-Arden 0.755 | NO |
| Gal | Lyly | **Lyly** | 1.134 | 0.919 | 0.908 | 0.951 | Lyly 0.309 | yes |
| AShrew | Anon-AShrew | **Anon-Leir** | 1.011 | 0.871 | 0.808 | 0.939 | Anon-Leir 0.690 | NO |
| TCKL | Anon-Leir | **Anon-AShrew** | 1.164 | 0.826 | 0.771 | 0.910 | Anon-AShrew 0.732 | NO |
| Alphonsus | Greene | **Anon-Leir** | 1.110 | 1.066 | 1.160 | 0.995 | Anon-Leir 0.707 | NO |
| Orlando | Greene | **Lodge** | 0.739 | 1.255 | 1.110 | 1.248 | Lodge 0.739 | NO |
| FriarBacon | Greene | **Greene** | 0.895 | 1.303 | 1.079 | 1.322 | Greene 0.693 | yes |
| JamesIV | Greene | **Lodge** | 1.134 | 0.998 | 0.894 | 1.054 | Lodge 0.738 | NO |
| Alcazar | Peele | **Peele** | 0.604 | 1.418 | 1.229 | 1.377 | Peele 0.577 | yes |
| EdwardI | Peele | **Peele** | 0.772 | 1.249 | 1.073 | 1.261 | Peele 0.609 | yes |
| David | Peele | **Peele** | 0.586 | 1.413 | 1.184 | 1.395 | Peele 0.554 | yes |
| Wounds | Lodge | **Peele** | 0.639 | 1.386 | 1.266 | 1.322 | Peele 0.630 | NO |
| Soliman | Anon-Soliman | **Anon-Arden** | 0.964 | 1.065 | 0.749 | 1.217 | Anon-Arden 0.739 | NO |
| Locrine | Anon-Locrine | **Peele** | 0.770 | 1.297 | 1.260 | 1.219 | Peele 0.611 | NO |
| Selimus | Anon-Selimus | **Anon-TRKJ** | 0.960 | 1.151 | 1.095 | 1.131 | Anon-TRKJ 0.841 | NO |
| TRKJ | Anon-TRKJ | **Peele** | 0.914 | 1.213 | 1.074 | 1.217 | Peele 0.670 | NO |
| JackStraw | Anon-JackStraw | **Marlowe** | 0.795 | 1.158 | 1.200 | 1.085 | Anon-TTR3 0.829 | NO |
| EdwardIII | Anon-EdwardIII | **Anon-Locrine** | 0.945 | 1.096 | 1.003 | 1.114 | Anon-Locrine 0.846 | NO |
| Arden | Anon-Arden | **Anon-Soliman** | 1.006 | 0.800 | 0.726 | 0.904 | Anon-Soliman 0.749 | NO |
| TTR3 | Anon-TTR3 | **Anon-Soliman** | 0.992 | 1.079 | 0.921 | 1.131 | Anon-Soliman 0.732 | NO |
| Endymion | Lyly | **Lyly** | 1.174 | 0.948 | 1.069 | 0.902 | Lyly 0.330 | yes |

Accuracy: 22/48

