# Burrows's Zeta: marker-word tests

2,000-word chunks, proper nouns removed, candidate words present in >= 5 plays, 150 markers per side. Markers are chosen with the scored play and its family held out. Chunks are classified by nearest training centroid in (share of A-markers, share of B-markers). Read the question pairs against the benchmarks.

| pair | type | plays | chunks | accuracy | AUC |
|---|---|---|---|---|---|
| Marlowe vs Shakespeare early, Henry VI excluded | QUESTION | 7 vs 5 | 95 | 0.79 | 0.89 |
| Marlowe vs Henry VI 1-3 | QUESTION | 7 vs 3 | 79 | 0.65 | 0.64 |
| Marlowe vs Shakespeare early (all 8) | QUESTION | 7 vs 8 | 126 | 0.60 | 0.65 |
| Marlowe vs Shakespeare later | QUESTION | 7 vs 11 | 161 | 0.92 | 0.98 |
| Shakespeare early (all 8) vs Shakespeare later | SAME-AUTHOR | 8 vs 11 | 191 | 0.54 | 0.58 |
| Shakespeare early, Henry VI excluded vs Shakespeare later | SAME-AUTHOR | 5 vs 11 | 160 | 0.72 | 0.73 |
| Marlowe 1587-89 vs Marlowe 1589-93 | SAME-AUTHOR | 3 vs 4 | 48 | 0.54 | 0.26 |
| Shakespeare 1595-97 vs Shakespeare 1599-1611 | SAME-AUTHOR | 5 vs 6 | 113 | 0.74 | 0.84 |
| Henry VI 1-3 vs Shakespeare early, Henry VI excluded | SAME-AUTHOR? | 3 vs 5 | 65 | 0.80 | 0.90 |
| Greene vs Peele | DIFFERENT | 4 vs 4 | 52 | 0.44 | 0.44 |
| Marlowe vs Greene | DIFFERENT | 7 vs 4 | 74 | 0.76 | 0.86 |
| Marlowe vs Peele | DIFFERENT | 7 vs 4 | 74 | 0.49 | 0.51 |
| Marlowe vs Anonymous heroic | DIFFERENT | 7 vs 8 | 108 | 0.70 | 0.77 |
| Henry VI 1-3 vs Greene | DIFFERENT | 3 vs 4 | 57 | 0.81 | 0.89 |
| Henry VI 1-3 vs Peele | DIFFERENT | 3 vs 4 | 57 | 0.84 | 0.90 |
| Shakespeare early, Henry VI excluded vs Greene | DIFFERENT | 5 vs 4 | 73 | 0.82 | 0.93 |
| Shakespeare early, Henry VI excluded vs Peele | DIFFERENT | 5 vs 4 | 73 | 0.81 | 0.87 |
| Shakespeare later vs Fletcher | DIFFERENT | 11 vs 3 | 145 | 0.81 | 0.69 |

## Per-play results (share of chunks placed with set A)

### Marlowe (A) vs Shakespeare early, Henry VI excluded (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 1.00 | 0.332 | 0.180 |
| 2Tam (Marlowe) | A | 8 | 1.00 | 0.377 | 0.157 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.349 | 0.246 |
| DrFaust (Marlowe) | A | 5 | 0.60 | 0.281 | 0.243 |
| JoM (Marlowe) | A | 8 | 0.00 | 0.261 | 0.288 |
| Ed2 (Marlowe) | A | 9 | 0.56 | 0.292 | 0.244 |
| MP (Marlowe) | A | 4 | 1.00 | 0.327 | 0.262 |
| Tit (Shakespeare) | B | 9 | 0.33 | 0.269 | 0.282 |
| R3 (Shakespeare) | B | 13 | 0.23 | 0.265 | 0.283 |
| Shr (Shakespeare) | B | 10 | 0.00 | 0.192 | 0.314 |
| TGV (Shakespeare) | B | 8 | 0.00 | 0.190 | 0.324 |
| Err (Shakespeare) | B | 7 | 0.00 | 0.172 | 0.337 |

Markers for A: ye, pride, through, fire, power, cast, sword, land, cruel, martial, stars, heavens, walls, hundred, rich, wherein, soul, overthrow, crowns, view, greater, brave, lie, base, gold, ride, pierce, swords, triumph, breast

