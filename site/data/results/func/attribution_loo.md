# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-150 words)

Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.

| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |
|---|---|---|---|---|---|---|---|---|
| 1Tam | Marlowe | **Peele** | 0.888 | 1.350 | 1.197 | 1.303 | Peele 0.510 | NO |
| 2Tam | Marlowe | **Peele** | 0.802 | 1.329 | 1.255 | 1.242 | Peele 0.491 | NO |
| Dido | Marlowe | **Kyd** | 0.771 | 1.252 | 1.061 | 1.271 | Kyd 0.704 | NO |
| DrFaust | Marlowe | **Lyly** | 0.931 | 1.130 | 1.074 | 1.114 | Lyly 0.839 | NO |
| JoM | Marlowe | **Anon-TTR3** | 1.031 | 0.949 | 0.882 | 1.009 | Anon-TTR3 0.657 | NO |
| Ed2 | Marlowe | **Marlowe** | 0.692 | 1.029 | 0.810 | 1.152 | Kyd 0.742 | yes |
| MP | Marlowe | **Marlowe** | 0.685 | 1.259 | 1.125 | 1.240 | Anon-Locrine 0.782 | yes |
| 2H6 | Shakespeare | **Anon-Soliman** | 0.870 | 0.959 | 0.896 | 1.001 | Anon-Soliman 0.812 | NO |
| 3H6 | Shakespeare | **Kyd** | 0.751 | 1.109 | 0.903 | 1.179 | Kyd 0.607 | NO |
| 1H6 | Shakespeare | **Peele** | 0.782 | 1.119 | 1.095 | 1.097 | Peele 0.762 | NO |
| Tit | Shakespeare | **Kyd** | 0.965 | 0.893 | 0.792 | 0.986 | Kyd 0.744 | NO |
| R3 | Shakespeare | **Shakespeare** | 1.081 | 0.738 | 0.756 | 0.803 | Kyd 0.823 | yes |
| Shr | Shakespeare | **Dekker** | 1.250 | 0.822 | 0.763 | 0.918 | Dekker 0.696 | NO |
| TGV | Shakespeare | **Shakespeare** | 1.404 | 0.626 | 0.699 | 0.724 | Anon-Leir 0.763 | yes |
| Err | Shakespeare | **Shakespeare** | 1.235 | 0.610 | 0.674 | 0.717 | Anon-Arden 0.708 | yes |
| R2 | Shakespeare | **Anon-Selimus** | 1.028 | 0.818 | 0.939 | 0.812 | Anon-Selimus 0.807 | NO |
| MND | Shakespeare | **Shakespeare** | 1.136 | 0.817 | 0.921 | 0.822 | Fletcher 0.866 | yes |
| Rom | Shakespeare | **Shakespeare** | 1.240 | 0.633 | 0.621 | 0.791 | Anon-EdwardIII 0.935 | yes |
| MV | Shakespeare | **Shakespeare** | 1.402 | 0.631 | 0.823 | 0.651 | Lyly 0.769 | yes |
| 1H4 | Shakespeare | **Shakespeare** | 1.213 | 0.700 | 0.875 | 0.704 | Beaumont 0.844 | yes |
| JC | Shakespeare | **Shakespeare** | 1.106 | 0.664 | 0.958 | 0.601 | Anon-Arden 0.726 | yes |
| Ham | Shakespeare | **Shakespeare** | 1.293 | 0.634 | 1.059 | 0.496 | Ford 0.713 | yes |
| Mac | Shakespeare | **Shakespeare** | 1.029 | 0.752 | 1.039 | 0.659 | Middleton 0.820 | yes |
| Lr | Shakespeare | **Shakespeare** | 1.302 | 0.524 | 0.912 | 0.455 | Ford 0.802 | yes |
| WT | Shakespeare | **Shakespeare** | 1.392 | 0.545 | 0.906 | 0.481 | Ford 0.618 | yes |
| Tmp | Shakespeare | **Shakespeare** | 1.238 | 0.570 | 0.831 | 0.568 | Ford 0.800 | yes |
| ST | Kyd | **Anon-TTR3** | 0.768 | 1.077 | 0.738 | 1.261 | Anon-TTR3 0.760 | NO |
| OWT | Peele | **Anon-Arden** | 1.131 | 0.937 | 0.958 | 0.947 | Anon-Arden 0.767 | NO |
| Gal | Lyly | **Lyly** | 1.127 | 0.949 | 0.922 | 0.985 | Lyly 0.300 | yes |
| AShrew | Anon-AShrew | **Anon-Leir** | 1.034 | 0.915 | 0.803 | 1.007 | Anon-Leir 0.687 | NO |
| TCKL | Anon-Leir | **Anon-AShrew** | 1.174 | 0.878 | 0.806 | 0.967 | Anon-AShrew 0.726 | NO |
| ShoeHol | Dekker | **Beaumont** | 1.061 | 0.912 | 0.912 | 0.945 | Beaumont 0.755 | NO |
| RT | Middleton | **Fletcher** | 1.100 | 0.945 | 1.137 | 0.852 | Fletcher 0.725 | NO |
| KBP | Beaumont | **Fletcher** | 1.085 | 0.834 | 0.992 | 0.801 | Fletcher 0.596 | NO |
| FS | Fletcher | **Beaumont** | 0.978 | 1.086 | 1.138 | 1.022 | Beaumont 0.676 | NO |
| Prize | Fletcher | **Fletcher** | 1.359 | 0.813 | 1.064 | 0.733 | Fletcher 0.474 | yes |
| IP | Fletcher | **Fletcher** | 1.025 | 1.034 | 1.226 | 0.907 | Fletcher 0.533 | yes |
| Perkin | Ford | **Middleton** | 1.033 | 0.947 | 1.234 | 0.798 | Middleton 0.797 | NO |
| TPSW | Ford | **Fletcher** | 1.402 | 0.739 | 0.878 | 0.751 | Fletcher 0.680 | NO |
| Alphonsus | Greene | **Anon-Leir** | 1.047 | 1.048 | 1.132 | 0.980 | Anon-Leir 0.670 | NO |
| Orlando | Greene | **Lodge** | 0.714 | 1.203 | 1.062 | 1.211 | Lodge 0.678 | NO |
| FriarBacon | Greene | **Greene** | 0.823 | 1.273 | 1.050 | 1.304 | Greene 0.663 | yes |
| JamesIV | Greene | **Lodge** | 1.103 | 1.029 | 0.886 | 1.105 | Lodge 0.742 | NO |
| Alcazar | Peele | **Peele** | 0.561 | 1.330 | 1.129 | 1.323 | Peele 0.555 | yes |
| EdwardI | Peele | **Peele** | 0.735 | 1.317 | 1.096 | 1.329 | Peele 0.580 | yes |
| David | Peele | **Marlowe** | 0.496 | 1.303 | 1.065 | 1.329 | Peele 0.518 | NO |
| Wounds | Lodge | **Peele** | 0.587 | 1.386 | 1.195 | 1.352 | Peele 0.577 | NO |
| Soliman | Anon-Soliman | **Anon-Arden** | 0.961 | 1.027 | 0.708 | 1.218 | Anon-Arden 0.685 | NO |
| Locrine | Anon-Locrine | **Peele** | 0.718 | 1.297 | 1.183 | 1.251 | Peele 0.585 | NO |
| Selimus | Anon-Selimus | **Anon-TRKJ** | 0.885 | 1.173 | 1.060 | 1.175 | Anon-TRKJ 0.774 | NO |
| TRKJ | Anon-TRKJ | **Peele** | 0.827 | 1.186 | 1.016 | 1.218 | Peele 0.635 | NO |
| JackStraw | Anon-JackStraw | **Marlowe** | 0.766 | 1.210 | 1.230 | 1.117 | Anon-TTR3 0.820 | NO |
| EdwardIII | Anon-EdwardIII | **Anon-Locrine** | 0.850 | 1.010 | 0.943 | 1.047 | Anon-Locrine 0.811 | NO |
| Arden | Anon-Arden | **Anon-Soliman** | 1.044 | 0.908 | 0.840 | 0.984 | Anon-Soliman 0.690 | NO |
| TTR3 | Anon-TTR3 | **Anon-Soliman** | 0.954 | 1.115 | 0.914 | 1.181 | Anon-Soliman 0.702 | NO |
| Endymion | Lyly | **Lyly** | 1.177 | 1.022 | 1.106 | 0.964 | Lyly 0.318 | yes |

Accuracy: 22/56

