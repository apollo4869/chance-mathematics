# Reproducing the publication vectors

Run from the project root, using Node.js and Python 3.12:

```powershell
python -m pip install -r assets/visuals/requirements.txt
$env:CHANCE_CJK_FONT = 'C:\Windows\Fonts\NotoSansSC-VF.ttf'
python tools/generate-math-visuals.py
```

The generator also recognizes the workspace-local `qa/visual-runtime` dependencies used by this build. The CJK font must already be installed; it is never downloaded or redistributed. `print-manifest.json` records the actual font and resolved face hashes, package versions, and every vector-file hash. The SVG uses glyph outlines and the vector PDF embeds subset TrueType fonts. See `font-notice.txt` for notices extracted from the installed font's original name table and Matplotlib's DejaVu font licence.

Variable-font conversion fixes weight at 400 and preserves the original font's `head.created` and `head.modified` values with `recalcTimestamp=False`. Its local cache filename includes the source-font SHA-256 and conversion-policy version. Removing that generated cache and rebuilding must reproduce the same font, PDF and SVG bytes; a warm cache is not required for determinism.

`math-model.js` is the mathematical source shared with the browser experiment. Node evaluates it to produce `data.json` and `spec.json`; Python reads that same data for all six groups of vectors. Random-walk panels reuse the existing `BookMath.walk` implementation and seed 918273, with the same pseudorandom increment prefixes separately rescaled at n=16,64,256. They are neither independent samples nor successive refinements of one continuous trajectory.

All figures have Chinese and English SVG/PDF files in `print/`. PNGs in `qa/math-visuals/` are local inspection renders only, not print originals. Every figure uses line styles, shapes, endpoint markers or hatching in addition to any color. Fixed white backgrounds preserve the original print contrast; the website can place them on a neutral figure card in dark mode without recoloring mathematics.

The typewriter model uses half-open intervals and the exact enumeration in Chapter 7. The conditional-expectation figure is abstract Hilbert geometry and its Pythagorean relation is an identity of squared L2 norms. It is not a pointwise identity of values or a statement that all random variables inhabit a plane.

The generator validates interval partitions and fixed-point hits, every scaled walk increment, spike area, mass/mean/variance of both discrete laws, and conditional-slice normalization. These numerical/model checks support the illustration and do not substitute for the book's proofs.
