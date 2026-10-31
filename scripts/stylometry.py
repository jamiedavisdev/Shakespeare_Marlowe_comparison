"""Stylometric comparison: Marlowe vs early Shakespeare, with controls.

Produces results/*.md tables and results/*.png figures.
"""
import json, re, pathlib, itertools, collections
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform, pdist
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.decomposition import PCA

import sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
CORPUS = os.environ.get('CORPUS', 'main')   # main = Folger/EMED corpus; ep = all-EarlyPrint corpus
CLEAN = ROOT / 'data' / ('clean' if CORPUS == 'main' else 'clean_' + CORPUS)
RESROOT = ROOT / 'results' / ('' if CORPUS == 'main' else CORPUS)
FEATURES = sys.argv[1] if len(sys.argv) > 1 else 'mfw150'   # mfw150 | mfw500 | func
RES = RESROOT / FEATURES
RES.mkdir(parents=True, exist_ok=True)
WORD_RE = re.compile(r"[a-z]+(?:['\-][a-z]+)*")
N_WORDS = {'mfw150': 150, 'mfw500': 500, 'func': 150}[FEATURES]
CULL = 0.8 if FEATURES == 'mfw500' else 0.0   # keep only words present in this share of plays
CHUNK = 2000           # tokens per chunk for the classifier tests
SEED = 0
FUNCTION_WORDS = """a about above after again against all am among an and any are art as at ay be because been before
being both but by can cannot could did do does doth dost done down each either else ere even ever every few for forth from
had has hast hath have having he hence her here hers herself him himself his hither how i if in into is it its itself let
many may me might mine more most much must my myself nay neither never no none nor not nothing now of off oft often on once
one only or other our ours out over own same shall shalt she should since so some still such than that the thee their them
themselves then thence there therefore these they thine this thither those thou though through thus thy thyself till tis to
too under until unto up upon us very was we well were wert what when whence where wherefore whether which while whilst who
whom whose why will wilt with within without would ye yea yet yonder you your yours yourself""".split()

manifest = json.loads((CLEAN / 'manifest.json').read_text())
WORKS = {w['id']: w for w in manifest}
MAIN = [w['id'] for w in manifest if w['group'] != 'altsource']
GROUPS = collections.defaultdict(list)
for w in manifest:
    GROUPS[w['group']].append(w['id'])
def present(L): return [w for w in L if w in WORKS]
EARLY_CONTROLS = present(['ST', 'OWT', 'Gal', 'AShrew', 'TCKL'])
LATE_CONTROLS = present(['ShoeHol', 'RT', 'KBP'])
FLETCHER = present(['FS', 'Prize', 'IP'])
# plays sharing plot/characters: never let one train the model that scores another
FAMILIES = [{'1H6', '2H6', '3H6', 'R3', 'TTR3'}, {'1Tam', '2Tam'}, {'Shr', 'AShrew'}, {'ST', 'Soliman'}]
GREENE = present(['Alphonsus', 'Orlando', 'FriarBacon', 'JamesIV'])
PEELE = present(['OWT', 'Alcazar', 'EdwardI', 'David'])
ANON_HEROIC = present(['Soliman', 'Locrine', 'Selimus', 'TRKJ', 'JackStraw', 'EdwardIII', 'Arden', 'TTR3'])
def related(wid):
    for f in FAMILIES:
        if wid in f:
            return f
    return {wid}
FORD = present(['Perkin', 'TPSW'])

def tokens(wid):
    return WORD_RE.findall((CLEAN / f'{wid}.txt').read_text().lower())

TOK = {w['id']: tokens(w['id']) for w in manifest}

def label(wid):
    w = WORKS[wid]
    return f"{wid} ({w['author']})"

# ---------------------------------------------------------------- features
def top_vocab(ids, n):
    c = collections.Counter()
    df = collections.Counter()
    for i in ids:
        c.update(TOK[i])
        df.update(set(TOK[i]))
    if FEATURES == 'func':
        return [w for w in FUNCTION_WORDS if c[w] > 0]
    ok = [w for w, _ in c.most_common() if df[w] >= CULL * len(ids)]
    return ok[:n]

def rel_freq(toks, vocab):
    c = collections.Counter(toks)
    n = len(toks)
    return np.array([c[v] / n * 1000 for v in vocab])

