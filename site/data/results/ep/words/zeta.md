# Burrows's Zeta: marker-word tests

2,000-word chunks, proper nouns removed, candidate words present in >= 5 plays, 150 markers per side. Markers are chosen with the scored play and its family held out. Chunks are classified by nearest training centroid in (share of A-markers, share of B-markers). Read the question pairs against the benchmarks.

| pair | type | plays | chunks | accuracy | AUC |
|---|---|---|---|---|---|
| Marlowe vs Shakespeare early, Henry VI excluded | QUESTION | 7 vs 5 | 94 | 0.85 | 0.93 |
| Marlowe vs Henry VI 1-3 | QUESTION | 7 vs 3 | 78 | 0.58 | 0.63 |
| Marlowe vs Shakespeare early (all 8) | QUESTION | 7 vs 8 | 124 | 0.63 | 0.70 |
| Marlowe vs Shakespeare later | QUESTION | 7 vs 11 | 156 | 0.94 | 0.98 |
| Shakespeare early (all 8) vs Shakespeare later | SAME-AUTHOR | 8 vs 11 | 184 | 0.57 | 0.59 |
| Shakespeare early, Henry VI excluded vs Shakespeare later | SAME-AUTHOR | 5 vs 11 | 154 | 0.69 | 0.71 |
| Marlowe 1587-89 vs Marlowe 1589-93 | SAME-AUTHOR | 3 vs 4 | 48 | 0.52 | 0.23 |
| Shakespeare 1595-97 vs Shakespeare 1599-1611 | SAME-AUTHOR | 5 vs 6 | 108 | 0.72 | 0.82 |
| Henry VI 1-3 vs Shakespeare early, Henry VI excluded | SAME-AUTHOR? | 3 vs 5 | 63 | 0.79 | 0.87 |
| Greene vs Peele | DIFFERENT | 4 vs 4 | 49 | 0.43 | 0.36 |
| Marlowe vs Greene | DIFFERENT | 7 vs 4 | 74 | 0.69 | 0.62 |
| Marlowe vs Peele | DIFFERENT | 7 vs 4 | 71 | 0.54 | 0.35 |
| Marlowe vs Anonymous heroic | DIFFERENT | 7 vs 8 | 107 | 0.57 | 0.48 |
| Henry VI 1-3 vs Greene | DIFFERENT | 3 vs 4 | 56 | 0.61 | 0.64 |
| Henry VI 1-3 vs Peele | DIFFERENT | 3 vs 4 | 53 | 0.68 | 0.76 |
| Shakespeare early, Henry VI excluded vs Greene | DIFFERENT | 5 vs 4 | 72 | 0.71 | 0.81 |
| Shakespeare early, Henry VI excluded vs Peele | DIFFERENT | 5 vs 4 | 69 | 0.80 | 0.76 |

## Per-play results (share of chunks placed with set A)

### Marlowe (A) vs Shakespeare early, Henry VI excluded (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 1.00 | 0.326 | 0.163 |
| 2Tam (Marlowe) | A | 8 | 1.00 | 0.337 | 0.139 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.326 | 0.230 |
| DrFaust (Marlowe) | A | 5 | 1.00 | 0.272 | 0.233 |
| JoM (Marlowe) | A | 8 | 0.38 | 0.260 | 0.284 |
| Ed2 (Marlowe) | A | 9 | 0.56 | 0.247 | 0.253 |
| MP (Marlowe) | A | 4 | 1.00 | 0.308 | 0.255 |
| Tit (Shakespeare) | B | 9 | 0.33 | 0.239 | 0.293 |
| R3 (Shakespeare) | B | 13 | 0.15 | 0.227 | 0.299 |
| Shr (Shakespeare) | B | 9 | 0.00 | 0.170 | 0.314 |
| TGV (Shakespeare) | B | 8 | 0.00 | 0.185 | 0.306 |
| Err (Shakespeare) | B | 7 | 0.00 | 0.182 | 0.358 |

Markers for A: ay, straight, die, pride, power, ye, cruel, jove, cast, fire, through, speech, hundred, base, enough, overthrow, thanks, greater, lie, wherein, content, martial, pierce, methinks, view, soul, force, brave, rich, follow

