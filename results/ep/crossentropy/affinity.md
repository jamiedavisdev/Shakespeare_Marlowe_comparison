# Affinity (double-centred cross-entropy, bits/char), variant = plain

Negative = the play is specifically well predicted by that author model, after removing each model's overall predictiveness and each play's overall predictability. Each row sums to zero.

| play | author | group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) | strongest affinity |
|---|---|---|---|---|---|---|---|---|---|
| 2H6 | Shakespeare | shakespeare_early | +0.025 | -0.084 | +0.005 | +0.047 | +0.039 | -0.033 | **Sh-early** |
| 3H6 | Shakespeare | shakespeare_early | +0.014 | -0.080 | +0.042 | +0.035 | +0.040 | -0.052 | **Sh-early** |
| 1H6 | Shakespeare | shakespeare_early | +0.005 | -0.064 | +0.020 | +0.026 | +0.042 | -0.029 | **Sh-early** |
| Tit | Shakespeare | shakespeare_early | -0.014 | +0.012 | +0.006 | +0.026 | -0.023 | -0.007 | **Peele** |
| R3 | Shakespeare | shakespeare_early | +0.063 | -0.065 | -0.037 | +0.067 | +0.021 | -0.048 | **Sh-early** |
| Shr | Shakespeare | shakespeare_early | +0.056 | -0.030 | -0.072 | -0.033 | +0.034 | +0.045 | **Sh-later** |
| TGV | Shakespeare | shakespeare_early | +0.039 | -0.030 | -0.060 | +0.002 | +0.037 | +0.012 | **Sh-later** |
| Err | Shakespeare | shakespeare_early | +0.047 | -0.021 | -0.072 | +0.015 | +0.034 | -0.003 | **Sh-later** |
| R2 | Shakespeare | shakespeare_later | +0.051 | -0.059 | -0.066 | +0.064 | +0.018 | -0.008 | **Sh-later** |
| MND | Shakespeare | shakespeare_later | +0.019 | -0.019 | -0.079 | -0.012 | +0.035 | +0.056 | **Sh-later** |
| Rom | Shakespeare | shakespeare_later | +0.054 | -0.027 | -0.071 | +0.010 | +0.021 | +0.013 | **Sh-later** |
| MV | Shakespeare | shakespeare_later | +0.030 | -0.032 | -0.085 | +0.017 | +0.045 | +0.024 | **Sh-later** |
| 1H4 | Shakespeare | shakespeare_later | +0.044 | -0.035 | -0.077 | +0.041 | +0.014 | +0.013 | **Sh-later** |
| JC | Shakespeare | shakespeare_later | +0.020 | -0.015 | +0.008 | -0.001 | +0.009 | -0.022 | **Anon-heroic** |
| Ham | Shakespeare | shakespeare_later | +0.037 | -0.010 | -0.115 | +0.032 | +0.029 | +0.027 | **Sh-later** |
| Mac | Shakespeare | shakespeare_later | +0.034 | -0.008 | -0.124 | +0.037 | +0.031 | +0.030 | **Sh-later** |
| Lr | Shakespeare | shakespeare_later | +0.050 | -0.027 | -0.111 | +0.039 | +0.031 | +0.017 | **Sh-later** |
| WT | Shakespeare | shakespeare_later | +0.038 | -0.026 | -0.116 | +0.026 | +0.044 | +0.034 | **Sh-later** |
| Tmp | Shakespeare | shakespeare_later | +0.025 | -0.011 | -0.107 | +0.024 | +0.036 | +0.033 | **Sh-later** |
| 1Tam | Marlowe | marlowe | -0.184 | +0.122 | +0.168 | -0.051 | -0.073 | +0.018 | **Marlowe** |
| 2Tam | Marlowe | marlowe | -0.147 | +0.104 | +0.119 | -0.028 | -0.082 | +0.035 | **Marlowe** |
| Dido | Marlowe | marlowe | -0.002 | +0.036 | -0.017 | -0.054 | -0.010 | +0.046 | **Greene** |
| DrFaust | Marlowe | marlowe | +0.001 | +0.045 | +0.021 | -0.084 | -0.006 | +0.023 | **Greene** |
| JoM | Marlowe | marlowe | -0.003 | +0.004 | -0.001 | +0.023 | -0.014 | -0.009 | **Peele** |
| Ed2 | Marlowe | marlowe | +0.057 | -0.025 | +0.036 | +0.034 | -0.064 | -0.037 | **Peele** |
| MP | Marlowe | marlowe | -0.037 | +0.003 | +0.059 | +0.012 | -0.021 | -0.017 | **Marlowe** |
| ST | Kyd | control | +0.002 | -0.017 | +0.021 | -0.001 | +0.009 | -0.014 | **Sh-early** |
| OWT | Peele | control | +0.035 | +0.015 | -0.022 | -0.051 | +0.020 | +0.003 | **Greene** |
| Gal | Lyly | control | +0.006 | +0.050 | -0.040 | -0.045 | -0.002 | +0.032 | **Greene** |
| AShrew | Anon-AShrew | control | +0.002 | +0.006 | +0.028 | -0.073 | +0.008 | +0.030 | **Greene** |
| TCKL | Anon-Leir | control | +0.023 | +0.008 | -0.000 | -0.021 | +0.013 | -0.022 | **Anon-heroic** |
| Alphonsus | Greene | control_ep | -0.048 | +0.017 | +0.117 | -0.012 | -0.028 | -0.047 | **Marlowe** |
| Orlando | Greene | control_ep | -0.069 | +0.072 | +0.061 | -0.018 | -0.046 | +0.001 | **Marlowe** |
| FriarBacon | Greene | control_ep | -0.040 | -0.005 | +0.043 | +0.016 | -0.043 | +0.029 | **Peele** |
| JamesIV | Greene | control_ep | +0.018 | -0.001 | -0.000 | +0.020 | -0.012 | -0.025 | **Anon-heroic** |
| Alcazar | Peele | control_ep | -0.103 | +0.052 | +0.095 | +0.011 | +0.003 | -0.057 | **Marlowe** |
| EdwardI | Peele | control_ep | +0.001 | -0.024 | +0.032 | -0.045 | +0.061 | -0.025 | **Greene** |
| David | Peele | control_ep | -0.086 | +0.068 | +0.060 | +0.026 | -0.062 | -0.006 | **Marlowe** |
| Wounds | Lodge | control_ep | -0.020 | +0.012 | +0.036 | -0.052 | -0.006 | +0.030 | **Greene** |
| Soliman | Anon-Soliman | control_ep | -0.025 | +0.031 | +0.048 | -0.035 | -0.007 | -0.013 | **Greene** |
| Locrine | Anon-Locrine | control_ep | -0.050 | +0.044 | +0.067 | -0.051 | -0.055 | +0.045 | **Peele** |
| Selimus | Anon-Selimus | control_ep | -0.085 | +0.058 | +0.076 | -0.034 | -0.007 | -0.009 | **Marlowe** |
| TRKJ | Anon-TRKJ | control_ep | +0.020 | -0.015 | +0.033 | +0.023 | -0.034 | -0.028 | **Peele** |
| JackStraw | Anon-JackStraw | control_ep | +0.047 | -0.002 | +0.019 | +0.042 | -0.054 | -0.051 | **Peele** |
| EdwardIII | Anon-EdwardIII | control_ep | -0.007 | -0.014 | +0.008 | +0.024 | -0.011 | -0.001 | **Sh-early** |
| Arden | Anon-Arden | control_ep | +0.014 | -0.014 | -0.005 | -0.022 | +0.014 | +0.013 | **Greene** |
| TTR3 | Anon-TTR3 | control_ep | +0.036 | -0.054 | +0.042 | +0.026 | -0.016 | -0.035 | **Sh-early** |
| Endymion | Lyly | control_ep | +0.005 | +0.053 | +0.006 | -0.043 | -0.013 | -0.009 | **Greene** |

## Group means

| group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) |
|---|---|---|---|---|---|---|
| Marlowe plays | -0.045 | +0.041 | +0.055 | -0.021 | -0.039 | +0.008 |
| Shakespeare early | +0.029 | -0.045 | -0.021 | +0.023 | +0.028 | -0.014 |
|   of which Henry VI 1-3 | +0.015 | -0.076 | +0.022 | +0.036 | +0.040 | -0.038 |
|   of which Tit, R3, Shr, TGV, Err | +0.038 | -0.027 | -0.047 | +0.015 | +0.021 | -0.000 |
| Shakespeare later | +0.037 | -0.024 | -0.086 | +0.025 | +0.028 | +0.020 |
| early controls | +0.014 | +0.012 | -0.003 | -0.038 | +0.010 | +0.006 |
| Greene | -0.035 | +0.021 | +0.055 | +0.001 | -0.032 | -0.011 |
| Peele | -0.038 | +0.028 | +0.041 | -0.015 | +0.006 | -0.021 |
| anonymous heroic 1587-94 | -0.006 | +0.004 | +0.036 | -0.003 | -0.021 | -0.010 |
| Lodge, Lyly Endymion | -0.007 | +0.033 | +0.021 | -0.048 | -0.010 | +0.011 |
