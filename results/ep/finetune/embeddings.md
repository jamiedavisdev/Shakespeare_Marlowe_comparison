# Embedding geometry of the fine-tuned GPT-2 author models

Word list: 400 whole-word, lower-case GPT-2 tokens that occur at least 3 times in every model's training text (ranked by the smallest count across sets; names and sentence-initial forms excluded). Same models, seeds and token budget (78,192) as the task-vector test.

For each model the token-embedding rows of these words are taken and the pairwise cosine between every two words is computed. Three ways to compare two models:

1. **raw geometry**: correlation of the two pairwise-cosine matrices. Expected near 1 for every pair, because the pretrained geometry barely moves at this budget; reported to show that the raw distances carry no information about the fine-tune.
2. **change in geometry** (the relative-embedding test): correlation of the change in pairwise cosine from pretrained, model vs model. Coordinate-free: it asks whether the two fine-tunes moved the same word pairs closer together or further apart, whatever happened to the absolute vectors.
3. **embedding delta**: cosine between the two models' (fine-tuned − pretrained) embedding rows for these words. The embedding-layer counterpart of the task-vector cosine (which excluded embeddings).

Read every number against the controls: seed-only pairs are the ceiling, same-author-different-plays pairs are the author signal, different-author pairs are the floor. If same-author pairs do not sit above different-author pairs, the geometry records text and register, not author.

## Key pairs

| pair | type | change in geometry | embedding delta | raw geometry |
|---|---|---|---|---|
| Marlowe_s1 vs Marlowe_s2 | seed only, same data: Marlowe s1 vs s2 | 0.941 | 0.898 | 1.0000 |
| ShLater_s1 vs ShLater_s2 | seed only, same data: Shakespeare-later s1 vs s2 | 0.931 | 0.887 | 1.0000 |
| Marlowe_A vs Marlowe_B | same author, different plays: Marlowe A vs B | 0.452 | 0.333 | 1.0000 |
| ShLater_A vs ShLater_B | same author, different plays: Shakespeare-later A vs B | 0.402 | 0.309 | 1.0000 |
| ShEarlyNonH6 vs ShLater_s1 | same author, different period: Shakespeare early (non-H6) vs later | 0.387 | 0.318 | 0.9999 |
| Marlowe_s1 vs ShEarlyNonH6 | QUESTION: Marlowe vs Shakespeare early (non-H6) | 0.437 | 0.318 | 0.9999 |
| Marlowe_s1 vs ShLater_s1 | QUESTION: Marlowe vs Shakespeare later | 0.373 | 0.270 | 0.9999 |
| Marlowe_s1 vs Greene | different, same register: Marlowe vs Greene | 0.447 | 0.334 | 1.0000 |
| Marlowe_s1 vs Peele | different, same register: Marlowe vs Peele | 0.450 | 0.320 | 1.0000 |
| Marlowe_s1 vs AnonHeroic | different, same register: Marlowe vs anonymous heroic | 0.462 | 0.347 | 1.0000 |
| Greene vs Peele | different: Greene vs Peele | 0.391 | 0.290 | 1.0000 |
| ShEarlyNonH6 vs Greene | different: Shakespeare early (non-H6) vs Greene | 0.386 | 0.297 | 0.9999 |
| ShEarlyNonH6 vs Peele | different: Shakespeare early (non-H6) vs Peele | 0.383 | 0.273 | 1.0000 |

## Change in geometry, all models

