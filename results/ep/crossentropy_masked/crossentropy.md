# Cross-entropy of each play under character-level author models (bits/char, lower = more predictable)

Order-6 Witten-Bell character models. Variant: masked (masked = proper nouns replaced by a placeholder, and plays sharing plot/characters excluded from training together). The held-out play is never in training. Marlowe, Sh-early, Sh-later, Sh-all, Greene, Peele and Anon-heroic models are truncated to 273,328 characters (= the smaller of the Greene and Peele corpora) so they are the same size, drawing an equal share of characters from each training play; Fletcher (3 plays), Ford (2) and the single-play controls are smaller, so their entropies are biased upward and are listed for reference only.

| held-out play | author | Marlowe | Sh-early | Sh-later | Sh-all | Greene | Peele | Anon-heroic | Fletcher | Ford | Kyd | Lodge | Lyly | Anon-AShrew | Anon-Leir | Dekker | Middleton | Beaumont | best size-matched model | Marlowe − Sh-all |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | 2.286 | 2.304 | 2.256 | 2.249 | 2.378 | 2.379 | 2.258 | - | - | 2.547 | 2.653 | 2.609 | 2.894 | 2.626 | - | - | - | **Sh-all** | +0.037 |
| 3H6 | Shakespeare | 2.226 | 2.250 | 2.230 | 2.211 | 2.322 | 2.316 | 2.190 | - | - | 2.461 | 2.568 | 2.561 | 2.866 | 2.548 | - | - | - | **Anon-heroic** | +0.014 |
| 1H6 | Shakespeare | 2.289 | 2.336 | 2.293 | 2.268 | 2.382 | 2.396 | 2.253 | - | - | 2.557 | 2.657 | 2.639 | 2.998 | 2.628 | - | - | - | **Anon-heroic** | +0.021 |
| Tit | Shakespeare | 2.244 | 2.207 | 2.258 | 2.220 | 2.353 | 2.305 | 2.236 | - | - | 2.489 | 2.598 | 2.579 | 2.834 | 2.594 | - | - | - | **Sh-early** | +0.024 |
| R3 | Shakespeare | 2.274 | 2.232 | 2.187 | 2.179 | 2.357 | 2.348 | 2.219 | - | - | 2.495 | 2.617 | 2.560 | 2.890 | 2.550 | - | - | - | **Sh-all** | +0.096 |
| Shr | Shakespeare | 2.351 | 2.244 | 2.243 | 2.235 | 2.334 | 2.406 | 2.306 | - | - | 2.589 | 2.719 | 2.550 | - | 2.587 | - | - | - | **Sh-all** | +0.117 |
| TGV | Shakespeare | 2.262 | 2.171 | 2.165 | 2.146 | 2.283 | 2.351 | 2.211 | - | - | 2.488 | 2.640 | 2.455 | 2.710 | 2.496 | - | - | - | **Sh-all** | +0.116 |
| Err | Shakespeare | 2.319 | 2.234 | 2.213 | 2.224 | 2.360 | 2.394 | 2.261 | - | - | 2.564 | 2.707 | 2.558 | 2.735 | 2.586 | - | - | - | **Sh-later** | +0.095 |
| R2 | Shakespeare | 2.325 | 2.240 | 2.247 | 2.216 | 2.408 | 2.391 | 2.281 | - | - | 2.556 | 2.671 | 2.640 | 2.947 | 2.622 | - | - | - | **Sh-all** | +0.108 |
| MND | Shakespeare | 2.414 | 2.326 | 2.298 | 2.309 | 2.443 | 2.481 | 2.396 | - | - | 2.655 | 2.743 | 2.591 | 2.871 | 2.692 | - | - | - | **Sh-later** | +0.105 |
| Rom | Shakespeare | 2.373 | 2.288 | 2.263 | 2.257 | 2.423 | 2.448 | 2.337 | - | - | 2.610 | 2.733 | 2.614 | 2.859 | 2.657 | - | - | - | **Sh-all** | +0.116 |
| MV | Shakespeare | 2.318 | 2.244 | 2.217 | 2.219 | 2.382 | 2.403 | 2.285 | - | - | 2.589 | 2.708 | 2.537 | 2.788 | 2.575 | - | - | - | **Sh-later** | +0.100 |
| 1H4 | Shakespeare | 2.378 | 2.294 | 2.261 | 2.259 | 2.451 | 2.460 | 2.354 | - | - | 2.649 | 2.789 | 2.628 | 2.885 | 2.669 | - | - | - | **Sh-all** | +0.119 |
| JC | Shakespeare | 2.246 | 2.179 | 2.147 | 2.144 | 2.314 | 2.333 | 2.218 | - | - | 2.477 | 2.604 | 2.484 | 2.782 | 2.551 | - | - | - | **Sh-all** | +0.101 |
| Ham | Shakespeare | 2.396 | 2.323 | 2.240 | 2.263 | 2.468 | 2.481 | 2.364 | - | - | 2.625 | 2.780 | 2.635 | 2.889 | 2.657 | - | - | - | **Sh-later** | +0.133 |
| Mac | Shakespeare | 2.409 | 2.334 | 2.263 | 2.281 | 2.489 | 2.501 | 2.393 | - | - | 2.655 | 2.773 | 2.674 | 2.947 | 2.712 | - | - | - | **Sh-later** | +0.128 |
| Lr | Shakespeare | 2.396 | 2.305 | 2.238 | 2.255 | 2.457 | 2.477 | 2.352 | - | - | 2.618 | 2.752 | 2.609 | 2.907 | 2.647 | - | - | - | **Sh-later** | +0.142 |
| WT | Shakespeare | 2.382 | 2.284 | 2.221 | 2.239 | 2.445 | 2.471 | 2.350 | - | - | 2.627 | 2.780 | 2.598 | 2.878 | 2.618 | - | - | - | **Sh-later** | +0.143 |
| Tmp | Shakespeare | 2.452 | 2.384 | 2.311 | 2.329 | 2.526 | 2.551 | 2.438 | - | - | 2.721 | 2.857 | 2.682 | 2.960 | 2.750 | - | - | - | **Sh-later** | +0.123 |
| 1Tam | Marlowe | 2.312 | 2.386 | 2.424 | 2.363 | 2.323 | 2.275 | 2.291 | - | - | 2.624 | 2.625 | 2.695 | 3.014 | 2.754 | - | - | - | **Peele** | -0.051 |
| 2Tam | Marlowe | 2.310 | 2.397 | 2.401 | 2.361 | 2.356 | 2.294 | 2.322 | - | - | 2.628 | 2.665 | 2.707 | 2.999 | 2.799 | - | - | - | **Peele** | -0.051 |
| Dido | Marlowe | 2.284 | 2.333 | 2.376 | 2.326 | 2.349 | 2.382 | 2.328 | - | - | 2.592 | 2.633 | 2.623 | 2.867 | 2.706 | - | - | - | **Marlowe** | -0.042 |
| DrFaust | Marlowe | 2.336 | 2.355 | 2.372 | 2.337 | 2.366 | 2.416 | 2.356 | - | - | 2.634 | 2.784 | 2.638 | 2.882 | 2.748 | - | - | - | **Marlowe** | -0.000 |
| JoM | Marlowe | 2.276 | 2.255 | 2.282 | 2.253 | 2.365 | 2.370 | 2.273 | - | - | 2.502 | 2.677 | 2.599 | 2.778 | 2.569 | - | - | - | **Sh-all** | +0.024 |
| Ed2 | Marlowe | 2.150 | 2.211 | 2.252 | 2.201 | 2.231 | 2.195 | 2.145 | - | - | 2.436 | 2.512 | 2.562 | 2.762 | 2.574 | - | - | - | **Anon-heroic** | -0.051 |
| MP | Marlowe | 2.103 | 2.149 | 2.206 | 2.152 | 2.228 | 2.203 | 2.113 | - | - | 2.368 | 2.508 | 2.496 | 2.800 | 2.484 | - | - | - | **Marlowe** | -0.050 |
| ST | Kyd | 2.219 | 2.228 | 2.269 | 2.225 | 2.293 | 2.318 | 2.210 | - | - | - | 2.554 | 2.555 | 2.844 | 2.548 | - | - | - | **Anon-heroic** | -0.007 |
| OWT | Peele | 2.342 | 2.312 | 2.325 | 2.305 | 2.329 | 2.412 | 2.303 | - | - | 2.625 | 2.707 | 2.515 | 2.743 | 2.648 | - | - | - | **Anon-heroic** | +0.037 |
| Gal | Lyly | 2.260 | 2.247 | 2.221 | 2.210 | 2.268 | 2.323 | 2.232 | - | - | 2.564 | 2.627 | 2.343 | 2.809 | 2.548 | - | - | - | **Sh-all** | +0.049 |
| AShrew | Anon-AShrew | 2.145 | 2.173 | 2.193 | 2.170 | 2.145 | 2.236 | 2.172 | - | - | 2.439 | 2.584 | 2.471 | - | 2.451 | - | - | - | **Greene** | -0.024 |
| TCKL | Anon-Leir | 2.186 | 2.146 | 2.171 | 2.134 | 2.214 | 2.270 | 2.131 | - | - | 2.397 | 2.544 | 2.421 | 2.668 | - | - | - | - | **Anon-heroic** | +0.052 |
| Alphonsus | Greene | 2.209 | 2.259 | 2.329 | 2.261 | 2.280 | 2.282 | 2.179 | - | - | 2.505 | 2.512 | 2.524 | 2.806 | 2.546 | - | - | - | **Anon-heroic** | -0.052 |
| Orlando | Greene | 2.327 | 2.419 | 2.468 | 2.424 | 2.413 | 2.419 | 2.350 | - | - | 2.637 | 2.665 | 2.681 | 2.951 | 2.788 | - | - | - | **Marlowe** | -0.097 |
| FriarBacon | Greene | 2.368 | 2.417 | 2.469 | 2.432 | 2.478 | 2.460 | 2.439 | - | - | 2.720 | 2.760 | 2.706 | 2.875 | 2.807 | - | - | - | **Marlowe** | -0.064 |
| JamesIV | Greene | 2.310 | 2.297 | 2.324 | 2.296 | 2.391 | 2.375 | 2.271 | - | - | 2.532 | 2.552 | 2.566 | 2.832 | 2.585 | - | - | - | **Anon-heroic** | +0.014 |
| Alcazar | Peele | 2.191 | 2.321 | 2.376 | 2.294 | 2.330 | 2.320 | 2.221 | - | - | 2.537 | 2.591 | 2.718 | 3.052 | 2.742 | - | - | - | **Marlowe** | -0.103 |
| EdwardI | Peele | 2.283 | 2.317 | 2.362 | 2.313 | 2.327 | 2.398 | 2.287 | - | - | 2.598 | 2.661 | 2.636 | 2.877 | 2.709 | - | - | - | **Marlowe** | -0.030 |
| David | Peele | 2.183 | 2.300 | 2.324 | 2.290 | 2.307 | 2.312 | 2.259 | - | - | 2.539 | 2.545 | 2.615 | 2.927 | 2.684 | - | - | - | **Marlowe** | -0.107 |
| Wounds | Lodge | 2.283 | 2.324 | 2.391 | 2.317 | 2.325 | 2.373 | 2.312 | - | - | 2.560 | - | 2.653 | 3.018 | 2.727 | - | - | - | **Marlowe** | -0.033 |
| Soliman | Anon-Soliman | 2.238 | 2.238 | 2.285 | 2.246 | 2.297 | 2.323 | 2.220 | - | - | - | 2.603 | 2.549 | 2.854 | 2.608 | - | - | - | **Anon-heroic** | -0.008 |
| Locrine | Anon-Locrine | 2.361 | 2.450 | 2.494 | 2.452 | 2.428 | 2.429 | 2.421 | - | - | 2.678 | 2.708 | 2.768 | 3.084 | 2.845 | - | - | - | **Marlowe** | -0.091 |
| Selimus | Anon-Selimus | 2.262 | 2.309 | 2.340 | 2.290 | 2.352 | 2.341 | 2.256 | - | - | 2.567 | 2.620 | 2.634 | 2.946 | 2.650 | - | - | - | **Anon-heroic** | -0.028 |
| TRKJ | Anon-TRKJ | 2.291 | 2.268 | 2.312 | 2.261 | 2.368 | 2.350 | 2.258 | - | - | 2.524 | 2.648 | 2.664 | 2.969 | 2.638 | - | - | - | **Anon-heroic** | +0.030 |
| JackStraw | Anon-JackStraw | 2.171 | 2.125 | 2.169 | 2.119 | 2.255 | 2.194 | 2.092 | - | - | 2.440 | 2.541 | 2.479 | 2.790 | 2.468 | - | - | - | **Anon-heroic** | +0.053 |
| EdwardIII | Anon-EdwardIII | 2.242 | 2.266 | 2.273 | 2.236 | 2.360 | 2.324 | 2.249 | - | - | 2.538 | 2.664 | 2.612 | 2.966 | 2.655 | - | - | - | **Sh-all** | +0.006 |
| Arden | Anon-Arden | 2.265 | 2.234 | 2.259 | 2.245 | 2.308 | 2.363 | 2.256 | - | - | 2.485 | 2.654 | 2.514 | 2.709 | 2.527 | - | - | - | **Sh-early** | +0.021 |
| TTR3 | Anon-TTR3 | 2.144 | 2.197 | 2.181 | 2.156 | 2.215 | 2.213 | 2.091 | - | - | 2.369 | 2.510 | 2.442 | 2.741 | 2.447 | - | - | - | **Anon-heroic** | -0.012 |
| Endymion | Lyly | 2.259 | 2.247 | 2.229 | 2.217 | 2.300 | 2.328 | 2.220 | - | - | 2.496 | 2.596 | 2.500 | 2.824 | 2.532 | - | - | - | **Sh-all** | +0.042 |

