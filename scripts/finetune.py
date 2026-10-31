"""Neural version of the test: fine-tune GPT-2 small per author, then
   (A) held-out perplexity of every play under every model  (behavioural comparison)
   (B) cosine similarity between fine-tuning weight deltas  (the 'compare the weights' idea, done fairly:
       same initialisation, same token budget, with seed-only and same-author-different-plays controls)
   (C) embedding geometry: for a fixed list of words shared by every training set, how the pairwise
       cosine between word embeddings changes under each fine-tune (coordinate-free, so it would also
       work for models that share no initialisation), plus the plain cosine of the embedding deltas.

Outputs results/finetune/{perplexity.md, taskvectors.md, embeddings.md, *.json, embeddings.npz}.
EMB_ONLY=1 trains the same models but writes only the embedding-geometry outputs (no perplexity, no task vectors).
"""
import json, re, pathlib, math, time, sys, collections
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
CORPUS = os.environ.get('CORPUS', 'main')
EMB_ONLY = os.environ.get('EMB_ONLY') == '1'
CLEAN = ROOT / 'data' / ('clean' if CORPUS == 'main' else 'clean_' + CORPUS)
RES = ROOT / 'results' / ('' if CORPUS == 'main' else CORPUS) / 'finetune'; RES.mkdir(parents=True, exist_ok=True)
DEV = 'mps' if torch.backends.mps.is_available() else 'cpu'
SEQ = 256; BS = 8; EPOCHS = 3; LR = 5e-5
manifest = {w['id']: w for w in json.loads((CLEAN / 'manifest.json').read_text()) if w['group'] != 'altsource'}
A = collections.defaultdict(list)
for w in manifest.values(): A[w['author']].append(w['id'])
SE_NONH6 = [w for w in ['Tit', 'Shr', 'TGV', 'Err'] if w in manifest]
SL = [w for w in manifest if manifest[w]['group'] == 'shakespeare_later']
ANON = [w for w in ['Soliman', 'Locrine', 'Selimus', 'TRKJ', 'JackStraw', 'EdwardIII', 'Arden', 'TTR3'] if w in manifest]
MODELS = {   # name -> (training plays, seed)
    'Marlowe_s1': (A['Marlowe'], 1), 'Marlowe_s2': (A['Marlowe'], 2),
    'Marlowe_A': (['1Tam', '2Tam', 'Dido'], 1), 'Marlowe_B': (['DrFaust', 'JoM', 'Ed2', 'MP'], 1),
    'ShLater_s1': (SL, 1), 'ShLater_s2': (SL, 2),
    'ShLater_A': ([w for w in ['R2', 'MND', 'Rom', 'MV', '1H4'] if w in manifest], 1), 'ShLater_B': ([w for w in ['JC', 'Ham', 'Mac', 'Lr', 'WT', 'Tmp'] if w in manifest], 1),
    'ShEarlyNonH6': (SE_NONH6, 1),
    'Greene': (A['Greene'], 1), 'Peele': (A['Peele'], 1), 'AnonHeroic': (ANON, 1), 'Fletcher': (A['Fletcher'], 1),
}
MODELS = {k: v for k, v in MODELS.items() if v[0]}
tok = GPT2TokenizerFast.from_pretrained('gpt2')
def text(wid): return (CLEAN / f'{wid}.txt').read_text()
TOKS = {w: tok(text(w))['input_ids'] for w in manifest}
BUDGET = min(sum(len(TOKS[w]) for w in A['Greene']), sum(len(TOKS[w]) for w in A['Peele']))
print(f'device={DEV} token budget per model={BUDGET}', flush=True)

def train_ids(plays):
    share = BUDGET // len(plays)
    ids = []
    for w in plays: ids += TOKS[w][:share]
    return ids

def batches(ids, seed):
    g = torch.Generator().manual_seed(seed)
    n = len(ids) // SEQ
    X = torch.tensor(ids[:n * SEQ]).view(n, SEQ)
    perm = torch.randperm(n, generator=g)
    for i in range(0, n, BS):
        yield X[perm[i:i + BS]]

def finetune(plays, seed):
    torch.manual_seed(seed)
    model = GPT2LMHeadModel.from_pretrained('gpt2').to(DEV)
    model.train()
    opt = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=0.0)
    ids = train_ids(plays)
    for ep in range(EPOCHS):
        tot = 0; nb = 0
        for xb in batches(ids, seed * 100 + ep):
            xb = xb.to(DEV)
            loss = model(xb, labels=xb).loss
            opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0); opt.step()
            tot += loss.item(); nb += 1
        print(f'    epoch {ep+1} loss {tot/nb:.3f}', flush=True)
    model.eval()
    return model