Markers for B: marry, tongue, indeed, wife, morrow, very, reason, mad, patience, bid, fault, jest, strait, patiented, hours, woe, merry, tender, gentle, withal, hour, cold, plead, hark, true, knowst, signior, even, own, word

### Marlowe (A) vs Henry VI 1-3 (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.50 | 0.246 | 0.266 |
| 2Tam (Marlowe) | A | 8 | 0.75 | 0.240 | 0.245 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.258 | 0.243 |
| DrFaust (Marlowe) | A | 5 | 0.80 | 0.216 | 0.201 |
| JoM (Marlowe) | A | 8 | 0.38 | 0.217 | 0.296 |
| Ed2 (Marlowe) | A | 9 | 0.67 | 0.206 | 0.250 |
| MP (Marlowe) | A | 4 | 1.00 | 0.235 | 0.238 |
| 1H6 (Shakespeare) | B | 9 | 0.33 | 0.221 | 0.321 |
| 2H6 (Shakespeare) | B | 11 | 0.91 | 0.212 | 0.261 |
| 3H6 (Shakespeare) | B | 10 | 0.50 | 0.214 | 0.277 |

Markers for A: ay, die, straight, cast, fetch, rich, jove, damned, wherein, present, serve, greater, ye, pearl, pierce, cruel, power, fire, vain, fiery, pride, hang, wealth, hundred, wait, walk, poison, besides, runs, ears

Markers for B: thinks, dye, peace, john, tongue, answer, virtuous, reason, help, ne'er, tender, sign, fight, broke, knee, truth, loss, together, intent, lost, courage, right, forbidden, valiant, ten, crowned, yield, strife, woman, bold

### Marlowe (A) vs Shakespeare early (all 8) (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.75 | 0.279 | 0.202 |
| 2Tam (Marlowe) | A | 8 | 0.75 | 0.297 | 0.177 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.292 | 0.236 |
| DrFaust (Marlowe) | A | 5 | 0.60 | 0.251 | 0.237 |
| JoM (Marlowe) | A | 8 | 0.00 | 0.232 | 0.300 |
| Ed2 (Marlowe) | A | 9 | 0.56 | 0.233 | 0.247 |
| MP (Marlowe) | A | 4 | 0.50 | 0.265 | 0.260 |
| 1H6 (Shakespeare) | B | 9 | 0.89 | 0.301 | 0.265 |
| 2H6 (Shakespeare) | B | 11 | 0.64 | 0.266 | 0.273 |
| 3H6 (Shakespeare) | B | 10 | 0.70 | 0.287 | 0.279 |
| Tit (Shakespeare) | B | 9 | 0.22 | 0.230 | 0.286 |
| R3 (Shakespeare) | B | 13 | 0.15 | 0.227 | 0.299 |
| Shr (Shakespeare) | B | 9 | 0.00 | 0.150 | 0.299 |
| TGV (Shakespeare) | B | 8 | 0.00 | 0.154 | 0.299 |
| Err (Shakespeare) | B | 7 | 0.00 | 0.174 | 0.330 |

Markers for A: ay, straight, die, pride, cast, power, jove, ye, cruel, rich, fire, wherein, greater, hundred, pierce, lie, hang, martial, torments, enough, vain, methinks, perish, overthrow, conquering, fiery, pull, damned, base, poison

Markers for B: tongue, marry, reason, very, indeed, dye, peace, tender, wife, morrow, thinks, patience, ne'er, patiented, virtuous, strait, even, woman, truth, mad, fault, together, dost, hour, help, cold, jest, woe, hither, merry

