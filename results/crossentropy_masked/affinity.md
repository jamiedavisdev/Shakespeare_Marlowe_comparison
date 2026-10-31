# Affinity (double-centred cross-entropy, bits/char), variant = masked

Negative = the play is specifically well predicted by that author model, after removing each model's overall predictiveness and each play's overall predictability. Each row sums to zero.

| play | author | group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) | strongest affinity |
|---|---|---|---|---|---|---|---|---|---|
| 1Tam | Marlowe | marlowe | -0.006 | +0.055 | +0.116 | -0.052 | -0.108 | -0.006 | **Peele** |
| 2Tam | Marlowe | marlowe | -0.021 | +0.057 | +0.088 | -0.030 | -0.098 | +0.004 | **Peele** |
| Dido | Marlowe | marlowe | -0.047 | +0.011 | +0.058 | -0.029 | -0.013 | +0.020 | **Marlowe** |
| DrFaust | Marlowe | marlowe | -0.027 | -0.001 | +0.020 | -0.027 | -0.007 | +0.041 | **Marlowe** |
| JoM | Marlowe | marlowe | -0.039 | -0.020 | +0.004 | +0.037 | +0.002 | +0.018 | **Marlowe** |
| Ed2 | Marlowe | marlowe | -0.013 | -0.044 | +0.037 | +0.031 | -0.029 | +0.019 | **Sh-early** |
| MP | Marlowe | marlowe | -0.063 | +0.013 | +0.076 | +0.020 | -0.023 | -0.023 | **Marlowe** |
| 2H6 | Shakespeare | shakespeare_early | -0.029 | +0.030 | -0.029 | +0.035 | -0.004 | -0.003 | **Sh-later** |
| 3H6 | Shakespeare | shakespeare_early | -0.039 | +0.033 | +0.001 | +0.032 | -0.013 | -0.013 | **Marlowe** |
| 1H6 | Shakespeare | shakespeare_early | -0.043 | +0.044 | +0.001 | +0.023 | -0.008 | -0.017 | **Marlowe** |
| Tit | Shakespeare | shakespeare_early | -0.021 | -0.047 | +0.022 | +0.053 | -0.016 | +0.008 | **Sh-early** |
| R3 | Shakespeare | shakespeare_early | +0.007 | -0.005 | -0.058 | +0.045 | +0.012 | -0.001 | **Sh-later** |
| Shr | Shakespeare | shakespeare_early | +0.032 | -0.045 | -0.056 | -0.009 | +0.026 | +0.052 | **Sh-later** |
| TGV | Shakespeare | shakespeare_early | +0.027 | -0.047 | -0.063 | +0.012 | +0.045 | +0.027 | **Sh-later** |
| Err | Shakespeare | shakespeare_early | +0.026 | -0.034 | -0.074 | +0.033 | +0.047 | +0.002 | **Sh-later** |
| R2 | Shakespeare | shakespeare_later | +0.020 | -0.044 | -0.033 | +0.051 | +0.007 | -0.000 | **Sh-early** |
| MND | Shakespeare | shakespeare_later | +0.033 | -0.039 | -0.065 | +0.006 | +0.029 | +0.037 | **Sh-later** |
| Rom | Shakespeare | shakespeare_later | +0.021 | -0.048 | -0.077 | +0.041 | +0.027 | +0.036 | **Sh-later** |
| MV | Shakespeare | shakespeare_later | +0.020 | -0.033 | -0.074 | +0.029 | +0.039 | +0.018 | **Sh-later** |
| 1H4 | Shakespeare | shakespeare_later | +0.013 | -0.044 | -0.078 | +0.047 | +0.025 | +0.037 | **Sh-later** |
| JC | Shakespeare | shakespeare_later | +0.009 | -0.029 | -0.057 | +0.037 | +0.028 | +0.012 | **Sh-later** |
| Ham | Shakespeare | shakespeare_later | +0.017 | -0.026 | -0.123 | +0.053 | +0.037 | +0.042 | **Sh-later** |
| Mac | Shakespeare | shakespeare_later | +0.013 | -0.032 | -0.114 | +0.057 | +0.041 | +0.036 | **Sh-later** |
| Lr | Shakespeare | shakespeare_later | +0.025 | -0.044 | -0.117 | +0.053 | +0.043 | +0.041 | **Sh-later** |
| WT | Shakespeare | shakespeare_later | +0.021 | -0.048 | -0.124 | +0.060 | +0.043 | +0.048 | **Sh-later** |
| Tmp | Shakespeare | shakespeare_later | +0.003 | -0.037 | -0.105 | +0.058 | +0.036 | +0.045 | **Sh-later** |
| ST | Kyd | control | -0.031 | -0.008 | +0.037 | +0.003 | +0.005 | -0.006 | **Marlowe** |
| OWT | Peele | control | +0.017 | -0.010 | -0.011 | -0.042 | +0.044 | +0.002 | **Greene** |
| Gal | Lyly | control | +0.016 | +0.027 | -0.008 | -0.044 | +0.012 | -0.003 | **Greene** |
| AShrew | Anon-AShrew | control | -0.039 | -0.022 | +0.004 | -0.014 | +0.007 | +0.064 | **Marlowe** |
| TCKL | Anon-Leir | control | +0.003 | -0.021 | +0.008 | -0.008 | +0.023 | -0.005 | **Sh-early** |
| ShoeHol | Dekker | control | +0.037 | -0.046 | -0.068 | -0.021 | +0.031 | +0.068 | **Sh-later** |
| RT | Middleton | control | -0.024 | -0.051 | -0.092 | +0.070 | +0.049 | +0.047 | **Sh-later** |
| KBP | Beaumont | control | +0.020 | -0.023 | -0.052 | +0.016 | +0.008 | +0.032 | **Sh-later** |
| FS | Fletcher | control_multi | +0.014 | +0.018 | -0.032 | -0.018 | -0.010 | +0.028 | **Sh-later** |
| Prize | Fletcher | control_multi | +0.007 | -0.052 | -0.106 | +0.050 | +0.047 | +0.055 | **Sh-later** |
| IP | Fletcher | control_multi | -0.004 | -0.024 | -0.072 | +0.055 | +0.023 | +0.021 | **Sh-later** |
| Perkin | Ford | control_multi | -0.002 | -0.017 | -0.044 | +0.059 | +0.026 | -0.022 | **Sh-later** |
| TPSW | Ford | control_multi | -0.002 | -0.049 | -0.054 | +0.025 | +0.042 | +0.040 | **Sh-later** |
| Alphonsus | Greene | control_ep | -0.001 | +0.041 | +0.123 | -0.051 | -0.038 | -0.074 | **Anon-heroic** |
| Orlando | Greene | control_ep | -0.026 | +0.084 | +0.123 | -0.073 | -0.052 | -0.056 | **Greene** |
| FriarBacon | Greene | control_ep | -0.015 | +0.026 | +0.085 | -0.045 | -0.047 | -0.004 | **Peele** |
| JamesIV | Greene | control_ep | +0.032 | +0.019 | +0.042 | -0.017 | -0.019 | -0.057 | **Anon-heroic** |
| Alcazar | Peele | control_ep | -0.046 | +0.057 | +0.127 | -0.037 | -0.035 | -0.066 | **Anon-heroic** |
| EdwardI | Peele | control_ep | +0.009 | +0.014 | +0.071 | -0.080 | +0.027 | -0.040 | **Greene** |
| David | Peele | control_ep | -0.047 | +0.039 | +0.077 | -0.039 | -0.022 | -0.009 | **Marlowe** |
| Wounds | Lodge | control_ep | -0.008 | +0.042 | +0.106 | -0.089 | -0.028 | -0.023 | **Greene** |
| Soliman | Anon-Soliman | control_ep | +0.022 | +0.038 | +0.071 | -0.057 | -0.018 | -0.056 | **Greene** |
| Locrine | Anon-Locrine | control_ep | -0.022 | +0.062 | +0.117 | -0.081 | -0.066 | -0.009 | **Greene** |
| Selimus | Anon-Selimus | control_ep | -0.012 | +0.046 | +0.085 | -0.034 | -0.034 | -0.051 | **Anon-heroic** |
| TRKJ | Anon-TRKJ | control_ep | +0.020 | +0.026 | +0.070 | -0.026 | -0.033 | -0.057 | **Anon-heroic** |
| JackStraw | Anon-JackStraw | control_ep | +0.048 | +0.035 | +0.071 | -0.007 | -0.055 | -0.091 | **Anon-heroic** |
| EdwardIII | Anon-EdwardIII | control_ep | +0.003 | +0.024 | +0.038 | -0.003 | -0.025 | -0.035 | **Anon-heroic** |
| Arden | Anon-Arden | control_ep | +0.046 | +0.032 | +0.033 | -0.069 | +0.001 | -0.042 | **Greene** |
| TTR3 | Anon-TTR3 | control_ep | +0.013 | +0.085 | +0.051 | -0.038 | -0.028 | -0.082 | **Anon-heroic** |
| Endymion | Lyly | control_ep | +0.032 | +0.038 | +0.022 | -0.044 | -0.002 | -0.046 | **Anon-heroic** |

