# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-500 words)

Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.

| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |
|---|---|---|---|---|---|---|---|---|
| 1Tam | Marlowe | **Peele** | 0.777 | 1.361 | 1.152 | 1.334 | Peele 0.629 | NO |
| 2Tam | Marlowe | **Peele** | 0.754 | 1.289 | 1.181 | 1.232 | Peele 0.628 | NO |
| Dido | Marlowe | **Marlowe** | 0.771 | 1.101 | 1.005 | 1.119 | Peele 0.816 | yes |
| DrFaust | Marlowe | **Marlowe** | 0.885 | 1.089 | 1.019 | 1.096 | Greene 0.916 | yes |
| JoM | Marlowe | **Anon-AShrew** | 0.974 | 0.962 | 0.881 | 1.025 | Anon-AShrew 0.789 | NO |
| Ed2 | Marlowe | **Marlowe** | 0.744 | 1.110 | 0.845 | 1.227 | Anon-TTR3 0.773 | yes |
| MP | Marlowe | **Marlowe** | 0.742 | 1.191 | 1.017 | 1.219 | Anon-TTR3 0.786 | yes |
| 2H6 | Shakespeare | **Anon-Selimus** | 0.873 | 1.027 | 1.045 | 1.010 | Anon-Selimus 0.850 | NO |
| 3H6 | Shakespeare | **Anon-EdwardIII** | 0.818 | 1.085 | 1.011 | 1.096 | Anon-EdwardIII 0.731 | NO |
| 1H6 | Shakespeare | **Anon-EdwardIII** | 0.829 | 1.135 | 1.160 | 1.081 | Anon-EdwardIII 0.783 | NO |
| Tit | Shakespeare | **Shakespeare** | 0.935 | 0.856 | 0.822 | 0.927 | Kyd 0.885 | yes |
| R3 | Shakespeare | **Anon-EdwardIII** | 0.971 | 0.842 | 0.938 | 0.843 | Anon-EdwardIII 0.835 | NO |
| Shr | Shakespeare | **Dekker** | 1.186 | 0.813 | 0.883 | 0.846 | Dekker 0.719 | NO |
| TGV | Shakespeare | **Shakespeare** | 1.270 | 0.766 | 0.849 | 0.810 | Lyly 0.835 | yes |
| Err | Shakespeare | **Anon-Arden** | 1.189 | 0.775 | 0.876 | 0.806 | Anon-Arden 0.718 | NO |
| R2 | Shakespeare | **Anon-EdwardIII** | 0.960 | 0.884 | 0.893 | 0.925 | Anon-EdwardIII 0.811 | NO |
| MND | Shakespeare | **Shakespeare** | 1.157 | 0.726 | 0.955 | 0.688 | Fletcher 0.859 | yes |
| Rom | Shakespeare | **Shakespeare** | 1.183 | 0.638 | 0.819 | 0.672 | Anon-Arden 0.896 | yes |
| MV | Shakespeare | **Shakespeare** | 1.285 | 0.657 | 0.825 | 0.689 | Beaumont 0.842 | yes |
| 1H4 | Shakespeare | **Shakespeare** | 1.174 | 0.681 | 0.870 | 0.690 | Beaumont 0.840 | yes |
| JC | Shakespeare | **Shakespeare** | 1.163 | 0.689 | 0.976 | 0.626 | Fletcher 0.870 | yes |
| Ham | Shakespeare | **Shakespeare** | 1.239 | 0.642 | 0.991 | 0.561 | Ford 0.864 | yes |
| Mac | Shakespeare | **Shakespeare** | 1.135 | 0.748 | 1.028 | 0.666 | Fletcher 0.856 | yes |
| Lr | Shakespeare | **Shakespeare** | 1.285 | 0.610 | 0.878 | 0.596 | Fletcher 0.835 | yes |
| WT | Shakespeare | **Shakespeare** | 1.349 | 0.615 | 0.887 | 0.594 | Ford 0.755 | yes |
| Tmp | Shakespeare | **Shakespeare** | 1.203 | 0.689 | 0.962 | 0.636 | Fletcher 0.799 | yes |
| ST | Kyd | **Anon-TTR3** | 0.855 | 1.146 | 0.945 | 1.210 | Anon-TTR3 0.785 | NO |
| OWT | Peele | **Beaumont** | 1.114 | 0.932 | 1.007 | 0.914 | Beaumont 0.782 | NO |
| Gal | Lyly | **Lyly** | 1.073 | 1.026 | 1.050 | 1.001 | Lyly 0.459 | yes |
| AShrew | Anon-AShrew | **Beaumont** | 0.975 | 0.984 | 0.955 | 1.007 | Beaumont 0.734 | NO |
| TCKL | Anon-Leir | **Anon-TTR3** | 1.185 | 0.922 | 0.909 | 0.961 | Anon-TTR3 0.819 | NO |
| ShoeHol | Dekker | **Beaumont** | 1.112 | 0.904 | 0.883 | 0.954 | Beaumont 0.749 | NO |
| RT | Middleton | **Ford** | 1.146 | 0.901 | 1.032 | 0.862 | Ford 0.802 | NO |
| KBP | Beaumont | **Dekker** | 1.187 | 0.815 | 0.913 | 0.828 | Dekker 0.732 | NO |
| FS | Fletcher | **Beaumont** | 1.034 | 0.977 | 1.149 | 0.885 | Beaumont 0.821 | NO |
| Prize | Fletcher | **Fletcher** | 1.338 | 0.793 | 0.962 | 0.772 | Fletcher 0.650 | yes |
| IP | Fletcher | **Fletcher** | 1.183 | 0.964 | 1.201 | 0.840 | Fletcher 0.612 | yes |
| Perkin | Ford | **Ford** | 1.068 | 0.987 | 1.107 | 0.921 | Ford 0.849 | yes |
| TPSW | Ford | **Fletcher** | 1.324 | 0.807 | 0.909 | 0.821 | Fletcher 0.707 | NO |
| Alphonsus | Greene | **Anon-Locrine** | 0.937 | 1.134 | 1.124 | 1.087 | Anon-Locrine 0.777 | NO |
| Orlando | Greene | **Greene** | 0.828 | 1.194 | 1.053 | 1.201 | Greene 0.786 | yes |
| FriarBacon | Greene | **Greene** | 0.939 | 1.166 | 1.074 | 1.155 | Greene 0.741 | yes |
| JamesIV | Greene | **Lodge** | 1.048 | 1.130 | 0.989 | 1.163 | Lodge 0.764 | NO |
| Alcazar | Peele | **Anon-Locrine** | 0.634 | 1.306 | 1.114 | 1.296 | Anon-Locrine 0.607 | NO |
| EdwardI | Peele | **Peele** | 0.858 | 1.160 | 1.013 | 1.184 | Peele 0.804 | yes |
| David | Peele | **Marlowe** | 0.603 | 1.241 | 1.053 | 1.256 | Anon-EdwardIII 0.692 | NO |
| Wounds | Lodge | **Greene** | 0.763 | 1.290 | 1.117 | 1.276 | Greene 0.714 | NO |
| Soliman | Anon-Soliman | **Anon-Selimus** | 0.940 | 1.042 | 0.875 | 1.128 | Anon-Selimus 0.865 | NO |
| Locrine | Anon-Locrine | **Peele** | 0.767 | 1.290 | 1.163 | 1.248 | Peele 0.643 | NO |
| Selimus | Anon-Selimus | **Anon-Locrine** | 0.847 | 1.204 | 1.023 | 1.230 | Anon-Locrine 0.758 | NO |
| TRKJ | Anon-TRKJ | **Peele** | 0.847 | 1.135 | 0.922 | 1.210 | Peele 0.841 | NO |
| JackStraw | Anon-JackStraw | **Anon-TTR3** | 0.943 | 1.080 | 1.127 | 1.020 | Anon-TTR3 0.838 | NO |
| EdwardIII | Anon-EdwardIII | **Peele** | 0.839 | 0.973 | 0.887 | 1.036 | Peele 0.815 | NO |
| Arden | Anon-Arden | **Anon-AShrew** | 0.991 | 0.891 | 0.864 | 0.951 | Anon-AShrew 0.786 | NO |
| TTR3 | Anon-TTR3 | **Kyd** | 0.909 | 1.166 | 1.040 | 1.177 | Kyd 0.791 | NO |
| Endymion | Lyly | **Lyly** | 1.129 | 1.045 | 1.130 | 0.978 | Lyly 0.462 | yes |

Accuracy: 24/56

