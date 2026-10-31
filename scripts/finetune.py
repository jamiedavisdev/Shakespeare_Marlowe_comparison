"""Neural version of the test: fine-tune GPT-2 small per author, then
   (A) held-out perplexity of every play under every model  (behavioural comparison)
   (B) cosine similarity between fine-tuning weight deltas  (the 'compare the weights' idea, done fairly:
       same initialisation, same token budget, with seed-only and same-author-different-plays controls)

Outputs results/finetune/{perplexity.md, taskvectors.md, *.json}.
"""
import json, re, pathlib, math, time, sys, collections
import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

ROOT = pathlib.Path(__file__).resolve().parents[1]
import os
CORPUS = os.environ.get('CORPUS', 'main')
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

def main():
    base = GPT2LMHeadModel.from_pretrained('gpt2')
    base_vec = torch.cat([p.detach().flatten() for n, p in base.named_parameters() if 'wte' not in n and 'wpe' not in n])
    base_bits = {w: None for w in manifest}
    bm = base.to(DEV).eval()
    for w in manifest: base_bits[w] = bits_per_token(bm, w)
    del bm
    deltas = {}; ppl = {}
    for name, (plays, seed) in MODELS.items():
        t0 = time.time(); print(f'== {name}: {len(plays)} plays, seed {seed}', flush=True)
        m = finetune(plays, seed)
        vec = torch.cat([p.detach().flatten().cpu() for n, p in m.named_parameters() if 'wte' not in n and 'wpe' not in n])
        deltas[name] = (vec - base_vec).half()
        ppl[name] = {w: bits_per_token(m, w) for w in manifest}
        print(f'   done in {time.time()-t0:.0f}s; bits/token on own training plays: ' + ', '.join(f'{w}={ppl[name][w]:.2f}' for w in plays[:3]), flush=True)
        del m; torch.mps.empty_cache() if DEV == 'mps' else None
        json.dump({'base': base_bits, 'models': {k: {'plays': MODELS[k][0], 'seed': MODELS[k][1]} for k in ppl}, 'bits': ppl}, open(RES / 'perplexity.json', 'w'), indent=1)
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
    pairs = [('seed only, same data: Marlowe s1 vs s2', 'Marlowe_s1', 'Marlowe_s2'), ('seed only, same data: Shakespeare-later s1 vs s2', 'ShLater_s1', 'ShLater_s2'),
             ('same author, different plays: Marlowe A vs B', 'Marlowe_A', 'Marlowe_B'), ('same author, different plays: Shakespeare-later A vs B', 'ShLater_A', 'ShLater_B'),
             ('same author, different period: Shakespeare early (non-H6) vs later', 'ShEarlyNonH6', 'ShLater_s1'),
             ('QUESTION: Marlowe vs Shakespeare early (non-H6)', 'Marlowe_s1', 'ShEarlyNonH6'), ('QUESTION: Marlowe vs Shakespeare later', 'Marlowe_s1', 'ShLater_s1'),
             ('different, same register: Marlowe vs Greene', 'Marlowe_s1', 'Greene'), ('different, same register: Marlowe vs Peele', 'Marlowe_s1', 'Peele'),
             ('different, same register: Marlowe vs anonymous heroic', 'Marlowe_s1', 'AnonHeroic'), ('different: Greene vs Peele', 'Greene', 'Peele'),
             ('different: Shakespeare early (non-H6) vs Greene', 'ShEarlyNonH6', 'Greene'), ('different: Shakespeare early (non-H6) vs Peele', 'ShEarlyNonH6', 'Peele'),
             ('different, different period: Shakespeare later vs Fletcher', 'ShLater_s1', 'Fletcher'), ('different, different period: Marlowe vs Fletcher', 'Marlowe_s1', 'Fletcher')]
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