@torch.no_grad()
def bits_per_token(model, wid):
    ids = TOKS[wid]; n = len(ids) // SEQ
    X = torch.tensor(ids[:n * SEQ]).view(n, SEQ)
    tot = 0.0; cnt = 0
    for i in range(0, n, 16):
        xb = X[i:i + 16].to(DEV)
        logits = model(xb).logits[:, :-1]
        lp = torch.log_softmax(logits.float(), -1).gather(-1, xb[:, 1:, None]).squeeze(-1)
        tot += -lp.sum().item(); cnt += lp.numel()
    return tot / cnt / math.log(2)

PAIRS = [('seed only, same data: Marlowe s1 vs s2', 'Marlowe_s1', 'Marlowe_s2'), ('seed only, same data: Shakespeare-later s1 vs s2', 'ShLater_s1', 'ShLater_s2'),
         ('same author, different plays: Marlowe A vs B', 'Marlowe_A', 'Marlowe_B'), ('same author, different plays: Shakespeare-later A vs B', 'ShLater_A', 'ShLater_B'),
         ('same author, different period: Shakespeare early (non-H6) vs later', 'ShEarlyNonH6', 'ShLater_s1'),
         ('QUESTION: Marlowe vs Shakespeare early (non-H6)', 'Marlowe_s1', 'ShEarlyNonH6'), ('QUESTION: Marlowe vs Shakespeare later', 'Marlowe_s1', 'ShLater_s1'),
         ('different, same register: Marlowe vs Greene', 'Marlowe_s1', 'Greene'), ('different, same register: Marlowe vs Peele', 'Marlowe_s1', 'Peele'),
         ('different, same register: Marlowe vs anonymous heroic', 'Marlowe_s1', 'AnonHeroic'), ('different: Greene vs Peele', 'Greene', 'Peele'),
         ('different: Shakespeare early (non-H6) vs Greene', 'ShEarlyNonH6', 'Greene'), ('different: Shakespeare early (non-H6) vs Peele', 'ShEarlyNonH6', 'Peele'),
         ('different, different period: Shakespeare later vs Fletcher', 'ShLater_s1', 'Fletcher'), ('different, different period: Marlowe vs Fletcher', 'Marlowe_s1', 'Fletcher')]

def word_list(n_max=400, min_count=3):
    """Words every model will see in training: whole-word GPT-2 tokens (leading space), all lower-case
    (drops names and sentence-initial forms), at least min_count uses in every training set, ranked by
    the smallest count across sets. Fixed before training so every model is measured on the same words."""
    counts = [collections.Counter(train_ids(plays)) for plays, seed in MODELS.values()]
    shared = set.intersection(*[set(c) for c in counts])
    scored = []
    for t in shared:
        tt = tok.convert_ids_to_tokens(t)
        if not (tt.startswith('Ġ') and tt[1:].isalpha() and tt[1:].islower()): continue
        m = min(c[t] for c in counts)
        if m >= min_count: scored.append((m, t))
    scored.sort(reverse=True)
    return [t for m, t in scored[:n_max]]