### Marlowe (A) vs Shakespeare later (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 1.00 | 0.310 | 0.205 |
| 2Tam (Marlowe) | A | 8 | 1.00 | 0.305 | 0.197 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.309 | 0.267 |
| DrFaust (Marlowe) | A | 5 | 0.80 | 0.267 | 0.300 |
| JoM (Marlowe) | A | 8 | 0.38 | 0.259 | 0.343 |
| Ed2 (Marlowe) | A | 9 | 0.89 | 0.275 | 0.269 |
| MP (Marlowe) | A | 4 | 1.00 | 0.303 | 0.287 |
| R2 (Shakespeare) | B | 10 | 0.20 | 0.235 | 0.335 |
| MND (Shakespeare) | B | 7 | 0.00 | 0.210 | 0.406 |
| Rom (Shakespeare) | B | 11 | 0.00 | 0.205 | 0.412 |
| MV (Shakespeare) | B | 10 | 0.00 | 0.169 | 0.409 |
| 1H4 (Shakespeare) | B | 11 | 0.00 | 0.176 | 0.387 |
| JC (Shakespeare) | B | 9 | 0.00 | 0.180 | 0.407 |
| Ham (Shakespeare) | B | 13 | 0.00 | 0.173 | 0.456 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.183 | 0.415 |
| Lr (Shakespeare) | B | 11 | 0.00 | 0.173 | 0.449 |
| WT (Shakespeare) | B | 11 | 0.00 | 0.147 | 0.421 |
| Tmp (Shakespeare) | B | 7 | 0.00 | 0.185 | 0.438 |

Markers for A: ay, die, straight, pride, unto, jove, lives, vain, thousand, base, yield, ye, perish, wealth, wrath, hope, mighty, serve, overthrow, conquered, soul, greater, fury, charge, martial, force, conquering, revenge, wherein, slain

Markers for B: indeed, tongue, very, hour, itself, business, mark, three, own, mad, beseech, truth, find, fellow, morrow, old, does, even, reason, matter, ear, two, answer, purpose, thing, dear, known, together, better, between

### Shakespeare early (all 8) (A) vs Shakespeare later (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.11 | 0.239 | 0.350 |
| 2H6 (Shakespeare) | A | 11 | 0.09 | 0.236 | 0.344 |
| 3H6 (Shakespeare) | A | 10 | 0.20 | 0.250 | 0.317 |
| Tit (Shakespeare) | A | 9 | 0.89 | 0.245 | 0.251 |
| R3 (Shakespeare) | A | 13 | 0.15 | 0.229 | 0.333 |
| Shr (Shakespeare) | A | 9 | 0.11 | 0.204 | 0.309 |
| TGV (Shakespeare) | A | 8 | 0.50 | 0.218 | 0.283 |
| Err (Shakespeare) | A | 7 | 0.43 | 0.214 | 0.290 |
| R2 (Shakespeare) | B | 10 | 1.00 | 0.309 | 0.275 |
| MND (Shakespeare) | B | 7 | 0.14 | 0.251 | 0.344 |
| Rom (Shakespeare) | B | 11 | 0.27 | 0.244 | 0.326 |
| MV (Shakespeare) | B | 10 | 0.40 | 0.237 | 0.319 |
| 1H4 (Shakespeare) | B | 11 | 0.36 | 0.214 | 0.316 |
| JC (Shakespeare) | B | 9 | 0.33 | 0.211 | 0.335 |
| Ham (Shakespeare) | B | 13 | 0.00 | 0.199 | 0.386 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.208 | 0.364 |
| Lr (Shakespeare) | B | 11 | 0.00 | 0.207 | 0.376 |
| WT (Shakespeare) | B | 11 | 0.00 | 0.211 | 0.375 |
| Tmp (Shakespeare) | B | 7 | 0.00 | 0.224 | 0.391 |

Markers for A: unto, yield, plead, witness, sent, proud, because, sake, virtuous, long, belike, revenge, won, send, lives, sign, holy, haply, false, forward, hope, deadly, thinks, happy, loss, scorn, angry, help, whom, talk

Markers for B: does, itself, mark, something, show, ear, further, lie, lies, business, fire, nothing, strange, has, question, seem, fellow, part, put, o'er, three, things, themselves, find, em, without, alack, beseech, dear, th