Markers for B: tongue, indeed, very, marry, wife, mad, husband, fool, better, reason, patience, woman, jest, merry, hours, awhile, know'st, word, bid, plead, fault, hither, told, tomorrow, she's, even, house, dear, daughter, withal

### Marlowe (A) vs Henry VI 1-3 (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.38 | 0.257 | 0.288 |
| 2Tam (Marlowe) | A | 8 | 0.88 | 0.278 | 0.265 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.269 | 0.231 |
| DrFaust (Marlowe) | A | 5 | 1.00 | 0.251 | 0.200 |
| JoM (Marlowe) | A | 8 | 0.88 | 0.231 | 0.260 |
| Ed2 (Marlowe) | A | 9 | 0.44 | 0.215 | 0.274 |
| MP (Marlowe) | A | 4 | 0.75 | 0.247 | 0.270 |
| 1H6 (Shakespeare) | B | 9 | 0.67 | 0.230 | 0.309 |
| 2H6 (Shakespeare) | B | 11 | 0.55 | 0.210 | 0.255 |
| 3H6 (Shakespeare) | B | 11 | 0.27 | 0.228 | 0.262 |

Markers for A: ye, gold, cast, rich, present, fetch, wherein, stars, land, fire, villain, pearl, damned, greater, golden, serve, pierce, straight, walk, slave, swords, hundred, fiery, vain, pride, cruel, walls, desires, wait, imperial

Markers for B: tongue, peace, together, awhile, title, virtuous, sign, tender, help, fight, answer, reason, broke, ten, foul, stands, heir, lost, valiant, methinks, enemies, bold, claim, knee, humble, false, bloody, loss, quarrel, crowned

### Marlowe (A) vs Shakespeare early (all 8) (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.50 | 0.301 | 0.225 |
| 2Tam (Marlowe) | A | 8 | 0.88 | 0.333 | 0.189 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.304 | 0.269 |
| DrFaust (Marlowe) | A | 5 | 0.40 | 0.253 | 0.229 |
| JoM (Marlowe) | A | 8 | 0.00 | 0.232 | 0.323 |
| Ed2 (Marlowe) | A | 9 | 0.44 | 0.241 | 0.264 |
| MP (Marlowe) | A | 4 | 0.50 | 0.280 | 0.270 |
| 1H6 (Shakespeare) | B | 9 | 0.89 | 0.328 | 0.233 |
| 2H6 (Shakespeare) | B | 11 | 0.64 | 0.286 | 0.248 |
| 3H6 (Shakespeare) | B | 11 | 0.64 | 0.298 | 0.245 |
| Tit (Shakespeare) | B | 9 | 0.22 | 0.221 | 0.300 |
| R3 (Shakespeare) | B | 13 | 0.23 | 0.265 | 0.283 |
| Shr (Shakespeare) | B | 10 | 0.00 | 0.152 | 0.310 |
| TGV (Shakespeare) | B | 8 | 0.00 | 0.168 | 0.315 |
| Err (Shakespeare) | B | 7 | 0.00 | 0.182 | 0.337 |

Markers for A: ye, pride, cast, fire, gold, rich, land, wherein, stars, power, cruel, greater, hundred, walls, martial, golden, pierce, through, swords, lie, crowns, vain, soul, view, cursed, heavens, imperial, overthrow, conquering, ride

Markers for B: tongue, very, marry, awhile, indeed, reason, better, woman, patience, together, tender, virtuous, mad, wife, foul, peace, hither, fault, hour, house, merry, hours, even, jest, know'st, fool, cold, much, between, true

### Marlowe (A) vs Shakespeare later (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 1.00 | 0.335 | 0.237 |
| 2Tam (Marlowe) | A | 8 | 1.00 | 0.348 | 0.217 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.354 | 0.282 |
| DrFaust (Marlowe) | A | 5 | 0.40 | 0.280 | 0.304 |
| JoM (Marlowe) | A | 8 | 0.25 | 0.289 | 0.337 |
| Ed2 (Marlowe) | A | 9 | 0.89 | 0.298 | 0.260 |
| MP (Marlowe) | A | 4 | 1.00 | 0.343 | 0.292 |
| R2 (Shakespeare) | B | 10 | 0.30 | 0.269 | 0.343 |
| MND (Shakespeare) | B | 8 | 0.00 | 0.182 | 0.378 |
| Rom (Shakespeare) | B | 11 | 0.00 | 0.208 | 0.422 |
| MV (Shakespeare) | B | 10 | 0.00 | 0.177 | 0.401 |
| 1H4 (Shakespeare) | B | 11 | 0.00 | 0.200 | 0.375 |
| JC (Shakespeare) | B | 9 | 0.00 | 0.200 | 0.410 |
| Ham (Shakespeare) | B | 14 | 0.00 | 0.181 | 0.456 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.210 | 0.445 |
| Lr (Shakespeare) | B | 12 | 0.00 | 0.186 | 0.464 |
| WT (Shakespeare) | B | 12 | 0.00 | 0.143 | 0.422 |
| Tmp (Shakespeare) | B | 8 | 0.00 | 0.147 | 0.426 |

