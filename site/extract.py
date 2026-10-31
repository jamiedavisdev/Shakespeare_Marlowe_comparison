import json, csv, re, math, sys
import numpy as np
import os
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
out={}
works=json.load(open(P+'scripts/works.json'))
plays=[]
for w in works:
    if w['group']=='altsource': continue
    try:
        txt=open(P+'data/clean/'+w['id']+'.txt').read()
        n=len(txt.split())
    except Exception: n=None
    plays.append(dict(id=w['id'],title=w['title'],author=w['author'],group=w['group'],date=w.get('date'),words=n))
out['plays']=plays
# MDS from func distance matrix
rows=list(csv.reader(open(P+'results/func/distance_matrix_cosine_delta.csv')))
names=rows[0][1:]
D=np.array([[float(x) for x in r[1:]] for r in rows[1:]])
n=len(names)
J=np.eye(n)-np.ones((n,n))/n
B=-0.5*J@(D**2)@J
vals,vecs=np.linalg.eigh(B)
idx=np.argsort(vals)[::-1][:2]
X=vecs[:,idx]*np.sqrt(np.maximum(vals[idx],0))
out['mds']={nm:[round(float(X[i,0]),3),round(float(X[i,1]),3)] for i,nm in enumerate(names)}
out['mds_var']=[round(float(v/np.sum(np.maximum(vals,0))),3) for v in vals[idx]]
out['dist']={nm:{names[j]:round(float(D[i,j]),3) for j in range(n)} for i,nm in enumerate(names)}
# GI
out['gi']=json.load(open(P+'results/gi_verify/gi_scores.json'))
out['gi_ep']=json.load(open(P+'results/ep/gi_verify/gi_scores.json'))
# pairwise
def pairwise(path):
    res=[]
    for line in open(path):
        m=re.match(r'\| (QUESTION|SAME-AUTHOR|DIFFERENT)\s+(.+?) \| (\d+) plays \| (\d+) plays \| (\d+) \| ([\d.]+) \| ([\d.]+) \|',line)
        if m:
            res.append(dict(type=m.group(1),name=m.group(2).strip(),nA=int(m.group(3)),nB=int(m.group(4)),chunks=int(m.group(5)),acc=float(m.group(6)),auc=float(m.group(7))))
    return res
out['pairwise']=pairwise(P+'results/func/pairwise_distinguishability.md')
out['pairwise_ep']=pairwise(P+'results/ep/func/pairwise_distinguishability.md')
# scenes
sc={}
for pid in ['1H6','2H6','3H6','R3','Tit']:
    d=json.load(open(P+f'results/scene_scan/{pid}_scenes.json'))
    sc[pid]=[dict(scene=s['scene'],words=s['words'],P={k:round(v,3) for k,v in s['P'].items()},dH={k:round(v,3) for k,v in s['dH'].items()},prior=s.get('prior','')) for s in d]
out['scenes']=sc
# verse-only 2H6
vo={}
cur=None
for line in open(P+'results/scene_scan/prose_verse.md'):
    if line.startswith('## '): cur=line[3:].strip()
    m=re.match(r'\| ([\d.]+) \| (\d+) \| ([\d.\-]+) \| ([+\-][\d.]+) \| (\d+) \| ([\d.\-]+) \| ([+\-\d.]+|-) \| (.*?) \|',line)
    if m and cur:
        vo.setdefault(cur,[]).append(dict(scene=m.group(1),vwords=int(m.group(2)),Pv=None if m.group(3)=='-' else float(m.group(3)),dHv=float(m.group(4)),pwords=int(m.group(5)),Pp=None if m.group(6)=='-' else float(m.group(6)),prior=m.group(8).strip()))