def chunks(toks, size=CHUNK):
    out = [toks[i:i + size] for i in range(0, len(toks), size)]
    if len(out) > 1 and len(out[-1]) < size // 2:
        out[-2] += out[-1]
        out.pop()
    return out

def char_ngrams(toks, n=4):
    s = ' ' + ' '.join(toks) + ' '
    return collections.Counter(s[i:i + n] for i in range(len(s) - n + 1))

def zscore_fit(X):
    mu = X.mean(0); sd = X.std(0); sd[sd == 0] = 1
    return mu, sd

def cosine_delta_matrix(Z):
    return squareform(pdist(Z, metric='cosine'))

def burrows_delta_matrix(Z):
    return squareform(pdist(Z, metric='cityblock')) / Z.shape[1]

# ---------------------------------------------------------------- 1. distances
def distance_analysis():
    vocab = top_vocab(MAIN, N_WORDS)
    X = np.array([rel_freq(TOK[i], vocab) for i in MAIN])
    mu, sd = zscore_fit(X)
    Z = (X - mu) / sd
    D = cosine_delta_matrix(Z)
    Db = burrows_delta_matrix(Z)
    idx = {w: k for k, w in enumerate(MAIN)}

    # save matrix
    with open(RES / 'distance_matrix_cosine_delta.csv', 'w') as f:
        f.write('work,' + ','.join(MAIN) + '\n')
        for i, w in enumerate(MAIN):
            f.write(w + ',' + ','.join(f'{d:.4f}' for d in D[i]) + '\n')

    def mean_dist(A, B, M=D):
        vals = [M[idx[a], idx[b]] for a in A for b in B if a != b]
        return np.mean(vals), np.std(vals), len(vals)

    sets = {k: v for k, v in {
        'Marlowe': GROUPS['marlowe'],
        'Shakespeare early (<=1594)': GROUPS['shakespeare_early'],
        'Shakespeare later (1595-1611)': GROUPS['shakespeare_later'],
        'Controls early (Kyd, Peele, Lyly, A Shrew, Leir)': EARLY_CONTROLS,
        'Controls later (Dekker, Middleton, Beaumont)': LATE_CONTROLS,
        'Fletcher (3 plays)': FLETCHER,
        'Ford (2 plays)': FORD,
        'Greene (4 plays, 1587-91)': GREENE,
        'Peele (4 plays, 1589-94)': PEELE,
        'Anonymous heroic/history 1587-94 (8 plays)': ANON_HEROIC,
    }.items() if v}
    lines = ['# Group-mean distances (cosine delta on z-scored word frequencies, features=%s)\n' % FEATURES,
             'Lower = more similar. Diagonal = within-group (different plays by the same group).\n',
             '| | ' + ' | '.join(sets) + ' |', '|---|' + '---|' * len(sets)]
    names = list(sets)
    for a in names:
        row = [a]
        for b in names:
            m, s, n = mean_dist(sets[a], sets[b])
            row.append(f'{m:.3f} ± {s:.3f} (n={n})')
        lines.append('| ' + ' | '.join(row) + ' |')
    lines.append('\n## Same table with classic Burrows Delta (mean |z| difference)\n')
    lines.append('| | ' + ' | '.join(sets) + ' |'); lines.append('|---|' + '---|' * len(sets))
    for a in names:
        row = [a]
        for b in names:
            m, s, n = mean_dist(sets[a], sets[b], Db)
            row.append(f'{m:.3f}')
        lines.append('| ' + ' | '.join(row) + ' |')

    # per-Marlowe-play nearest neighbours
    lines.append('\n## Nearest neighbours of each Marlowe play (cosine delta)\n')
    lines.append('| Marlowe play | 1st | 2nd | 3rd | nearest Shakespeare play |'); lines.append('|---|---|---|---|---|')
    for m in GROUPS['marlowe']:
        order = sorted((D[idx[m], idx[o]], o) for o in MAIN if o != m)
        nn = [f'{label(o)} {d:.3f}' for d, o in order[:3]]
        sh = next(f'{label(o)} {d:.3f}' for d, o in order if WORKS[o]['author'] == 'Shakespeare')
        lines.append(f'| {label(m)} | ' + ' | '.join(nn) + f' | {sh} |')
    lines.append('\n## Nearest neighbours of each early Shakespeare play\n')
    lines.append('| Play | 1st | 2nd | 3rd | nearest Marlowe play |'); lines.append('|---|---|---|---|---|')
    for m in GROUPS['shakespeare_early']:
        order = sorted((D[idx[m], idx[o]], o) for o in MAIN if o != m)
        nn = [f'{label(o)} {d:.3f}' for d, o in order[:3]]
        ma = next(f'{label(o)} {d:.3f}' for d, o in order if WORKS[o]['author'] == 'Marlowe')
        lines.append(f'| {label(m)} | ' + ' | '.join(nn) + f' | {ma} |')
    (RES / 'group_distances.md').write_text('\n'.join(lines) + '\n')

    # dendrogram
    L = linkage(squareform(D, checks=False), method='average')
    fig, ax = plt.subplots(figsize=(9, 16))
    colors = {'marlowe': '#c0392b', 'shakespeare_early': '#1f618d', 'shakespeare_later': '#5dade2', 'control': '#7f8c8d', 'control_multi': '#27ae60', 'control_ep': '#f39c12'}
    dn = dendrogram(L, labels=[label(w) for w in MAIN], orientation='left', ax=ax, leaf_font_size=9)
    for lbl in ax.get_ymajorticklabels():
        wid = lbl.get_text().split()[0]
        lbl.set_color(colors[WORKS[wid]['group']])
    ax.set_title(f'Average-linkage clustering, cosine delta, features={FEATURES}\nred=Marlowe  dark blue=Shakespeare ≤1594  light blue=Shakespeare later  grey=controls  green=Fletcher/Ford  orange=1587-94 controls (EarlyPrint)')
    ax.set_xlabel('cosine delta')
    fig.tight_layout(); fig.savefig(RES / 'dendrogram.png', dpi=150); plt.close(fig)

    # PCA
    pca = PCA(n_components=2, random_state=SEED).fit(Z)
    P = pca.transform(Z)
    fig, ax = plt.subplots(figsize=(10, 8))
    for g, c in colors.items():
        ii = [idx[w] for w in GROUPS[g]]
        if not ii: continue
        ax.scatter(P[ii, 0], P[ii, 1], c=c, s=60, label=g, edgecolor='k', linewidth=0.5)
    for w in MAIN:
        ax.annotate(w, P[idx[w]], fontsize=8, xytext=(4, 3), textcoords='offset points')
    ax.axhline(0, color='#ccc', lw=0.5); ax.axvline(0, color='#ccc', lw=0.5)
    ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.0%})'); ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.0%})')
    ax.set_title(f'PCA of z-scored word frequencies, features={FEATURES}'); ax.legend()
    fig.tight_layout(); fig.savefig(RES / 'pca.png', dpi=150); plt.close(fig)
    return vocab