Markers for A: ye, gold, pride, unto, lives, princely, war, walls, thousand, wrath, yield, base, die, vain, martial, golden, land, soul, brave, crowns, mighty, straight, accursed, triumph, perish, because, field, hope, overthrow, proud

Markers for B: indeed, very, tongue, itself, mark, business, hour, beseech, mad, does, reason, three, fool, true, certain, ear, tonight, honest, better, find, matter, dear, truth, nothing, known, old, two, even, kind, much

### Shakespeare early (all 8) (A) vs Shakespeare later (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.00 | 0.236 | 0.358 |
| 2H6 (Shakespeare) | A | 11 | 0.00 | 0.247 | 0.353 |
| 3H6 (Shakespeare) | A | 11 | 0.00 | 0.252 | 0.312 |
| Tit (Shakespeare) | A | 9 | 0.89 | 0.264 | 0.227 |
| R3 (Shakespeare) | A | 13 | 0.31 | 0.252 | 0.338 |
| Shr (Shakespeare) | A | 10 | 0.00 | 0.197 | 0.277 |
| TGV (Shakespeare) | A | 8 | 0.00 | 0.220 | 0.283 |
| Err (Shakespeare) | A | 7 | 0.29 | 0.215 | 0.293 |
| R2 (Shakespeare) | B | 10 | 1.00 | 0.303 | 0.261 |
| MND (Shakespeare) | B | 8 | 0.12 | 0.217 | 0.293 |
| Rom (Shakespeare) | B | 11 | 0.27 | 0.233 | 0.309 |
| MV (Shakespeare) | B | 10 | 0.20 | 0.233 | 0.308 |
| 1H4 (Shakespeare) | B | 11 | 0.64 | 0.256 | 0.292 |
| JC (Shakespeare) | B | 9 | 0.11 | 0.224 | 0.331 |
| Ham (Shakespeare) | B | 14 | 0.00 | 0.197 | 0.368 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.207 | 0.371 |
| Lr (Shakespeare) | B | 12 | 0.00 | 0.218 | 0.364 |
| WT (Shakespeare) | B | 12 | 0.00 | 0.210 | 0.347 |
| Tmp (Shakespeare) | B | 8 | 0.00 | 0.206 | 0.352 |

Markers for A: unto, plead, yield, proud, witness, because, sake, princely, sent, sons, virtuous, lives, won, enemies, hope, war, field, mean, foes, send, scorn, therefore, towns, belike, she, sign, words, loss, long, fame

Markers for B: does, itself, mark, something, things, further, ear, show, strange, nothing, business, ho, o'er, lie, question, old, lies, part, breath, th, certain, seem, power, work, spirits, beseech, fire, alack, themselves, anything

### Shakespeare early, Henry VI excluded (A) vs Shakespeare later (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Tit (Shakespeare) | A | 9 | 0.33 | 0.227 | 0.261 |
| R3 (Shakespeare) | A | 13 | 0.31 | 0.252 | 0.338 |
| Shr (Shakespeare) | A | 10 | 0.10 | 0.209 | 0.271 |
| TGV (Shakespeare) | A | 8 | 0.50 | 0.263 | 0.266 |
| Err (Shakespeare) | A | 7 | 0.43 | 0.271 | 0.292 |
| R2 (Shakespeare) | B | 10 | 0.50 | 0.283 | 0.277 |
| MND (Shakespeare) | B | 8 | 0.12 | 0.205 | 0.311 |
| Rom (Shakespeare) | B | 11 | 0.27 | 0.262 | 0.301 |
| MV (Shakespeare) | B | 10 | 0.10 | 0.247 | 0.319 |
| 1H4 (Shakespeare) | B | 11 | 0.18 | 0.223 | 0.289 |
| JC (Shakespeare) | B | 9 | 0.00 | 0.199 | 0.347 |
| Ham (Shakespeare) | B | 14 | 0.00 | 0.186 | 0.366 |
| Mac (Shakespeare) | B | 8 | 0.00 | 0.198 | 0.377 |
| Lr (Shakespeare) | B | 12 | 0.00 | 0.214 | 0.372 |
| WT (Shakespeare) | B | 12 | 0.00 | 0.205 | 0.318 |
| Tmp (Shakespeare) | B | 8 | 0.00 | 0.211 | 0.349 |

