# Embedding geometry of the fine-tuned GPT-2 author models

Word list: 400 whole-word, lower-case GPT-2 tokens that occur at least 3 times in every model's training text (ranked by the smallest count across sets; names and sentence-initial forms excluded). Same models, seeds and token budget (78,818) as the task-vector test.

For each model the token-embedding rows of these words are taken and the pairwise cosine between every two words is computed. Three ways to compare two models:

1. **raw geometry**: correlation of the two pairwise-cosine matrices. Expected near 1 for every pair, because the pretrained geometry barely moves at this budget; reported to show that the raw distances carry no information about the fine-tune.
2. **change in geometry** (the relative-embedding test): correlation of the change in pairwise cosine from pretrained, model vs model. Coordinate-free: it asks whether the two fine-tunes moved the same word pairs closer together or further apart, whatever happened to the absolute vectors.
3. **embedding delta**: cosine between the two models' (fine-tuned − pretrained) embedding rows for these words. The embedding-layer counterpart of the task-vector cosine (which excluded embeddings).

Read every number against the controls: seed-only pairs are the ceiling, same-author-different-plays pairs are the author signal, different-author pairs are the floor. If same-author pairs do not sit above different-author pairs, the geometry records text and register, not author.

## Key pairs

| pair | type | change in geometry | embedding delta | raw geometry |
|---|---|---|---|---|
| Marlowe_s1 vs Marlowe_s2 | seed only, same data: Marlowe s1 vs s2 | 0.937 | 0.898 | 1.0000 |
| ShLater_s1 vs ShLater_s2 | seed only, same data: Shakespeare-later s1 vs s2 | 0.932 | 0.887 | 1.0000 |
| Marlowe_A vs Marlowe_B | same author, different plays: Marlowe A vs B | 0.457 | 0.330 | 1.0000 |
| ShLater_A vs ShLater_B | same author, different plays: Shakespeare-later A vs B | 0.399 | 0.304 | 0.9999 |
| ShEarlyNonH6 vs ShLater_s1 | same author, different period: Shakespeare early (non-H6) vs later | 0.386 | 0.301 | 0.9999 |
| Marlowe_s1 vs ShEarlyNonH6 | QUESTION: Marlowe vs Shakespeare early (non-H6) | 0.414 | 0.294 | 0.9999 |
| Marlowe_s1 vs ShLater_s1 | QUESTION: Marlowe vs Shakespeare later | 0.355 | 0.248 | 0.9999 |
| Marlowe_s1 vs Greene | different, same register: Marlowe vs Greene | 0.430 | 0.319 | 1.0000 |
| Marlowe_s1 vs Peele | different, same register: Marlowe vs Peele | 0.447 | 0.317 | 1.0000 |
| Marlowe_s1 vs AnonHeroic | different, same register: Marlowe vs anonymous heroic | 0.460 | 0.338 | 1.0000 |
| Greene vs Peele | different: Greene vs Peele | 0.383 | 0.285 | 1.0000 |
| ShEarlyNonH6 vs Greene | different: Shakespeare early (non-H6) vs Greene | 0.357 | 0.264 | 0.9999 |
| ShEarlyNonH6 vs Peele | different: Shakespeare early (non-H6) vs Peele | 0.379 | 0.254 | 0.9999 |
| ShLater_s1 vs Fletcher | different, different period: Shakespeare later vs Fletcher | 0.312 | 0.244 | 0.9999 |
| Marlowe_s1 vs Fletcher | different, different period: Marlowe vs Fletcher | 0.306 | 0.229 | 0.9999 |

## Change in geometry, all models