# ---------------------------------------------------------------- 2. leave-one-work-out attribution
def loo_attribution():
    lines = ['# Leave-one-play-out attribution (nearest author centroid, cosine delta, top-%d words)\n' % N_WORDS,
             'Each play is held out together with any play sharing its plot/characters (Henry VI 1-3 + Richard III; Tamburlaine 1+2; the two Shrew plays); vocabulary, z-scores and author centroids are recomputed from the rest. '
             'Shakespeare, Marlowe, Fletcher and Ford centroids use all their remaining plays; each other control author is a single play.\n',
             '| Held-out play | True author | Predicted | d(Marlowe) | d(Shakespeare) | d(Sh. early only) | d(Sh. later only) | d(nearest control) | correct |',
             '|---|---|---|---|---|---|---|---|---|']
    correct = 0; total = 0
    for held in MAIN:
        rest = [w for w in MAIN if w not in related(held)]
        vocab = top_vocab(rest, N_WORDS)
        X = np.array([rel_freq(TOK[i], vocab) for i in rest])
        mu, sd = zscore_fit(X)
        Z = (X - mu) / sd
        z_h = (rel_freq(TOK[held], vocab) - mu) / sd
        by_author = collections.defaultdict(list)
        for i, w in enumerate(rest):
            by_author[WORKS[w]['author']].append(Z[i])
        def cos(a, b):
            return 1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        cents = {a: np.mean(v, axis=0) for a, v in by_author.items()}
        dists = {a: cos(z_h, c) for a, c in cents.items()}
        pred = min(dists, key=dists.get)
        sh_e = [Z[i] for i, w in enumerate(rest) if WORKS[w]['group'] == 'shakespeare_early']
        if not sh_e: sh_e = [Z[0]]
        sh_l = [Z[i] for i, w in enumerate(rest) if WORKS[w]['group'] == 'shakespeare_later']
        if not sh_l: sh_l = [Z[0]]
        d_e = cos(z_h, np.mean(sh_e, 0)); d_l = cos(z_h, np.mean(sh_l, 0))
        ctrl = {a: d for a, d in dists.items() if a not in ('Marlowe', 'Shakespeare')}
        nc = min(ctrl, key=ctrl.get)
        ok = pred == WORKS[held]['author']
        correct += ok; total += 1
        lines.append(f"| {held} | {WORKS[held]['author']} | **{pred}** | {dists['Marlowe']:.3f} | {dists['Shakespeare']:.3f} | {d_e:.3f} | {d_l:.3f} | {nc} {ctrl[nc]:.3f} | {'yes' if ok else 'NO'} |")
    lines.append(f'\nAccuracy: {correct}/{total}\n')
    (RES / 'attribution_loo.md').write_text('\n'.join(lines) + '\n')

