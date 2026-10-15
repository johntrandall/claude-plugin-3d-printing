---
name: 3d-printing-recycling-and-waste
description: Reference knowledge on filament spool disposal/reuse, failed-print and scrap recycling (home extrusion, mail-in programs, makerspace drop-off), waste-reducing slicer/design choices, and material-specific recycling reality. Auto-invoke when disposing of spools, dealing with failed-print scrap, planning to recycle filament, or choosing waste-minimizing print settings.
last_refreshed: 2026-10-15
---

# 3D Printing Recycling and Waste: Practical Reference

This document is the working reference for what to actually do with 3D printing waste - empty spools, failed prints, supports, purge towers, and material scrap. It is structured so the most common decision ("I have an empty spool, where does it go?") is answerable from the decision tree at the bottom, while the body covers the honest reality of each option.

Most confidence markers in this document are **Observed** from 2024-2025 vendor pages, recycler program descriptions, and community reports - they have not been individually tested. Where a number is brand-specific (a published shred-and-extrude diameter tolerance, a stated CO2 figure), treat it as the manufacturer's claim, not an independent measurement. Take-back programs especially are **Inferred current as of June 2026** - verify with the vendor before shipping anything; this segment of the industry churns yearly.

---

## 1. The Honest Reality of "Biodegradable" PLA

PLA is the most-printed filament and is widely sold with green marketing - "plant-based," "biodegradable," "compostable." All three claims are true with significant asterisks that the marketing tends to drop.

**PLA is industrially compostable, not home-compostable, not landfill-biodegradable.** The relevant standards are ASTM D6400 and EN 13432 / ISO 17088. To meet them, PLA must disintegrate in conditions an industrial composting facility provides - roughly 55-70 °C sustained heat, high humidity, active microbial culture, and tumbling for 60-180 days. Your backyard compost bin does not reach those temperatures. A landfill does not reach those temperatures either, and is moisture-and-oxygen-poor on purpose.

**In a landfill, PLA persists for decades, possibly centuries.** Published studies on PLA in soil and landfill environments consistently show very slow degradation - single-digit percent mass loss over years. PLA in a landfill is functionally a plastic; it just happens to have come from corn starch instead of crude oil.

