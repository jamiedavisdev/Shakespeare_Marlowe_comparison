# Cross-entropy of each play under character-level author models (bits/char, lower = more predictable)

Order-6 Witten-Bell character models. Variant: plain (masked = proper nouns replaced by a placeholder, and plays sharing plot/characters excluded from training together). The held-out play is never in training. Marlowe, Sh-early, Sh-later, Sh-all, Greene, Peele and Anon-heroic models are truncated to 284,531 characters (= the smaller of the Greene and Peele corpora) so they are the same size, drawing an equal share of characters from each training play; Fletcher (3 plays), Ford (2) and the single-play controls are smaller, so their entropies are biased upward and are listed for reference only.

| held-out play | author | Marlowe | Sh-early | Sh-later | Sh-all | Greene | Peele | Anon-heroic | Fletcher | Ford | Kyd | Lodge | Lyly | Anon-AShrew | Anon-Leir | Dekker | Middleton | Beaumont | best size-matched model | Marlowe − Sh-all |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | 2.342 | 2.216 | 2.330 | 2.230 | 2.445 | 2.448 | 2.278 | - | - | 2.660 | 2.831 | 2.798 | 3.014 | 2.750 | - | - | - | **Sh-early** | +0.112 |
| 3H6 | Shakespeare | 2.258 | 2.148 | 2.295 | 2.168 | 2.360 | 2.377 | 2.186 | - | - | 2.593 | 2.759 | 2.768 | 2.998 | 2.697 | - | - | - | **Sh-early** | +0.090 |
| 1H6 | Shakespeare | 2.331 | 2.246 | 2.356 | 2.244 | 2.434 | 2.462 | 2.293 | - | - | 2.673 | 2.806 | 2.798 | 3.090 | 2.741 | - | - | - | **Sh-all** | +0.087 |
| Tit | Shakespeare | 2.329 | 2.340 | 2.358 | 2.320 | 2.450 | 2.414 | 2.331 | - | - | 2.612 | 2.685 | 2.731 | 2.921 | 2.732 | - | - | - | **Sh-all** | +0.010 |
| R3 | Shakespeare | 2.328 | 2.184 | 2.237 | 2.185 | 2.413 | 2.380 | 2.212 | - | - | 2.597 | 2.753 | 2.707 | 2.964 | 2.650 | - | - | - | **Sh-early** | +0.143 |
| Shr | Shakespeare | 2.467 | 2.365 | 2.348 | 2.342 | 2.459 | 2.539 | 2.450 | - | - | 2.711 | 2.861 | 2.694 | 2.751 | 2.719 | - | - | - | **Sh-all** | +0.125 |
| TGV | Shakespeare | 2.311 | 2.226 | 2.221 | 2.204 | 2.354 | 2.402 | 2.278 | - | - | 2.570 | 2.708 | 2.532 | 2.767 | 2.589 | - | - | - | **Sh-all** | +0.107 |
| Err | Shakespeare | 2.373 | 2.289 | 2.263 | 2.274 | 2.422 | 2.453 | 2.318 | - | - | 2.632 | 2.785 | 2.630 | 2.794 | 2.654 | - | - | - | **Sh-later** | +0.098 |
| R2 | Shakespeare | 2.375 | 2.249 | 2.267 | 2.228 | 2.468 | 2.435 | 2.310 | - | - | 2.634 | 2.798 | 2.753 | 3.021 | 2.715 | - | - | - | **Sh-all** | +0.147 |
| MND | Shakespeare | 2.502 | 2.448 | 2.413 | 2.421 | 2.552 | 2.611 | 2.534 | - | - | 2.794 | 2.871 | 2.716 | 2.953 | 2.827 | - | - | - | **Sh-later** | +0.081 |
| Rom | Shakespeare | 2.475 | 2.378 | 2.359 | 2.349 | 2.512 | 2.535 | 2.429 | - | - | 2.727 | 2.857 | 2.708 | 2.937 | 2.761 | - | - | - | **Sh-all** | +0.125 |
| MV | Shakespeare | 2.375 | 2.297 | 2.269 | 2.265 | 2.443 | 2.483 | 2.364 | - | - | 2.654 | 2.796 | 2.615 | 2.853 | 2.654 | - | - | - | **Sh-all** | +0.110 |
| 1H4 | Shakespeare | 2.441 | 2.346 | 2.329 | 2.307 | 2.519 | 2.505 | 2.404 | - | - | 2.751 | 2.906 | 2.740 | 2.951 | 2.761 | - | - | - | **Sh-all** | +0.134 |
| JC | Shakespeare | 2.392 | 2.341 | 2.389 | 2.271 | 2.453 | 2.475 | 2.345 | - | - | 2.740 | 2.722 | 2.738 | 2.907 | 2.806 | - | - | - | **Sh-all** | +0.121 |
| Ham | Shakespeare | 2.423 | 2.360 | 2.280 | 2.297 | 2.499 | 2.508 | 2.407 | - | - | 2.664 | 2.837 | 2.698 | 2.913 | 2.698 | - | - | - | **Sh-later** | +0.126 |
| Mac | Shakespeare | 2.456 | 2.397 | 2.307 | 2.332 | 2.539 | 2.545 | 2.446 | - | - | 2.725 | 2.851 | 2.752 | 3.000 | 2.776 | - | - | - | **Sh-later** | +0.123 |
| Lr | Shakespeare | 2.398 | 2.305 | 2.247 | 2.259 | 2.469 | 2.473 | 2.360 | - | - | 2.641 | 2.791 | 2.649 | 2.899 | 2.659 | - | - | - | **Sh-later** | +0.139 |
| WT | Shakespeare | 2.395 | 2.315 | 2.251 | 2.265 | 2.465 | 2.495 | 2.386 | - | - | 2.673 | 2.822 | 2.652 | 2.902 | 2.650 | - | - | - | **Sh-later** | +0.130 |
| Tmp | Shakespeare | 2.486 | 2.433 | 2.362 | 2.368 | 2.566 | 2.590 | 2.488 | - | - | 2.786 | 2.931 | 2.751 | 3.001 | 2.791 | - | - | - | **Sh-later** | +0.118 |
| 1Tam | Marlowe | 2.130 | 2.421 | 2.492 | 2.415 | 2.344 | 2.334 | 2.327 | - | - | 2.708 | 2.715 | 2.790 | 3.065 | 2.828 | - | - | - | **Marlowe** | -0.285 |
| 2Tam | Marlowe | 2.179 | 2.413 | 2.453 | 2.396 | 2.378 | 2.336 | 2.354 | - | - | 2.678 | 2.747 | 2.775 | 3.047 | 2.849 | - | - | - | **Marlowe** | -0.217 |
| Dido | Marlowe | 2.478 | 2.500 | 2.472 | 2.454 | 2.507 | 2.564 | 2.521 | - | - | 2.773 | 2.811 | 2.832 | 3.018 | 2.816 | - | - | - | **Sh-all** | +0.024 |
| DrFaust | Marlowe | 2.465 | 2.493 | 2.495 | 2.458 | 2.462 | 2.552 | 2.482 | - | - | 2.773 | 2.925 | 2.791 | 2.975 | 2.877 | - | - | - | **Sh-all** | +0.007 |
| JoM | Marlowe | 2.394 | 2.384 | 2.404 | 2.378 | 2.501 | 2.475 | 2.381 | - | - | 2.646 | 2.823 | 2.732 | 2.899 | 2.722 | - | - | - | **Sh-all** | +0.015 |
| Ed2 | Marlowe | 2.269 | 2.171 | 2.257 | 2.178 | 2.327 | 2.241 | 2.169 | - | - | 2.499 | 2.614 | 2.681 | 2.857 | 2.600 | - | - | - | **Anon-heroic** | +0.091 |
| MP | Marlowe | 2.157 | 2.181 | 2.262 | 2.198 | 2.287 | 2.266 | 2.171 | - | - | 2.461 | 2.631 | 2.609 | 2.832 | 2.541 | - | - | - | **Marlowe** | -0.041 |
| ST | Kyd | 2.383 | 2.348 | 2.411 | 2.343 | 2.461 | 2.483 | 2.361 | - | - | - | 2.744 | 2.746 | 2.992 | 2.707 | - | - | - | **Sh-all** | +0.041 |
| OWT | Peele | 2.393 | 2.357 | 2.345 | 2.332 | 2.388 | 2.471 | 2.355 | - | - | 2.686 | 2.774 | 2.566 | 2.789 | 2.684 | - | - | - | **Sh-all** | +0.061 |
| Gal | Lyly | 2.302 | 2.329 | 2.264 | 2.263 | 2.332 | 2.387 | 2.322 | - | - | 2.651 | 2.708 | 2.437 | 2.869 | 2.648 | - | - | - | **Sh-all** | +0.039 |
| AShrew | Anon-AShrew | 2.214 | 2.202 | 2.249 | 2.199 | 2.221 | 2.313 | 2.237 | - | - | 2.501 | 2.656 | 2.544 | - | 2.500 | - | - | - | **Sh-all** | +0.015 |
| TCKL | Anon-Leir | 2.208 | 2.177 | 2.194 | 2.156 | 2.245 | 2.291 | 2.157 | - | - | 2.437 | 2.587 | 2.473 | 2.694 | - | - | - | - | **Sh-all** | +0.052 |
| Alphonsus | Greene | 2.338 | 2.387 | 2.512 | 2.380 | 2.455 | 2.451 | 2.333 | - | - | 2.668 | 2.690 | 2.700 | 2.947 | 2.731 | - | - | - | **Anon-heroic** | -0.042 |
| Orlando | Greene | 2.436 | 2.560 | 2.575 | 2.545 | 2.568 | 2.553 | 2.500 | - | - | 2.792 | 2.858 | 2.846 | 3.062 | 2.926 | - | - | - | **Marlowe** | -0.110 |
| FriarBacon | Greene | 2.483 | 2.502 | 2.574 | 2.516 | 2.619 | 2.573 | 2.546 | - | - | 2.868 | 2.946 | 2.875 | 3.027 | 2.928 | - | - | - | **Marlowe** | -0.033 |
| JamesIV | Greene | 2.346 | 2.310 | 2.336 | 2.309 | 2.429 | 2.409 | 2.298 | - | - | 2.572 | 2.612 | 2.628 | 2.871 | 2.608 | - | - | - | **Anon-heroic** | +0.037 |
| Alcazar | Peele | 2.294 | 2.434 | 2.501 | 2.423 | 2.490 | 2.494 | 2.335 | - | - | 2.642 | 2.770 | 2.900 | 3.169 | 2.875 | - | - | - | **Marlowe** | -0.129 |
| EdwardI | Peele | 2.356 | 2.314 | 2.395 | 2.329 | 2.390 | 2.509 | 2.324 | - | - | 2.697 | 2.805 | 2.782 | 2.992 | 2.766 | - | - | - | **Sh-early** | +0.027 |
| David | Peele | 2.363 | 2.500 | 2.518 | 2.485 | 2.555 | 2.480 | 2.437 | - | - | 2.722 | 2.777 | 2.810 | 3.093 | 2.800 | - | - | - | **Marlowe** | -0.122 |
| Wounds | Lodge | 2.389 | 2.405 | 2.454 | 2.392 | 2.438 | 2.496 | 2.434 | - | - | 2.703 | - | 2.809 | 3.137 | 2.857 | - | - | - | **Marlowe** | -0.004 |
| Soliman | Anon-Soliman | 2.328 | 2.368 | 2.410 | 2.371 | 2.399 | 2.439 | 2.334 | - | - | 2.464 | 2.732 | 2.686 | 2.971 | 2.745 | - | - | - | **Marlowe** | -0.043 |
| Locrine | Anon-Locrine | 2.430 | 2.507 | 2.556 | 2.506 | 2.509 | 2.517 | 2.519 | - | - | 2.766 | 2.805 | 2.858 | 3.161 | 2.926 | - | - | - | **Marlowe** | -0.076 |
| Selimus | Anon-Selimus | 2.367 | 2.494 | 2.537 | 2.475 | 2.499 | 2.538 | 2.438 | - | - | 2.733 | 2.816 | 2.825 | 3.087 | 2.815 | - | - | - | **Marlowe** | -0.108 |
| TRKJ | Anon-TRKJ | 2.349 | 2.298 | 2.371 | 2.291 | 2.433 | 2.388 | 2.296 | - | - | 2.633 | 2.783 | 2.798 | 3.043 | 2.732 | - | - | - | **Sh-all** | +0.058 |
| JackStraw | Anon-JackStraw | 2.194 | 2.129 | 2.175 | 2.133 | 2.270 | 2.187 | 2.091 | - | - | 2.465 | 2.594 | 2.541 | 2.806 | 2.482 | - | - | - | **Anon-heroic** | +0.061 |
| EdwardIII | Anon-EdwardIII | 2.251 | 2.228 | 2.275 | 2.211 | 2.363 | 2.340 | 2.252 | - | - | 2.580 | 2.726 | 2.669 | 2.996 | 2.662 | - | - | - | **Sh-all** | +0.040 |
| Arden | Anon-Arden | 2.339 | 2.295 | 2.329 | 2.311 | 2.384 | 2.432 | 2.332 | - | - | 2.573 | 2.751 | 2.595 | 2.781 | 2.620 | - | - | - | **Sh-early** | +0.028 |
| TTR3 | Anon-TTR3 | 2.203 | 2.098 | 2.219 | 2.120 | 2.275 | 2.245 | 2.128 | - | - | 2.455 | 2.635 | 2.579 | 2.802 | 2.520 | - | - | - | **Sh-early** | +0.084 |
| Endymion | Lyly | 2.387 | 2.418 | 2.396 | 2.385 | 2.419 | 2.461 | 2.367 | - | - | 2.668 | 2.762 | 2.650 | 2.967 | 2.689 | - | - | - | **Anon-heroic** | +0.001 |