# ---------------------------------------------------------------- 3. pairwise distinguishability
def pair_test(A, B, feature='words'):
    """Leave-one-play-out logistic regression on 2000-word chunks. Returns acc, auc, per-work mean P(A)."""
    ids = A + B
    chunk_data = {w: chunks(TOK[w]) for w in ids}
    probs, truth, perwork = [], [], {}
    for held in ids:
        train = [w for w in ids if w not in related(held)]
        tr_chunks = [(c, 1 if w in A else 0) for w in train for c in chunk_data[w]]
        if feature == 'words':
            vocab = top_vocab(train, N_WORDS)
            fx = lambda c: rel_freq(c, vocab)
        else:
            cnt = collections.Counter()
            for c, _ in tr_chunks:
                cnt.update(char_ngrams(c))
            vocab = [g for g, _ in cnt.most_common(1000)]
            def fx(c, vocab=vocab):
                g = char_ngrams(c); n = sum(g.values())
                return np.array([g[v] / n * 1000 for v in vocab])
        Xtr = np.array([fx(c) for c, _ in tr_chunks]); ytr = np.array([y for _, y in tr_chunks])
        mu, sd = zscore_fit(Xtr)
        clf = LogisticRegression(C=0.1, class_weight='balanced', max_iter=2000).fit((Xtr - mu) / sd, ytr)
        Xte = np.array([fx(c) for c in chunk_data[held]])
        p = clf.predict_proba((Xte - mu) / sd)[:, 1]
        probs += list(p); truth += [1 if held in A else 0] * len(p)
        perwork[held] = float(np.mean(p))
    probs = np.array(probs); truth = np.array(truth)
    acc = float(np.mean((probs > 0.5) == truth))
    auc = float(roc_auc_score(truth, probs))
    return acc, auc, perwork, len(truth)