out['verse_only']=vo
# cross-entropy ep masked
ce=json.load(open(P+'results/ep/crossentropy_masked/crossentropy.json'))
epw={w['id']:w for w in json.load(open(P+'scripts/works_ep.json'))}
M=['Marlowe','Sh-early','Sh-later','Greene','Peele','Anon-heroic']
out['ce_ep']={pid:{m:(None if (r.get(m) is None or (isinstance(r[m],float) and math.isnan(r[m]))) else round(r[m],4)) for m in M} for pid,r in ce['rows'].items() if pid in epw and epw[pid]['group']!='altsource'}
out['ce_ep_meta']={pid:dict(author=epw[pid]['author'],group=epw[pid]['group'],title=epw[pid]['title'],date=epw[pid].get('date')) for pid in out['ce_ep']}
ceq=json.load(open(P+'results/q/crossentropy_masked/crossentropy.json'))
out['ce_q']={pid:{m:(None if (r.get(m) is None or (isinstance(r[m],float) and math.isnan(r[m]))) else round(r[m],4)) for m in M} for pid,r in ceq['rows'].items()}
# task vectors
tv=json.load(open(P+'results/finetune/taskvectors.json'))
out['tv']=dict(names=tv['names'],cosine=[[round(x,3) for x in row] for row in tv['cosine']])
tve=json.load(open(P+'results/ep/finetune/taskvectors.json'))
out['tv_ep']=dict(names=tve['names'],cosine=[[round(x,3) for x in row] for row in tve['cosine']])
# embedding geometry (correlation of the change in pairwise word-embedding cosine), same model grid
for key,rel in (('emb','results/finetune/embeddings.json'),('emb_ep','results/ep/finetune/embeddings.json')):
    if os.path.exists(P+rel):
        e=json.load(open(P+rel)); out[key]=dict(names=e['names'],cosine=[[round(x,3) for x in row] for row in e['corr_delta_cos']],words=len(e['words']))
# perplexity ep
pp=json.load(open(P+'results/ep/finetune/perplexity.json'))
out['ppl_ep']=pp

# word profiles and Zeta
def slim_zeta(z):
    return dict(k=z['k'],min_plays=z['min_plays'],vocab=z['vocab'],
        pairs=[dict(type=q['type'],A=q['A'],B=q['B'],playsA=q['playsA'],playsB=q['playsB'],chunks=q['chunks'],acc=q['acc'],auc=q['auc'],
                    markersA=q['markersA'][:30],markersB=q['markersB'][:30],centroidA=q['centroidA'],centroidB=q['centroidB'],
                    points=[dict(play=pt['play'],side=pt['side'],sA=pt['sA'],sB=pt['sB'],pred=pt['pred']) for pt in q['points']],per_play=q['per_play']) for q in z['pairs']],
        projection=dict(A=z['projection']['A'],B=z['projection']['B'],markersA=z['projection']['markersA'][:40],markersB=z['projection']['markersB'][:40],
                        centroidA=z['projection']['centroidA'],centroidB=z['projection']['centroidB'],points=z['projection']['points'],per_play=z['projection']['per_play']))
def slim_prof(w):
    return dict(vocab_size=w['vocab_size'],pairs=[dict(type=q['type'],A=q['A'],B=q['B'],playsA=q['playsA'],playsB=q['playsB'],topA=q['topA'][:20],topB=q['topB'][:20],per_play=q['per_play']) for q in w['pairs']])
for corp,sub in (('main',''),('ep','ep/')):
    zp=P+f'results/{sub}words/zeta.json'; wp=P+f'results/{sub}words/word_profiles.json'
    if os.path.exists(zp): out['zeta' if corp=='main' else 'zeta_ep']=slim_zeta(json.load(open(zp)))
    if os.path.exists(wp): out['words' if corp=='main' else 'words_ep']=slim_prof(json.load(open(wp)))
