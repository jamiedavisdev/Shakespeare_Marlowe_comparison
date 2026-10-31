# Editorial-source confound check

Shakespeare comes from the Folger Shakespeare editions, Marlowe and most controls from Folger EMED, and the 1587-94 controls from EarlyPrint (EEBO-TCP with standardised spellings). If editorial conventions drove the distances, the same play in two editions would sit far apart. Cosine-delta distances between each alternate-edition text and (a) its own main-corpus edition, (b) the other plays by the same author, (c) the nearest play by anyone else.

| alternate text | source | d(same play, main edition) | mean d(other plays, same author) | nearest play by another author |
|---|---|---|---|---|
| DrFaust_PG | gutenberg | 0.009 | 1.013 | OWT (Peele) 0.805 |
| JoM_PG | gutenberg | 0.046 | 1.034 | ST (Kyd) 0.716 |
| ST_EP | earlyprint | 0.054 | nan | Soliman (Anon-Soliman) 0.586 |
| DrFaust_EP | earlyprint | 0.066 | 1.033 | Arden (Anon-Arden) 0.734 |
| Ed2_EP | earlyprint | 0.065 | 0.851 | TTR3 (Anon-TTR3) 0.715 |

## Words whose frequency differs most between editions of the same play (mean |Δz| over all pairs)

| word | mean |Δz| | DrFaust_PG / DrFaust (per 1000) | JoM_PG / JoM (per 1000) | ST_EP / ST (per 1000) | DrFaust_EP / DrFaust (per 1000) | Ed2_EP / Ed2 (per 1000) |
|---|---|---|---|---|---|---|
| i'll | 1.35 | 5.2 / 5.1 | 3.5 / 3.7 | 0.0 / 2.7 | 0.0 / 5.1 | 0.0 / 2.6 |
| t | 1.23 | 0.0 / 0.5 | 0.1 / 1.5 | 1.8 / 0.8 | 1.5 / 0.5 | 3.0 / 0.5 |
| ay | 0.83 | 2.0 / 1.9 | 2.2 / 2.2 | 1.0 / 2.6 | 1.4 / 1.9 | 0.8 / 1.6 |
| tis | 0.70 | 0.8 / 0.8 | 2.1 / 2.1 | 0.0 / 0.9 | 0.0 / 0.8 | 0.0 / 2.1 |
| o | 0.60 | 3.6 / 3.3 | 4.3 / 0.7 | 2.6 / 2.8 | 3.2 / 3.3 | 1.8 / 1.8 |
| there | 0.45 | 1.2 / 1.1 | 2.7 / 2.7 | 2.4 / 1.9 | 1.8 / 1.1 | 1.8 / 1.7 |
| i | 0.40 | 26.5 / 27.0 | 26.3 / 26.2 | 22.6 / 18.6 | 32.0 / 27.0 | 25.0 / 21.8 |
| is | 0.32 | 10.1 / 10.1 | 8.5 / 8.8 | 9.7 / 8.9 | 10.9 / 10.1 | 11.5 / 9.7 |
| than | 0.31 | 1.5 / 1.5 | 1.9 / 1.4 | 1.3 / 1.5 | 1.3 / 1.5 | 1.5 / 1.7 |
| here | 0.28 | 2.1 / 2.1 | 3.5 / 3.5 | 4.5 / 4.0 | 2.6 / 2.1 | 3.4 / 3.3 |
| where | 0.24 | 2.4 / 2.4 | 1.5 / 1.4 | 2.5 / 2.2 | 2.6 / 2.4 | 1.4 / 1.2 |
| let | 0.24 | 2.2 / 2.2 | 4.0 / 4.0 | 3.3 / 3.1 | 2.4 / 2.2 | 3.9 / 3.4 |
| then | 0.23 | 4.1 / 4.0 | 4.0 / 4.4 | 4.4 / 4.3 | 4.2 / 4.0 | 3.2 / 3.1 |
| on | 0.21 | 3.3 / 3.6 | 2.4 / 2.5 | 3.5 / 3.4 | 3.3 / 3.6 | 3.3 / 3.4 |
| we | 0.20 | 3.2 / 3.2 | 5.2 / 5.2 | 3.8 / 3.7 | 3.4 / 3.2 | 7.3 / 6.3 |