def geometry_report(E0, E, W):
    """E0: pretrained embedding rows for W (|W| x d); E: name -> fine-tuned rows. Three comparisons between
    models: (i) correlation of the raw pairwise-cosine matrices (expected ~1: the pretrained geometry
    dominates), (ii) correlation of the CHANGE in pairwise cosine from pretrained (the relative-geometry
    test), (iii) cosine of the embedding deltas over the W rows (coordinate-dependent, valid here only
    because every model starts from the same weights)."""
    names = list(E)
    iu = torch.triu_indices(len(W), len(W), 1)
    def cosmat(X):
        Xn = X / X.norm(dim=1, keepdim=True); return (Xn @ Xn.T)[iu[0], iu[1]]
    def corr(a, b):
        a = a - a.mean(); b = b - b.mean(); return float(a @ b / (a.norm() * b.norm()))
    def cos(a, b): return float(a @ b / (a.norm() * b.norm()))
    S0 = cosmat(E0)
    raw = {n: cosmat(E[n]) for n in names}
    dS = {n: raw[n] - S0 for n in names}
    dE = {n: (E[n] - E0).flatten() for n in names}
    k = len(names)
    C_raw = np.zeros((k, k)); C_dS = np.zeros((k, k)); C_dE = np.zeros((k, k))
    for i, a in enumerate(names):
        for j, b in enumerate(names):
            C_raw[i, j] = corr(raw[a], raw[b]); C_dS[i, j] = corr(dS[a], dS[b]); C_dE[i, j] = cos(dE[a], dE[b])
    moved = {n: float(dS[n].abs().mean()) for n in names}
    words = [tok.convert_ids_to_tokens(t)[1:] for t in W]
    json.dump({'names': names, 'words': words, 'corr_raw_cos': C_raw.tolist(), 'corr_delta_cos': C_dS.tolist(),
               'cos_embedding_delta': C_dE.tolist(), 'mean_abs_change_in_pairwise_cos': moved},
              open(RES / 'embeddings.json', 'w'), indent=1)
    np.savez_compressed(RES / 'embeddings.npz', words=np.array(words), base=E0.numpy(), **{n: E[n].numpy() for n in names})
    idx = {n: i for i, n in enumerate(names)}
    L = ['# Embedding geometry of the fine-tuned GPT-2 author models\n',
         f'Word list: {len(W)} whole-word, lower-case GPT-2 tokens that occur at least 3 times in every model\'s training text '
         f'(ranked by the smallest count across sets; names and sentence-initial forms excluded). '
         f'Same models, seeds and token budget ({BUDGET:,}) as the task-vector test.\n',
         'For each model the token-embedding rows of these words are taken and the pairwise cosine between every two words is computed. '
         'Three ways to compare two models:\n',
         '1. **raw geometry**: correlation of the two pairwise-cosine matrices. Expected near 1 for every pair, because the pretrained geometry '
         'barely moves at this budget; reported to show that the raw distances carry no information about the fine-tune.',
         '2. **change in geometry** (the relative-embedding test): correlation of the change in pairwise cosine from pretrained, '
         'model vs model. Coordinate-free: it asks whether the two fine-tunes moved the same word pairs closer together or further apart, '
         'whatever happened to the absolute vectors.',
         '3. **embedding delta**: cosine between the two models\' (fine-tuned − pretrained) embedding rows for these words. '
         'The embedding-layer counterpart of the task-vector cosine (which excluded embeddings).\n',
         'Read every number against the controls: seed-only pairs are the ceiling, same-author-different-plays pairs are the author signal, '
         'different-author pairs are the floor. If same-author pairs do not sit above different-author pairs, the geometry records text and register, not author.\n',
         '## Key pairs\n', '| pair | type | change in geometry | embedding delta | raw geometry |', '|---|---|---|---|---|']
    for desc, a, b in PAIRS:
        if a in idx and b in idx:
            L.append(f'| {a} vs {b} | {desc} | {C_dS[idx[a], idx[b]]:.3f} | {C_dE[idx[a], idx[b]]:.3f} | {C_raw[idx[a], idx[b]]:.4f} |')
    L += ['\n## Change in geometry, all models\n', '| | ' + ' | '.join(names) + ' |', '|---|' + '---|' * k]
    for i, a in enumerate(names): L.append(f'| {a} | ' + ' | '.join(f'{C_dS[i, j]:.3f}' for j in range(k)) + ' |')
    L += ['\n## Embedding delta cosine, all models\n', '| | ' + ' | '.join(names) + ' |', '|---|' + '---|' * k]
    for i, a in enumerate(names): L.append(f'| {a} | ' + ' | '.join(f'{C_dE[i, j]:.3f}' for j in range(k)) + ' |')
    L += ['\n## How much each model moved the geometry\n', 'Mean absolute change in pairwise cosine from pretrained, over all word pairs.\n', '| model | mean abs change |', '|---|---|']
    for n in names: L.append(f'| {n} | {moved[n]:.5f} |')
    L += ['\n## The words\n', ', '.join(words) + '\n']
    (RES / 'embeddings.md').write_text('\n'.join(L) + '\n')
    print('embedding geometry written: ' + ', '.join(f'{a} vs {b} {C_dS[idx[a], idx[b]]:.3f}' for d, a, b in PAIRS[:4] if a in idx and b in idx), flush=True)