def pairwise_tests():
    M = GROUPS['marlowe']; SE = GROUPS['shakespeare_early']; SL = GROUPS['shakespeare_later']
    M_a = ['1Tam', '2Tam', 'Dido']; M_b = ['DrFaust', 'JoM', 'Ed2', 'MP']
    SE_a = present(['2H6', '3H6', '1H6', 'Tit']); SE_b = present(['R3', 'Shr', 'TGV', 'Err'])
    tests = [
        ('QUESTION  Marlowe vs Shakespeare early', M, SE),
        ('QUESTION  Marlowe vs Shakespeare early, Henry VI excluded', M, present(['Tit', 'R3', 'Shr', 'TGV', 'Err'])),
        ('QUESTION  Marlowe vs Shakespeare early, histories/Titus only (genre-matched)', M, SE_a),
        ('QUESTION  Marlowe vs Shakespeare later', M, SL),
        ('QUESTION  Marlowe vs all Shakespeare', M, SE + SL),
        ('SAME-AUTHOR  Shakespeare early vs Shakespeare later', SE, SL),
        ('SAME-AUTHOR  Shakespeare early histories/Titus vs early R3+comedies', SE_a, SE_b),
        ('SAME-AUTHOR  Shakespeare 1595-97 vs 1599-1611', present(['R2', 'MND', 'Rom', 'MV', '1H4', 'LLL']), present(['JC', 'Ham', 'Mac', 'Lr', 'WT', 'Tmp'])),
        ('SAME-AUTHOR  Marlowe 1587-89 vs Marlowe 1589-93', M_a, M_b),
        ('DIFFERENT  Shakespeare later vs Fletcher (same period, 3 plays)', SL, FLETCHER),
        ('DIFFERENT  Shakespeare early vs Fletcher', SE, FLETCHER),
        ('DIFFERENT  Marlowe vs Fletcher', M, FLETCHER),
        ('DIFFERENT  Fletcher vs Ford', FLETCHER, FORD),
        ('DIFFERENT  Shakespeare later vs Ford', SL, FORD),
        ('DIFFERENT  Marlowe vs Ford', M, FORD),
        ('DIFFERENT  Marlowe vs Greene (same register, same years)', M, GREENE),
        ('DIFFERENT  Marlowe vs Peele (same register, same years)', M, PEELE),
        ('DIFFERENT  Marlowe vs anonymous heroic/history 1587-94', M, ANON_HEROIC),
        ('DIFFERENT  Shakespeare early vs Greene', SE, GREENE),
        ('DIFFERENT  Shakespeare early vs Peele', SE, PEELE),
        ('DIFFERENT  Shakespeare early vs anonymous heroic/history 1587-94', SE, ANON_HEROIC),
        ('DIFFERENT  Greene vs Peele', GREENE, PEELE),
        ('DIFFERENT  Henry VI 1-3 + Titus vs Greene', SE_a, GREENE),
        ('QUESTION  Henry VI 1-3 + Titus vs Marlowe (repeat, for comparison)', SE_a, M),
    ]
    do_chars = FEATURES == 'mfw150'
    lines = ['# Pairwise distinguishability (leave-one-play-out logistic regression on %d-word chunks)\n' % CHUNK,
             'Can a classifier trained on the *other* plays tell which set a held-out play\'s chunks belong to? '
             'For two sets by the same author we expect accuracy near chance (0.5) and AUC near 0.5; '
             'for different authors we expect values near 1. The question pair should be read against the two benchmarks.\n',
             '| Test | set A | set B | chunks | words: acc | words: AUC | char-4gram: acc | char-4gram: AUC |',
             '|---|---|---|---|---|---|---|---|']
    details = ['\n# Per-play mean P(set A), words model\n']
    for name, A, B in tests:
        if len(A) < 2 or len(B) < 2:
            continue
        acc_w, auc_w, pw_w, n = pair_test(A, B, 'words')
        acc_c, auc_c, pw_c, _ = pair_test(A, B, 'chars') if do_chars else (float('nan'), float('nan'), {w: float('nan') for w in A + B}, 0)
        lines.append(f'| {name} | {len(A)} plays | {len(B)} plays | {n} | {acc_w:.2f} | {auc_w:.2f} | {acc_c:.2f} | {auc_c:.2f} |')
        details.append(f'\n## {name}\n')
        details.append('| play | set | P(A) words | P(A) chars |'); details.append('|---|---|---|---|')
        for w in A + B:
            details.append(f"| {label(w)} | {'A' if w in A else 'B'} | {pw_w[w]:.2f} | {pw_c[w]:.2f} |")
        print(f'{name}: words acc={acc_w:.2f} auc={auc_w:.2f} | chars acc={acc_c:.2f} auc={auc_c:.2f}', flush=True)
    (RES / 'pairwise_distinguishability.md').write_text('\n'.join(lines + details) + '\n')

