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
# perplexity ep
pp=json.load(open(P+'results/ep/finetune/perplexity.json'))
out['ppl_ep']=pp
json.dump(out,open(sys.argv[1],'w'))
print({k:(len(v) if hasattr(v,'__len__') else v) for k,v in out.items()})
print(out['mds_var']); print(list(pp.keys())); print(type(pp['bits']), list(pp['bits'])[:2] if isinstance(pp['bits'],dict) else pp['bits'][:1]); print(pp['models'])