### Shakespeare early, Henry VI excluded (A) vs Shakespeare later (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Tit (Shakespeare) | A | 9 | 0.11 | 0.223 | 0.281 |
| R3 (Shakespeare) | A | 13 | 0.15 | 0.229 | 0.333 |
| Shr (Shakespeare) | A | 9 | 0.22 | 0.220 | 0.344 |
| TGV (Shakespeare) | A | 8 | 0.50 | 0.253 | 0.296 |
| Err (Shakespeare) | A | 7 | 0.29 | 0.245 | 0.291 |
| R2 (Shakespeare) | B | 10 | 0.50 | 0.274 | 0.301 |
| MND (Shakespeare) | B | 7 | 0.14 | 0.227 | 0.370 |
| Rom (Shakespeare) | B | 11 | 0.36 | 0.267 | 0.343 |
| MV (Shakespeare) | B | 10 | 0.20 | 0.233 | 0.339 |
| 1H4 (Shakespeare) | B | 11 | 0.09 | 0.220 | 0.338 |
| JC (Shakespeare) | B | 9 | 0.00 | 0.214 | 0.371 |
| Ham (Shakespeare) | B | 13 | 0.00 | 0.202 | 0.384 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.205 | 0.385 |
| Lr (Shakespeare) | B | 11 | 0.00 | 0.196 | 0.397 |
| WT (Shakespeare) | B | 11 | 0.00 | 0.207 | 0.383 |
| Tmp (Shakespeare) | B | 7 | 0.00 | 0.245 | 0.389 |

Markers for A: plead, unto, witness, sake, sent, company, haply, knew, jest, long, withal, belike, send, deadly, holy, signior, she, because, wench, goodly, marry, scorn, cheer, mean, happy, thereof, bid, service, warrant, home

Markers for B: further, itself, mark, does, lie, question, speech, lies, fire, three, seem, only, enough, show, part, o'er, find, work, yea, something, known, answer, point, put, has, run, seek, already, strange, ear

### Marlowe 1587-89 (A) vs Marlowe 1589-93 (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.00 | 0.217 | 0.248 |
| 2Tam (Marlowe) | A | 8 | 0.00 | 0.228 | 0.247 |
| Dido (Marlowe) | A | 6 | 0.00 | 0.211 | 0.338 |
| DrFaust (Marlowe) | B | 5 | 0.20 | 0.184 | 0.325 |
| JoM (Marlowe) | B | 8 | 0.00 | 0.157 | 0.316 |
| Ed2 (Marlowe) | B | 9 | 0.00 | 0.214 | 0.273 |
| MP (Marlowe) | B | 4 | 0.00 | 0.237 | 0.368 |

Markers for A: jove, looks, eyes, feet, mighty, speech, martial, light, seat, worthy, sit, barbarous, watery, carcases, stout, cruel, conquered, warlike, feed, armed, wound, foe, wide, flames, highest, siege, wrath, pierce, conquering, terror

Markers for B: gone, done, please, speak, word, therefore, money, thing, hast, nay, trust, has, gentle, comes, ruled, resolute, tush, hither, read, pray, seeing, things, way, whilst, news, home, wish, yourself, true, very

### Shakespeare 1595-97 (A) vs Shakespeare 1599-1611 (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| R2 (Shakespeare) | A | 10 | 0.50 | 0.271 | 0.268 |
| MND (Shakespeare) | A | 7 | 0.71 | 0.302 | 0.279 |
| Rom (Shakespeare) | A | 11 | 0.91 | 0.284 | 0.258 |
| MV (Shakespeare) | A | 10 | 0.50 | 0.245 | 0.289 |
| 1H4 (Shakespeare) | A | 11 | 0.64 | 0.258 | 0.243 |
| JC (Shakespeare) | B | 9 | 0.56 | 0.290 | 0.279 |
| Ham (Shakespeare) | B | 13 | 0.31 | 0.236 | 0.346 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.242 | 0.341 |
| Lr (Shakespeare) | B | 11 | 0.18 | 0.248 | 0.356 |
| WT (Shakespeare) | B | 11 | 0.09 | 0.232 | 0.355 |
| Tmp (Shakespeare) | B | 7 | 0.14 | 0.259 | 0.360 |

