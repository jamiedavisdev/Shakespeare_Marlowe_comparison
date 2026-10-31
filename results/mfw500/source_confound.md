# Editorial-source confound check

Shakespeare comes from the Folger Shakespeare editions, Marlowe and most controls from Folger EMED, and the 1587-94 controls from EarlyPrint (EEBO-TCP with standardised spellings). If editorial conventions drove the distances, the same play in two editions would sit far apart. Cosine-delta distances between each alternate-edition text and (a) its own main-corpus edition, (b) the other plays by the same author, (c) the nearest play by anyone else.

| alternate text | source | d(same play, main edition) | mean d(other plays, same author) | nearest play by another author |
|---|---|---|---|---|
| DrFaust_PG | gutenberg | 0.017 | 0.952 | Endymion (Lyly) 0.900 |
| JoM_PG | gutenberg | 0.024 | 1.000 | AShrew (Anon-AShrew) 0.814 |
| ST_EP | earlyprint | 0.017 | nan | Soliman (Anon-Soliman) 0.749 |
| DrFaust_EP | earlyprint | 0.015 | 0.962 | FriarBacon (Greene) 0.905 |
| Ed2_EP | earlyprint | 0.022 | 0.892 | 3H6 (Shakespeare) 0.773 |

## Words whose frequency differs most between editions of the same play (mean |Δz| over all pairs)

| word | mean |Δz| | DrFaust_PG / DrFaust (per 1000) | JoM_PG / JoM (per 1000) | ST_EP / ST (per 1000) | DrFaust_EP / DrFaust (per 1000) | Ed2_EP / Ed2 (per 1000) |
|---|---|---|---|---|---|---|
| t | 1.23 | 0.0 / 0.5 | 0.1 / 1.5 | 1.8 / 0.8 | 1.5 / 0.5 | 3.0 / 0.5 |
| near | 0.91 | 0.3 / 0.3 | 0.2 / 0.2 | 0.3 / 0.2 | 0.7 / 0.3 | 0.8 / 0.4 |
| ay | 0.83 | 2.0 / 1.9 | 2.2 / 2.2 | 1.0 / 2.6 | 1.4 / 1.9 | 0.8 / 1.6 |
| o | 0.60 | 3.6 / 3.3 | 4.3 / 0.7 | 2.6 / 2.8 | 3.2 / 3.3 | 1.8 / 1.8 |
| faith | 0.48 | 0.4 / 0.9 | 0.6 / 0.6 | 0.4 / 0.4 | 0.4 / 0.9 | 0.0 / 0.0 |
| show | 0.48 | 0.2 / 0.5 | 0.1 / 0.2 | 0.7 / 0.7 | 0.5 / 0.5 | 0.1 / 0.1 |
| there | 0.45 | 1.2 / 1.1 | 2.7 / 2.7 | 2.4 / 1.9 | 1.8 / 1.1 | 1.8 / 1.7 |
| loved | 0.43 | 0.0 / 0.1 | 0.1 / 0.3 | 0.4 / 0.4 | 0.1 / 0.1 | 0.2 / 0.3 |
| i | 0.40 | 26.5 / 27.0 | 26.3 / 26.2 | 22.6 / 18.6 | 32.0 / 27.0 | 25.0 / 21.8 |
| over | 0.35 | 0.5 / 0.5 | 0.0 / 0.0 | 0.3 / 0.2 | 0.5 / 0.5 | 0.5 / 0.3 |
| new | 0.33 | 0.1 / 0.2 | 0.1 / 0.2 | 0.2 / 0.2 | 0.3 / 0.2 | 0.3 / 0.3 |
| is | 0.32 | 10.1 / 10.1 | 8.5 / 8.8 | 9.7 / 8.9 | 10.9 / 10.1 | 11.5 / 9.7 |
| than | 0.31 | 1.5 / 1.5 | 1.9 / 1.4 | 1.3 / 1.5 | 1.3 / 1.5 | 1.5 / 1.7 |
| makes | 0.30 | 0.2 / 0.4 | 0.1 / 0.2 | 0.5 / 0.4 | 0.4 / 0.4 | 0.7 / 0.7 |
| here | 0.28 | 2.1 / 2.1 | 3.5 / 3.5 | 4.5 / 4.0 | 2.6 / 2.1 | 3.4 / 3.3 |
