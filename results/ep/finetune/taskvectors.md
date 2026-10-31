# Cosine similarity between fine-tuning weight deltas (GPT-2 small, embeddings excluded)

Every model starts from the same pretrained GPT-2 and sees the same number of tokens (78,192), 3 epochs, lr 5e-05. The delta is (fine-tuned − pretrained) over all non-embedding parameters.

| | Marlowe_s1 | Marlowe_s2 | Marlowe_A | Marlowe_B | ShLater_s1 | ShLater_s2 | ShLater_A | ShLater_B | ShEarlyNonH6 | Greene | Peele | AnonHeroic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marlowe_s1 | 1.013 | 0.779 | 0.521 | 0.562 | 0.250 | 0.251 | 0.258 | 0.241 | 0.272 | 0.294 | 0.284 | 0.298 |
| Marlowe_s2 | 0.779 | 1.013 | 0.524 | 0.558 | 0.249 | 0.251 | 0.255 | 0.239 | 0.272 | 0.294 | 0.283 | 0.298 |
| Marlowe_A | 0.521 | 0.524 | 1.013 | 0.273 | 0.231 | 0.232 | 0.235 | 0.223 | 0.251 | 0.282 | 0.283 | 0.284 |
| Marlowe_B | 0.562 | 0.558 | 0.273 | 1.013 | 0.247 | 0.249 | 0.260 | 0.242 | 0.277 | 0.284 | 0.270 | 0.290 |
| ShLater_s1 | 0.250 | 0.249 | 0.231 | 0.247 | 1.014 | 0.760 | 0.514 | 0.526 | 0.290 | 0.236 | 0.221 | 0.243 |
| ShLater_s2 | 0.251 | 0.251 | 0.232 | 0.249 | 0.760 | 1.014 | 0.498 | 0.524 | 0.292 | 0.239 | 0.224 | 0.246 |
| ShLater_A | 0.258 | 0.255 | 0.235 | 0.260 | 0.514 | 0.498 | 1.014 | 0.296 | 0.300 | 0.248 | 0.232 | 0.253 |
| ShLater_B | 0.241 | 0.239 | 0.223 | 0.242 | 0.526 | 0.524 | 0.296 | 1.014 | 0.283 | 0.224 | 0.209 | 0.229 |
| ShEarlyNonH6 | 0.272 | 0.272 | 0.251 | 0.277 | 0.290 | 0.292 | 0.300 | 0.283 | 1.014 | 0.269 | 0.252 | 0.270 |
| Greene | 0.294 | 0.294 | 0.282 | 0.284 | 0.236 | 0.239 | 0.248 | 0.224 | 0.269 | 1.013 | 0.286 | 0.301 |
| Peele | 0.284 | 0.283 | 0.283 | 0.270 | 0.221 | 0.224 | 0.232 | 0.209 | 0.252 | 0.286 | 1.013 | 0.281 |
| AnonHeroic | 0.298 | 0.298 | 0.284 | 0.290 | 0.243 | 0.246 | 0.253 | 0.229 | 0.270 | 0.301 | 0.281 | 1.014 |

## Key pairs

| pair | type | cosine |
|---|---|---|
| Marlowe_s1 vs Marlowe_s2 | seed only, same data: Marlowe s1 vs s2 | 0.779 |
| ShLater_s1 vs ShLater_s2 | seed only, same data: Shakespeare-later s1 vs s2 | 0.760 |
| Marlowe_A vs Marlowe_B | same author, different plays: Marlowe A vs B | 0.273 |
| ShLater_A vs ShLater_B | same author, different plays: Shakespeare-later A vs B | 0.296 |
| ShEarlyNonH6 vs ShLater_s1 | same author, different period: Shakespeare early (non-H6) vs later | 0.290 |
| Marlowe_s1 vs ShEarlyNonH6 | QUESTION: Marlowe vs Shakespeare early (non-H6) | 0.272 |
| Marlowe_s1 vs ShLater_s1 | QUESTION: Marlowe vs Shakespeare later | 0.250 |
| Marlowe_s1 vs Greene | different, same register: Marlowe vs Greene | 0.294 |
| Marlowe_s1 vs Peele | different, same register: Marlowe vs Peele | 0.284 |
| Marlowe_s1 vs AnonHeroic | different, same register: Marlowe vs anonymous heroic | 0.298 |
| Greene vs Peele | different: Greene vs Peele | 0.286 |
| ShEarlyNonH6 vs Greene | different: Shakespeare early (non-H6) vs Greene | 0.269 |
| ShEarlyNonH6 vs Peele | different: Shakespeare early (non-H6) vs Peele | 0.252 |
