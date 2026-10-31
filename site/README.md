# Marlowe or Shakespeare? — interactive site

A single-page, dependency-free site that explains the study and lets a reader explore
every result. Published copy: https://claude.ai/artifact/HW36LyVAYhSprRwiVAwbXp

## Files

| file | purpose |
|---|---|
| `index.html` | the whole page: markup, CSS and chart code (hand-drawn SVG, no libraries). Loads `data.json` by relative `fetch`. |
| `data.json` | every number the charts use, generated from `results/` by `extract.py`. Do not edit by hand. |
| `extract.py` | rebuilds `data.json` from `scripts/works*.json` and `results/**`, and refreshes the copies below. Run after re-running any analysis. |
| `texts_main/`, `texts_ep/`, `texts_q/` | the cleaned dialogue-only texts the analyses used, one file per play per corpus (copied from `data/clean*`). Linked from the play cards. |
| `data/` | copies of the result tables, REPORT.md, NOTEBOOK.md and the corpus definitions that the page links to. |

## Regenerate the data

```
.venv/bin/python site/extract.py site/data.json
```

## Preview locally

The page fetches `data.json`, so it must be served over HTTP, not opened as a file:

```
python3 -m http.server 8000 --directory site
# then open http://localhost:8000/
```

## Deploy

Copy the whole folder except `extract.py` and this README to any static host (GitHub Pages, Netlify, S3, nginx).
Fonts come from Google Fonts; everything else is inline. No build step.

## Editing notes

- Colours are CSS tokens at the top of `<style>` with light and dark values; charts read them via `var(--…)`.
- Each chart is one self-contained block in the `<script>` and reads from the `D` object (the parsed `data.json`).
- The `<meta name="claude:viewport-fit-sides">` tag is for the claude.ai artifact viewer and is harmless elsewhere.