# ---------------------------------------------------------------- 4. Marlowe-share scan of early Shakespeare
def marlowe_scan():
    """Train Marlowe vs (all Shakespeare except the scanned play) and score each play's chunks."""
    M = GROUPS['marlowe']; S = GROUPS['shakespeare_early'] + GROUPS['shakespeare_later']
    lines = ['# Chunk-level Marlowe probability for each Shakespeare play\n',
             f'Classifier: Marlowe (7 plays) vs Shakespeare (all other plays), top-{N_WORDS} words, {CHUNK}-word chunks. '
             'Held-out play is never in training. Controls are scored by a Marlowe-vs-all-Shakespeare model.\n',
             '| Play | group | chunks | mean P(Marlowe) | chunks with P>0.5 | max P |', '|---|---|---|---|---|---|']
    def fit(train_M, train_S):
        vocab = top_vocab(train_M + train_S, N_WORDS)
        X = []; y = []
        for w in train_M:
            for c in chunks(TOK[w]): X.append(rel_freq(c, vocab)); y.append(1)
        for w in train_S:
            for c in chunks(TOK[w]): X.append(rel_freq(c, vocab)); y.append(0)
        X = np.array(X); mu, sd = zscore_fit(X)
        clf = LogisticRegression(C=0.1, class_weight='balanced', max_iter=2000).fit((X - mu) / sd, np.array(y))
        return lambda toks: clf.predict_proba(((np.array([rel_freq(c, vocab) for c in chunks(toks)]) - mu) / sd))[:, 1]
    for w in S:
        score = fit(M, [s for s in S if s not in related(w)])
        p = score(TOK[w])
        lines.append(f"| {label(w)} | {WORKS[w]['group']} | {len(p)} | {p.mean():.2f} | {(p > 0.5).sum()} | {p.max():.2f} |")
    score = fit(M, S)
    for w in [x for x in MAIN if WORKS[x]['author'] not in ('Marlowe', 'Shakespeare')]:
        p = score(TOK[w])
        lines.append(f"| {label(w)} | {WORKS[w]['group']} | {len(p)} | {p.mean():.2f} | {(p > 0.5).sum()} | {p.max():.2f} |")
    # Marlowe plays themselves, leave-one-out
    for w in M:
        score = fit([m for m in M if m not in related(w)], S)
        p = score(TOK[w])
        lines.append(f"| {label(w)} | marlowe (held out) | {len(p)} | {p.mean():.2f} | {(p > 0.5).sum()} | {p.max():.2f} |")
    (RES / 'marlowe_scan.md').write_text('\n'.join(lines) + '\n')

# ---------------------------------------------------------------- 5. source confound
def source_check():
    alts = [w['id'] for w in manifest if w['group'] == 'altsource']
    if not alts:
        return
    ids = MAIN + alts
    vocab = top_vocab(MAIN, N_WORDS)
    X = np.array([rel_freq(TOK[i], vocab) for i in ids])
    mu, sd = zscore_fit(X[:len(MAIN)])
    Z = (X - mu) / sd
    D = cosine_delta_matrix(Z); idx = {w: k for k, w in enumerate(ids)}
    lines = ['# Editorial-source confound check\n',
             'Shakespeare comes from the Folger Shakespeare editions, Marlowe and most controls from Folger EMED, and the 1587-94 controls '
             'from EarlyPrint (EEBO-TCP with standardised spellings). If editorial conventions drove the distances, the same play in two editions '
             'would sit far apart. Cosine-delta distances between each alternate-edition text and (a) its own main-corpus edition, '
             '(b) the other plays by the same author, (c) the nearest play by anyone else.\n',
             '| alternate text | source | d(same play, main edition) | mean d(other plays, same author) | nearest play by another author |', '|---|---|---|---|---|']
    for alt in alts:
        base = alt.rsplit('_', 1)[0]
        author = WORKS[alt]['author']
        others = [m for m in MAIN if WORKS[m]['author'] == author and m != base]
        mo = np.mean([D[idx[alt], idx[o]] for o in others]) if others else float('nan')
        nn = min((D[idx[alt], idx[o]], o) for o in MAIN if WORKS[o]['author'] != author)
        lines.append(f"| {alt} | {WORKS[alt]['source']} | {D[idx[alt], idx[base]]:.3f} | {mo:.3f} | {label(nn[1])} {nn[0]:.3f} |")
    lines.append('\n## Words whose frequency differs most between editions of the same play (mean |Δz| over all pairs)\n')
    gaps = np.mean([np.abs(Z[idx[a]] - Z[idx[a.rsplit('_', 1)[0]]]) for a in alts], axis=0)
    top = np.argsort(-gaps)[:15]
    lines.append('| word | mean |Δz| | ' + ' | '.join(f'{a} / {a.rsplit("_",1)[0]} (per 1000)' for a in alts) + ' |'); lines.append('|---|---|' + '---|' * len(alts))
    for t in top:
        lines.append(f"| {vocab[t]} | {gaps[t]:.2f} | " + ' | '.join(f"{X[idx[a], t]:.1f} / {X[idx[a.rsplit('_',1)[0]], t]:.1f}" for a in alts) + ' |')
    (RES / 'source_confound.md').write_text('\n'.join(lines) + '\n')

if __name__ == '__main__':
    print('distances...', flush=True); distance_analysis()
    print('loo attribution...', flush=True); loo_attribution()
    print('source check...', flush=True); source_check()
    print('marlowe scan...', flush=True); marlowe_scan()
    print('pairwise tests...', flush=True); pairwise_tests()
    print('done')