Markers for A: unto, hours, fair, john, love's, gentle, rude, sake, back, soul, high, company, because, sad, swear, unless, next, soon, meet, kinsman, day, flower, stay, happy, ancient, sin, die, therefore, youth, morrow

Markers for B: has, does, th, em, free, speech, prithee, most, itself, fellow, fit, saw, seem, something, put, almost, command, business, known, toward, madness, own, between, work, strange, might, thing, thought, cast, hark

### Henry VI 1-3 (A) vs Shakespeare early, Henry VI excluded (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.89 | 0.361 | 0.237 |
| 2H6 (Shakespeare) | A | 11 | 0.36 | 0.301 | 0.267 |
| 3H6 (Shakespeare) | A | 10 | 0.80 | 0.333 | 0.271 |
| Tit (Shakespeare) | B | 9 | 0.33 | 0.276 | 0.267 |
| Shr (Shakespeare) | B | 9 | 0.00 | 0.199 | 0.289 |
| TGV (Shakespeare) | B | 8 | 0.00 | 0.199 | 0.307 |
| Err (Shakespeare) | B | 7 | 0.00 | 0.192 | 0.304 |

Markers for A: yield, fight, john, ten, foe, courage, brave, force, proud, only, quickly, crowned, lost, ground, thinks, answer, dare, valiant, further, through, fled, blood, thine, glorious, wounds, fly, strength, head, speech, raise

Markers for B: home, bid, knew, dear, fetch, present, plead, eye, morrow, indeed, word, kind, wife, own, dinner, wench, signior, business, company, please, going, self, walk, humour, comes, mad, withal, sake, marry, dull

### Greene (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Alphonsus (Greene) | A | 5 | 0.60 | 0.268 | 0.224 |
| Orlando (Greene) | A | 5 | 0.40 | 0.268 | 0.224 |
| FriarBacon (Greene) | A | 7 | 0.71 | 0.267 | 0.216 |
| JamesIV (Greene) | A | 9 | 0.33 | 0.268 | 0.251 |
| OWT (Peele) | B | 3 | 1.00 | 0.287 | 0.202 |
| Alcazar (Peele) | B | 5 | 0.60 | 0.211 | 0.225 |
| EdwardI (Peele) | B | 9 | 0.89 | 0.319 | 0.241 |
| David (Peele) | B | 6 | 0.17 | 0.218 | 0.280 |

Markers for A: place, fond, although, loves, simple, fancy, mark, only, ll, brook, sport, else, heard, yes, sirrah, wit, mind, warrant, yourself, canst, prove, fit, get, boast, mean, hap, high, favours, believe, frolic

Markers for B: strength, ye, beauteous, comfort, bear, sight, glory, hair, cast, flesh, ground, renowned, tops, young, behold, welcome, soft, bright, bones, passage, holy, lo, follow, sake, name, ears, fields, beat, bosom, pity

### Marlowe (A) vs Greene (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.88 | 0.237 | 0.192 |
| 2Tam (Marlowe) | A | 8 | 1.00 | 0.290 | 0.192 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.266 | 0.207 |
| DrFaust (Marlowe) | A | 5 | 0.80 | 0.252 | 0.225 |
| JoM (Marlowe) | A | 8 | 0.88 | 0.249 | 0.202 |
| Ed2 (Marlowe) | A | 9 | 1.00 | 0.277 | 0.205 |
| MP (Marlowe) | A | 4 | 1.00 | 0.293 | 0.223 |
| Alphonsus (Greene) | B | 5 | 0.80 | 0.257 | 0.232 |
| Orlando (Greene) | B | 5 | 0.60 | 0.235 | 0.245 |
| FriarBacon (Greene) | B | 7 | 0.57 | 0.188 | 0.215 |
| JamesIV (Greene) | B | 9 | 1.00 | 0.261 | 0.232 |

Markers for A: soul, ay, thousand, cast, being, pity, ye, enough, about, bear, ears, pierce, hateful, name, offer, strong, body, dies, again, blood, power, damned, having, poison, eternal, presently, hang, sake, cruel, sight

