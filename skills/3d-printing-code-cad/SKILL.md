---
name: 3d-printing-code-cad
type: procedure
description: "Code-CAD workflow for designing printable parts in Python with build123d: pure-geometry part scripts + the shared cadlib.py (STL/STEP export, multi-view PNG render, live preview), the printed fit-gauge methodology for measuring unknown shafts and holes, the calibration-coupon procedure for per-printer hole shrinkage, and per-part documentation conventions. Auto-invoke when designing a replacement or custom part in code, measuring a shaft/bore/press-fit for printing, asking 'model this in Python', or setting up build123d."
tags: [3d-printing, cad, build123d]
---

# Code CAD with build123d

Design printable parts as small Python scripts instead of driving a GUI CAD
app. A part is a script; the script is the lossless, diffable, re-runnable
record of the design. Code CAD helpers by Finn Randall (`scripts/cadlib.py` and
`scripts/calibration.py`, MIT licensed, see the copyright headers).

## Convention: always present the part folder path

In every exchange about a part, state its folder path (e.g.
`~/dev/3d-prints/<part>/`) so the user can explore it in Finder, every
response, not only when files change.

## Layout: one folder per part

```
<project>/
  cadlib.py            # the shared helper library (copy from scripts/ here)
  <part name>/
    <part>.py          # pure geometry + a PARAMETERS block
    <Part name>.md     # the part's doc: measurements, decisions, gotchas
    <part>.png         # multi-view render (generated - never hand-edit)
    <part>.stl         # what BambuStudio slices (generated)
    <part>.step        # editable CAD original - the lossless record (generated)
```

Small projects keep everything flat in the part folder (`out_dir="."`);
otherwise exports land in `out/` beside the script. All generated files are
rewritten on every run - never hand-edit them.

## The part script contract

- **Pure geometry.** The script defines shapes with build123d; `cadlib`
  handles export, reporting, and preview. Three calls:
  `cadlib.save(shape, "name")` → STL + STEP + printed bbox/volume/mass report;
  `cadlib.render(shape, "name")` → shaded multi-view PNG contact sheet;
  `cadlib.show(shape)` → live ocp_vscode preview if a viewer is listening
  (never raises when it isn't).
- **A PARAMETERS block at the top** - every adjustable dimension is a named
  constant in mm, commented with what it is and where the number came from.
  See `scripts/calibration.py` for the exemplar shape of a part script.
- **Material default is PETG** - PLA is brittle in flexure, which matters for
  the clips and knobs this workflow mostly produces. Mass estimates use
  `cadlib.FILAMENT_DENSITY`.
- **Render before you print.** The multi-view sheet exists to catch geometry
  mistakes before they become a failed print - and it gives you
  something to show the person before they commit filament to a print. The top/bottom
  views are deliberately tilted ~20° off-axis: flat shading makes raised
  features on flat faces invisible from straight above.

## Fit methodology: the crown jewels

### 1. Calibration coupon first (per printer × material × profile)

Printed holes always come out undersize (extrusion width, slicer
compensation, die-swell at inside corners). The error is roughly a **constant
diameter offset, not a percentage**, so one measurement covers every hole.
Print `scripts/calibration.py` (nominal 3/4/5/6 mm holes) flat on the bed in
the actual material and profile, let it **cool fully**, then caliper each
hole across two perpendicular diameters and **take the smaller** (holes print
oval; a pin must pass the smaller). The four offsets should agree within
~0.05 mm; if not, distrust the smallest hole. Add the offset to every nominal
bore in later parts. Re-run when filament brand or nozzle changes.

### 2. Bespoke fit gauges for unknown shafts

When a dimension can't be measured confidently (D-shaft flat depth, bore
clearance), don't guess - print a gauge plate that brackets it:

- **Sweep the uncertain dimension in steps** (e.g. flat depth 2.4→3.2 mm in
  0.2 steps), centered on your best estimate.
- **Give every hole in a shape-sweep row the same loose clearance**, so fit
  tightness can't be mistaken for the shape signal. Sweep clearance in a
  separate row of plain round holes.
- **Exploit asymmetric failure modes.** A hole with a flat *deeper* than the
  shaft's blocks entirely; a *shallower* one fits with rock. So: **the
  deepest hole that still accepts the shaft is the answer.** For clearance:
  the tightest hole that slides on - it absorbs printer undersizing and
  measurement error together, which push the same way and needn't be
  separated.
- **When adopting a bracketed value, take the safe end.** A slightly-shallow
  flat costs a little rotational slop; a slightly-deep one locks you out.
- **Labels: engraved large, no decimal point** - the number is ×0.1 mm
  (`24` = 2.4 mm). Decimal points don't survive being read off grey PETG at
  arm's length. Distinguish rows by hole shape and digit count.

### 3. Document measurement provenance

The part's `.md` records every measurement in a table with a **source
column** (`calipers`, `printed gauge - hole 24 fit, 26 blocked`, `approx`).
Keep a **"Superseded readings"** section: when a number turns out wrong,
don't delete it - record it, why it was wrong, and what caught it.
Self-consistent-but-wrong measurement pairs look fine on paper; often only
the photo/shape mismatch catches them.

### 4. Orientation diagrams generated from part constants

For anything whose orientation is ambiguous in prose ("N° from the flat" -
which side of a D-shaft is "the D"?), generate a to-scale diagram from the
**same constants as the part** (see the `orientation.py` pattern), so the
diagram cannot drift out of step with the geometry.

## Setup

```bash
uv pip install build123d          # brings numpy + pillow (render deps) with it
uv pip install ocp_vscode         # optional: live viewer
```

Copy `scripts/cadlib.py` into the project root; part scripts add the project
root to `sys.path` and `import cadlib` (see the `sys.path.insert` near the top of calibration.py).

## Files in this skill

Code CAD helpers by Finn Randall.

| file | what |
|---|---|
| `scripts/cadlib.py` | the shared library - save/render/show; docstrings carry the detailed rationale |
| `scripts/calibration.py` | the hole-shrinkage coupon AND the exemplar part-script shape |

## Related skills

`3d-printing-models-and-tools` covers *sourcing* existing models, mesh repair,
and GUI CAD picks - reach for it when someone else has already designed the
thing. This skill is for when you're designing the part yourself. Filament
choice questions route to `3d-printing-filaments`.
