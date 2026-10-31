"""Build clean spoken-text corpus from Folger Shakespeare TXT and EMED TEI XML.

Output: data/clean/<id>.txt  (one verse line / prose segment per line, dialogue only)
        data/clean/manifest.json (metadata + word counts)
"""
import json, re, sys, pathlib
import xml.etree.ElementTree as ET

import os
ROOT = pathlib.Path(__file__).resolve().parents[1]
CORPUS = os.environ.get('CORPUS', 'main')
OUT = ROOT / "data" / ("clean" if CORPUS == 'main' else "clean_" + CORPUS)
OUT.mkdir(parents=True, exist_ok=True)
WORKS_FILE = ROOT / 'scripts' / ('works.json' if CORPUS == 'main' else f'works_{CORPUS}.json')

def local(tag):
    return tag.split('}', 1)[-1]

# ---------------- EMED (TEI) ----------------
def emed_word(w):
    """Pick regularised form (EMED > SHC > orig)."""
    regs = []
    for el in w.iter():
        if local(el.tag) == 'reg':
            regs.append((el.get('resp', ''), ''.join(el.itertext())))
    if regs:
        for resp, txt in regs:
            if 'EMED' in resp:
                return txt
        return regs[0][1]
    for el in w.iter():
        if local(el.tag) == 'orig':
            return ''.join(el.itertext())
    return ''.join(w.itertext())

def emed_collect(node, buf):
    """Walk an <ab>/<l>/<p> and append tokens; newline at verse-line milestones."""
    for child in node:
        t = local(child.tag)
        if t in ('speaker', 'stage', 'note', 'fw', 'head'):
            continue
        if t == 'w':
            buf.append(emed_word(child))
        elif t == 'pc':
            buf.append(''.join(child.itertext()))
        elif t == 'c':
            buf.append(' ')
        elif t == 'milestone' and child.get('unit') == 'wln':
            buf.append('\n')
        elif t == 'lb':
            buf.append('\n')
        else:
            emed_collect(child, buf)

def parse_emed(path):
    tree = ET.parse(path)
    root = tree.getroot()
    body = None
    for el in root.iter():
        if local(el.tag) == 'body':
            body = el
            break
    buf = []
    for sp in body.iter():
        if local(sp.tag) != 'sp':
            continue
        for child in sp:
            t = local(child.tag)
            if t in ('speaker', 'stage', 'note'):
                continue
            emed_collect(child, buf)
        buf.append('\n')
    text = ''.join(buf)
    return text

# ---------------- Folger TXT ----------------
START_RE = re.compile(r'^(ACT \d+|INDUCTION|PROLOGUE|Scene \d+)\s*$')
HEADING_RE = re.compile(r'^(ACT \d+|Scene \d+|INDUCTION|PROLOGUE|EPILOGUE|CHORUS|FINIS|=+)\s*$')
SPEAKER_RE = re.compile(r"^([A-Z][A-Z0-9' .,\-]*[A-Z0-9.])(?:\s{2,}(.*))?$")

def parse_folger(path):
    raw = pathlib.Path(path).read_text(encoding='utf-8')
    lines = raw.splitlines()
    start = next(i for i, l in enumerate(lines) if START_RE.match(l))
    text = '\n'.join(lines[start:])
    # remove stage directions, possibly multi-line
    text = re.sub(r'\[[^\]]*\]', ' ', text, flags=re.S)
    out = []
    for line in text.splitlines():
        line = line.rstrip()
        if not line.strip() or HEADING_RE.match(line.strip()):
            continue
        m = SPEAKER_RE.match(line)
        if m:
            # speaker label line, possibly with inline speech after 2+ spaces
            rest = m.group(2)
            if rest and rest.strip():
                out.append(rest.strip())
            continue
        out.append(line.strip())
    return '\n'.join(out)


# ---------------- Gutenberg (Dyce-style layout) ----------------
GUT_START_RE = re.compile(r'^\s*(ACT\b|Enter\b|PROLOGUE|CHORUS\.)')
GUT_SPEAKER_RE = re.compile(r"^([A-Z][A-Z .'\-]*?)\.\s+(.*)$")