Markers for A: unto, plead, sake, witness, husband, sister, sent, sons, mean, she, send, jest, villain, because, belike, scorn, holy, home, knew, lives, withal, marry, company, deadly, wench, goodly, know'st, long, wife, cheer

Markers for B: further, itself, mark, does, question, things, power, lie, o'er, show, spirits, lies, seem, already, off, speech, work, spirit, part, th, point, heavens, fire, something, only, strange, act, new, set, ho

### Marlowe 1587-89 (A) vs Marlowe 1589-93 (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.00 | 0.233 | 0.306 |
| 2Tam (Marlowe) | A | 8 | 0.00 | 0.254 | 0.297 |
| Dido (Marlowe) | A | 6 | 0.17 | 0.212 | 0.343 |
| DrFaust (Marlowe) | B | 5 | 0.00 | 0.199 | 0.345 |
| JoM (Marlowe) | B | 8 | 0.00 | 0.154 | 0.344 |
| Ed2 (Marlowe) | B | 9 | 0.11 | 0.188 | 0.277 |
| MP (Marlowe) | B | 4 | 0.00 | 0.210 | 0.395 |

Markers for A: martial, looks, mighty, eyes, clouds, light, fame, waves, stars, triumph, sword, feet, seat, victory, worthy, barbarous, stout, cruel, speech, black, golden, conquered, rich, ye, foe, armed, passage, sit, walls, cities

Markers for B: gone, done, we'll, let's, please, therefore, there's, whilst, word, ne'er, that's, money, speak, hither, things, hast, none, house, trust, has, been, read, resolute, tush, pray, seeing, answer, whither, nay, wish

### Shakespeare 1595-97 (A) vs Shakespeare 1599-1611 (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| R2 (Shakespeare) | A | 10 | 0.50 | 0.253 | 0.283 |
| MND (Shakespeare) | A | 8 | 0.88 | 0.282 | 0.243 |
| Rom (Shakespeare) | A | 11 | 0.73 | 0.301 | 0.272 |
| MV (Shakespeare) | A | 10 | 0.40 | 0.274 | 0.277 |
| 1H4 (Shakespeare) | A | 11 | 0.73 | 0.276 | 0.248 |
| JC (Shakespeare) | B | 9 | 0.78 | 0.303 | 0.273 |
| Ham (Shakespeare) | B | 14 | 0.21 | 0.241 | 0.331 |
| Mac (Shakespeare) | B | 8 | 0.12 | 0.277 | 0.369 |
| Lr (Shakespeare) | B | 12 | 0.00 | 0.237 | 0.352 |
| WT (Shakespeare) | B | 12 | 0.00 | 0.244 | 0.338 |
| Tmp (Shakespeare) | B | 8 | 0.00 | 0.232 | 0.346 |

Markers for A: house, hours, fair, unto, gold, back, new, tears, meet, soul, sweet, rude, sake, gentle, sad, next, flower, love's, swear, unless, because, thousand, kinsman, youth, merry, faith, company, doth, hate, breast

Markers for B: does, has, th, he's, em, prithee, free, that's, fit, most, put, business, seem, might, speech, itself, command, almost, something, heavens, work, madness, sister, act, toward, known, thought, service, strange, cast

### Henry VI 1-3 (A) vs Shakespeare early, Henry VI excluded (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 1.00 | 0.379 | 0.231 |
| 2H6 (Shakespeare) | A | 11 | 0.36 | 0.285 | 0.254 |
| 3H6 (Shakespeare) | A | 11 | 0.73 | 0.319 | 0.248 |
| Tit (Shakespeare) | B | 9 | 0.33 | 0.258 | 0.259 |
| Shr (Shakespeare) | B | 10 | 0.00 | 0.189 | 0.285 |
| TGV (Shakespeare) | B | 8 | 0.00 | 0.190 | 0.268 |
| Err (Shakespeare) | B | 7 | 0.00 | 0.189 | 0.319 |

