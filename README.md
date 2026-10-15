# 3d-printing: a Claude Code plugin

Eight knowledge skills for hobby FDM 3D printing. They were written around a Bambu Lab A1 with an AMS Lite, but most of the material (filaments, drying, maintenance, recycling, model sources, licences, code CAD, publishing) applies to any consumer FDM printer. Prices are rough US figures; each skill says when they were last checked.

| Skill | What it covers |
|---|---|
| `3d-printing-filaments` | Filament families (PLA, PETG, ABS, ASA, TPU, nylon, PC, composites), properties, print settings, hardware requirements, a Bambu A1 compatibility table, brand notes |
| `3d-printing-filament-sourcing` | Where to buy 1.75 mm filament, a landed-cost comparison procedure, sale cycles, counterfeit warnings |
| `3d-printing-storage-and-maintenance` | Humidity targets, dryboxes and desiccant, drying temperatures and times, preventive maintenance, a defect-to-fix matrix |
| `3d-printing-recycling-and-waste` | Spool reuse and take-back, scrap recycling options, waste-reducing slicer and design choices |
| `3d-printing-models-and-tools` | Model sites and licences, AI model generators, CAD and mesh tools, mesh repair, file formats, slicer choice, a preview-render script |
| `3d-printing-code-cad` | Designing printable parts in Python with build123d, a printed fit-gauge method for unknown shafts and holes, a hole-shrinkage calibration coupon |
| `3d-model-publishing` | Packaging a listing and publishing to Printables, MakerWorld and Thingiverse, tagging, licence defaults, a map of model sites |
| `3d-printing-knowledge-refresh` | A procedure for keeping the other skills current |

## Install

```
/plugin marketplace add johntrandall/claude-plugins
/plugin install 3d-printing@johntrandall-plugins
```

## Requirements

- An FDM printer. The A1-specific notes are for the Bambu Lab A1; the rest is general.
- Bambu Studio or another slicer (OrcaSlicer and PrusaSlicer are covered).
- For the preview script in `3d-printing-models-and-tools`: OpenSCAD, and macOS paths (`brew install --cask openscad`).
- For `3d-printing-code-cad`: `uv` and build123d (`uv pip install build123d`).

## Credits

Code CAD helpers by Finn Randall (`skills/3d-printing-code-cad/scripts/cadlib.py` and `calibration.py`), MIT licensed.

## Disclaimer

This plugin is not affiliated with Bambu Lab, Prusa, or any vendor or site it mentions.

## Licence

MIT, see [LICENSE](LICENSE).
