---
name: 3d-printing-models-and-tools
description: Reference knowledge on where to source 3D models, AI generation tools, CAD/mesh-editing software stack, mesh repair, file formats, and slicer choice. Includes a zero-context preview-render script (scripts/render-previews.sh) for .scad/.stl/.obj/.3mf. Auto-invoke when sourcing a model, choosing a CAD tool, editing/repairing a mesh, picking a slicer, or when the user asks for preview images/renders of a model file.
last_refreshed: 2026-10-15
---

# 3D Printing: Models, Tools, and Workflows

A practical reference for the agent advising on FDM (and occasionally resin) 3D printing. Covers where to get models, how to make them, how to fix them, and how to slice them. Current as of 2026-06 (prices as of October 2026) with explicit notes on what changes monthly (AI tools, slicer betas).

---

## 0. Convention: always present the project folder path

In every exchange about a print project, state the project's folder path
(e.g. `~/dev/3d-prints/<project>/`) so the user can explore it in Finder,
every response, not only when files change.

## 1. Where to Find Models

### Curated hobbyist marketplaces (general consumer)

**Printables.com** (Prusa)
- **Good for:** Functional prints, everyday items, models that *actually print*. Heavy curation, strong "print profile" culture where the uploader pre-tunes settings for PrusaSlicer.
- **License:** Predominantly Creative Commons (CC-BY, CC-BY-SA, CC-BY-NC). License is shown per-model.
- **Paywall:** None. Optional "tip the designer" and a contest/rewards system that pays designers in Prusa store credit.
- **Quality bar:** High. The community downvotes models that don't print, and the contest engine attracts engineering-grade uploaders.
- **Default starting point** for functional FDM prints.

**MakerWorld** (Bambu Lab)
- **Good for:** Bambu printers specifically. Models often ship as `.3mf` with AMS color mapping, support placement, and slicer settings baked in - load it in Bambu Studio and hit print.
- **License:** Bambu's own "Standard Digital File License" plus optional CC. Read the license per-model; commercial use rules are stricter than Printables.
- **Paywall:** Free downloads; designers earn "points" redeemable for store credit. Some models are "premium" (cost points).
- **Quality bar:** High for Bambu-flow models. Quality outside the AMS color-print niche is hit-or-miss.
- **Default for Bambu owners** who want zero-fuss multicolor.

**Thingiverse** (MakerBot/Stratasys)
- **Good for:** Historical archive - anything posted between roughly 2010 and 2020 likely lives only here. Tons of legacy designs, replacement parts for old appliances, etc.
- **License:** CC variants and the older Thingiverse-specific license. Per-model.
- **Paywall:** None.
- **Quality bar:** Wildly variable. No serious curation. Search returns ten broken remixes of one good design.
- **Use when:** Other sites don't have it. Treat all downloads as "needs verification before printing."

**Cults3D**
- **Good for:** Designer-priced models, especially fan art, tabletop terrain, decorative items. A real marketplace - many models are paid.
- **License:** Cults3D's own license terms; commercial use generally requires the designer's explicit permission or a separate license tier.
- **Paywall:** Mixed free/paid. Common price range $1–$15 per model.
- **Quality bar:** Generally good for paid models (designers want repeat customers).

**MyMiniFactory (MMF)**
- **Good for:** Tabletop miniatures (D&D, Warhammer-compatible), curated artistic models. Strong "Tribes" subscription model for ongoing minis releases.
- **License:** Per-model; MMF has a "personal use" default with explicit commercial license upgrades available.
- **Paywall:** Mixed free/paid. Tribes is a recurring monthly subscription ($5–$25/mo per creator) for ongoing drops.
- **Quality bar:** Very high for paid minis. Free section is solid but smaller.
- **Default for resin minis printing.**

**Pinshape**
- **Good for:** Largely obsolete; bought by Formlabs years ago and limped. Mention only if a legacy link points there.

### Meta-search and discovery

**Yeggi.com**
- **Good for:** Searches across Printables, Thingiverse, MyMiniFactory, Cults3D, Thangs, MakerWorld, and ~30 other sites simultaneously. The "Google for STLs."
- **Paywall:** None.
- **Use as the default first search** when you don't know which site has a model.