| | Marlowe_s1 | Marlowe_s2 | Marlowe_A | Marlowe_B | ShLater_s1 | ShLater_s2 | ShLater_A | ShLater_B | ShEarlyNonH6 | Greene | Peele | AnonHeroic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marlowe_s1 | 1.000 | 0.941 | 0.675 | 0.752 | 0.373 | 0.381 | 0.386 | 0.362 | 0.437 | 0.447 | 0.450 | 0.462 |
| Marlowe_s2 | 0.941 | 1.000 | 0.675 | 0.749 | 0.373 | 0.383 | 0.377 | 0.356 | 0.440 | 0.443 | 0.448 | 0.461 |
| Marlowe_A | 0.675 | 0.675 | 1.000 | 0.452 | 0.328 | 0.335 | 0.335 | 0.306 | 0.389 | 0.415 | 0.435 | 0.430 |
| Marlowe_B | 0.752 | 0.749 | 0.452 | 1.000 | 0.363 | 0.375 | 0.371 | 0.358 | 0.455 | 0.419 | 0.430 | 0.446 |
| ShLater_s1 | 0.373 | 0.373 | 0.328 | 0.363 | 1.000 | 0.931 | 0.662 | 0.671 | 0.387 | 0.333 | 0.301 | 0.374 |
| ShLater_s2 | 0.381 | 0.383 | 0.335 | 0.375 | 0.931 | 1.000 | 0.651 | 0.669 | 0.386 | 0.332 | 0.313 | 0.373 |
| ShLater_A | 0.386 | 0.377 | 0.335 | 0.371 | 0.662 | 0.651 | 1.000 | 0.402 | 0.414 | 0.363 | 0.338 | 0.379 |
| ShLater_B | 0.362 | 0.356 | 0.306 | 0.358 | 0.671 | 0.669 | 0.402 | 1.000 | 0.378 | 0.314 | 0.284 | 0.339 |
| ShEarlyNonH6 | 0.437 | 0.440 | 0.389 | 0.455 | 0.387 | 0.386 | 0.414 | 0.378 | 1.000 | 0.386 | 0.383 | 0.403 |
| Greene | 0.447 | 0.443 | 0.415 | 0.419 | 0.333 | 0.332 | 0.363 | 0.314 | 0.386 | 1.000 | 0.391 | 0.458 |
| Peele | 0.450 | 0.448 | 0.435 | 0.430 | 0.301 | 0.313 | 0.338 | 0.284 | 0.383 | 0.391 | 1.000 | 0.409 |
| AnonHeroic | 0.462 | 0.461 | 0.430 | 0.446 | 0.374 | 0.373 | 0.379 | 0.339 | 0.403 | 0.458 | 0.409 | 1.000 |

## Embedding delta cosine, all models

| | Marlowe_s1 | Marlowe_s2 | Marlowe_A | Marlowe_B | ShLater_s1 | ShLater_s2 | ShLater_A | ShLater_B | ShEarlyNonH6 | Greene | Peele | AnonHeroic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marlowe_s1 | 1.000 | 0.898 | 0.581 | 0.679 | 0.270 | 0.279 | 0.286 | 0.241 | 0.318 | 0.334 | 0.320 | 0.347 |
| Marlowe_s2 | 0.898 | 1.000 | 0.585 | 0.676 | 0.271 | 0.280 | 0.284 | 0.242 | 0.320 | 0.334 | 0.321 | 0.350 |
| Marlowe_A | 0.581 | 0.585 | 1.000 | 0.333 | 0.233 | 0.241 | 0.247 | 0.207 | 0.271 | 0.311 | 0.315 | 0.311 |
| Marlowe_B | 0.679 | 0.676 | 0.333 | 1.000 | 0.268 | 0.275 | 0.281 | 0.248 | 0.329 | 0.322 | 0.313 | 0.345 |
| ShLater_s1 | 0.270 | 0.271 | 0.233 | 0.268 | 1.000 | 0.887 | 0.583 | 0.601 | 0.318 | 0.239 | 0.210 | 0.263 |
| ShLater_s2 | 0.279 | 0.280 | 0.241 | 0.275 | 0.887 | 1.000 | 0.580 | 0.602 | 0.323 | 0.244 | 0.216 | 0.270 |
| ShLater_A | 0.286 | 0.284 | 0.247 | 0.281 | 0.583 | 0.580 | 1.000 | 0.309 | 0.338 | 0.258 | 0.235 | 0.280 |
| ShLater_B | 0.241 | 0.242 | 0.207 | 0.248 | 0.601 | 0.602 | 0.309 | 1.000 | 0.295 | 0.220 | 0.198 | 0.233 |
| ShEarlyNonH6 | 0.318 | 0.320 | 0.271 | 0.329 | 0.318 | 0.323 | 0.338 | 0.295 | 1.000 | 0.297 | 0.273 | 0.304 |
| Greene | 0.334 | 0.334 | 0.311 | 0.322 | 0.239 | 0.244 | 0.258 | 0.220 | 0.297 | 1.000 | 0.290 | 0.330 |
| Peele | 0.320 | 0.321 | 0.315 | 0.313 | 0.210 | 0.216 | 0.235 | 0.198 | 0.273 | 0.290 | 1.000 | 0.297 |
| AnonHeroic | 0.347 | 0.350 | 0.311 | 0.345 | 0.263 | 0.270 | 0.280 | 0.233 | 0.304 | 0.330 | 0.297 | 1.000 |