| | Marlowe_s1 | Marlowe_s2 | Marlowe_A | Marlowe_B | ShLater_s1 | ShLater_s2 | ShLater_A | ShLater_B | ShEarlyNonH6 | Greene | Peele | AnonHeroic | Fletcher |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marlowe_s1 | 1.000 | 0.937 | 0.672 | 0.743 | 0.355 | 0.349 | 0.371 | 0.323 | 0.414 | 0.430 | 0.447 | 0.460 | 0.306 |
| Marlowe_s2 | 0.937 | 1.000 | 0.684 | 0.735 | 0.361 | 0.358 | 0.369 | 0.344 | 0.415 | 0.441 | 0.442 | 0.469 | 0.322 |
| Marlowe_A | 0.672 | 0.684 | 1.000 | 0.457 | 0.328 | 0.325 | 0.337 | 0.304 | 0.376 | 0.407 | 0.423 | 0.426 | 0.276 |
| Marlowe_B | 0.743 | 0.735 | 0.457 | 1.000 | 0.363 | 0.358 | 0.366 | 0.346 | 0.441 | 0.430 | 0.426 | 0.458 | 0.297 |
| ShLater_s1 | 0.355 | 0.361 | 0.328 | 0.363 | 1.000 | 0.932 | 0.658 | 0.675 | 0.386 | 0.323 | 0.283 | 0.363 | 0.312 |
| ShLater_s2 | 0.349 | 0.358 | 0.325 | 0.358 | 0.932 | 1.000 | 0.660 | 0.666 | 0.375 | 0.328 | 0.278 | 0.366 | 0.313 |
| ShLater_A | 0.371 | 0.369 | 0.337 | 0.366 | 0.658 | 0.660 | 1.000 | 0.399 | 0.430 | 0.354 | 0.306 | 0.385 | 0.308 |
| ShLater_B | 0.323 | 0.344 | 0.304 | 0.346 | 0.675 | 0.666 | 0.399 | 1.000 | 0.377 | 0.312 | 0.257 | 0.339 | 0.333 |
| ShEarlyNonH6 | 0.414 | 0.415 | 0.376 | 0.441 | 0.386 | 0.375 | 0.430 | 0.377 | 1.000 | 0.357 | 0.379 | 0.406 | 0.316 |
| Greene | 0.430 | 0.441 | 0.407 | 0.430 | 0.323 | 0.328 | 0.354 | 0.312 | 0.357 | 1.000 | 0.383 | 0.446 | 0.279 |
| Peele | 0.447 | 0.442 | 0.423 | 0.426 | 0.283 | 0.278 | 0.306 | 0.257 | 0.379 | 0.383 | 1.000 | 0.409 | 0.299 |
| AnonHeroic | 0.460 | 0.469 | 0.426 | 0.458 | 0.363 | 0.366 | 0.385 | 0.339 | 0.406 | 0.446 | 0.409 | 1.000 | 0.298 |
| Fletcher | 0.306 | 0.322 | 0.276 | 0.297 | 0.312 | 0.313 | 0.308 | 0.333 | 0.316 | 0.279 | 0.299 | 0.298 | 1.000 |

## Embedding delta cosine, all models

| | Marlowe_s1 | Marlowe_s2 | Marlowe_A | Marlowe_B | ShLater_s1 | ShLater_s2 | ShLater_A | ShLater_B | ShEarlyNonH6 | Greene | Peele | AnonHeroic | Fletcher |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Marlowe_s1 | 1.000 | 0.898 | 0.589 | 0.662 | 0.248 | 0.246 | 0.269 | 0.218 | 0.294 | 0.319 | 0.317 | 0.338 | 0.229 |
| Marlowe_s2 | 0.898 | 1.000 | 0.593 | 0.657 | 0.248 | 0.246 | 0.266 | 0.220 | 0.292 | 0.322 | 0.318 | 0.337 | 0.231 |
| Marlowe_A | 0.589 | 0.593 | 1.000 | 0.330 | 0.224 | 0.223 | 0.238 | 0.196 | 0.256 | 0.296 | 0.314 | 0.306 | 0.202 |
| Marlowe_B | 0.662 | 0.657 | 0.330 | 1.000 | 0.248 | 0.247 | 0.270 | 0.226 | 0.306 | 0.307 | 0.309 | 0.335 | 0.227 |
| ShLater_s1 | 0.248 | 0.248 | 0.224 | 0.248 | 1.000 | 0.887 | 0.571 | 0.604 | 0.301 | 0.223 | 0.195 | 0.242 | 0.244 |
| ShLater_s2 | 0.246 | 0.246 | 0.223 | 0.247 | 0.887 | 1.000 | 0.566 | 0.598 | 0.298 | 0.224 | 0.195 | 0.242 | 0.246 |
| ShLater_A | 0.269 | 0.266 | 0.238 | 0.270 | 0.571 | 0.566 | 1.000 | 0.304 | 0.318 | 0.236 | 0.216 | 0.258 | 0.236 |
| ShLater_B | 0.218 | 0.220 | 0.196 | 0.226 | 0.604 | 0.598 | 0.304 | 1.000 | 0.288 | 0.206 | 0.186 | 0.219 | 0.243 |
| ShEarlyNonH6 | 0.294 | 0.292 | 0.256 | 0.306 | 0.301 | 0.298 | 0.318 | 0.288 | 1.000 | 0.264 | 0.254 | 0.283 | 0.236 |
| Greene | 0.319 | 0.322 | 0.296 | 0.307 | 0.223 | 0.224 | 0.236 | 0.206 | 0.264 | 1.000 | 0.285 | 0.325 | 0.211 |
| Peele | 0.317 | 0.318 | 0.314 | 0.309 | 0.195 | 0.195 | 0.216 | 0.186 | 0.254 | 0.285 | 1.000 | 0.302 | 0.202 |
| AnonHeroic | 0.338 | 0.337 | 0.306 | 0.335 | 0.242 | 0.242 | 0.258 | 0.219 | 0.283 | 0.325 | 0.302 | 1.000 | 0.221 |
| Fletcher | 0.229 | 0.231 | 0.202 | 0.227 | 0.244 | 0.246 | 0.236 | 0.243 | 0.236 | 0.211 | 0.202 | 0.221 | 1.000 |

