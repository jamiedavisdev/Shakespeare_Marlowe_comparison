# Cosine similarity between fine-tuning weight deltas (GPT-2 small, embeddings excluded)

Every model starts from the same pretrained GPT-2 and sees the same number of tokens (78,818), 3 epochs, lr 5e-05. The delta is (fine-tuned − pretrained) over all non-embedding parameters.

| | Marlowe_s1 | Marlowe_s2 | Marlowe_A | Marlowe_B | ShLater_s1 | ShLater_s2 | ShLater_A | ShLater_B | ShEarlyNonH6 | Greene | Peele | AnonHeroic | Fletcher |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marlowe_s1 | 1.013 | 0.777 | 0.520 | 0.548 | 0.213 | 0.213 | 0.215 | 0.205 | 0.232 | 0.270 | 0.265 | 0.273 | 0.224 |
| Marlowe_s2 | 0.777 | 1.013 | 0.523 | 0.544 | 0.214 | 0.215 | 0.216 | 0.205 | 0.232 | 0.272 | 0.267 | 0.275 | 0.224 |
| Marlowe_A | 0.520 | 0.523 | 1.013 | 0.272 | 0.197 | 0.196 | 0.195 | 0.188 | 0.212 | 0.261 | 0.265 | 0.262 | 0.212 |
| Marlowe_B | 0.548 | 0.544 | 0.272 | 1.014 | 0.215 | 0.216 | 0.222 | 0.211 | 0.237 | 0.259 | 0.256 | 0.264 | 0.226 |
| ShLater_s1 | 0.213 | 0.214 | 0.197 | 0.215 | 1.014 | 0.750 | 0.495 | 0.512 | 0.271 | 0.191 | 0.186 | 0.195 | 0.212 |
| ShLater_s2 | 0.213 | 0.215 | 0.196 | 0.216 | 0.750 | 1.015 | 0.477 | 0.511 | 0.271 | 0.190 | 0.186 | 0.197 | 0.213 |
| ShLater_A | 0.215 | 0.216 | 0.195 | 0.222 | 0.495 | 0.477 | 1.014 | 0.270 | 0.284 | 0.194 | 0.192 | 0.198 | 0.199 |
| ShLater_B | 0.205 | 0.205 | 0.188 | 0.211 | 0.512 | 0.511 | 0.270 | 1.014 | 0.261 | 0.182 | 0.176 | 0.184 | 0.219 |
| ShEarlyNonH6 | 0.232 | 0.232 | 0.212 | 0.237 | 0.271 | 0.271 | 0.284 | 0.261 | 1.014 | 0.211 | 0.205 | 0.208 | 0.204 |
| Greene | 0.270 | 0.272 | 0.261 | 0.259 | 0.191 | 0.190 | 0.194 | 0.182 | 0.211 | 1.013 | 0.276 | 0.301 | 0.205 |
| Peele | 0.265 | 0.267 | 0.265 | 0.256 | 0.186 | 0.186 | 0.192 | 0.176 | 0.205 | 0.276 | 1.013 | 0.270 | 0.200 |
| AnonHeroic | 0.273 | 0.275 | 0.262 | 0.264 | 0.195 | 0.197 | 0.198 | 0.184 | 0.208 | 0.301 | 0.270 | 1.014 | 0.206 |
| Fletcher | 0.224 | 0.224 | 0.212 | 0.226 | 0.212 | 0.213 | 0.199 | 0.219 | 0.204 | 0.205 | 0.200 | 0.206 | 1.014 |

## Key pairs

| pair | type | cosine |
|---|---|---|
| Marlowe_s1 vs Marlowe_s2 | seed only, same data: Marlowe s1 vs s2 | 0.777 |
| ShLater_s1 vs ShLater_s2 | seed only, same data: Shakespeare-later s1 vs s2 | 0.750 |
| Marlowe_A vs Marlowe_B | same author, different plays: Marlowe A vs B | 0.272 |
| ShLater_A vs ShLater_B | same author, different plays: Shakespeare-later A vs B | 0.270 |
| ShEarlyNonH6 vs ShLater_s1 | same author, different period: Shakespeare early (non-H6) vs later | 0.271 |
| Marlowe_s1 vs ShEarlyNonH6 | QUESTION: Marlowe vs Shakespeare early (non-H6) | 0.232 |
| Marlowe_s1 vs ShLater_s1 | QUESTION: Marlowe vs Shakespeare later | 0.213 |
| Marlowe_s1 vs Greene | different, same register: Marlowe vs Greene | 0.270 |
| Marlowe_s1 vs Peele | different, same register: Marlowe vs Peele | 0.265 |
| Marlowe_s1 vs AnonHeroic | different, same register: Marlowe vs anonymous heroic | 0.273 |
| Greene vs Peele | different: Greene vs Peele | 0.276 |
| ShEarlyNonH6 vs Greene | different: Shakespeare early (non-H6) vs Greene | 0.211 |
| ShEarlyNonH6 vs Peele | different: Shakespeare early (non-H6) vs Peele | 0.205 |
| ShLater_s1 vs Fletcher | different, different period: Shakespeare later vs Fletcher | 0.212 |
| Marlowe_s1 vs Fletcher | different, different period: Marlowe vs Fletcher | 0.224 |