Markers for A: fight, yield, sword, foe, through, methinks, brave, field, title, colors, head, proud, valiant, towns, ten, set, state, dare, prisoner, courage, force, quickly, victory, treason, battle, only, enemies, wert, crowned, ambitious

Markers for B: husband, home, dear, bid, knew, fool, fetch, sister, wife, mad, present, slave, plead, villain, walk, indeed, thank, letter, wench, word, looked, ha, saw, told, dinner, dull, self, business, bitter, know'st

### Greene (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Alphonsus (Greene) | A | 5 | 0.40 | 0.268 | 0.229 |
| Orlando (Greene) | A | 5 | 0.60 | 0.312 | 0.237 |
| FriarBacon (Greene) | A | 7 | 0.43 | 0.316 | 0.212 |
| JamesIV (Greene) | A | 9 | 0.33 | 0.304 | 0.262 |
| OWT (Peele) | B | 4 | 1.00 | 0.250 | 0.168 |
| Alcazar (Peele) | B | 5 | 0.20 | 0.268 | 0.229 |
| EdwardI (Peele) | B | 10 | 0.80 | 0.327 | 0.242 |
| David (Peele) | B | 7 | 0.14 | 0.218 | 0.250 |

Markers for A: place, ll, fond, high, fancy, only, fit, maid, simple, lands, stay, mark, loves, state, marriage, sport, although, mean, heard, favours, get, sirrah, mind, girl, both, knows, damsel, brook, wealth, hap

Markers for B: brother, strength, golden, behold, sight, bear, cast, young, tops, flesh, renowned, water, bones, hair, ye, fields, name, dearest, souls, earthly, bosom, comfort, soft, tyranny, holy, beauteous, welcome, pity, glory, blood

### Marlowe (A) vs Greene (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.88 | 0.251 | 0.212 |
| 2Tam (Marlowe) | A | 8 | 1.00 | 0.297 | 0.200 |
| Dido (Marlowe) | A | 6 | 1.00 | 0.273 | 0.211 |
| DrFaust (Marlowe) | A | 5 | 1.00 | 0.285 | 0.216 |
| JoM (Marlowe) | A | 8 | 1.00 | 0.285 | 0.201 |
| Ed2 (Marlowe) | A | 9 | 1.00 | 0.279 | 0.192 |
| MP (Marlowe) | A | 4 | 1.00 | 0.310 | 0.207 |
| Alphonsus (Greene) | B | 5 | 0.60 | 0.227 | 0.240 |
| Orlando (Greene) | B | 5 | 0.60 | 0.224 | 0.236 |
| FriarBacon (Greene) | B | 7 | 0.57 | 0.198 | 0.261 |
| JamesIV (Greene) | B | 9 | 0.78 | 0.247 | 0.269 |

Markers for A: i'll, tis, soul, thousand, let's, that's, we'll, ne'er, cast, pity, ye, about, being, war, favor, golden, lives, blood, walls, brother, ears, pierce, treasure, bear, having, clouds, straight, eternal, hateful, honors

Markers for B: ll, honour, nought, daughter, merry, secret, favour, fond, maid, lands, favours, borne, fancy, mark, trust, wife, woe, deem, state, courteous, indeed, counsel, tongue, although, friend, wise, wrong, thoughts, wend, damsel

### Marlowe (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.38 | 0.312 | 0.253 |
| 2Tam (Marlowe) | A | 8 | 0.12 | 0.306 | 0.287 |
| Dido (Marlowe) | A | 6 | 0.83 | 0.332 | 0.226 |
| DrFaust (Marlowe) | A | 5 | 1.00 | 0.343 | 0.201 |
| JoM (Marlowe) | A | 8 | 1.00 | 0.325 | 0.207 |
| Ed2 (Marlowe) | A | 9 | 0.89 | 0.333 | 0.197 |
| MP (Marlowe) | A | 4 | 1.00 | 0.378 | 0.223 |
| OWT (Peele) | B | 4 | 1.00 | 0.260 | 0.188 |
| Alcazar (Peele) | B | 5 | 0.80 | 0.311 | 0.239 |
| EdwardI (Peele) | B | 10 | 1.00 | 0.330 | 0.246 |
| David (Peele) | B | 7 | 0.86 | 0.328 | 0.238 |