Markers for B: nought, daughter, merry, wife, fond, mark, trust, woe, fancy, although, proud, deem, found, tongue, frolic, dear, wrong, wend, lass, indeed, ill, wise, vouchsafe, boast, blade, sayest, thoughts, ready, same, try

### Marlowe (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.50 | 0.268 | 0.258 |
| 2Tam (Marlowe) | A | 8 | 0.38 | 0.253 | 0.274 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.302 | 0.229 |
| DrFaust (Marlowe) | A | 5 | 0.80 | 0.276 | 0.235 |
| JoM (Marlowe) | A | 8 | 1.00 | 0.298 | 0.208 |
| Ed2 (Marlowe) | A | 9 | 1.00 | 0.293 | 0.197 |
| MP (Marlowe) | A | 4 | 1.00 | 0.328 | 0.240 |
| OWT (Peele) | B | 3 | 1.00 | 0.333 | 0.251 |
| Alcazar (Peele) | B | 5 | 1.00 | 0.263 | 0.245 |
| EdwardI (Peele) | B | 9 | 1.00 | 0.349 | 0.251 |
| David (Peele) | B | 6 | 1.00 | 0.312 | 0.267 |

Markers for A: ay, stay, mean, die, th, ll, wherein, place, base, else, speech, heard, tears, speak, cannot, thence, pierce, knows, cut, death, loves, greater, grief, pardon, presently, jove, only, none, power, resolve

Markers for B: beauteous, wife, lo, glory, bones, welcome, soft, sing, bless, royalty, ground, young, forth, thanks, best, fight, comfort, erst, shine, beat, advise, chosen, anointed, joy, deed, just, counsel, promise, fields, tops

### Marlowe (A) vs Anonymous heroic (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.00 | 0.229 | 0.251 |
| 2Tam (Marlowe) | A | 8 | 0.25 | 0.244 | 0.223 |
| Dido (Marlowe) | A | 6 | 0.83 | 0.236 | 0.233 |
| DrFaust (Marlowe) | A | 5 | 0.40 | 0.215 | 0.255 |
| JoM (Marlowe) | A | 8 | 0.00 | 0.182 | 0.299 |
| Ed2 (Marlowe) | A | 9 | 0.44 | 0.199 | 0.275 |
| MP (Marlowe) | A | 4 | 0.25 | 0.215 | 0.278 |
| Soliman (Anon-Soliman) | B | 8 | 0.38 | 0.240 | 0.280 |
| Locrine (Anon-Locrine) | B | 7 | 0.57 | 0.242 | 0.263 |
| Selimus (Anon-Selimus) | B | 8 | 0.12 | 0.249 | 0.309 |
| TRKJ (Anon-TRKJ) | B | 6 | 0.00 | 0.200 | 0.321 |
| JackStraw (Anon-JackStraw) | B | 4 | 0.00 | 0.173 | 0.310 |
| EdwardIII (Anon-EdwardIII) | B | 9 | 0.33 | 0.259 | 0.291 |
| Arden (Anon-Arden) | B | 9 | 0.11 | 0.213 | 0.259 |
| TTR3 (Anon-TTR3) | B | 8 | 0.00 | 0.197 | 0.297 |

Markers for A: hundred, ye, jove, th, rich, means, pierce, soul, pride, kiss, treasury, runs, lives, hateful, looks, fury, seat, thousand, ride, pearl, presently, remain, fit, perish, meet, higher, jove's, slaves, entertain, turn

Markers for B: counsel, tongue, john, forward, took, ill, peace, brief, honest, case, coming, wife, better, faith, right, needs, forget, own, thinks, thing, among, true, try, certain, indeed, hour, young, fault, joy, dismal

### Henry VI 1-3 (A) vs Greene (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.89 | 0.318 | 0.200 |
| 2H6 (Shakespeare) | A | 11 | 0.64 | 0.289 | 0.198 |
| 3H6 (Shakespeare) | A | 10 | 0.80 | 0.297 | 0.192 |
| Alphonsus (Greene) | B | 5 | 0.80 | 0.271 | 0.197 |
| Orlando (Greene) | B | 5 | 0.40 | 0.199 | 0.237 |
| FriarBacon (Greene) | B | 7 | 0.29 | 0.195 | 0.232 |
| JamesIV (Greene) | B | 9 | 0.78 | 0.324 | 0.220 |