## Summary: mean cross-entropy gap (bits/char) for groups of held-out plays

Positive = the Marlowe model finds these plays *more* surprising than the Shakespeare model does.

| held-out group | H(Marlowe) − H(Sh-all) | H(Marlowe) − H(Sh-early) | H(Marlowe) − H(Sh-later) | H(Sh-early) − H(Sh-later) |
|---|---|---|---|---|
| Marlowe plays | -0.032 | -0.045 | -0.078 | -0.033 |
| Shakespeare early | +0.065 | +0.034 | +0.051 | +0.017 |
| Shakespeare early, Henry VI excluded | +0.089 | +0.072 | +0.077 | +0.005 |
| Henry VI 1-3 | +0.024 | -0.030 | +0.007 | +0.037 |
| Shakespeare later | +0.120 | +0.081 | +0.126 | +0.045 |
| early controls (Kyd, Peele, Lyly, A Shrew, Leir) | +0.022 | +0.009 | -0.006 | -0.015 |
| Greene | -0.049 | -0.044 | -0.094 | -0.050 |
| Peele | -0.051 | -0.063 | -0.097 | -0.034 |
| Lodge | -0.033 | -0.040 | -0.108 | -0.067 |
| anonymous heroic/history 1587-94 | -0.004 | -0.014 | -0.042 | -0.028 |

## Reading guide

* Same-author benchmark: how much lower is H under the author's own (other-plays) model than under a different author's? For Shakespeare-early plays, compare H(Sh-later) [same author, different period] with H(Marlowe) [the hypothesis]. If Marlowe wrote early Shakespeare, H(Marlowe) should be about as low as H(Sh-later) for those plays, and lower than it is for the control plays.