Markers for A: tis, i'll, stay, let's, mean, we'll, that's, ne'er, cannot, favor, wherein, pardon, none, crowns, place, born, heard, slave, honors, there's, only, again, walls, many, greater, th, else, knows, pierce, thence

Markers for B: honour, ll, favour, borne, beauteous, thanks, bones, sing, wife, honours, young, welcome, brother, forth, counsel, ground, royalty, nought, honourable, advise, soft, glory, wench, lo, bosom, fields, servant, just, anointed, honoured

### Marlowe (A) vs Anonymous heroic (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1Tam (Marlowe) | A | 8 | 0.12 | 0.236 | 0.257 |
| 2Tam (Marlowe) | A | 8 | 0.38 | 0.263 | 0.230 |
| Dido (Marlowe) | A | 6 | 0.67 | 0.264 | 0.234 |
| DrFaust (Marlowe) | A | 5 | 0.80 | 0.257 | 0.228 |
| JoM (Marlowe) | A | 8 | 0.25 | 0.251 | 0.264 |
| Ed2 (Marlowe) | A | 9 | 0.56 | 0.239 | 0.276 |
| MP (Marlowe) | A | 4 | 0.75 | 0.275 | 0.247 |
| Soliman (Anon-Soliman) | B | 8 | 0.00 | 0.215 | 0.287 |
| Locrine (Anon-Locrine) | B | 7 | 0.43 | 0.236 | 0.267 |
| Selimus (Anon-Selimus) | B | 8 | 0.12 | 0.223 | 0.313 |
| TRKJ (Anon-TRKJ) | B | 6 | 0.00 | 0.194 | 0.310 |
| JackStraw (Anon-JackStraw) | B | 4 | 0.00 | 0.170 | 0.312 |
| EdwardIII (Anon-EdwardIII) | B | 9 | 0.11 | 0.244 | 0.307 |
| Arden (Anon-Arden) | B | 9 | 0.11 | 0.190 | 0.259 |
| TTR3 (Anon-TTR3) | B | 9 | 0.00 | 0.159 | 0.276 |

Markers for A: i'll, tis, let's, that's, we'll, hundred, ye, favor, heaven, born, rich, th, there's, honors, soul, pierce, pride, labor, armor, twas, ride, runs, lives, ne'er, fury, favors, pearl, means, slave, meet

Markers for B: ll, honour, favour, counsel, forward, tongue, took, honours, ill, case, thing, better, honest, brief, nought, valour, thinks, honoured, after, certain, indeed, try, borne, coming, forget, wife, news, way, lands, care

### Henry VI 1-3 (A) vs Greene (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.89 | 0.298 | 0.219 |
| 2H6 (Shakespeare) | A | 11 | 1.00 | 0.284 | 0.212 |
| 3H6 (Shakespeare) | A | 11 | 1.00 | 0.318 | 0.196 |
| Alphonsus (Greene) | B | 5 | 0.80 | 0.233 | 0.244 |
| Orlando (Greene) | B | 5 | 0.20 | 0.180 | 0.279 |
| FriarBacon (Greene) | B | 7 | 0.00 | 0.169 | 0.259 |
| JamesIV (Greene) | B | 9 | 0.56 | 0.252 | 0.264 |

Markers for A: i'll, tis, we'll, let's, enemies, that's, ne'er, blood, heir, strength, peace, colors, being, spirit, methinks, ten, pity, foul, title, along, whiles, shame, awhile, answer, towns, quickly, brother, soul, together, where's

Markers for B: ll, honour, nought, favour, maid, fit, mighty, fancy, fond, dear, favours, ye, merry, lovely, daughter, thoughts, courteous, serve, advise, mark, wealth, greater, past, train, strange, scape, secret, silver, high, girl

### Henry VI 1-3 (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| 1H6 (Shakespeare) | A | 9 | 0.89 | 0.368 | 0.224 |
| 2H6 (Shakespeare) | A | 11 | 1.00 | 0.335 | 0.210 |
| 3H6 (Shakespeare) | A | 11 | 1.00 | 0.323 | 0.205 |
| OWT (Peele) | B | 4 | 0.50 | 0.245 | 0.197 |
| Alcazar (Peele) | B | 5 | 0.20 | 0.249 | 0.273 |
| EdwardI (Peele) | B | 10 | 0.50 | 0.308 | 0.261 |
| David (Peele) | B | 7 | 0.00 | 0.241 | 0.280 |