## How much each model moved the geometry

Mean absolute change in pairwise cosine from pretrained, over all word pairs.

| model | mean abs change |
|---|---|
| Marlowe_s1 | 0.00055 |
| Marlowe_s2 | 0.00054 |
| Marlowe_A | 0.00052 |
| Marlowe_B | 0.00050 |
| ShLater_s1 | 0.00051 |
| ShLater_s2 | 0.00052 |
| ShLater_A | 0.00050 |
| ShLater_B | 0.00053 |
| ShEarlyNonH6 | 0.00053 |
| Greene | 0.00050 |
| Peele | 0.00047 |
| AnonHeroic | 0.00051 |

## The words

the, to, and, of, my, in, a, with, that, be, his, me, this, for, is, your, you, not, thou, he, will, have, as, all, thee, thy, it, him, shall, so, by, from, we, on, our, at, are, now, but, or, their, her, may, if, what, make, hath, d, let, no, us, these, am, do, was, here, see, love, upon, where, man, she, them, come, then, would, such, should, how, than, more, can, take, when, they, like, up, out, one, go, w, must, say, know, give, heart, mine, good, some, there, had, were, time, never, well, art, think, did, great, th, death, men, down, any, an, tell, life, hear, hand, thus, yet, away, which, leave, much, day, made, before, every, into, nor, fear, live, too, name, keep, rest, fair, both, still, f, poor, dead, stand, far, set, call, look, first, been, mind, once, means, ever, world, again, t, hast, forth, whom, blood, why, little, might, against, long, could, other, v, sir, whose, hands, cannot, himself, true, night, mean, though, un, e, shalt, sweet, myself, speak, cause, comes, makes, done, hold, since, head, many, part, m, b, hence, ye, bear, bring, fall, fire, full, high, those, being, through, two, about, n, till, joy, seek, lives, sure, within, came, old, j, g, thoughts, serve, son, eyes, hope, words, else, face, near, left, best, put, while, ent, own, way, want, off, said, gentle, welcome, eye, gone, father, stay, young, turn, run, last, back, over, who, r, st, grief, honour, dear, unto, grace, sight, soul, none, therefore, wrong, house, nothing, sound, meet, friend, return, better, place, another, show, end, sc, ha, l, h, p, haste, pardon, wit, villain, pray, thousand, lie, fly, doubt, save, looks, worth, base, ground, sit, right, most, dis, de, farewell, borne, pleasure, bid, rich, earth, sleep, lost, friends, wind, thought, seen, water, change, home, hard, power, find, same, under, get, dare, fortune, bloody, kiss, sword, gro, prove, thank, faith, lose, peace, bed, brother, charge, send, wife, alone, please, brought, command, gave, walk, lo, foot, break, service, sent, given, body, enough, talk, without, pass, each, help, use, after, en, pl, s, gracious, presently, lust, noble, brave, cheer, hearts, heaven, mad, breath, sin, duty, desire, wear, strike, hate, daughter, die, wish, lay, hundred, cast, draw, chance, late, content, soon, saw, half, fight, light, word, days, free, met, three, follow, person, found, very, years, need, bet, only, ch, fetch, foul, loving, yours, tears, wise