## Summary: mean cross-entropy gap (bits/char) for groups of held-out plays

Positive = the Marlowe model finds these plays *more* surprising than the Shakespeare model does.

| held-out group | H(Marlowe) − H(Sh-all) | H(Marlowe) − H(Sh-early) | H(Marlowe) − H(Sh-later) | H(Sh-early) − H(Sh-later) |
|---|---|---|---|---|
| Marlowe plays | -0.058 | -0.070 | -0.109 | -0.039 |
| Shakespeare early | +0.097 | +0.091 | +0.041 | -0.049 |
| Shakespeare early, Henry VI excluded | +0.097 | +0.081 | +0.076 | -0.005 |
| Henry VI 1-3 | +0.096 | +0.107 | -0.017 | -0.123 |
| Shakespeare later | +0.123 | +0.077 | +0.113 | +0.036 |
| early controls (Kyd, Peele, Lyly, A Shrew, Leir) | +0.041 | +0.017 | +0.007 | -0.010 |
| Greene | -0.037 | -0.039 | -0.099 | -0.060 |
| Peele | -0.041 | -0.050 | -0.088 | -0.038 |
| Lodge | -0.004 | -0.016 | -0.066 | -0.049 |
| anonymous heroic/history 1587-94 | +0.006 | +0.006 | -0.051 | -0.057 |

## Reading guide

* Same-author benchmark: how much lower is H under the author's own (other-plays) model than under a different author's? For Shakespeare-early plays, compare H(Sh-later) [same author, different period] with H(Marlowe) [the hypothesis]. If Marlowe wrote early Shakespeare, H(Marlowe) should be about as low as H(Sh-later) for those plays, and lower than it is for the control plays.