Markers for A: tis, i'll, we'll, let's, title, twas, ne'er, myself, place, that's, heard, tears, answer, stay, speak, yield, peace, else, colors, awhile, again, heir, thought, off, whiles, only, false, tongue, treason, where's

Markers for B: honour, ye, ll, favour, beauteous, golden, fields, heavens, cast, sing, sacred, gold, knowest, erst, thanks, honours, advise, lovely, hair, rich, mighty, forth, behold, brother, silver, lusty, pleasant, wench, tops, honourable

### Shakespeare early, Henry VI excluded (A) vs Greene (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Tit (Shakespeare) | A | 9 | 0.89 | 0.304 | 0.200 |
| R3 (Shakespeare) | A | 13 | 1.00 | 0.305 | 0.214 |
| Shr (Shakespeare) | A | 10 | 1.00 | 0.281 | 0.190 |
| TGV (Shakespeare) | A | 8 | 1.00 | 0.286 | 0.197 |
| Err (Shakespeare) | A | 7 | 1.00 | 0.334 | 0.153 |
| Alphonsus (Greene) | B | 5 | 0.60 | 0.225 | 0.273 |
| Orlando (Greene) | B | 5 | 0.20 | 0.196 | 0.308 |
| FriarBacon (Greene) | B | 7 | 0.14 | 0.194 | 0.289 |
| JamesIV (Greene) | B | 9 | 0.78 | 0.309 | 0.281 |

Markers for A: i'll, tis, that's, let's, we'll, husband, sake, bear, brother, sister, there's, along, very, today, hither, withal, plead, thank, being, tomorrow, told, bid, sons, she's, ne'er, holy, cold, deliver, mad, foul

Markers for B: ll, honour, nought, heavens, state, brave, secret, sword, mighty, favour, seek, content, fancy, proud, dare, high, favours, maid, scape, only, yield, train, fond, ye, thoughts, over, lands, deem, foe, courteous

### Shakespeare early, Henry VI excluded (A) vs Peele (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| Tit (Shakespeare) | A | 9 | 0.78 | 0.315 | 0.227 |
| R3 (Shakespeare) | A | 13 | 0.85 | 0.364 | 0.237 |
| Shr (Shakespeare) | A | 10 | 1.00 | 0.389 | 0.146 |
| TGV (Shakespeare) | A | 8 | 1.00 | 0.399 | 0.138 |
| Err (Shakespeare) | A | 7 | 1.00 | 0.391 | 0.130 |
| OWT (Peele) | B | 4 | 1.00 | 0.335 | 0.172 |
| Alcazar (Peele) | B | 5 | 0.00 | 0.220 | 0.325 |
| EdwardI (Peele) | B | 10 | 0.60 | 0.344 | 0.285 |
| David (Peele) | B | 7 | 0.00 | 0.234 | 0.316 |

Markers for A: tis, i'll, very, that's, let's, today, better, mean, we'll, there's, husband, heard, else, cannot, plead, thank, word, mad, none, bid, slave, jest, tongue, myself, indeed, gentle, awhile, she's, twas, patience

Markers for B: honour, ye, heavens, sword, thanks, favour, ll, follow, ground, fight, golden, through, glory, pride, feet, content, beauteous, fire, mighty, sacred, cast, borne, tops, honours, sight, knowest, erst, behold, land, fields

### Shakespeare later (A) vs Fletcher (B)

| play | set | chunks | placed as A | A-marker share | B-marker share |
|---|---|---|---|---|---|
| R2 (Shakespeare) | A | 10 | 1.00 | 0.375 | 0.216 |
| MND (Shakespeare) | A | 8 | 1.00 | 0.356 | 0.222 |
| Rom (Shakespeare) | A | 11 | 1.00 | 0.379 | 0.228 |
| MV (Shakespeare) | A | 10 | 1.00 | 0.351 | 0.228 |
| 1H4 (Shakespeare) | A | 11 | 1.00 | 0.352 | 0.212 |
| JC (Shakespeare) | A | 9 | 1.00 | 0.350 | 0.222 |
| Ham (Shakespeare) | A | 14 | 1.00 | 0.368 | 0.220 |
| Mac (Shakespeare) | A | 8 | 0.88 | 0.363 | 0.248 |
| Lr (Shakespeare) | A | 12 | 1.00 | 0.384 | 0.221 |
| WT (Shakespeare) | A | 12 | 1.00 | 0.348 | 0.249 |
| Tmp (Shakespeare) | A | 8 | 1.00 | 0.348 | 0.243 |
| FS (Fletcher) | B | 10 | 1.00 | 0.398 | 0.245 |
| Prize (Fletcher) | B | 11 | 1.00 | 0.315 | 0.275 |
| IP (Fletcher) | B | 11 | 0.55 | 0.256 | 0.329 |