## Group means

| group | A(Marlowe) | A(Sh-early) | A(Sh-later) | A(Greene) | A(Peele) | A(Anon-heroic) |
|---|---|---|---|---|---|---|
| Marlowe plays | -0.031 | +0.010 | +0.057 | -0.007 | -0.039 | +0.010 |
| Shakespeare early | -0.005 | -0.009 | -0.032 | +0.028 | +0.011 | +0.007 |
|   of which Henry VI 1-3 | -0.037 | +0.036 | -0.009 | +0.030 | -0.008 | -0.011 |
|   of which Tit, R3, Shr, TGV, Err | +0.014 | -0.036 | -0.046 | +0.027 | +0.023 | +0.018 |
| Shakespeare later | +0.018 | -0.039 | -0.088 | +0.045 | +0.032 | +0.032 |
| early controls | -0.007 | -0.007 | +0.006 | -0.021 | +0.018 | +0.010 |
| later controls | +0.011 | -0.040 | -0.071 | +0.021 | +0.029 | +0.049 |
| Fletcher | +0.006 | -0.019 | -0.070 | +0.029 | +0.020 | +0.035 |
| Ford | -0.002 | -0.033 | -0.049 | +0.042 | +0.034 | +0.009 |
| Greene | -0.002 | +0.042 | +0.093 | -0.047 | -0.039 | -0.048 |
| Peele | -0.017 | +0.025 | +0.066 | -0.050 | +0.004 | -0.028 |
| anonymous heroic 1587-94 | +0.015 | +0.043 | +0.067 | -0.040 | -0.032 | -0.053 |
| Lodge, Lyly Endymion | +0.012 | +0.040 | +0.064 | -0.066 | -0.015 | -0.034 |