# ---- links to sources and copies of texts / tables for the site ----
import shutil
SITE=os.path.dirname(os.path.abspath(__file__))
FOLGER_SLUG={'1H6':'henry-vi-part-1','2H6':'henry-vi-part-2','3H6':'henry-vi-part-3','Tit':'titus-andronicus','R3':'richard-iii','Shr':'the-taming-of-the-shrew','TGV':'the-two-gentlemen-of-verona','Err':'the-comedy-of-errors','R2':'richard-ii','MND':'a-midsummer-nights-dream','Rom':'romeo-and-juliet','MV':'the-merchant-of-venice','1H4':'henry-iv-part-1','JC':'julius-caesar','Ham':'hamlet','Mac':'macbeth','Lr':'king-lear','WT':'the-winters-tale','Tmp':'the-tempest'}
def tcp_of(w):
    f=w.get('file','')
    m=re.search(r'(A\d{5})\.xml$',f)
    return m.group(1) if m else None
qw={w['id']:w for w in json.load(open(P+'scripts/works_q.json'))}
links={}
for w in works:
    if w['group']=='altsource': continue
    L=[]
    if w['source']=='folger':
        L.append(dict(label='Folger Shakespeare, read online',url=f"https://www.folger.edu/explore/shakespeares-works/{FOLGER_SLUG[w['id']]}/read/",kind='source'))
        L.append(dict(label='Folger plain-text download',url=f"https://flgr.sh/txtfss{w['id']}txt",kind='source'))
    elif w['source']=='emed':
        L.append(dict(label='Folger EMED edition',url=f"https://emed.folger.edu/{w['id']}",kind='source'))
        L.append(dict(label='EMED TEI/XML (regularised spelling)',url=f"https://emed.folger.edu/sites/default/files/folger_encodings/xml/EMED-{w['id']}-3.xml",kind='source'))
    elif w['source']=='earlyprint':
        t=w.get('tcp') or tcp_of(w)
        L.append(dict(label=f'EarlyPrint / EEBO-TCP {t}',url=f"https://texts.earlyprint.org/works/{t}.xml",kind='source'))
    e=epw.get(w['id'])
    if e and e.get('source')=='earlyprint':
        t=tcp_of(e)
        if t=='A11954': L.append(dict(label='1623 First Folio, EarlyPrint (TCP A11954)',url='https://texts.earlyprint.org/works/A11954.xml',kind='early'))
        elif t and not any(t in x['url'] for x in L): L.append(dict(label=f'Early quarto, EarlyPrint (TCP {t})',url=f"https://texts.earlyprint.org/works/{t}.xml",kind='early'))
    q=qw.get(w['id'])
    if q:
        t=tcp_of(q)
        if t and not any(t in x['url'] for x in L): L.append(dict(label=f'Early quarto, EarlyPrint (TCP {t})'+(' · '+q['note'] if q.get('note') else ''),url=f"https://texts.earlyprint.org/works/{t}.xml",kind='early'))
    texts={}
    for corp,sub in (('main','clean'),('ep','clean_ep'),('q','clean_q')):
        src=P+f'data/{sub}/{w["id"]}.txt'
        if os.path.exists(src):
            dst=os.path.join(SITE,f'texts_{corp}',w['id']+'.txt'); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(src,dst)
            texts[corp]=f'texts_{corp}/{w["id"]}.txt'
    links[w['id']]=dict(links=L,texts=texts,source=w['source'],note=w.get('note',''))