Markers for A: john, ne'er, dye, thinks, enemies, strength, spirit, strong, open, blood, answer, off, soul, along, whiles, ten, pity, quickly, being, peace, foul, speak, reason, shame, again, forbear, body, reign, longer, after

Markers for B: nought, frolic, dear, fit, lovely, fancy, entertain, jove, advise, thoughts, lest, mark, die, merry, wealth, greater, daughter, show, silver, deem, loves, fare, lass, wend, wise, beauty, fond, past, put, strange

### Henry VI 1-3 (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.89 | 0.378 | 0.209 |
| 2H6 (Shakespeare) | A | 11 | 0.91 | 0.295 | 0.224 |
| 3H6 (Shakespeare) | A | 10 | 1.00 | 0.354 | 0.209 |
| OWT (Peele) | B | 3 | 0.67 | 0.282 | 0.218 |
| Alcazar (Peele) | B | 5 | 0.20 | 0.208 | 0.243 |
| EdwardI (Peele) | B | 9 | 1.00 | 0.328 | 0.264 |
| David (Peele) | B | 6 | 0.50 | 0.279 | 0.269 |

Markers for A: dye, ne'er, thinks, answer, speak, place, tears, else, heard, peace, myself, whiles, stay, ll, intent, virtuous, thine, off, only, false, strong, th, yield, able, knee, thought, till, talk, tongue, sign

Markers for B: beauteous, thanks, ye, fields, mighty, silver, welcome, knowest, erst, advise, cast, hair, sacred, tops, lovely, lo, pass, rich, bright, sing, shine, brought, follow, nought, damned, store, cursed, fire, lusty, bounds

### Shakespeare early, Henry VI excluded (A) vs Greene (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Tit (Shakespeare) | A | 9 | 0.78 | 0.311 | 0.210 |
| R3 (Shakespeare) | A | 13 | 0.92 | 0.319 | 0.194 |
| Shr (Shakespeare) | A | 9 | 1.00 | 0.296 | 0.207 |
| TGV (Shakespeare) | A | 8 | 1.00 | 0.306 | 0.184 |
| Err (Shakespeare) | A | 7 | 1.00 | 0.331 | 0.167 |
| Alphonsus (Greene) | B | 5 | 0.80 | 0.269 | 0.235 |
| Orlando (Greene) | B | 5 | 0.20 | 0.197 | 0.277 |
| FriarBacon (Greene) | B | 7 | 0.71 | 0.223 | 0.252 |
| JamesIV (Greene) | B | 9 | 0.89 | 0.321 | 0.261 |

Markers for A: very, sake, bear, morrow, bid, withal, along, ne'er, told, cold, being, hours, plead, comes, hither, patiented, name, coming, business, deliver, sorrow, ears, own, wherefore, holy, service, belike, knowst, patience, mad

Markers for B: proud, nought, content, brave, seek, frolic, dare, thanks, mighty, crave, only, fancy, jove, thoughts, deem, although, mark, scape, foe, ready, yield, greater, silver, straight, fail, pride, die, lass, fare, whereas

### Shakespeare early, Henry VI excluded (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Tit (Shakespeare) | A | 9 | 0.89 | 0.308 | 0.231 |
| R3 (Shakespeare) | A | 13 | 0.85 | 0.336 | 0.227 |
| Shr (Shakespeare) | A | 9 | 1.00 | 0.351 | 0.196 |
| TGV (Shakespeare) | A | 8 | 1.00 | 0.337 | 0.159 |
| Err (Shakespeare) | A | 7 | 1.00 | 0.379 | 0.144 |
| OWT (Peele) | B | 3 | 1.00 | 0.380 | 0.238 |
| Alcazar (Peele) | B | 5 | 0.20 | 0.205 | 0.267 |
| EdwardI (Peele) | B | 9 | 0.78 | 0.360 | 0.289 |
| David (Peele) | B | 6 | 0.00 | 0.243 | 0.300 |

