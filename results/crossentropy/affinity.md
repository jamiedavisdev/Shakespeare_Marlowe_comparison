# Affinity (double-centred cross-entropy, bits/char), variant = plain

Negative = the play is specifically well predicted by that author model, after removing each model's overall predictiveness and each play's overall predictability. Each row sums to zero.

| play | author | group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) | strongest affinity |
|---|---|---|---|---|---|---|---|---|---|
| 1Tam | Marlowe | marlowe | -0.194 | +0.115 | +0.180 | -0.051 | -0.066 | +0.016 | **Marlowe** |
| 2Tam | Marlowe | marlowe | -0.156 | +0.104 | +0.132 | -0.030 | -0.077 | +0.028 | **Marlowe** |
| Dido | Marlowe | marlowe | -0.015 | +0.026 | -0.004 | -0.050 | -0.007 | +0.049 | **Greene** |
| DrFaust | Marlowe | marlowe | -0.009 | +0.035 | +0.007 | -0.071 | +0.002 | +0.036 | **Greene** |
| JoM | Marlowe | marlowe | -0.031 | -0.005 | +0.011 | +0.037 | -0.021 | +0.010 | **Marlowe** |
| Ed2 | Marlowe | marlowe | +0.042 | -0.043 | +0.027 | +0.054 | -0.060 | -0.020 | **Peele** |
| MP | Marlowe | marlowe | -0.049 | -0.006 | +0.065 | +0.022 | -0.020 | -0.013 | **Marlowe** |
| 2H6 | Shakespeare | shakespeare_early | +0.000 | -0.109 | +0.002 | +0.069 | +0.053 | -0.015 | **Sh-early** |
| 3H6 | Shakespeare | shakespeare_early | -0.002 | -0.094 | +0.042 | +0.049 | +0.044 | -0.038 | **Sh-early** |
| 1H6 | Shakespeare | shakespeare_early | -0.008 | -0.089 | +0.021 | +0.044 | +0.042 | -0.011 | **Sh-early** |
| Tit | Shakespeare | shakespeare_early | -0.026 | +0.005 | +0.005 | +0.038 | -0.020 | -0.002 | **Marlowe** |
| R3 | Shakespeare | shakespeare_early | +0.054 | -0.073 | -0.034 | +0.071 | +0.030 | -0.048 | **Sh-early** |
| Shr | Shakespeare | shakespeare_early | +0.037 | -0.043 | -0.084 | -0.011 | +0.033 | +0.069 | **Sh-later** |
| TGV | Shakespeare | shakespeare_early | +0.007 | -0.024 | -0.071 | +0.021 | +0.024 | +0.043 | **Sh-later** |
| Err | Shakespeare | shakespeare_early | +0.023 | -0.023 | -0.075 | +0.029 | +0.040 | +0.007 | **Sh-later** |
| R2 | Shakespeare | shakespeare_later | +0.044 | -0.067 | -0.058 | +0.070 | +0.021 | -0.011 | **Sh-early** |
| MND | Shakespeare | shakespeare_later | +0.011 | -0.035 | -0.067 | -0.008 | +0.037 | +0.061 | **Sh-later** |
| Rom | Shakespeare | shakespeare_later | +0.038 | -0.052 | -0.074 | +0.038 | +0.023 | +0.027 | **Sh-later** |
| MV | Shakespeare | shakespeare_later | +0.020 | -0.036 | -0.080 | +0.030 | +0.043 | +0.024 | **Sh-later** |
| 1H4 | Shakespeare | shakespeare_later | +0.029 | -0.037 | -0.070 | +0.054 | +0.011 | +0.013 | **Sh-later** |
| JC | Shakespeare | shakespeare_later | +0.009 | -0.014 | +0.004 | +0.009 | +0.016 | -0.024 | **Anon-heroic** |
| Ham | Shakespeare | shakespeare_later | +0.019 | -0.013 | -0.119 | +0.045 | +0.033 | +0.035 | **Sh-later** |
| Mac | Shakespeare | shakespeare_later | +0.015 | -0.014 | -0.124 | +0.054 | +0.030 | +0.039 | **Sh-later** |
| Lr | Shakespeare | shakespeare_later | +0.023 | -0.042 | -0.125 | +0.067 | +0.037 | +0.039 | **Sh-later** |
| WT | Shakespeare | shakespeare_later | +0.016 | -0.033 | -0.125 | +0.051 | +0.039 | +0.052 | **Sh-later** |
| Tmp | Shakespeare | shakespeare_later | +0.002 | -0.023 | -0.103 | +0.051 | +0.026 | +0.048 | **Sh-later** |
| ST | Kyd | control | -0.012 | -0.026 | +0.019 | +0.013 | +0.014 | -0.009 | **Sh-early** |
| OWT | Peele | control | +0.023 | -0.000 | -0.030 | -0.047 | +0.047 | +0.008 | **Greene** |
| Gal | Lyly | control | +0.005 | +0.058 | -0.033 | -0.056 | -0.002 | +0.027 | **Greene** |
| AShrew | Anon-AShrew | control | -0.030 | -0.029 | +0.004 | -0.017 | +0.006 | +0.065 | **Marlowe** |
| TCKL | Anon-Leir | control | +0.009 | -0.007 | -0.003 | -0.007 | +0.011 | -0.004 | **Greene** |
| ShoeHol | Dekker | control | +0.044 | -0.035 | -0.068 | -0.020 | +0.020 | +0.058 | **Sh-later** |
| RT | Middleton | control | -0.011 | -0.057 | -0.109 | +0.070 | +0.045 | +0.062 | **Sh-later** |
| KBP | Beaumont | control | +0.026 | -0.022 | -0.050 | +0.015 | +0.004 | +0.027 | **Sh-later** |
| FS | Fletcher | control_multi | +0.022 | +0.032 | -0.040 | -0.031 | -0.017 | +0.035 | **Sh-later** |
| Prize | Fletcher | control_multi | +0.019 | -0.052 | -0.111 | +0.044 | +0.041 | +0.058 | **Sh-later** |
| IP | Fletcher | control_multi | -0.002 | -0.009 | -0.073 | +0.052 | +0.008 | +0.025 | **Sh-later** |
| Perkin | Ford | control_multi | +0.018 | -0.018 | -0.052 | +0.058 | +0.018 | -0.024 | **Sh-later** |
| TPSW | Ford | control_multi | -0.009 | -0.039 | -0.069 | +0.021 | +0.044 | +0.053 | **Sh-later** |
| Alphonsus | Greene | control_ep | -0.030 | +0.036 | +0.150 | -0.043 | -0.037 | -0.076 | **Anon-heroic** |
| Orlando | Greene | control_ep | -0.049 | +0.102 | +0.093 | -0.055 | -0.057 | -0.034 | **Peele** |
| FriarBacon | Greene | control_ep | -0.017 | +0.033 | +0.091 | -0.030 | -0.062 | -0.015 | **Peele** |
| JamesIV | Greene | control_ep | +0.042 | +0.030 | +0.035 | -0.019 | -0.027 | -0.061 | **Anon-heroic** |
| Alcazar | Peele | control_ep | -0.076 | +0.083 | +0.113 | -0.023 | -0.009 | -0.088 | **Anon-heroic** |
| EdwardI | Peele | control_ep | +0.031 | +0.019 | +0.067 | -0.091 | +0.043 | -0.068 | **Greene** |
| David | Peele | control_ep | -0.068 | +0.088 | +0.089 | -0.005 | -0.069 | -0.035 | **Peele** |
| Wounds | Lodge | control_ep | +0.000 | +0.036 | +0.074 | -0.088 | -0.018 | -0.004 | **Greene** |
| Soliman | Anon-Soliman | control_ep | +0.006 | +0.064 | +0.082 | -0.077 | -0.023 | -0.053 | **Greene** |
| Locrine | Anon-Locrine | control_ep | -0.033 | +0.072 | +0.105 | -0.088 | -0.069 | +0.012 | **Greene** |
| Selimus | Anon-Selimus | control_ep | -0.070 | +0.083 | +0.105 | -0.065 | -0.016 | -0.037 | **Marlowe** |
| TRKJ | Anon-TRKJ | control_ep | +0.033 | +0.016 | +0.072 | -0.013 | -0.047 | -0.061 | **Anon-heroic** |
| JackStraw | Anon-JackStraw | control_ep | +0.073 | +0.038 | +0.060 | -0.003 | -0.074 | -0.093 | **Anon-heroic** |
| EdwardIII | Anon-EdwardIII | control_ep | +0.016 | +0.015 | +0.039 | -0.012 | -0.023 | -0.035 | **Anon-heroic** |
| Arden | Anon-Arden | control_ep | +0.058 | +0.030 | +0.037 | -0.074 | -0.013 | -0.037 | **Greene** |
| TTR3 | Anon-TTR3 | control_ep | +0.060 | -0.030 | +0.073 | -0.008 | -0.028 | -0.066 | **Anon-heroic** |
| Endymion | Lyly | control_ep | +0.022 | +0.077 | +0.047 | -0.079 | -0.025 | -0.042 | **Greene** |