def parse_gutenberg(path):
    raw = pathlib.Path(path).read_text(encoding='utf-8', errors='replace')
    lines = raw.splitlines()
    s = next(i for i, l in enumerate(lines) if '*** START OF' in l) + 1
    e = next(i for i, l in enumerate(lines) if '*** END OF' in l)
    lines = lines[s:e]
    # cut footnotes section
    for i, l in enumerate(lines):
        if re.match(r'^\s*\[?Footnotes?\b', l):
            lines = lines[:i]
            break
    first = next(i for i, l in enumerate(lines) if GUT_START_RE.match(l))
    text = '\n'.join(lines[first:])
    text = re.sub(r'\[[^\]]*\]', ' ', text, flags=re.S)
    out = []
    for line in text.splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(' '))
        if indent >= 8:            # stage directions / headings
            continue
        line = line.strip()
        if re.fullmatch(r"[A-Z0-9 .,'\-]+", line):   # ACT I., SCENE II., name lists
            continue
        m = GUT_SPEAKER_RE.match(line)
        if m:
            line = m.group(2).strip()
        if line:
            out.append(line)
    return '\n'.join(out)


# ---------------- EarlyPrint (TEI, <w reg=...>) ----------------
def ep_collect(node, buf):
    for child in node:
        t = local(child.tag)
        if t in ('speaker', 'stage', 'note', 'fw', 'head', 'figure'):
            continue
        if t == 'w':
            txt = child.get('reg') or ''.join(child.itertext())
            buf.append(txt.replace('\u017f', 's'))
            buf.append(' ')
        elif t == 'pc':
            buf.append(''.join(child.itertext()))
            buf.append(' ')
        elif t in ('l', 'p', 'ab', 'lg'):
            ep_collect(child, buf)
            buf.append('\n')
        else:
            ep_collect(child, buf)

_EP_CACHE = {}
def parse_earlyprint(path, select=None):
    if path not in _EP_CACHE:
        _EP_CACHE[path] = ET.parse(path).getroot()
    root = _EP_CACHE[path]
    if select and 'head' in select:        # one play inside a collection (the Folio)
        pat = re.compile(select['head'], re.I)
        def head_of(d): return re.sub(r'\s+', ' ', ''.join(''.join(h.itertext()) for h in d if local(h.tag) == 'head'))
        body = next(d for d in root.iter() if local(d.tag) == 'div' and d.get('type') == 'play' and pat.search(head_of(d)))
    elif select and 'text_index' in select:  # one <text> inside a <group> (Tamburlaine 1 and 2)
        texts = [t for t in root.iter() if local(t.tag) == 'text' and any(local(c.tag) == 'body' for c in t)]
        body = next(c for c in texts[select['text_index']] if local(c.tag) == 'body')
    else:
        body = next(el for el in root.iter() if local(el.tag) == 'body')
    buf = []
    def walk(node):
        for child in node:
            t = local(child.tag)
            if t in ('speaker', 'stage', 'note', 'fw', 'head', 'figure', 'front', 'back'):
                continue
            if t == 'sp':
                ep_collect(child, buf); buf.append('\n')
            elif t in ('l', 'p', 'ab', 'lg'):        # speech lines the quarto printed without a speaker label
                ep_collect(child, buf); buf.append('\n')
            else:
                walk(child)
    walk(body)
    text = ''.join(buf)
    text = re.sub(r' +([,.;:!?])', r'\1', text)   # re-attach punctuation
    text = text.replace('\u00a0', ' ')
    return text

# ---------------- normalisation ----------------
def normalise(text):
    text = text.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    text = text.replace('—', ' -- ').replace('–', ' -- ')
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r' *\n *', '\n', text)
    text = re.sub(r'\n{2,}', '\n', text)
    return text.strip() + '\n'

WORD_RE = re.compile(r"[A-Za-z]+(?:['\-][A-Za-z]+)*")

def main():
    works = json.loads(WORKS_FILE.read_text())
    manifest = []
    for w in works:
        path = ROOT / w['file']
        text = parse_earlyprint(path, w.get('select')) if w['source'] == 'earlyprint' else {'emed': parse_emed, 'folger': parse_folger, 'gutenberg': parse_gutenberg}[w['source']](path)
        text = normalise(text)
        (OUT / f"{w['id']}.txt").write_text(text, encoding='utf-8')
        nw = len(WORD_RE.findall(text))
        w = dict(w, words=nw, lines=text.count('\n'))
        manifest.append(w)
        print(f"{w['id']:8s} {w['author']:12s} {w['group']:18s} words={nw:6d}")
    (OUT / 'manifest.json').write_text(json.dumps(manifest, indent=1))

if __name__ == '__main__':
    main()