Markers for A: very, strait, heard, morrow, ne'er, mean, th, ll, cold, word, else, bid, tongue, patiented, marry, jest, plead, fault, nay, business, speak, cannot, witness, till, signior, knowst, knew, told, humour, knows

Markers for B: thanks, follow, ye, beauteous, through, mighty, glory, ground, fight, knowest, run, silver, erst, pride, feet, sight, tops, fire, content, welcome, sacred, proud, borne, thunder, bright, cast, de, foe, bones, fields

## Projection: Marlowe vs Shakespeare markers applied to Henry VI, Richard III and the register controls

Markers trained on all Marlowe vs all Shakespeare outside the Henry VI family (so Henry VI 1-3 and Richard III are out of sample; Greene, Peele, the anonymous plays and Kyd are never in training). Mean marker shares per play; the Marlowe centroid is at (0.388, 0.210) and the Shakespeare centroid at (0.165, 0.431).

| play | author | chunks | Marlowe-marker share | Shakespeare-marker share | nearer |
|---|---|---|---|---|---|
| 1H6 | Shakespeare | 9 | 0.287 | 0.305 | Marlowe (67% of chunks) |
| 2H6 | Shakespeare | 11 | 0.235 | 0.338 | Shakespeare (18% of chunks) |
| 3H6 | Shakespeare | 10 | 0.253 | 0.313 | Shakespeare (20% of chunks) |
| R3 | Shakespeare | 13 | 0.207 | 0.364 | Shakespeare (0% of chunks) |
| Alphonsus | Greene | 5 | 0.300 | 0.263 | Marlowe (100% of chunks) |
| Orlando | Greene | 5 | 0.288 | 0.215 | Marlowe (100% of chunks) |
| FriarBacon | Greene | 7 | 0.254 | 0.286 | Marlowe (71% of chunks) |
| JamesIV | Greene | 9 | 0.255 | 0.325 | Shakespeare (33% of chunks) |
| OWT | Peele | 3 | 0.251 | 0.427 | Shakespeare (0% of chunks) |
| Alcazar | Peele | 5 | 0.356 | 0.216 | Marlowe (100% of chunks) |
| EdwardI | Peele | 9 | 0.280 | 0.318 | Marlowe (44% of chunks) |
| David | Peele | 6 | 0.361 | 0.224 | Marlowe (100% of chunks) |
| Soliman | Anon-Soliman | 8 | 0.295 | 0.295 | Marlowe (88% of chunks) |
| Locrine | Anon-Locrine | 7 | 0.338 | 0.244 | Marlowe (100% of chunks) |
| Selimus | Anon-Selimus | 8 | 0.327 | 0.283 | Marlowe (100% of chunks) |
| TRKJ | Anon-TRKJ | 6 | 0.294 | 0.274 | Marlowe (83% of chunks) |
| JackStraw | Anon-JackStraw | 4 | 0.243 | 0.277 | Marlowe (75% of chunks) |
| EdwardIII | Anon-EdwardIII | 9 | 0.263 | 0.313 | Shakespeare (44% of chunks) |
| Arden | Anon-Arden | 9 | 0.218 | 0.340 | Shakespeare (11% of chunks) |
| TTR3 | Anon-TTR3 | 8 | 0.264 | 0.306 | Marlowe (38% of chunks) |
| ST | Kyd | 9 | 0.278 | 0.277 | Marlowe (67% of chunks) |

Marlowe markers: ay, die, straight, pride, jove, lives, unto, base, ye, yield, soul, vain, perish, wrath, mighty, overthrow, thousand, wherein, charge, hope, greater, slain, martial, conquered, pierce, wealth, force, cast, conquering, power, brave, view, cruel, hundred, content, torments, fury, serve, pull, eternal

Shakespeare markers: indeed, tongue, very, mad, hour, own, reason, morrow, business, matter, even, old, itself, wife, marry, truth, find, better, dear, beseech, thing, kind, three, mark, two, dost, true, together, patience, honest, fellow, ear, between, answer, believe, cold, known, woe, ne'er, purpose