## How much each model moved the geometry

Mean absolute change in pairwise cosine from pretrained, over all word pairs.

| model | mean abs change |
|---|---|
| Marlowe_s1 | 0.00055 |
| Marlowe_s2 | 0.00055 |
| Marlowe_A | 0.00053 |
| Marlowe_B | 0.00052 |
| ShLater_s1 | 0.00055 |
| ShLater_s2 | 0.00054 |
| ShLater_A | 0.00053 |
| ShLater_B | 0.00055 |
| ShEarlyNonH6 | 0.00055 |
| Greene | 0.00050 |
| Peele | 0.00048 |
| AnonHeroic | 0.00051 |
| Fletcher | 0.00056 |

## The words

the, and, to, of, my, a, in, that, be, with, this, me, for, your, is, you, his, not, thou, will, he, as, have, all, thee, thy, it, him, shall, so, by, from, we, on, at, our, are, now, but, or, her, their, what, may, if, love, make, d, no, us, am, let, do, here, these, see, was, upon, then, man, would, come, should, she, can, such, more, take, when, where, out, they, than, like, up, one, how, go, life, say, know, w, heart, give, must, mine, good, there, had, were, some, them, hath, time, never, well, art, men, think, th, did, an, tell, down, name, great, hand, any, hear, too, day, thus, yet, away, which, leave, much, world, made, nor, fear, death, before, into, live, rest, father, keep, fair, both, still, heaven, head, look, blood, hands, dead, friends, long, first, been, m, f, t, once, ever, little, far, set, hast, poor, might, against, every, again, other, sir, sweet, whose, speak, cannot, true, mind, night, stand, could, un, r, e, noble, bear, myself, cause, comes, done, hold, mean, since, those, earth, bring, fire, though, many, being, two, about, grief, grace, till, seek, lives, sure, within, why, old, part, g, l, hence, unto, thoughts, soul, die, wife, eyes, words, fall, else, face, makes, means, near, left, full, best, turn, own, want, off, st, n, h, b, gentle, welcome, forth, eye, gone, hope, stay, wrong, himself, young, put, run, last, call, way, through, said, who, fortune, dear, sight, lie, fly, arms, none, serve, house, nothing, meet, friend, better, place, another, high, ent, show, end, back, joy, whom, save, looks, ground, sit, came, power, while, right, most, over, de, ha, p, shalt, farewell, wit, pray, pleasure, kiss, bid, sin, doubt, faith, sleep, charge, boy, worth, lost, wind, sound, thought, seen, talk, country, change, home, hard, find, fl, under, get, sc, v, dare, sword, thousand, desire, prove, thank, lose, peace, bed, brother, alone, son, command, base, walk, break, common, service, sent, given, body, enough, return, without, state, each, help, same, use, after, dis, j, pl, haste, pardon, maid, lust, villain, bloody, royal, brave, wise, gro, duty, wear, rich, hate, daughter, enemy, therefore, straight, lay, send, please, draw, brought, chance, mother, late, content, saw, lo, half, black, cut, water, light, days, pass, met, three, follow, person, very, need, bet, qu, en, ch, s, presently, loving, yours, wound, loves, shame, glad, bow, mad, beauty, horse, lies, bes