**Thangs**
- **Good for:** Geometric search ("upload a photo, find similar models"), and a meta-aggregator of other sites' content. Also hosts originals.
- **License:** Per-model.
- **Paywall:** Free with optional paid tier for unlimited geometric searches and faster downloads.
- **Quality bar:** Aggregator quality reflects the source site.

### Engineering / CAD-grade

**GrabCAD Community**
- **Good for:** Parametric engineering parts - bearings, brackets, fasteners, electronics enclosures, full assemblies. Frequently `.STEP` files (editable in CAD), not just STL.
- **License:** GrabCAD's community license - generally free for personal and non-commercial use. Read the per-model terms.
- **Paywall:** None (the paid product is GrabCAD Workbench / Print, the company's professional tooling).
- **Quality bar:** High for engineering content. Login required.
- **Default for "I need a CAD-quality bracket / a real-world part's STEP file."**

**McMaster-Carr** (not a model site, but worth knowing)
- Their parts catalog includes downloadable STEP files for nearly every fastener, bearing, pneumatic fitting, etc. Best reference dimension source on the internet.

### Generic 3D asset stores (less suited for printing)

**Sketchfab** - mostly textured assets for renders/games. Some printable, many not (no concept of wall thickness or watertightness). License model varies (CC + commercial).

**CGTrader, TurboSquid, Free3D** - marketplaces aimed at VFX/games. Print-quality models exist but are the minority; most are surface meshes that look right but won't slice cleanly.

**Fab.com** (Epic Games' unified asset marketplace, replaces Quixel/Sketchfab Store/Unreal Marketplace) - render/game-asset oriented, similar caveats.

**Hugging Face** - has a small but growing 3D models section (mostly outputs of AI generation research). Useful for finding example datasets and research artifacts more than ready-to-print models.

**GitHub** - yes, many models live here, especially:
- OpenSCAD source for parametric designs (search `language:OpenSCAD`).
- CadQuery / build123d Python scripts.
- Voron printer parts, RatRig parts, Klipper-related accessories.
- Open-source hardware projects (Prusa MK4 source files, Voron mods).
- Treat as "the model + the code that generated it" - usually higher provenance than a bare STL.

### Patreon and similar creator-direct

A meaningful share of high-end tabletop miniature designers publish primarily through **Patreon**, **Tribes (MMF)**, or **Kickstarter STL drops**. Tiers typically $5–$15/mo, with each month delivering a themed set (10–40 minis). Notable examples in the space: Artisan Guild, Cast n Play, Loot Studios, Archvillain Games, Titan Forge, Lord of the Print. License is "personal use only" by default; commercial (selling prints) requires a per-creator commercial tier.

### License decision shorthand

- **CC-BY:** print, modify, redistribute, sell prints - but credit the designer.
- **CC-BY-SA:** same, but derivatives must also be CC-BY-SA.
- **CC-BY-NC:** personal use only; no selling prints or derivatives commercially.
- **CC-BY-ND:** print as-is, no derivatives, credit required.
- **"Personal use"** (MMF default, many Patreon): print for yourself; don't sell prints; don't redistribute the file.
- **Bambu Standard License:** check per-model; some prohibit re-uploading even modified versions.

When in doubt, contact the designer. Most are happy to license commercially for a flat fee or revenue share.

---

## 2. AI-Generated Models: Current State (2026-Q2)

This section changes monthly. Below reflects mid-2026; re-research before relying on specifics.

### Honest summary

AI image/text → 3D has crossed from "useless toy" into "genuinely useful for some categories" between 2024 and 2026, but **it is not "press button, print figurine."** Expect 5–15 minutes of cleanup per model for figurines, much more for anything mechanical.

### The current contenders

**Meshy.ai** - Most commonly recommended "default" as of mid-2026 for figurines and stylized objects. Text-to-3D and image-to-3D. Cleaner topology than most competitors, decent texturing, exports STL/OBJ/GLB/FBX/3MF. Free tier with ~200 monthly credits; paid tiers $20–$60/mo. Printability for character/figurine prompts is "usually slice-ready after a watertight check."

**Tripo (Tripo3D / TripoAI)** - Fast generation, good detail. Frequent complaint: produces shells that look right but have internal cavities, sealed-off "filled" regions where you wanted a hollow, or non-manifold edges in fine detail. Free tier; paid $20–$50/mo. Strong on stylized characters, weaker on mechanical.

**Rodin / Hyper3D Rodin** - High-fidelity output, frequently cited as best-in-class for figurine surface detail in late 2025 / early 2026. Topology is generally cleaner than Tripo's. Subscription; pro tiers $30–$80/mo. Has been used commercially by tabletop miniature designers as a sketch-pass tool.

**Hunyuan3D (Tencent)** - Open-weight model (Hunyuan3D-2.5 released 2025, 2.6+ rumored). Genuinely competitive output; runnable locally on a 24GB+ GPU. Free if you have hardware; web access via Tencent's interface has limited free tier. Best choice for users who want to self-host or for batch generation without per-model costs.

**Common Sense Machines (CSM)** - Pivoted into more of an enterprise/agent platform. Less consumer-facing in 2026.

**Trellis (Microsoft Research)** - Open-source, image-to-3D, strong topology on many tests. Self-hostable.

**Hitem3D** - Newer 2025 entrant focused specifically on print-readiness; explicit watertightness claims in marketing. Worth trying for FDM-targeted generation.

### What the meshes look like

Common defects regardless of tool:
- **Non-manifold edges** (edges shared by more than two faces, or zero faces) - the slicer's most-hated defect.
- **Flipped normals** - inside-out faces; slicer can't tell "inside" from "outside."
- **Internal geometry** - phantom faces inside the model that confuse infill.
- **Sealed cavities** where the prompt implied a hollow (a cup that's solid inside).
- **Sub-wall-thickness features** - a sword blade 0.1mm thick that can't be printed at 0.4mm nozzle.
- **Bad bottom** - figurines often have no flat surface to print from, requiring manual flat-cut or a custom base.
- **Lo-res blob bases** - feet/hands often melt into a low-detail blob.

### Required post-processing pipeline

1. **Open in Blender or Meshmixer** (or use a slicer's built-in repair).
2. **Run a watertight / manifold check.** Blender's "3D Print Toolbox" addon (built in, ship-default since ~3.6) does this in one click.
3. **Fix non-manifold edges**, fill holes, recompute normals (Blender: `Shift+N`).
4. **Decimate if oversized.** AI tools often emit 1M+ poly meshes for a 50mm figurine; decimate to 200–500k polys before slicing.
5. **Add a flat base** - Boolean subtract with a cube at the desired bottom plane, or use the slicer's "cut" tool.
6. **Check wall thickness** - Blender's Print Toolbox flags thin walls. Either thicken in the editor or accept the parts will be supports-only / decorative.
7. **Slice and pre-render the layer view** to catch obvious explosions before printing.

### Best-for matrix

| Use case | Recommended AI tool (2026-Q2) | Caveat |
|---|---|---|
| Character / figurine for tabletop | Meshy or Rodin | Resin print expected; FDM works for ≥50mm scale |
| Stylized decorative object | Meshy | Lower fidelity is OK |
| Self-hosted batch generation | Hunyuan3D / Trellis | Need GPU |
| Mechanical bracket, gear, enclosure | **Don't.** Use CAD. | AI tools don't understand tolerances |
| Concept sketch → refine in CAD | Any of them | Use as starting geometry, retopo in CAD |

**Hard rule:** for anything that has to mate with another part, AI is concept-only. Re-model in OnShape / Fusion / FreeCAD with real dimensions.

---

## 3. CAD and Modeling Tools

Pick by use case, not by feature checklist.

### Parametric / engineering (history-based modelers)

**OnShape**
- Browser-based, real Parasolid kernel (same as SolidWorks), genuinely professional.
- Free for "public" documents (everyone can see your work). Paid tiers ($1500/yr+) for private work.
- **Default recommendation** for a new hobbyist starting parametric CAD in 2026 - no install, no fragility, real version control, runs on anything including a Chromebook.

**Fusion 360**
- Free "Personal use" license - gated by usage type, has had several waves of feature-restriction (no rapid file switching, at most 10 active editable files, etc.) but parametric modeling itself is still free.
- Mature, cross-platform (Mac/Windows; no Linux), strong sheet-metal and CAM (machining toolpaths) for users headed toward CNC.
- Default for users who already know it; OK for new users who can tolerate Autodesk's account/cloud quirks.

**FreeCAD**
- Open-source, runs anywhere including Linux. **FreeCAD 1.0 released late 2024**, which removed the long-standing "topological naming problem" - finally usable for non-trivial assemblies.
- Default for users who refuse subscription/cloud software, or who want to scriptable-extend their CAD.

**SolidWorks Maker** - $48/yr hobbyist tier of full SolidWorks. Locked to "maker" (no commercial use). Worth it if you've used SolidWorks at school/work.

**Shapr3D** - iPad / Apple Silicon Mac focused, touch-and-pencil friendly. Subscription, $25–$40/mo. Genuinely good for sketch-on-couch parametric modeling.

### Mesh / artistic / sculpting

**Blender** (free, open-source)
- Industry-dominant for non-parametric 3D. Sculpting, mesh editing, animation, rendering.
- The 3D-Print Toolbox addon (ships built-in) is the agent's first stop for mesh repair, wall thickness checks, and volume/weight estimation.
- **Default recommendation for artistic / mesh-based work.**

**ZBrush** - sculpting heavyweight, used by professional figurine designers. Now $36/mo or $400 perpetual. Maxon-owned.

**Nomad Sculpt** - iPad sculpting, $20 one-time. Surprisingly capable; many tabletop minis are now sculpted on iPad.

### Programmatic / code-CAD

**OpenSCAD**
- Functional language, immutable, declarative geometry. Pure text-source CAD.
- Old (2010), stable, slow renderer.
- Default for parametric designs you want to share as source ("here's a customizable mount, edit these three variables").
- Many community libraries: BOSL2 (Belfry OpenScad Library 2) is the de facto standard library.

**CadQuery** (Python)
- Python library wrapping the OpenCASCADE kernel. STEP/BREP-native (not mesh-native like OpenSCAD).
- Better for engineering parts where you care about real solid geometry, fillets, chamfers.
- Less actively developed than build123d in 2025–2026.

**build123d** (Python)
- The successor to CadQuery, by one of CadQuery's primary developers. Cleaner API, more Pythonic, actively maintained.
- **Default recommendation for "I want to code my CAD in Python in 2026."**

**JSCAD** - JavaScript / browser-based OpenSCAD analogue. Niche but works.

### Quick mods and repair

**Tinkercad** - browser-based, Autodesk-owned, primitives-and-boolean modeling. Great for kids, quick name plates, modifying an existing STL with a hole or text.

**Meshmixer** - Autodesk killed development in 2021 but it still works and is still the go-to tool many users reach for to repair, hollow, smooth, and add supports. Free, Mac and Windows.

**Bambu Studio / OrcaSlicer mesh editing** - both have built-in cut, split, hollow, hole-add, text-emboss, mesh boolean, and auto-repair. Often sufficient for "I just need to chop this thing in half."

**PrusaSlicer cut / split-to-objects** - same.

**Netfabb online** (now Autodesk Netfabb, browser version is `service.netfabb.com`) - upload an STL, get a repaired STL back. Free. Best last-resort for "this mesh is broken and I don't want to deal with it."

### Pipeline: sculpting → printing

For high-detail organic models:
1. Sculpt in ZBrush (or Blender sculpt mode, or Nomad).
2. Decimate to printable poly count (ZBrush has Decimation Master; Blender has the Decimate modifier).
3. Export STL or OBJ.
4. Resin: import to Chitubox or Lychee, hollow, drain holes, supports, slice.
5. FDM: import to Bambu Studio / OrcaSlicer / PrusaSlicer, orient, supports, slice.

### Recommended default stack

- **If you want one parametric tool: OnShape.** Browser, no install, real kernel, free for hobby/public projects, version-controlled, runs on Chromebooks.
- **If you want one artistic tool: Blender.** Free, dominant, sculpting + mesh edit + repair all in one. The 3D-Print Toolbox alone justifies the install.
- **If you want one Python code-CAD: build123d.** Actively maintained, cleaner API than CadQuery, OpenCASCADE-backed.
- **For quick remixes: Bambu Studio or OrcaSlicer.** The slicer is already open; don't context-switch.

---

## 4. Common Mesh-Editing Operations

Operations the agent should be able to advise on:

### Scaling

- **In CAD:** rebuilds the geometry at the new size - features (fillet radius, hole diameter) scale proportionally. This is what you want for "make this bracket 25% bigger but keep the M3 hole at 3mm."
- **In slicer:** scales the mesh uniformly. Fast and fine for figurines, terrain, decorative parts. Bad for anything that mates with hardware - your 5mm hole becomes 6.25mm.
- **In Blender:** scaling is just a transform; the underlying mesh is unchanged. Apply the transform (`Ctrl+A → Scale`) to bake the new size in.
- **Rule of thumb:** if the model has features that interact with the physical world (holes, threads, snap-fits, mating surfaces), scale in CAD, never in the slicer.

### Splitting / cutting to fit the build plate

- All major slicers have a "cut" plane tool that splits at a plane and optionally adds connectors (alignment pegs).
- For more control: Blender boolean modifier with a cube intersect; or Meshmixer's plane-cut.
- Add **alignment dowels or dovetails** at the cut plane unless you're gluing two flat halves. Bambu Studio and OrcaSlicer can auto-add connectors as part of the cut.

### Hollowing

- **Resin context:** non-negotiable for cost and cure-stress reasons. Use Chitubox / Lychee's hollow tool (typically 2–3mm wall) and add drain holes (≥3mm diameter) at lowest points so uncured resin can escape.
- **FDM context:** the slicer's infill percentage already creates "hollow." Manual hollowing in CAD is only worth doing for large decorative pieces where you want a true thin shell to save grams and time, or to embed something (lights, magnets).

### Repairing non-manifold geometry

Order from least to most invasive:
1. **Slicer auto-repair** (Bambu Studio, PrusaSlicer "Repair through Netfabb" or "Fix model"). One click, usually works for minor issues.
2. **Blender 3D-Print Toolbox** (ships built-in): "Check All" reports problems; per-issue buttons fix them.
3. **Meshmixer** (`Analysis → Inspector`): visualizes problems as colored arrows; "Auto Repair All" handles most.
4. **Netfabb online** (`service.netfabb.com`): upload, download fixed version, free.
5. **Reconstruct from scratch** in CAD if the mesh is too broken to repair - sometimes faster than fixing.

### Adding tolerance / clearance

For FDM:
- **Press fits (parts that should snap together once):** ~0.1–0.2mm clearance per side (0.2–0.4mm total on diameters).
- **Sliding fits (drawers, linear motion):** ~0.3–0.5mm per side.
- **Hole that will be tapped:** print at the tap's "tap drill diameter" minus ~0.05mm (FDM holes print slightly undersized; tap will cut clean threads).
- **Hole that a screw passes through:** screw shaft diameter + 0.4–0.6mm (FDM holes are not round; oversize and use a washer).
- **Heat-set inserts (Voron-style):** match the insert's nominal diameter; the iron melts the plastic to size.
- **Magnets:** match the magnet diameter exactly; the press-fit relies on slight FDM hole shrinkage.

These are starting points. The honest answer is "print a tolerance test cube once per filament" - every printer + filament combination calibrates differently. Calibration test models exist on Printables; search "tolerance test."

### Mirroring, arraying, boolean ops

- All major slicers support these directly. Useful for: making a left-handed version of a right-handed bracket (mirror), printing many copies of one part (array), or combining two STLs into one print (boolean union).
- For complex booleans, do them in CAD or Blender, not the slicer.

### Reducing polygon count

Why: STLs over ~50MB choke many slicers (Cura especially), and AI-generated meshes routinely emit 5–20M poly garbage.

- **Blender Decimate modifier** - set "Ratio" to ~0.1, render, check the result. Most figurines stay visually identical at 10–20% of original poly count.
- **ZBrush Decimation Master** - preserves UV/detail better, more controllable.
- **Meshmixer `Edit → Reduce`** - fast, simple.

### File format conversion (STEP → STL → 3MF)

- **STEP → STL:** done at export from CAD. The CAD tool tessellates the BREP solid into triangles. Higher "deviation" / "tolerance" = fewer triangles, cruder curves. Set deviation to ~0.01mm for nice curves on a 50mm part.
- **STL → 3MF:** Bambu Studio, OrcaSlicer, PrusaSlicer all save as 3MF by default. The 3MF file includes the original mesh plus your slicer settings, color assignments, support placement, and modifier volumes.
- **OBJ → STL:** Blender, Meshmixer. OBJ supports vertex colors and material groups, which are lost going to STL.

What each format preserves:
- **STEP:** real solid geometry, history (sometimes), tolerances, assembly structure. Editable in any CAD.
- **STL:** triangle soup. No metadata, no color, no units (assumed mm), no history.
- **OBJ:** triangles + UV coordinates + vertex colors + material refs.
- **3MF:** triangles + color + supports + slicer settings + multi-part metadata + units. The modern STL replacement.
- **G-code:** the final machine instructions; not a model. Don't share G-code unless the recipient has your exact printer model and firmware version.

### Embedding text / engraving

- **In CAD:** use the text feature, extrude positive (raised) or negative (recessed).
- **In Blender:** Text object, convert to mesh, boolean union/difference.
- **In a slicer:** all major slicers have a text emboss tool. Easiest path for "add my name to this case."
- **Tip:** recessed text prints cleaner than raised text on FDM. Raised text under 1mm tall tends to be unreadable due to layer height and seam.

---

## 5. File Formats

| Format | Type | Preserves | When to use |
|---|---|---|---|
| **STEP** (.step / .stp) | BREP solid | Real geometry, history, units | CAD interchange. The "source code" of an engineering part. |
| **3MF** (.3mf) | Triangle mesh + metadata | Colors, supports, slicer settings, multi-part, units | Modern slicer-default. Send to someone who has the same slicer; they can print without re-configuring. |
| **STL** (.stl) | Triangle mesh | Triangles only | Universal interchange. Use when you don't know what slicer the recipient has. |
| **OBJ** (.obj) | Triangle mesh + extras | Triangles + UV + vertex colors + material refs | Mostly for AI-generated models with texture, or interchange with rendering tools. |
| **G-code** (.gcode / .bgcode) | Machine instructions | None of the above - it IS the toolpath | Final output. Printer-and-firmware specific. Don't share. |
| **F3D / SLDPRT / IPT** | Proprietary CAD | Full native data | Source files in Fusion / SolidWorks / Inventor respectively. Almost always also export STEP. |

**3MF status (2026):** widely supported by Bambu Studio, OrcaSlicer, PrusaSlicer, Cura, and most upload sites (Printables and MakerWorld accept both 3MF and STL). 3MF is becoming the default for new uploads, especially on MakerWorld where the AMS color/material assignments require it. STL is not going away - it remains the lowest-common-denominator interchange - but new content increasingly ships 3MF-first with STL as a fallback download.

---

## 6. Slicer Pipeline

### Current (2026-Q2) recommendations

| Printer | Recommended slicer | Why |
|---|---|---|
| Bambu Lab (A1 / P1 / X1 / H2D) | **Bambu Studio** | Official, AMS integration, cloud sync, print monitoring |
| Bambu Lab, but want offline / more control | **OrcaSlicer** | OSS fork of Bambu Studio with broader printer support |
| Prusa (MK3 / MK4 / Core One / XL) | **PrusaSlicer** | Native, best MMU/MMU3 multi-material support |
| Creality (Ender, K1, K2) | **OrcaSlicer** | Best community profiles, calibration features, beats Cura |
| Voron / RatRig / custom | **OrcaSlicer** | Per-printer profile flexibility |
| Resin (Elegoo, Anycubic, Phrozen) | **Lychee** or **Chitubox** | FDM slicers don't do resin |

### Bambu Lab A1 notes (generic, from experience)

- **Usable X width is about 248 mm, not 256.** The A1 excludes a strip of about 8 mm down the left edge (plus the front-left calibration corner). A single piece wider than roughly 248 mm fails with "no object fully inside the print volume" at any position, and rotating makes the bounding box worse. Split wider parts.
- **The toolhead LED is a dim light.** It is controllable from the screen or Bambu Studio, but camera frames stay dark with it on. There is no external light port.
- **A print that heats and moves but extrudes nothing** usually means the filament was never loaded into the extruder. Load it first (Prepare, Load Filament, pick the AMS tray) and confirm it extrudes before starting. A cold-extruded filament tip can deform and refuse to re-feed; cut the tip clean before reloading.
- **Check the first layer yourself.** Telemetry can report "running" for a print that is not depositing plastic. Confirm the bed target temperature is right for the material (about 80 C for PETG on textured PEI, not 35 C), that filament is actually loaded, and that the first layer adheres.
- **Command-line slicing can silently default to PLA.** If you slice with a system filament profile file passed by path, inherited settings such as `filament_type` and nozzle temperature may not resolve, and the slicer falls back to PLA temperatures with no error. Check the G-code header (`; filament_type = PETG`, nozzle near 255, bed near 80) before printing. Using the printer's own loaded-filament profiles, or a self-contained merged profile, avoids it.

### The slicer landscape

**OrcaSlicer** - the OSS fork that became the dominant non-Bambu default in 2024–2026. Built on Bambu Studio's codebase but adds support for ~50 printer brands, broader calibration tooling (pressure advance test, flow ratio test, temperature towers built in), and more aggressive support generation options. Active development continues with frequent releases.

**Bambu Studio** - official for Bambu hardware. Cloud-first; the AMS multi-color workflow is best-in-class. Closed-source but free. Use this if you have a Bambu printer and aren't a tinkerer; otherwise OrcaSlicer is a strict superset.

**PrusaSlicer** - the original modern slicer, by Josef Průša / Prusa Research. Best for Prusa hardware. Strong organic supports (their implementation came first), Arachne variable-width perimeters, MMU3 multi-material. Slower release cadence than OrcaSlicer but very stable.

**Cura** (UltiMaker) - the long-time default, still excellent. Plugin ecosystem. Better than OrcaSlicer for some legacy non-mainstream printers. Tends to lag OrcaSlicer on calibration features and modern infill/support innovations. Default for users who started with Cura and have no reason to switch.

**SuperSlicer** - a PrusaSlicer fork with extra power-user features. Less actively developed than OrcaSlicer; user base has largely migrated.

**Lychee Slicer** - resin-first. Free tier with watermark / wait time; pro tier ~$60/yr. Best UX of the resin slicers; many users prefer it over Chitubox.

**Chitubox** - resin-first, made by the company that makes the controller boards in most consumer resin printers. Free basic; "Pro" tier paid. Slightly clunkier than Lychee but rock-solid support generation.

### Modern slicer features worth knowing (2025–2026)

- **Organic / tree supports** - biomimetic branching supports that use less material and break away cleaner than traditional supports. All major slicers now support this; PrusaSlicer's implementation is often considered the reference, OrcaSlicer's is most-configurable.
- **Lightning infill** - minimal-material infill pattern that only supports the top surface. Use when print speed matters and the part won't see vertical load.
- **Scarf seam joints** - angled seam overlap that hides the Z-seam visually; introduced into Bambu Studio / OrcaSlicer in 2024.
- **Polyhole compensation** - automatically adjusts hole geometry to compensate for the polygon-vs-circle approximation in FDM (holes print slightly undersized; this fixes them).
- **Per-object settings** - different layer height, infill, or supports per object on the same plate. All major slicers support; OrcaSlicer's UI is best.
- **Calibration suite** - pressure advance, flow ratio, maximum volumetric flow, temperature tower, retraction, all generated as standardized test prints. OrcaSlicer leads here.
- **Klipper integration** - direct upload to Klipper / Moonraker for non-vendor printers. Native in OrcaSlicer.

---

## 7. Workflow Patterns

### "I downloaded this model and it's not quite right"

The standard remix flow:

1. **Identify the source format.** If it's a STEP/F3D/SLDPRT, open in CAD and edit directly - best case.
2. **If only an STL is available:**
   - Small change (move a hole, add text, scale a feature): Tinkercad or the slicer's modifier tools.
   - Medium change (resize a feature, add a mounting tab): Meshmixer or Blender boolean.
   - Large change (re-engineer a section): trace the STL in CAD using "Convert Mesh to BRep" (Fusion, FreeCAD) or just remodel from scratch using the STL as a reference.
3. **Verify mesh is still manifold** before slicing.
4. **Respect the license** when re-publishing.

### "I need a custom bracket / mount / spacer"

The parametric flow:

1. Measure the constraining hardware (calipers, ideally digital, ideally 0.01mm resolution).
2. Open OnShape (or your CAD of choice). Create a new sketch on the front plane.
3. Sketch the 2D profile. Use construction geometry and dimensional constraints (not free dragging) so the design is parametric and editable later.
4. Extrude / revolve / loft into 3D. Add fillets last.
5. Print a test in PLA at draft quality (0.3mm layer, 15% infill, 2 walls). Verify fit.
6. Iterate. Final print in the structural filament you actually need (PETG for outdoor, ABS/ASA for heat, PA-CF for stiffness).

### "I want a one-off enclosure for a PCB"

The fastest paths:

- **Hammond / Bopla style:** browse Printables for "enclosure for X" (where X is your PCB family - Raspberry Pi, Arduino, ESP32 dev board). Almost everything common has been done.
- **Generic enclosure generators:** the website `boxes.py` generates parametric laser-cut and 3D-printed boxes from a web form. OpenSCAD has multiple parametric-box libraries (PolyBox, etc.).
- **From scratch:** in CAD, sketch your PCB outline + mounting hole pattern, extrude a base, sketch a wall profile around it, extrude up, top with a lid. ~30 min for a simple PCB.

### "I want to print a miniature for tabletop"

1. **Source:** MyMiniFactory (paid), a creator's Patreon, free section of MMF / Cults3D / Printables, or AI-generate via Meshy/Rodin for one-offs.
2. **Slicer:** resin printer + Lychee or Chitubox (resin is dramatically better for minis than FDM).
3. **Orient:** mini at 45° leaning back, on supports. Use Lychee's auto-orient as a starting suggestion, then manually verify no critical surface (face, weapon detail) is touching supports.
4. **Supports:** medium density, light tips on detail areas, heavy on weight-bearing.
5. **Slice and print.** Wash 5 min in IPA, cure 2–5 min UV.

### "I want to print something functional in engineering material"

1. CAD the part with real tolerances. Print a coupon (small test piece with the critical fit) first.
2. Choose filament: PETG (general-purpose, outdoor), PC (high temp), PA-CF / PA-GF (stiff, dimensionally stable), TPU (flexible).
3. Slice: 4–6 walls (perimeters), 20–40% infill, gyroid or honeycomb pattern (better isotropy than rectilinear).
4. Print. Anneal if using PA / PC for maximum strength.

### "The slicer says my model has errors"

1. Try the slicer's auto-repair first.
2. If that fails, open in Blender, run 3D-Print Toolbox "Check All," fix what it reports.
3. If still broken: upload to `service.netfabb.com`, download repaired version.
4. If still broken: the mesh is fundamentally bad; either find a different model or remodel in CAD.

---


## 8. Preview Rendering (scripted, zero-context)

When the user wants to *see* a model (.scad, .stl, .obj, .3mf, .amf), do NOT hand-roll OpenSCAD invocations or reason about geometry in-context. Run the bundled script:

```bash
${CLAUDE_PLUGIN_ROOT}/skills/3d-printing-models-and-tools/scripts/render-previews.sh <model-file> [outdir]
```

- Emits `<basename>-preview-{iso,front,side,top}.png` (1600×1200) next to the input (or in `outdir`) and prints the paths.
- `.scad` renders directly; mesh formats are wrapped in a temp `import()` automatically.
- Requires OpenSCAD (`brew install --cask openscad`) and assumes macOS paths (it falls back to `/Applications/OpenSCAD.app`). Uses preview-quality render - fast, fine for visual checks. Gotcha baked into the script: modern OpenSCAD's `--render` flag takes an argument and will silently swallow the input path - the script deliberately omits it.
- After running, either `Read` the PNGs you need (each costs one image) or just give the user the file paths - the render itself consumes no context.
- For a custom angle, add a view to the `VIEWS` array (`name:rx,ry,rz` camera rotation).

---

## Quick reference checklist

When you're about to advise the user on a 3D printing task, check:

- [ ] Source of the model identified (which site, what license)?
- [ ] Format appropriate for the task (STEP for engineering edits, 3MF for slicer handoff, STL for universal)?
- [ ] Mesh verified manifold before slicing?
- [ ] Scale done in CAD (not slicer) if it has mating features?
- [ ] Tolerances appropriate for FDM (press fits 0.1–0.2mm, sliding 0.3–0.5mm)?
- [ ] Slicer chosen for the printer (OrcaSlicer for most non-Bambu in 2026)?
- [ ] If AI-generated: post-processed (watertight check, decimate, base added)?
- [ ] If commercial intent: license allows it, or designer contacted?
- [ ] Project folder path stated to the user (see section 0)?