Markers for A: hath, doth, himself, son, them, therefore, answer, tears, yea, forth, speech, whom, eye, question, vile, part, spirits, seem, news, came, woe, spirit, note, ho, did, wherein, shalt, heavens, awhile, says

Markers for B: ye, dare, wench, sure, believe, em, yes, cure, new, win, woman, honest, ill, deserve, virtuous, has, pure, forced, taken, hope, carry, women, enjoy, heed, suddenly, free, equal, care, light, handsomely

## Projection: Marlowe vs Shakespeare markers applied to Henry VI, Richard III and the register controls

Markers trained on all Marlowe vs all Shakespeare outside the Henry VI family (so Henry VI 1-3 and Richard III are out of sample; Greene, Peele, the anonymous plays and Kyd are never in training). Mean marker shares per play; the Marlowe centroid is at (0.428, 0.203) and the Shakespeare centroid at (0.185, 0.417).

| play | author | chunks | Marlowe-marker share | Shakespeare-marker share | nearer |
|---|---|---|---|---|---|
| 1H6 | Shakespeare | 9 | 0.331 | 0.296 | Marlowe (78% of chunks) |
| 2H6 | Shakespeare | 11 | 0.269 | 0.317 | Shakespeare (36% of chunks) |
| 3H6 | Shakespeare | 11 | 0.293 | 0.287 | Marlowe (64% of chunks) |
| R3 | Shakespeare | 13 | 0.238 | 0.356 | Shakespeare (8% of chunks) |
| Alphonsus | Greene | 5 | 0.355 | 0.253 | Marlowe (100% of chunks) |
| Orlando | Greene | 5 | 0.323 | 0.217 | Marlowe (100% of chunks) |
| FriarBacon | Greene | 7 | 0.296 | 0.284 | Marlowe (71% of chunks) |
| JamesIV | Greene | 9 | 0.284 | 0.311 | Shakespeare (22% of chunks) |
| OWT | Peele | 4 | 0.213 | 0.348 | Shakespeare (0% of chunks) |
| Alcazar | Peele | 5 | 0.400 | 0.200 | Marlowe (100% of chunks) |
| EdwardI | Peele | 10 | 0.301 | 0.280 | Marlowe (60% of chunks) |
| David | Peele | 7 | 0.363 | 0.188 | Marlowe (100% of chunks) |
| Soliman | Anon-Soliman | 8 | 0.315 | 0.293 | Marlowe (50% of chunks) |
| Locrine | Anon-Locrine | 7 | 0.360 | 0.237 | Marlowe (100% of chunks) |
| Selimus | Anon-Selimus | 8 | 0.346 | 0.258 | Marlowe (100% of chunks) |
| TRKJ | Anon-TRKJ | 6 | 0.339 | 0.256 | Marlowe (100% of chunks) |
| JackStraw | Anon-JackStraw | 4 | 0.275 | 0.257 | Marlowe (75% of chunks) |
| EdwardIII | Anon-EdwardIII | 9 | 0.324 | 0.300 | Marlowe (67% of chunks) |
| Arden | Anon-Arden | 9 | 0.247 | 0.336 | Shakespeare (22% of chunks) |
| TTR3 | Anon-TTR3 | 9 | 0.280 | 0.268 | Marlowe (44% of chunks) |
| ST | Kyd | 10 | 0.280 | 0.255 | Marlowe (50% of chunks) |

Marlowe markers: ye, pride, gold, walls, princely, war, unto, lives, land, soul, die, golden, yield, martial, wrath, base, brave, thousand, wherein, mighty, vain, triumph, crowns, overthrow, sword, cast, field, charge, straight, greater, view, swords, accursed, perish, force, pierce, conquered, hundred, eternal, conquering

Shakespeare markers: indeed, very, tongue, mad, reason, fool, business, hour, better, itself, mark, honest, beseech, true, dear, find, matter, awhile, word, certain, patience, does, even, three, kind, much, tonight, hours, ear, two, marry, old, believe, truth, merry, known, together, dost, woe, between