## Group means

| group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) |
|---|---|---|---|---|---|---|
| Marlowe plays | -0.059 | +0.033 | +0.060 | -0.013 | -0.036 | +0.015 |
| Shakespeare early | +0.011 | -0.056 | -0.024 | +0.039 | +0.031 | +0.000 |
|   of which Henry VI 1-3 | -0.003 | -0.097 | +0.022 | +0.054 | +0.046 | -0.022 |
|   of which Tit, R3, Shr, TGV, Err | +0.019 | -0.032 | -0.052 | +0.029 | +0.021 | +0.014 |
| Shakespeare later | +0.021 | -0.033 | -0.085 | +0.042 | +0.029 | +0.028 |
| early controls | -0.001 | -0.001 | -0.008 | -0.023 | +0.015 | +0.018 |
| later controls | +0.020 | -0.038 | -0.075 | +0.022 | +0.023 | +0.049 |
| Fletcher | +0.013 | -0.010 | -0.075 | +0.021 | +0.011 | +0.039 |
| Ford | +0.005 | -0.029 | -0.061 | +0.039 | +0.031 | +0.015 |
| Greene | -0.014 | +0.051 | +0.092 | -0.037 | -0.046 | -0.046 |
| Peele | -0.023 | +0.047 | +0.060 | -0.042 | +0.003 | -0.046 |
| anonymous heroic 1587-94 | +0.018 | +0.036 | +0.072 | -0.042 | -0.037 | -0.046 |
| Lodge, Lyly Endymion | +0.011 | +0.057 | +0.061 | -0.084 | -0.022 | -0.023 |
