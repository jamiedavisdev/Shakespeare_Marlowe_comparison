# Cross-entropy of each play under character-level author models (bits/char, lower = more predictable)

Order-6 Witten-Bell character models. Variant: masked (masked = proper nouns replaced by a placeholder, and plays sharing plot/characters excluded from training together). The held-out play is never in training. Marlowe, Sh-early, Sh-later, Sh-all, Greene, Peele and Anon-heroic models are truncated to 273,328 characters (= the smaller of the Greene and Peele corpora) so they are the same size, drawing an equal share of characters from each training play; Fletcher (3 plays), Ford (2) and the single-play controls are smaller, so their entropies are biased upward and are listed for reference only.

| held-out play | author | Marlowe | Sh-early | Sh-later | Sh-all | Greene | Peele | Anon-heroic | Fletcher | Ford | Kyd | Lodge | Lyly | Anon-AShrew | Anon-Leir | Dekker | Middleton | Beaumont | best size-matched model | Marlowe − Sh-all |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | 2.196 | 2.509 | 2.225 | 2.210 | 2.283 | 2.264 | 2.206 | - | - | 2.522 | 2.621 | 2.611 | 2.750 | 2.628 | - | - | - | **Marlowe** | -0.015 |
| 3H6 | Shakespeare | 2.197 | 2.436 | 2.249 | 2.226 | 2.280 | 2.269 | 2.164 | - | - | 2.443 | 2.562 | 2.576 | 2.831 | 2.561 | - | - | - | **Anon-heroic** | -0.030 |
| Tit | Shakespeare | 2.229 | 2.259 | 2.296 | 2.255 | 2.349 | 2.291 | 2.220 | - | - | 2.482 | 2.591 | 2.575 | 2.827 | 2.606 | - | - | - | **Anon-heroic** | -0.026 |
| R3 | Shakespeare | 2.260 | 2.507 | 2.216 | 2.212 | 2.341 | 2.324 | 2.223 | - | - | 2.519 | 2.635 | 2.595 | 2.874 | 2.587 | - | - | - | **Sh-all** | +0.049 |
| R2 | Shakespeare | 2.304 | 2.255 | 2.268 | 2.222 | 2.389 | 2.356 | 2.254 | - | - | 2.558 | 2.677 | 2.637 | 2.962 | 2.650 | - | - | - | **Sh-all** | +0.082 |
| Rom | Shakespeare | 2.363 | 2.334 | 2.280 | 2.272 | 2.394 | 2.441 | 2.331 | - | - | 2.610 | 2.731 | 2.597 | 2.831 | 2.650 | - | - | - | **Sh-all** | +0.092 |
| 1H4 | Shakespeare | 2.374 | 2.347 | 2.264 | 2.270 | 2.438 | 2.438 | 2.339 | - | - | 2.654 | 2.795 | 2.631 | 2.878 | 2.688 | - | - | - | **Sh-later** | +0.104 |
| LLL | Shakespeare | 2.514 | 2.522 | 2.394 | 2.400 | 2.541 | 2.597 | 2.468 | - | - | 2.773 | 2.879 | 2.686 | 3.013 | 2.786 | - | - | - | **Sh-later** | +0.114 |
| MND | Shakespeare | 2.409 | 2.421 | 2.322 | 2.336 | 2.442 | 2.474 | 2.387 | - | - | 2.654 | 2.742 | 2.590 | 2.868 | 2.693 | - | - | - | **Sh-later** | +0.073 |
| MV | Shakespeare | 2.318 | 2.330 | 2.205 | 2.220 | 2.378 | 2.410 | 2.289 | - | - | 2.591 | 2.712 | 2.544 | 2.792 | 2.579 | - | - | - | **Sh-later** | +0.098 |
| Ado | Shakespeare | 2.293 | 2.266 | 2.123 | 2.146 | 2.313 | 2.373 | 2.254 | - | - | 2.548 | 2.724 | 2.447 | 2.717 | 2.534 | - | - | - | **Sh-later** | +0.147 |
| 2H4 | Shakespeare | 2.403 | 2.353 | 2.258 | 2.259 | 2.466 | 2.441 | 2.352 | - | - | 2.682 | 2.795 | 2.668 | 2.876 | 2.740 | - | - | - | **Sh-later** | +0.144 |
| Lr | Shakespeare | 2.367 | 2.355 | 2.265 | 2.272 | 2.418 | 2.433 | 2.324 | - | - | 2.597 | 2.722 | 2.583 | 2.875 | 2.627 | - | - | - | **Sh-later** | +0.095 |
| Tro | Shakespeare | 2.424 | 2.449 | 2.331 | 2.342 | 2.505 | 2.513 | 2.408 | - | - | 2.699 | 2.786 | 2.679 | 2.940 | 2.748 | - | - | - | **Sh-later** | +0.082 |
| 1Tam | Marlowe | 2.312 | 2.407 | 2.436 | 2.365 | 2.323 | 2.275 | 2.291 | - | - | 2.624 | 2.625 | 2.695 | 3.014 | 2.754 | - | - | - | **Peele** | -0.053 |
| 2Tam | Marlowe | 2.310 | 2.414 | 2.415 | 2.362 | 2.356 | 2.294 | 2.322 | - | - | 2.628 | 2.665 | 2.707 | 2.999 | 2.799 | - | - | - | **Peele** | -0.052 |
| Dido | Marlowe | 2.284 | 2.376 | 2.405 | 2.357 | 2.349 | 2.382 | 2.328 | - | - | 2.592 | 2.633 | 2.623 | 2.867 | 2.706 | - | - | - | **Marlowe** | -0.073 |
| DrFaust | Marlowe | 2.336 | 2.416 | 2.367 | 2.334 | 2.366 | 2.416 | 2.356 | - | - | 2.634 | 2.784 | 2.638 | 2.882 | 2.748 | - | - | - | **Sh-all** | +0.002 |
| JoM | Marlowe | 2.276 | 2.310 | 2.297 | 2.272 | 2.365 | 2.370 | 2.273 | - | - | 2.502 | 2.677 | 2.599 | 2.778 | 2.569 | - | - | - | **Sh-all** | +0.004 |
| Ed2 | Marlowe | 2.150 | 2.113 | 2.206 | 2.133 | 2.231 | 2.195 | 2.145 | - | - | 2.436 | 2.512 | 2.562 | 2.762 | 2.574 | - | - | - | **Sh-early** | +0.017 |
| MP | Marlowe | 2.103 | 2.137 | 2.234 | 2.151 | 2.228 | 2.203 | 2.113 | - | - | 2.368 | 2.508 | 2.496 | 2.800 | 2.484 | - | - | - | **Marlowe** | -0.048 |
| ST | Kyd | 2.219 | 2.244 | 2.285 | 2.244 | 2.293 | 2.318 | 2.210 | - | - | - | 2.554 | 2.555 | 2.844 | 2.548 | - | - | - | **Anon-heroic** | -0.025 |
| OWT | Peele | 2.342 | 2.357 | 2.297 | 2.291 | 2.329 | 2.412 | 2.303 | - | - | 2.625 | 2.707 | 2.515 | 2.743 | 2.648 | - | - | - | **Sh-all** | +0.051 |
| Gal | Lyly | 2.260 | 2.317 | 2.231 | 2.220 | 2.268 | 2.323 | 2.232 | - | - | 2.564 | 2.627 | 2.343 | 2.809 | 2.548 | - | - | - | **Sh-all** | +0.040 |
| AShrew | Anon-AShrew | 2.145 | 2.181 | 2.166 | 2.141 | 2.145 | 2.236 | 2.172 | - | - | 2.439 | 2.584 | 2.471 | - | 2.451 | - | - | - | **Sh-all** | +0.004 |
| TCKL | Anon-Leir | 2.186 | 2.192 | 2.171 | 2.149 | 2.214 | 2.270 | 2.131 | - | - | 2.397 | 2.544 | 2.421 | 2.668 | - | - | - | - | **Anon-heroic** | +0.037 |
| Alphonsus | Greene | 2.209 | 2.284 | 2.341 | 2.276 | 2.280 | 2.282 | 2.179 | - | - | 2.505 | 2.512 | 2.524 | 2.806 | 2.546 | - | - | - | **Anon-heroic** | -0.066 |
| Orlando | Greene | 2.327 | 2.453 | 2.460 | 2.415 | 2.413 | 2.419 | 2.350 | - | - | 2.637 | 2.665 | 2.681 | 2.951 | 2.788 | - | - | - | **Marlowe** | -0.088 |
| FriarBacon | Greene | 2.368 | 2.471 | 2.447 | 2.397 | 2.478 | 2.460 | 2.439 | - | - | 2.720 | 2.760 | 2.706 | 2.875 | 2.807 | - | - | - | **Marlowe** | -0.028 |
| JamesIV | Greene | 2.310 | 2.319 | 2.310 | 2.288 | 2.391 | 2.375 | 2.271 | - | - | 2.532 | 2.552 | 2.566 | 2.832 | 2.585 | - | - | - | **Anon-heroic** | +0.022 |
| Alcazar | Peele | 2.191 | 2.298 | 2.392 | 2.290 | 2.330 | 2.320 | 2.221 | - | - | 2.537 | 2.591 | 2.718 | 3.052 | 2.742 | - | - | - | **Marlowe** | -0.099 |
| EdwardI | Peele | 2.283 | 2.298 | 2.338 | 2.283 | 2.327 | 2.398 | 2.287 | - | - | 2.598 | 2.661 | 2.636 | 2.877 | 2.709 | - | - | - | **Marlowe** | -0.000 |
| David | Peele | 2.183 | 2.271 | 2.325 | 2.266 | 2.307 | 2.312 | 2.259 | - | - | 2.539 | 2.545 | 2.615 | 2.927 | 2.684 | - | - | - | **Marlowe** | -0.083 |
| Wounds | Lodge | 2.283 | 2.335 | 2.430 | 2.338 | 2.325 | 2.373 | 2.312 | - | - | 2.560 | - | 2.653 | 3.018 | 2.727 | - | - | - | **Marlowe** | -0.055 |
| Soliman | Anon-Soliman | 2.238 | 2.278 | 2.290 | 2.258 | 2.297 | 2.323 | 2.220 | - | - | - | 2.603 | 2.549 | 2.854 | 2.608 | - | - | - | **Anon-heroic** | -0.020 |
| Locrine | Anon-Locrine | 2.361 | 2.475 | 2.510 | 2.450 | 2.428 | 2.429 | 2.421 | - | - | 2.678 | 2.708 | 2.768 | 3.084 | 2.845 | - | - | - | **Marlowe** | -0.089 |
| Selimus | Anon-Selimus | 2.262 | 2.315 | 2.367 | 2.305 | 2.352 | 2.341 | 2.256 | - | - | 2.567 | 2.620 | 2.634 | 2.946 | 2.650 | - | - | - | **Anon-heroic** | -0.043 |
| TRKJ | Anon-TRKJ | 2.291 | 2.267 | 2.327 | 2.269 | 2.368 | 2.350 | 2.258 | - | - | 2.524 | 2.648 | 2.664 | 2.969 | 2.638 | - | - | - | **Anon-heroic** | +0.022 |
| JackStraw | Anon-JackStraw | 2.171 | 2.142 | 2.171 | 2.128 | 2.255 | 2.194 | 2.092 | - | - | 2.440 | 2.541 | 2.479 | 2.790 | 2.468 | - | - | - | **Anon-heroic** | +0.043 |
| EdwardIII | Anon-EdwardIII | 2.242 | 2.260 | 2.271 | 2.230 | 2.360 | 2.324 | 2.249 | - | - | 2.538 | 2.664 | 2.612 | 2.966 | 2.655 | - | - | - | **Sh-all** | +0.013 |
| Arden | Anon-Arden | 2.265 | 2.259 | 2.242 | 2.224 | 2.308 | 2.363 | 2.256 | - | - | 2.485 | 2.654 | 2.514 | 2.709 | 2.527 | - | - | - | **Sh-all** | +0.042 |
| TTR3 | Anon-TTR3 | 2.144 | 2.421 | 2.175 | 2.159 | 2.215 | 2.213 | 2.091 | - | - | 2.369 | 2.510 | 2.442 | 2.741 | 2.447 | - | - | - | **Anon-heroic** | -0.015 |
| Endymion | Lyly | 2.259 | 2.307 | 2.219 | 2.212 | 2.300 | 2.328 | 2.220 | - | - | 2.496 | 2.596 | 2.500 | 2.824 | 2.532 | - | - | - | **Sh-all** | +0.046 |