out['links']=links
# gutenberg cross-check editions
out['extra_sources']=[dict(label='Doctor Faustus, Dyce edition (Project Gutenberg 779)',url='https://www.gutenberg.org/ebooks/779'),dict(label='The Jew of Malta, Dyce edition (Project Gutenberg 901)',url='https://www.gutenberg.org/ebooks/901'),dict(label='EarlyPrint corpus metadata',url='https://earlyprint.org/'),dict(label='Folger Shakespeare downloads',url='https://www.folger.edu/explore/shakespeares-works/download/'),dict(label='Folger Early Modern English Drama (EMED)',url='https://emed.folger.edu/')]
TABLES=[('results/gi_verify/gi_verify.md','Impostors verification, all plays (Folger/EMED corpus)','verify'),
 ('results/ep/gi_verify/gi_verify.md','Impostors verification, all plays (all-EarlyPrint corpus)','verify'),
 ('results/q/gi_verify/gi_verify.md','Impostors verification (quarto corpus)','verify'),
 ('results/func/pairwise_distinguishability.md','Chunk classifiers, function words, with per-play probabilities','classify'),
 ('results/ep/func/pairwise_distinguishability.md','Chunk classifiers, function words (all-EarlyPrint)','classify'),
 ('results/func/group_distances.md','Group distances and clustering, function words','map'),
 ('results/func/attribution_loo.md','Leave-one-play-out attribution, function words','map'),
 ('results/func/distance_matrix_cosine_delta.csv','Full distance matrix, cosine delta, function words (CSV)','map'),
 ('results/ep/crossentropy_masked/crossentropy.md','Character-model cross-entropy, names masked (all-EarlyPrint)','chars'),
 ('results/ep/crossentropy_masked/affinity.md','Double-centred affinities between author models','chars'),
 ('results/ep/crossentropy_masked/quarto_check.md','Folio vs quarto check for Titus and Richard III','chars'),
 ('results/crossentropy_masked/edition_effect.md','Edition effect: same play, two editions','chars'),
 ('results/q/crossentropy_masked/crossentropy.md','Character-model cross-entropy (quarto corpus)','chars'),
 ('results/words/word_profiles.md','Which words separate two sets of plays (Folger/EMED)','words'),
 ('results/ep/words/word_profiles.md','Which words separate two sets of plays (all-EarlyPrint)','words'),
 ('results/words/zeta.md','Burrows\'s Zeta: marker words, accuracies, Henry VI projection (Folger/EMED)','words'),
 ('results/ep/words/zeta.md','Burrows\'s Zeta (all-EarlyPrint)','words'),
 ('results/scene_scan/scene_scan.md','Scene scan of 1-3 Henry VI, Titus, Richard III','scenes'),
 ('results/scene_scan/prose_verse.md','Verse-only and prose-only rescoring of Henry VI','scenes'),
 ('results/finetune/taskvectors.md','GPT-2 weight-delta cosines (Folger/EMED)','idea'),
 ('results/ep/finetune/taskvectors.md','GPT-2 weight-delta cosines (all-EarlyPrint)','idea'),
 ('results/finetune/embeddings.md','GPT-2 relative embedding geometry (Folger/EMED)','idea'),
 ('results/ep/finetune/embeddings.md','GPT-2 relative embedding geometry (all-EarlyPrint)','idea'),
 ('results/ep/finetune/perplexity.md','GPT-2 held-out bits per token (all-EarlyPrint)','neural'),
 ('results/finetune/perplexity.md','GPT-2 held-out bits per token (Folger/EMED)','neural'),
 ('REPORT.md','Full report, version 2','doc'),('NOTEBOOK.md','Lab notebook: every step, bug and change of mind','doc'),('README.md','How to rerun everything','doc'),
 ('scripts/works.json','Corpus definition, Folger/EMED corpus','doc'),('scripts/works_ep.json','Corpus definition, all-EarlyPrint corpus','doc'),('scripts/works_q.json','Corpus definition, quarto corpus','doc')]
tabs=[]
for rel,label,sec in TABLES:
    src=P+rel
    if not os.path.exists(src): continue
    dst=os.path.join(SITE,'data',rel); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(src,dst)
    tabs.append(dict(path='data/'+rel,label=label,section=sec))
out['tables']=tabs
json.dump(out,open(sys.argv[1],'w'))
print({k:(len(v) if hasattr(v,'__len__') else v) for k,v in out.items()})
print(out['mds_var']); print(list(pp.keys())); print(type(pp['bits']), list(pp['bits'])[:2] if isinstance(pp['bits'],dict) else pp['bits'][:1]); print(pp['models'])