def main():
    base = GPT2LMHeadModel.from_pretrained('gpt2')
    base_vec = torch.cat([p.detach().flatten() for n, p in base.named_parameters() if 'wte' not in n and 'wpe' not in n])
    W = word_list(); print(f'embedding word list: {len(W)} words', flush=True)
    E0 = base.transformer.wte.weight.detach()[W].float().cpu().clone(); E = {}
    base_bits = {w: None for w in manifest}
    if not EMB_ONLY:
        bm = base.to(DEV).eval()
        for w in manifest: base_bits[w] = bits_per_token(bm, w)
        del bm
    deltas = {}; ppl = {}
    for name, (plays, seed) in MODELS.items():
        t0 = time.time(); print(f'== {name}: {len(plays)} plays, seed {seed}', flush=True)
        m = finetune(plays, seed)
        E[name] = m.transformer.wte.weight.detach()[W].float().cpu().clone()
        if EMB_ONLY:
            print(f'   done in {time.time()-t0:.0f}s', flush=True); del m; torch.mps.empty_cache() if DEV == 'mps' else None; continue
        vec = torch.cat([p.detach().flatten().cpu() for n, p in m.named_parameters() if 'wte' not in n and 'wpe' not in n])
        deltas[name] = (vec - base_vec).half()
        ppl[name] = {w: bits_per_token(m, w) for w in manifest}
        print(f'   done in {time.time()-t0:.0f}s; bits/token on own training plays: ' + ', '.join(f'{w}={ppl[name][w]:.2f}' for w in plays[:3]), flush=True)
        del m; torch.mps.empty_cache() if DEV == 'mps' else None
        json.dump({'base': base_bits, 'models': {k: {'plays': MODELS[k][0], 'seed': MODELS[k][1]} for k in ppl}, 'bits': ppl}, open(RES / 'perplexity.json', 'w'), indent=1)
    # ---- (C) embedding geometry
    geometry_report(E0, E, W)
    if EMB_ONLY: return
    # ---- (B) task-vector similarity
    names = list(deltas)
    C = np.zeros((len(names), len(names)))
    for i, a in enumerate(names):
        va = deltas[a].float()
        for j, b in enumerate(names):
            vb = deltas[b].float()
            C[i, j] = float(torch.dot(va, vb) / (va.norm() * vb.norm()))
    json.dump({'names': names, 'cosine': C.tolist(), 'norms': {n: float(deltas[n].float().norm()) for n in names}}, open(RES / 'taskvectors.json', 'w'), indent=1)
    lines = ['# Cosine similarity between fine-tuning weight deltas (GPT-2 small, embeddings excluded)\n',
             f'Every model starts from the same pretrained GPT-2 and sees the same number of tokens ({BUDGET:,}), {EPOCHS} epochs, lr {LR}. '
             'The delta is (fine-tuned − pretrained) over all non-embedding parameters.\n',
             '| | ' + ' | '.join(names) + ' |', '|---|' + '---|' * len(names)]
    for i, a in enumerate(names):
        lines.append(f'| {a} | ' + ' | '.join(f'{C[i,j]:.3f}' for j in range(len(names))) + ' |')
    pairs = PAIRS
    lines.append('\n## Key pairs\n'); lines.append('| pair | type | cosine |'); lines.append('|---|---|---|')
    idx = {n: i for i, n in enumerate(names)}
    for desc, a, b in pairs:
        if a not in idx or b not in idx: continue
        lines.append(f"| {a} vs {b} | {desc} | {C[idx[a], idx[b]]:.3f} |")
    (RES / 'taskvectors.md').write_text('\n'.join(lines) + '\n')
    # ---- (A) perplexity table
    scor = [m for m in ['Marlowe_s1', 'ShEarlyNonH6', 'ShLater_s1', 'Greene', 'Peele', 'AnonHeroic', 'Fletcher'] if m in MODELS]
    out = ['# Held-out bits per token under fine-tuned GPT-2 author models\n',
           'Rows = plays; columns = models. A play that was in a model\'s training set is marked "(train)". '
           'Marlowe plays are scored by the Marlowe model that did *not* train on them (Marlowe_A scores the B plays and vice versa). '
           'Base = pretrained GPT-2 without fine-tuning.\n',
           '| play | author | base | ' + ' | '.join(scor) + ' |', '|---|---|---|' + '---|' * len(scor)]
    for w in manifest:
        cells = []
        for mname in scor:
            tr = MODELS[mname][0]
            if w in tr:
                if mname == 'Marlowe_s1':
                    alt = 'Marlowe_B' if w in MODELS['Marlowe_A'][0] else 'Marlowe_A'
                    cells.append(f"{ppl[alt][w]:.3f}*")
                else:
                    cells.append('(train)')
            else:
                cells.append(f'{ppl[mname][w]:.3f}')
        out.append(f"| {w} | {manifest[w]['author']} | {base_bits[w]:.3f} | " + ' | '.join(cells) + ' |')
    out.append('\n\\* scored by the Marlowe model trained on the other half of the canon.\n')
    (RES / 'perplexity.md').write_text('\n'.join(out) + '\n')
    print('done')

if __name__ == '__main__':
    main()
