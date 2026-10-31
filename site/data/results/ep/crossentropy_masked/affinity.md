# Affinity (double-centred cross-entropy, bits/char), variant = masked

Negative = the play is specifically well predicted by that author model, after removing each model's overall predictiveness and each play's overall predictability. Each row sums to zero.

| play | author | group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) | strongest affinity |
|---|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | shakespeare_early | -0.004 | +0.021 | -0.033 | +0.023 | +0.011 | -0.018 | **Sh-later** |
| 3H6 | Shakespeare | shakespeare_early | -0.010 | +0.021 | -0.005 | +0.021 | +0.003 | -0.031 | **Anon-heroic** |
| 1H6 | Shakespeare | shakespeare_early | -0.016 | +0.038 | -0.011 | +0.013 | +0.014 | -0.037 | **Anon-heroic** |
| Tit | Shakespeare | shakespeare_early | -0.003 | -0.033 | +0.011 | +0.041 | -0.020 | +0.004 | **Sh-early** |
| R3 | Shakespeare | shakespeare_early | +0.025 | -0.011 | -0.062 | +0.043 | +0.021 | -0.016 | **Sh-later** |
| Shr | Shakespeare | shakespeare_early | +0.058 | -0.043 | -0.050 | -0.025 | +0.034 | +0.026 | **Sh-later** |
| TGV | Shakespeare | shakespeare_early | +0.041 | -0.043 | -0.054 | -0.002 | +0.053 | +0.006 | **Sh-later** |
| Err | Shakespeare | shakespeare_early | +0.042 | -0.036 | -0.063 | +0.019 | +0.039 | -0.001 | **Sh-later** |
| R2 | Shakespeare | shakespeare_later | +0.030 | -0.049 | -0.047 | +0.048 | +0.018 | +0.001 | **Sh-early** |
| MND | Shakespeare | shakespeare_later | +0.041 | -0.040 | -0.074 | +0.005 | +0.030 | +0.037 | **Sh-later** |
| Rom | Shakespeare | shakespeare_later | +0.038 | -0.041 | -0.071 | +0.023 | +0.035 | +0.017 | **Sh-later** |
| MV | Shakespeare | shakespeare_later | +0.031 | -0.038 | -0.070 | +0.029 | +0.037 | +0.012 | **Sh-later** |
| 1H4 | Shakespeare | shakespeare_later | +0.032 | -0.046 | -0.085 | +0.040 | +0.036 | +0.023 | **Sh-later** |
| JC | Shakespeare | shakespeare_later | +0.027 | -0.034 | -0.072 | +0.030 | +0.036 | +0.014 | **Sh-later** |
| Ham | Shakespeare | shakespeare_later | +0.038 | -0.029 | -0.118 | +0.044 | +0.045 | +0.020 | **Sh-later** |
| Mac | Shakespeare | shakespeare_later | +0.031 | -0.038 | -0.114 | +0.046 | +0.046 | +0.029 | **Sh-later** |
| Lr | Shakespeare | shakespeare_later | +0.046 | -0.039 | -0.112 | +0.041 | +0.048 | +0.016 | **Sh-later** |
| WT | Shakespeare | shakespeare_later | +0.043 | -0.048 | -0.117 | +0.042 | +0.054 | +0.026 | **Sh-later** |
| Tmp | Shakespeare | shakespeare_later | +0.029 | -0.033 | -0.112 | +0.037 | +0.050 | +0.029 | **Sh-later** |
| 1Tam | Marlowe | marlowe | -0.003 | +0.077 | +0.109 | -0.057 | -0.118 | -0.009 | **Peele** |
| 2Tam | Marlowe | marlowe | -0.016 | +0.077 | +0.075 | -0.035 | -0.111 | +0.010 | **Peele** |
| Dido | Marlowe | marlowe | -0.037 | +0.017 | +0.055 | -0.038 | -0.018 | +0.020 | **Greene** |
| DrFaust | Marlowe | marlowe | -0.010 | +0.015 | +0.026 | -0.046 | -0.008 | +0.024 | **Greene** |
| JoM | Marlowe | marlowe | -0.007 | -0.022 | -0.001 | +0.017 | +0.009 | +0.004 | **Sh-early** |
| Ed2 | Marlowe | marlowe | -0.027 | +0.040 | +0.076 | -0.012 | -0.060 | -0.017 | **Peele** |
| MP | Marlowe | marlowe | -0.044 | +0.009 | +0.060 | +0.016 | -0.022 | -0.019 | **Marlowe** |
| ST | Kyd | control | -0.017 | -0.002 | +0.033 | -0.008 | +0.005 | -0.011 | **Marlowe** |
| OWT | Peele | control | +0.025 | +0.001 | +0.009 | -0.053 | +0.017 | +0.001 | **Greene** |
| Gal | Lyly | control | +0.022 | +0.015 | -0.016 | -0.035 | +0.007 | +0.008 | **Greene** |
| AShrew | Anon-AShrew | control | -0.012 | +0.022 | +0.037 | -0.077 | +0.001 | +0.029 | **Greene** |
| TCKL | Anon-Leir | control | +0.020 | -0.014 | +0.005 | -0.017 | +0.027 | -0.021 | **Anon-heroic** |
| Alphonsus | Greene | control_ep | -0.027 | +0.029 | +0.093 | -0.021 | -0.032 | -0.042 | **Anon-heroic** |
| Orlando | Greene | control_ep | -0.052 | +0.046 | +0.090 | -0.032 | -0.038 | -0.014 | **Marlowe** |
| FriarBacon | Greene | control_ep | -0.050 | +0.005 | +0.051 | -0.006 | -0.036 | +0.035 | **Marlowe** |
| JamesIV | Greene | control_ep | +0.002 | -0.004 | +0.017 | +0.018 | -0.011 | -0.022 | **Anon-heroic** |
| Alcazar | Peele | control_ep | -0.082 | +0.054 | +0.104 | -0.008 | -0.031 | -0.038 | **Marlowe** |
| EdwardI | Peele | control_ep | -0.025 | +0.015 | +0.053 | -0.047 | +0.011 | -0.007 | **Greene** |
| David | Peele | control_ep | -0.078 | +0.046 | +0.064 | -0.018 | -0.027 | +0.013 | **Marlowe** |
| Wounds | Lodge | control_ep | -0.031 | +0.016 | +0.077 | -0.054 | -0.020 | +0.012 | **Greene** |
| Soliman | Anon-Soliman | control_ep | -0.008 | -0.002 | +0.039 | -0.015 | -0.002 | -0.013 | **Greene** |
| Locrine | Anon-Locrine | control_ep | -0.049 | +0.046 | +0.084 | -0.047 | -0.059 | +0.025 | **Peele** |
| Selimus | Anon-Selimus | control_ep | -0.028 | +0.025 | +0.051 | -0.002 | -0.026 | -0.019 | **Marlowe** |
| TRKJ | Anon-TRKJ | control_ep | +0.004 | -0.013 | +0.025 | +0.015 | -0.016 | -0.015 | **Peele** |
| JackStraw | Anon-JackStraw | control_ep | +0.024 | -0.016 | +0.022 | +0.043 | -0.031 | -0.041 | **Anon-heroic** |
| EdwardIII | Anon-EdwardIII | control_ep | -0.023 | +0.006 | +0.008 | +0.030 | -0.019 | -0.002 | **Marlowe** |
| Arden | Anon-Arden | control_ep | +0.005 | -0.021 | -0.001 | -0.017 | +0.025 | +0.010 | **Sh-early** |
| TTR3 | Anon-TTR3 | control_ep | -0.009 | +0.050 | +0.028 | -0.003 | -0.018 | -0.047 | **Anon-heroic** |
| Endymion | Lyly | control_ep | +0.015 | +0.009 | -0.014 | -0.008 | +0.007 | -0.010 | **Sh-later** |

## Group means

| group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) |
|---|---|---|---|---|---|---|
| Marlowe plays | -0.021 | +0.030 | +0.057 | -0.022 | -0.047 | +0.002 |
| Shakespeare early | +0.017 | -0.011 | -0.033 | +0.017 | +0.019 | -0.008 |
|   of which Henry VI 1-3 | -0.010 | +0.027 | -0.016 | +0.019 | +0.009 | -0.029 |
|   of which Tit, R3, Shr, TGV, Err | +0.033 | -0.033 | -0.044 | +0.015 | +0.025 | +0.004 |
| Shakespeare later | +0.035 | -0.040 | -0.090 | +0.035 | +0.040 | +0.020 |
| early controls | +0.008 | +0.004 | +0.014 | -0.038 | +0.011 | +0.001 |
| Greene | -0.031 | +0.019 | +0.063 | -0.010 | -0.029 | -0.011 |
| Peele | -0.040 | +0.029 | +0.058 | -0.032 | -0.007 | -0.008 |
| anonymous heroic 1587-94 | -0.011 | +0.009 | +0.032 | +0.000 | -0.018 | -0.013 |
| Lodge, Lyly Endymion | -0.008 | +0.013 | +0.032 | -0.031 | -0.006 | +0.001 |