## Summary: mean cross-entropy gap (bits/char) for groups of held-out plays

Positive = the Marlowe model finds these plays *more* surprising than the Shakespeare model does.

| held-out group | H(Marlowe) − H(Sh-all) | H(Marlowe) − H(Sh-early) | H(Marlowe) − H(Sh-later) | H(Sh-early) − H(Sh-later) |
|---|---|---|---|---|
| Marlowe plays | -0.029 | -0.057 | -0.084 | -0.027 |
| Shakespeare early | -0.005 | -0.207 | -0.026 | +0.181 |
| Shakespeare early, Henry VI excluded | +0.012 | -0.138 | -0.011 | +0.127 |
| Henry VI 1-3 | -0.022 | -0.276 | -0.041 | +0.236 |
| Shakespeare later | +0.103 | +0.014 | +0.106 | +0.092 |
| early controls (Kyd, Peele, Lyly, A Shrew, Leir) | +0.021 | -0.028 | +0.000 | +0.029 |
| Greene | -0.040 | -0.078 | -0.086 | -0.008 |
| Peele | -0.033 | -0.056 | -0.088 | -0.032 |
| Lodge | -0.055 | -0.051 | -0.147 | -0.096 |
| anonymous heroic/history 1587-94 | -0.006 | -0.055 | -0.047 | +0.008 |

## Reading guide

* Same-author benchmark: how much lower is H under the author's own (other-plays) model than under a different author's? For Shakespeare-early plays, compare H(Sh-later) [same author, different period] with H(Marlowe) [the hypothesis]. If Marlowe wrote early Shakespeare, H(Marlowe) should be about as low as H(Sh-later) for those plays, and lower than it is for the control plays.

