# Affinity (double-centred cross-entropy, bits/char), variant = masked

Negative = the play is specifically well predicted by that author model, after removing each model's overall predictiveness and each play's overall predictability. Each row sums to zero.

| play | author | group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) | strongest affinity |
|---|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | shakespeare_early | -0.051 | +0.208 | -0.042 | -0.029 | -0.056 | -0.030 | **Peele** |
| 3H6 | Shakespeare | shakespeare_early | -0.036 | +0.150 | -0.003 | -0.017 | -0.037 | -0.058 | **Anon-heroic** |
| Tit | Shakespeare | shakespeare_early | -0.011 | -0.035 | +0.035 | +0.044 | -0.023 | -0.009 | **Sh-early** |
| R3 | Shakespeare | shakespeare_early | -0.018 | +0.175 | -0.082 | -0.002 | -0.028 | -0.045 | **Sh-later** |
| R2 | Shakespeare | shakespeare_later | +0.033 | -0.070 | -0.022 | +0.053 | +0.012 | -0.005 | **Sh-early** |
| Rom | Shakespeare | shakespeare_later | +0.039 | -0.043 | -0.064 | +0.006 | +0.044 | +0.018 | **Sh-later** |
| 1H4 | Shakespeare | shakespeare_later | +0.040 | -0.040 | -0.089 | +0.040 | +0.031 | +0.017 | **Sh-later** |
| LLL | Shakespeare | shakespeare_later | +0.042 | -0.004 | -0.099 | +0.004 | +0.051 | +0.006 | **Sh-later** |
| MND | Shakespeare | shakespeare_later | +0.033 | -0.008 | -0.074 | +0.002 | +0.025 | +0.023 | **Sh-later** |
| MV | Shakespeare | shakespeare_later | +0.029 | -0.012 | -0.104 | +0.025 | +0.049 | +0.012 | **Sh-later** |
| Ado | Shakespeare | shakespeare_later | +0.056 | -0.025 | -0.134 | +0.011 | +0.062 | +0.029 | **Sh-later** |
| 2H4 | Shakespeare | shakespeare_later | +0.058 | -0.046 | -0.107 | +0.056 | +0.022 | +0.018 | **Sh-later** |
| Lr | Shakespeare | shakespeare_later | +0.040 | -0.026 | -0.082 | +0.027 | +0.033 | +0.008 | **Sh-later** |
| Tro | Shakespeare | shakespeare_later | +0.019 | -0.010 | -0.094 | +0.035 | +0.034 | +0.015 | **Sh-later** |
| 1Tam | Marlowe | marlowe | +0.005 | +0.046 | +0.108 | -0.049 | -0.106 | -0.005 | **Peele** |
| 2Tam | Marlowe | marlowe | -0.008 | +0.042 | +0.077 | -0.027 | -0.098 | +0.015 | **Peele** |
| Dido | Marlowe | marlowe | -0.036 | +0.002 | +0.064 | -0.036 | -0.012 | +0.018 | **Marlowe** |
| DrFaust | Marlowe | marlowe | -0.007 | +0.020 | +0.004 | -0.042 | -0.000 | +0.025 | **Greene** |
| JoM | Marlowe | marlowe | -0.005 | -0.025 | -0.005 | +0.019 | +0.015 | +0.002 | **Sh-early** |
| Ed2 | Marlowe | marlowe | +0.010 | -0.080 | +0.046 | +0.026 | -0.018 | +0.017 | **Sh-early** |
| MP | Marlowe | marlowe | -0.034 | -0.053 | +0.078 | +0.027 | -0.007 | -0.012 | **Sh-early** |
| ST | Kyd | control | -0.010 | -0.038 | +0.037 | +0.001 | +0.017 | -0.007 | **Sh-early** |
| OWT | Peele | control | +0.035 | -0.003 | -0.029 | -0.042 | +0.032 | +0.008 | **Greene** |
| Gal | Lyly | control | +0.021 | +0.026 | -0.028 | -0.035 | +0.011 | +0.005 | **Greene** |
| AShrew | Anon-AShrew | control | +0.004 | -0.013 | +0.005 | -0.060 | +0.022 | +0.042 | **Greene** |
| TCKL | Anon-Leir | control | +0.025 | -0.022 | -0.010 | -0.011 | +0.036 | -0.019 | **Sh-early** |
| Alphonsus | Greene | control_ep | -0.020 | +0.001 | +0.092 | -0.013 | -0.021 | -0.039 | **Anon-heroic** |
| Orlando | Greene | control_ep | -0.043 | +0.030 | +0.069 | -0.022 | -0.025 | -0.008 | **Marlowe** |
| FriarBacon | Greene | control_ep | -0.042 | +0.007 | +0.017 | +0.003 | -0.024 | +0.040 | **Marlowe** |
| JamesIV | Greene | control_ep | +0.014 | -0.030 | -0.006 | +0.030 | +0.005 | -0.014 | **Sh-early** |
| Alcazar | Peele | control_ep | -0.068 | -0.014 | +0.113 | +0.007 | -0.012 | -0.026 | **Marlowe** |
| EdwardI | Peele | control_ep | -0.005 | -0.044 | +0.030 | -0.026 | +0.036 | +0.010 | **Sh-early** |
| David | Peele | control_ep | -0.060 | -0.025 | +0.062 | +0.000 | -0.005 | +0.028 | **Marlowe** |
| Wounds | Lodge | control_ep | -0.026 | -0.028 | +0.101 | -0.049 | -0.010 | +0.013 | **Greene** |
| Soliman | Anon-Soliman | control_ep | -0.003 | -0.016 | +0.030 | -0.009 | +0.008 | -0.010 | **Sh-early** |
| Locrine | Anon-Locrine | control_ep | -0.043 | +0.018 | +0.086 | -0.041 | -0.048 | +0.028 | **Peele** |
| Selimus | Anon-Selimus | control_ep | -0.020 | -0.021 | +0.065 | +0.006 | -0.015 | -0.015 | **Sh-early** |
| TRKJ | Anon-TRKJ | control_ep | +0.014 | -0.063 | +0.031 | +0.027 | -0.001 | -0.007 | **Sh-early** |
| JackStraw | Anon-JackStraw | control_ep | +0.034 | -0.049 | +0.013 | +0.053 | -0.017 | -0.034 | **Sh-early** |
| EdwardIII | Anon-EdwardIII | control_ep | -0.009 | -0.045 | +0.000 | +0.045 | -0.000 | +0.009 | **Sh-early** |
| Arden | Anon-Arden | control_ep | +0.016 | -0.043 | -0.027 | -0.005 | +0.041 | +0.018 | **Sh-early** |
| TTR3 | Anon-TTR3 | control_ep | -0.033 | +0.191 | -0.021 | -0.026 | -0.037 | -0.074 | **Anon-heroic** |
| Endymion | Lyly | control_ep | +0.020 | +0.015 | -0.040 | -0.003 | +0.016 | -0.008 | **Sh-later** |

## Group means

| group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) |
|---|---|---|---|---|---|---|
| Marlowe plays | -0.011 | -0.007 | +0.053 | -0.012 | -0.032 | +0.009 |
| Shakespeare early | -0.029 | +0.125 | -0.023 | -0.001 | -0.036 | -0.035 |
|   of which Henry VI 1-3 | -0.044 | +0.179 | -0.023 | -0.023 | -0.047 | -0.044 |
|   of which Tit, R3, Shr, TGV, Err | -0.015 | +0.070 | -0.024 | +0.021 | -0.025 | -0.027 |
| Shakespeare later | +0.039 | -0.028 | -0.087 | +0.026 | +0.036 | +0.014 |
| early controls | +0.015 | -0.010 | -0.005 | -0.030 | +0.023 | +0.006 |
| Greene | -0.023 | +0.002 | +0.043 | -0.001 | -0.016 | -0.005 |
| Peele | -0.024 | -0.021 | +0.044 | -0.015 | +0.013 | +0.005 |
| anonymous heroic 1587-94 | -0.005 | -0.004 | +0.022 | +0.006 | -0.008 | -0.011 |
| Lodge, Lyly Endymion | -0.003 | -0.007 | +0.030 | -0.026 | +0.003 | +0.003 |