**PLA contaminates conventional recycling streams.** PLA looks similar to PET (#1, soda bottles) under automated optical sorting. When PLA enters a PET recycling bale at even a few percent contamination, it degrades the melt characteristics of the recycled PET - wrong glass transition temperature, wrong melt-flow index - and can render the whole bale low-grade or unusable. This is why most municipal curbside programs explicitly do NOT want PLA, and why putting PLA in the #1 PET bin is worse than putting it in the trash.

**Practical implication:** Do not assume "PLA is biodegradable" lets you compost it at home, throw it in the woods, or put it in curbside recycling. The realistic disposal options for PLA scrap are (a) an actual industrial composting facility that accepts PLA - uncommon, check first - (b) a take-back program that grinds it into pellets for re-extrusion, (c) home extrusion if you have the equipment, or (d) the trash. Sources: Filamentive's PLA recycling explainer ([filamentive.com](https://www.filamentive.com/how-to-recycle-pla-arising-from-3d-printing-material-waste/)); ASTM D6400 compostability testing ([infinitalab.com](https://infinitalab.com/blog/pla-biodegradability-compostability-testing/)); Dundee University literature review of filament recycling net-zero pathways ([discovery.dundee.ac.uk](https://discovery.dundee.ac.uk/ws/portalfiles/portal/105940561/1-s2.0-S0048969723036690-main.pdf)).

---

## 2. Empty Spool Disposal and Reuse

The empty spool is the highest-volume, easiest-to-handle piece of filament waste. There are three meaningful categories.

### 2a. Cardboard spools: kerbside paper recycling, or reuse

A growing fraction of brands ship on cardboard spools or cardboard refill cores. These go in kerbside paper/cardboard recycling without ceremony, or can be reused (cable spools, yarn dispensers, plant-pot rings).

Brands shipping fully cardboard spools or cardboard refill cores as of 2024-2026 (Observed):

- **Polymaker PolyTerra** - cardboard spool standard across the line.
- **MatterHackers MH Build Series** - explicit cardboard-spool SKU ([matterhackers.com](https://www.matterhackers.com/store/c/mh-build-series-pla-cardboard-spools)).
- **Prusament Refill** - naked filament coil with a small cardboard core, intended to reload an existing Prusament spool.
- **Eolas Prints** (EU) - cardboard packaging, recycled-content focus.
- **Bambu Lab Refill** - naked coil with a paper sleeve, designed for the reusable Bambu spool (see 2c).
- **Spectrum ReFill** - naked-coil refill model ([filamentia.cz](https://www.filamentia.cz/en/p/refill-spool)).
- **Filamentive refill** - naked coil compatible with Bambu reusable spools.

### 2b. Plastic spools: usually not curbside-recyclable

The default plastic spool is injection-moulded polystyrene (HIPS, resin code #6) or sometimes ABS (#7 "other"). Both are technically recyclable but are widely rejected by US municipal programs because the market for post-consumer #6 and #7 is thin and contamination risk is high. Plastic spools end up in one of:

1. **Trash.** The default if you have no other route.
2. **Brand take-back.** Some brands accept their own empty spools back - see 2d.
3. **Reuse.** Spools are well-shaped for storage, tool holders, plant pots, cable winders, yarn dispensers, light fixtures, parts bins. Printables and Thingiverse have hundreds of "spool conversion" designs - search `empty spool` or `spool reuse`. A small curated set worth pointing to:
   - Spool-to-parts-bin clip-in drawers (very popular).
   - Spool wall-mount organizers (drill into the wall, hang spools as bins).
   - Spool tabletop yarn / wire dispensers.
   - Spool planters with drainage cones.
   - Spool side-table bases (stack three, add a plywood top).

**Do not put plastic spools in #1 / #2 curbside bins unless you have confirmed your municipal facility accepts #6 or #7 - putting them in "as plastic, it'll get sorted" can downgrade the entire bale.**

### 2c. Refillable spool ecosystems

Several brands now sell a durable "master" spool plus naked-coil refills. This is the single most impactful per-print waste reduction available short of running a home extruder, because the spool is amortized over many kilograms.

- **Bambu Lab Reusable Spool + Refill** - a sturdy two-piece plastic spool that snaps together; Bambu sells "Refill" SKUs of PLA and PETG as naked coils that load onto the spool. Compatible with AMS and the Bambu refill rolls. Bambu sells the spool separately. Several third parties - notably Filamentive - sell naked coils explicitly compatible with the Bambu spool, expanding the refill range beyond Bambu's own colors. ([3dprintingcanada.com](https://3dprintingcanada.com/products/bambu-lab-reusable-spool), [digitmakers.ca AMS compatibility](https://www.digitmakers.ca/blogs/news/bambu-lab-ams-compatibility-guide-what-works-and-what-to-watch-out-for))
- **Prusament Refill** - naked coil + small cardboard core; reload into an empty Prusament spool. Prusa is explicit that this is the lowest-waste way to buy Prusament.
- **MatterHackers Refill** - naked coils for several MH Build Series and Pro Series colors ([matterhackers.com](https://www.matterhackers.com/store/c/3d-printer-filament-refills)).
- **Spectrum ReFill / Filamentia ReFill** - Eastern-European naked-coil ecosystem with its own dedicated refill spool ([filamentia.cz](https://www.filamentia.cz/en/p/refill-spool)).
- **Polymaker PolyTerra cardboard** - not strictly a "refill," but the cardboard spool itself recycles cleanly.
- **Print-it-yourself adapters** - Printables hosts adapters that let one brand's refill load onto another brand's spool (e.g. "spool adapter to reuse cardboard spool with Bambu Lab refills"). Practical, but check that the adapter handles AMS spool-detection geometry correctly before relying on it for unattended runs.

**Practical implication:** If you print frequently on a Bambu, Prusa, or MatterHackers machine, switching to refill SKUs is the single biggest waste-reduction lever you have - bigger than anything in the slicer.

### 2d. Spool take-back and mail-in programs

**Verify each of these with the vendor's current website before shipping anything - programs in this category appear, pause, and disappear yearly.** Observed status as of 2026-06:

- **TerraCycle "3D Printing Materials" Zero Waste Box** - active, paid-by-the-box service. Accepts ABS, ASA, PS, HIPS, PP, PE, PET, PETG, PC-ABS, Nylon, TPU, and empty spools. PLA and other compostable bioplastics are explicitly excluded from this box - use the separate "Biodegradable Plastics" Zero Waste Box for PLA. Boxes sold in two sizes (~40 L and ~140 L). Pre-paid shipping label affixed. Sold direct via TerraCycle and resold via Fisher Scientific, EarthHero, and DIY ([shop.terracycle.com](https://shop.terracycle.com/en-US/products/3d-printing-materials-zero-waste-box), [earthhero.com](https://earthhero.com/products/terracycle-3d-printing-materials-zero-waste-box)). Cost is the friction - boxes run hundreds of dollars, which only makes sense for a print farm or a makerspace.
- **Reflow (Netherlands / EU)** - recycled-content filament producer; historically accepts clean post-industrial PET and similar streams. Primary product is recycled rPET filament. Consumer-side scrap take-back varies - verify on their current site.
- **GreenGate3D** - recycled-PETG filament (US), made from rPET feedstock; small-scale consumer recycling sometimes available - verify.
- **Filamentive (UK)** - recycled-content filament; published "Recycle Your Filament" guidance - historically operated a take-back, but service availability has shifted; check current site.
- **Filament-PM "Responsible Spools" return program** - Czech-Republic-and-Slovakia-only as published, prepaid return of empty spools; spool-side rather than scrap-side ([filament-pm.com](https://shop.filament-pm.com/stranka/responsible-spools-87)).
- **3DTomorrow (UK) print-waste recycling program** - historically active for UK customers ([3dtomorrow.com](https://3dtomorrow.com/2021/02/02/print-waste-recycling-program/)).
- **eSun** - periodically announces consumer-side recycling initiatives; in practice the consumer mail-back has been intermittent. Their main "sustainability" play is selling PLA and bio-PCL ([esungroup.net](https://www.esungroup.net/news/news-529html/)).
- **Push Plastic, Factory Filament, 3D Innovators** - small-vendor programs; check current page. Factory Filament publishes a recycling program page ([factoryfilament.com](https://www.factoryfilament.com/pages/recycling)). 3D Innovators currently runs a spool-buyback rather than scrap-recycling ([3dinnovatorsofficial.com](https://3dinnovatorsofficial.com/recycle-program/)).
- **MatterHackers** - sells the cardboard-spool MH Build Series and the refill range, but the formal customer-side scrap mail-in has not been a flagship product; refills are the more reliable green path here.

If a program isn't on a vendor's current site, assume it has paused. Don't ship scrap to a stale address.

---

## 3. Failed Prints, Supports, Purge Towers, and Scrap

### 3a. Sort by material: non-negotiable

Recycling pathways that depend on extrusion (home or commercial) only work on a single resin. Mixed PLA + PETG + ABS pellets are useless - different melt temperatures, different chemistries. The first rule of usable scrap is a labeled bin per material. The second rule is a labeled bin per filament *family* even within "PLA" - silk PLA, PLA-CF, and standard PLA behave differently in re-extrusion.

For a hobbyist this usually means at minimum: PLA bin, PETG bin, ABS bin, "composite / contaminated / mixed" bin (which is going to trash). Multi-material AMS purge poops are their own category - see 3g.

### 3b. Home extrusion: honest economics

The mechanical pathway is: shred failed prints → dry pellets → extrude into 1.75 mm or 2.85 mm filament → wind onto spool. Commercial desktop systems exist; none are economically justifiable for a casual hobbyist on cost-per-kilogram alone.

Currently available (Observed 2024-2026):

| Product | What it does | Approximate price | Notes |
|---|---|---|---|
| **Filabot EX2** | Single-screw desktop extruder | ~$2,000-3,000 | Entry-level Filabot; fewer temperature zones. |
| **Filabot EX6** | Multi-zone desktop extruder | ~$10,000-30,000 (bundled) | Handles a wider material range; closer to a small studio tool ([store.makerwiz.com Filabot listing](https://store.makerwiz.com/collections/filabot)). |
| **3devo Composer / Precision** | Multi-zone desktop extruder with active diameter control | ~$10,000-25,000 | Highest published diameter consistency of the desktop class. |
| **ProtoCycler v3** | Integrated shred + extrude | Mid-five-figures | Turnkey, less common in 2025. |
| **Felfil Evo** | DIY-kit single-screw extruder | ~$1,500-2,500 kit | Cheapest; correspondingly more calibration work. |

Realistic diameter tolerance from any desktop extruder is **±0.05 mm at best, often ±0.10 mm on a typical setup** (Observed across community reports). For comparison, virgin name-brand filament publishes ±0.02-0.03 mm. The recycled filament is usable; it is not equivalent to virgin. Expect to blend with virgin (often 30-70%) to keep print quality acceptable.

**The economic break-even is poor.** A Filabot EX2 at $2,500, with maybe 80% material yield, replacing $20/kg PLA, pays back at ~150 kg of recycled scrap. Most hobbyists do not generate 150 kg of clean, sorted scrap in a lifetime. Home extrusion makes sense if (a) you are running a print farm, (b) you have a research or educational reason, (c) you want pellet → filament so you can buy cheap industrial-grade pellets, or (d) the project itself is the point. It does not make sense as a pure economic play.

Background: 3Dnatives' machine roundup ([3dnatives.com](https://www.3dnatives.com/en/recycling-plastic-filament-extruders-29052026/amp/)); Filabot product line ([filabot.com](https://www.filabot.com/)); 3devo's SHR3D IT shredder spec ([3dprintingindustry.com](https://3dprintingindustry.com/news/3devo-recycle-3d-printed-plastics-with-shr3dit-technical-specifications-pricing-107423/)).

### 3c. Shredders

Extrusion needs shredded feedstock. The two notable desktop options:

- **Filabot Reclaimer** - two-stage granulator sized for failed prints, paired with the Filabot extruder line ([filabot.com](https://www.filabot.com/en-au/products/filabot-reclaimer-1)).
- **3devo SHR3D IT** - granulator+sieve in one unit, paired with 3devo extruders.

For very small volumes, scissors plus patience works for cutting failed prints into bite-sized pieces that an extruder can re-melt - slow, but a no-capital starting point. Industrial granulators exist (Filabot Industrial Reclaimer, ~$9,000+) for makerspace-scale operation.

### 3d. Pellet feeders / direct-pellet extrusion

The newer pathway skips making filament entirely - the printer extrudes directly from pellets. This is closer to commodity injection moulding feedstock and lets you bypass the filament step.

- **Mahor XYZ V4** - a pellet extruder head that retrofits onto an existing 3D printer.
- **Piocreat G5 / G12** - purpose-built pellet 3D printers, more industrial scale (build volumes around 500 mm and larger), targeted at small-batch production rather than hobby ([Piocreat product listings](https://www.alibaba.com/product-detail/Piocreat-G12-Professional-Automatic-Pellet-Extruder_1600908086619.html)).

Pellet extrusion sidesteps the diameter-tolerance problem entirely - there is no filament to make. It does introduce new problems: lower layer-line resolution (pellet extruders use larger nozzles, typically 1-3 mm), grainy feeding, and the need for a dedicated machine. For a hobbyist this is currently a "watch this space" technology rather than a buy-today recommendation.

### 3e. Community drop-off: often the best practical option

Universities, FabLabs, public-library makerspaces, and hackerspaces sometimes accept clean sorted scrap, particularly PLA. They may run their own recycling experiments, donate to research groups, or aggregate for a regional take-back. This route has zero cost, no shipping carbon, and supports a local institution that probably already has a granulator. Call before driving over.

### 3f. Mail-in scrap programs

Same list as the spool take-backs in section 2d - TerraCycle Zero Waste Box accepts scrap and spools together for non-PLA thermoplastics; the Biodegradable Plastics box accepts PLA. Reflow, GreenGate3D, Filamentive, Filament-PM all historically operate scrap-side programs, but **verify current activity before shipping**.

### 3g. Multi-material AMS purge waste

When an AMS system swaps colors, it purges the previous filament into a waste chute - the "purge poop." This is by definition multi-material: PLA + PLA-silk + PLA-glow + PETG all mixed into one blob. **No extrusion pathway recycles this**; the materials are incompatible at the melt level. Realistic fates:

- **Trash.** The default and honest answer for almost everyone.
- **Sculpture stock.** A small art community casts AMS purge as colored "rainbow" stock and re-melts it into single-color blocks for hand-carving, lathe work, or use as a craft material. Niche, but real.
- **Drastically reduce the volume in the first place.** See section 4 - slicer-side flush-volume tuning and "purge into infill/object" features cut AMS waste by 50-80% from the defaults.

### 3h. Last resort: trash, done correctly

When no other route applies, the trash is the correct disposal. Two rules:

1. **Do not put unsorted 3D-printing plastic in curbside #1 / #2 recycling.** If your local facility doesn't accept the resin code, the bale is downgraded. PLA in a PET bale is the worst case - see section 1.
2. **Composite filaments (CF, GF, wood, metal-fill, glow) always go to trash**, never to any home recycling stream. The non-polymer additives contaminate any reclaim batch.

---

## 4. Designing for Less Waste

The cheapest recycled gram is the gram you didn't print. Slicer and design choices outweigh almost every recycling option in net impact.

### 4a. Bed adhesion: brim vs raft vs skirt

| Strategy | Material cost | When justified |
|---|---|---|
| **Skirt** | ~1-5 g | Default. Primes nozzle, does not touch the part. |
| **Brim** | ~5-30 g | Tall narrow parts, large-flat-area ABS/ASA on PEI. Removable cleanly. |
| **Raft** | ~30-200 g | Almost never on modern bed surfaces. Legacy practice from glass-bed days. Use mouse-ear or brim-only ear patches instead. |

A raft can easily out-mass the part itself on small prints. Modern PEI / textured PEI / smooth PEI sheets rarely need rafts - try a brim first.

### 4b. Tree supports vs normal supports

Tree supports (in PrusaSlicer, OrcaSlicer, Bambu Studio, Cura) use 30-70% less material than grid/normal supports for overhang-heavy parts. They also peel off cleaner. The trade-off is generation time and occasionally less reliable support for very small overhang features - but for most figurines, brackets, and organic shapes, tree supports are a strict waste win.

### 4c. AMS / multi-material purge reduction

The default flush volumes in Bambu Studio are conservative - designed to guarantee a clean color transition on every print regardless of geometry. They are usually 2-3× larger than necessary.

- **Tune flush volumes in the AMS material matrix.** For same-base-material color swaps (PLA to PLA, just a different color), 350-500 mm³ is often enough; the default may be 700-1000+ mm³.
- **OrcaSlicer "flush into object" / "flush into infill"** - directs the purge into the model's own infill or into a dedicated wall, eliminating most of the external purge poop. This is the single biggest AMS-waste-reduction lever.
- **Print order optimization** - group prints by color so each color is used for a continuous block rather than alternating per layer.
- **Avoid extreme color contrasts when not necessary** - going from black to white requires significantly more purge than between similar shades.

### 4d. Infill patterns

- **Gyroid** - strong in all axes, prints fast, uses material efficiently. Best general-purpose pick.
- **Lightning infill (PrusaSlicer/OrcaSlicer)** - only supports the top surface, uses minimal material. Excellent for decorative parts, cosplay, props, anything non-structural.
- **Cubic / cubic-subdivision** - strong for mechanical loads when you can't use gyroid.
- **Adaptive cubic** - varies density based on need; less material than uniform.

Switching from default 20% rectilinear to 15% gyroid on a decorative print can shave 20-30% of the part mass.

### 4e. Orientation to avoid supports

The single biggest design-side waste reduction is reorienting the part so overhangs disappear. Modern slicers can often suggest orientations (PrusaSlicer's "Place on face," Bambu Studio's auto-orient). A 30-second reorientation often beats hours of clever support tweaking.

### 4f. Calibration objects

The 3DBenchy is iconic, useful as a printer benchmark, and overkill for most calibration. For routine calibration, prefer:

- **Calibration cubes** (20 mm) - dimensional check, ~5 g.
- **Temperature towers** - single test print covers a 30-50 °C range.
- **Retraction towers** - covers your full retraction sweep in one print.
- **Single-wall cylinders** for flow / extrusion-multiplier tuning.

A Benchy is ~15 g; a 20 mm cube is ~5 g. If you Benchy every new spool, that's hundreds of grams a year of pure calibration scrap.

### 4g. Filler use of failed prints

Some users chop failed prints into small chunks and stuff them into the infill cavities of large parts mid-print (pause-and-stuff). Niche, fiddly, but real and material-efficient for single-color large parts.

---

## 5. Material-Specific Recycling Notes

| Material | Curbside? | Home extrude? | Mail-in? | Industrial compostable? | Notes |
|---|---|---|---|---|---|
| **PLA** | No (contaminates PET) | Yes (best home candidate) | TerraCycle Bio box; brand programs | Yes (ASTM D6400 facility only) | Default-and-honest answer for hobby waste. Mail-in or trash. |
| **PETG** | Rarely (not bottle-grade) | Yes, more moisture-sensitive | TerraCycle 3D box; specialty | No | Chemically PET-family but FDM-grade is not accepted in PET bottle streams. |
| **ABS** | Rarely | Yes, needs ventilation | TerraCycle 3D box | No | Same polymer family as Lego, car bumpers - industrially recyclable, hobbyist mixed-color is low-value. |
| **ASA** | No | Yes, similar to ABS | TerraCycle 3D box | No | Treat as ABS for recycling purposes. |
| **Nylon (PA6, PA12)** | No | Technical - needs aggressive drying | Specialty recyclers | No | Hygroscopic; difficult home reprocessing. |
| **PC (polycarbonate)** | No | Possible but high temps | Specialty | No | Industrial PC recycling exists; consumer-side rare. |
| **TPU** | No | Possible, blends poorly | Specialty | No | Elasticity makes diameter control hard. |
| **CF / GF composites** | No | **No - do not attempt** | TerraCycle 3D box for some | No | Fibers contaminate any reclaim stream. Trash or specialty take-back only. |
| **Wood-fill, metal-fill, glow** | No | No | Trash | No | Non-polymer additives ruin reclaim batches. |
| **Multi-material AMS purge** | No | No | Trash (or sculpture) | No | Mixed-material blob; no extrusion pathway works. |

---

## 6. Health and Safety in Recycling

If you do operate a shredder or extruder, the safety profile is non-trivial and worth taking seriously.

- **CF / GF dust is a respiratory hazard.** Carbon-fiber and glass-fiber filaments shed micro-fibers when shredded. Without dust extraction, those fibers go into your lungs. Do not shred CF / GF without a sealed shredder, local exhaust ventilation, and at minimum a P100 respirator. Honestly, just don't shred CF / GF at home.
- **ABS / ASA fumes during extrusion** include styrene and ultrafine particles. Same rules as printing ABS - ventilate aggressively, prefer an enclosed extruder vented outside, do not run in a sealed room you sit in.
- **PLA is the least hazardous to re-process**, but still produces some VOCs and ultrafine particles at melt. Ventilate.
- **Nylon extrusion** produces caprolactam emissions - irritating, not catastrophic. Ventilate.
- **Don't recycle contaminated stock.** Failed prints that touched casting resin, exotic dyes, food residue, or unknown surface treatments should not enter your reclaim stream - you don't know what's outgassing when you re-melt them.
- **PPE baseline**: safety glasses, cut-resistant gloves for shredder feed, P100 or better for composites, no loose long sleeves near the auger.

---

## 7. Notable Products, Projects, and Honest Greenwashing Assessments

### Polymaker PolyTerra "Plant a Tree" program

Polymaker plants one tree (via OneTreePlanted.org) per spool of PolyTerra PLA sold. Their published claim is that a mature tree absorbs ~22 kg CO2/year vs ~4 kg CO2 to produce-and-ship the spool ([polymaker.com sustainability](https://polymaker.com/why-polymaker/sustainability-2/)).

**Honest assessment** - the program is real, the partner is real, and the per-spool tree is genuinely planted. But the framing oversells the impact:

- "One mature tree at 22 kg/yr" assumes the sapling survives to maturity, which has a meaningful failure rate.
- Polymaker's 4 kg CO2 figure for a spool is the cradle-to-shelf estimate; it omits use-phase and end-of-life, which is where most of the print's actual carbon lives.
- PolyTerra is still single-use PLA on a cardboard spool - the cardboard spool itself is the more concrete win (it actually keeps a plastic spool out of the trash).
- Reddit discussion in 2024 has flagged that the tree-planting may have been quietly de-emphasized in some markets ([reddit thread](https://www.reddit.com/r/3Dprinting/comments/1f1rfsc/did_polymaker_polyterra_phase_out_the_tree/)) - verify the current page if the program is part of your buying decision.

Net: PolyTerra is a legitimately better choice than a generic PLA on a HIPS spool because of the cardboard spool. The tree program is a nice bonus, not a magic offset. Don't print extra parts because you think the trees cancel them out - they don't.

### Reflow (Amsterdam)

Recycled-content filament made from rPET feedstock; small EU producer. Honest pitch - actually using post-consumer plastic.

### GreenGate3D

US rPET filament from food-grade recycled PET. Smaller-scale than mainstream brands; legitimate recycled-content product.

### Filamentive (UK)

Recycled-content PLA, PETG, ABS, and a refill-coil program compatible with Bambu reusable spools. One of the most credible recycled-content brands in the FDM space - published material data on recycled fraction.

### Bambu Lab refillable ecosystem

The reusable spool + refill model is the most impactful waste reduction Bambu has shipped. Use it if you're on a Bambu printer.

---

## 8. Quick Decision Tree

```
I have an empty spool
├── Cardboard? → kerbside paper recycling, or reuse (yarn dispenser, parts bin)
├── Plastic, refillable system (Bambu / Prusa / Spectrum)? → keep, buy refills
├── Plastic, single-use, brand has take-back? → mail back (verify program active)
└── Plastic, single-use, no take-back? → reuse (Printables designs) or trash

I have a failed print / supports / scrap
├── What material?
│   ├── PLA - sorted, clean, ≥1 kg accumulated?
│   │   ├── Home extruder available? → shred, dry, extrude (blend with virgin)
│   │   ├── Local makerspace / FabLab takes it? → drop off (call first)
│   │   ├── TerraCycle Biodegradable Plastics Zero Waste Box? → yes (paid)
│   │   └── Otherwise → trash (NOT curbside PET - contaminates bale)
│   ├── PETG / ABS / ASA / Nylon / PC / TPU - sorted clean?
│   │   ├── Home extruder rated for the material? → shred, dry, extrude
│   │   ├── TerraCycle 3D Printing Materials Zero Waste Box? → yes (paid)
│   │   └── Otherwise → trash
│   ├── CF / GF / wood / metal-fill composite? → trash (no safe home pathway)
│   └── Multi-material AMS purge? → trash (or sculpture stock if you're that person)

I want to reduce waste going forward
├── Spool side → switch to refill SKUs (Bambu, Prusa, Filamentive)
├── Slicer side
│   ├── Tune AMS flush volumes (often 2-3× overspecified by default)
│   ├── Use OrcaSlicer "flush into infill / object"
│   ├── Tree supports instead of grid
│   ├── Gyroid or lightning infill instead of rectilinear at 20%
│   ├── Brim instead of raft (or skirt instead of brim)
│   └── Reorient parts to remove overhangs
└── Calibration side → 20 mm cube, not Benchy, for routine checks
```

---

## Sources and Further Reading

- Filamentive, "How to Recycle PLA arising from 3D Printing Material Waste" - [filamentive.com](https://www.filamentive.com/how-to-recycle-pla-arising-from-3d-printing-material-waste/)
- TerraCycle 3D Printing Materials Zero Waste Box - [shop.terracycle.com](https://shop.terracycle.com/en-US/products/3d-printing-materials-zero-waste-box)
- TerraCycle Biodegradable Plastics Zero Waste Box (PLA-accepting) - referenced from same shop
- Polymaker sustainability page (PolyTerra tree program) - [polymaker.com](https://polymaker.com/why-polymaker/sustainability-2/)
- Bambu Lab Reusable Spool product page - [3dprintingcanada.com listing](https://3dprintingcanada.com/products/bambu-lab-reusable-spool)
- Bambu Lab AMS compatibility - [digitmakers.ca](https://www.digitmakers.ca/blogs/news/bambu-lab-ams-compatibility-guide-what-works-and-what-to-watch-out-for)
- MatterHackers MH Build Series Cardboard Spools - [matterhackers.com](https://www.matterhackers.com/store/c/mh-build-series-pla-cardboard-spools)
- MatterHackers Refill range - [matterhackers.com](https://www.matterhackers.com/store/c/3d-printer-filament-refills)
- Filament-PM Responsible Spools program (CZ/SK) - [filament-pm.com](https://shop.filament-pm.com/stranka/responsible-spools-87)
- Spectrum ReFill spool - [filamentia.cz](https://www.filamentia.cz/en/p/refill-spool)
- Factory Filament recycling program - [factoryfilament.com](https://www.factoryfilament.com/pages/recycling)
- Filabot Reclaimer (granulator) - [filabot.com](https://www.filabot.com/en-au/products/filabot-reclaimer-1)
- Filabot EX2 vs EX6 comparison - [filabot.zendesk.com](https://filabot.zendesk.com/hc/en-us/articles/360009602773-What-are-the-differences-between-the-Filabot-EX2-and-Filabot-EX6)
- 3devo SHR3D IT technical specs - [3dprintingindustry.com](https://3dprintingindustry.com/news/3devo-recycle-3d-printed-plastics-with-shr3dit-technical-specifications-pricing-107423/)
- 3Dnatives best filament recyclers roundup - [3dnatives.com](https://www.3dnatives.com/en/recycling-plastic-filament-extruders-29052026/amp/)
- Siraya Tech "Can You Recycle 3D Printer Filament?" - [siraya.tech](https://siraya.tech/blogs/news/can-you-recycle-3d-printer-filament)
- Dundee University, "Net zero on 3D printing filament recycling" literature review - [discovery.dundee.ac.uk PDF](https://discovery.dundee.ac.uk/ws/portalfiles/portal/105940561/1-s2.0-S0048969723036690-main.pdf)
- ASTM D6400 / ISO 17088 compostability testing background - [infinitalab.com](https://infinitalab.com/blog/pla-biodegradability-compostability-testing/)

---

## Related Skills

- **`3d-printing-filaments`** - choosing what to print *with* (the upstream question).
- **`3d-printing-storage-and-maintenance`** - drying, storage, spool handling (overlaps with refillable-spool ecosystems).
- **`3d-printing-models-and-tools`** - what to print *of* (including spool-reuse designs).
