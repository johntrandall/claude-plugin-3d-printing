---
name: 3d-printing-filaments
description: Reference knowledge on FDM filament types, properties, use-case matching, print settings, and storage. Auto-invoke when selecting filament, troubleshooting material-specific print issues, or answering "what should I print this in?" questions.
last_refreshed: 2026-10-15
printer_specific: [bambu-a1]
---

# FDM / FFF Filament Reference

Prices are typical US dollar ranges as of October 2026.

This document is the working reference for choosing, printing, and storing FDM filament. It is structured so a brand-new printer owner can read the first two sections and immediately make a buying decision, while a more experienced user can drill into the matrices and hardware compatibility notes for tricky cases.

All temperature, strength, and cost numbers below are **typical ranges**, not specs for any one brand. Always defer to the manufacturer's TDS for a specific spool. Mark of confidence: properties and print settings are **Observed** across multiple 2024-2025 vendor datasheets and community sources; brand reputation notes are **Inferred** from community consensus, not a controlled comparison.

---

## 1. Orientation: "I just got a printer, what do I buy?"

If the printer is a typical 2024-2025 consumer machine (Bambu Lab A1/P1/X1C, Prusa MK4, Creality K1/K2, Elegoo Centauri, etc.) with a heated bed and the stock brass nozzle:

1. **Start with PLA.** It is forgiving, smells fine, prints fast, and looks good. Buy one spool of plain PLA from a known-good brand. This is what 80% of hobby prints should be.
2. **Add one spool of PETG** once you want something tougher, weather-tolerant, or food-contact-adjacent.
3. **Skip everything else until you have a specific use case.** ABS, nylon, PC, TPU, and CF blends all add complexity (enclosure, drying, hardened nozzles, moisture management) and you should only buy them when a project actually needs them.

### The Four-Line Shortlist

When in doubt, this is the practitioner default - credit to a top community comment on the canonical r/3Dprinting "explain filaments to me" thread:

- **PLA** - for most things.
- **PETG** - if you need extra impact and heat resistance.
- **ASA** - for something with lots of sun exposure.
- **Carbon-fiber blends** - if you need a very stiff part.

Memorize that. The rest of this document is for when the four-line answer isn't enough.

### What does my printer actually unlock?

The filament list a printer "supports" is gated by four things: nozzle material, maximum hotend temp, build plate / bed temp, and whether it has an enclosure (and how warm that enclosure gets). The Bambu Lab X1C is a useful reference machine because it's a very common starting point and it's near the upper end of what a consumer printer can do:

| Capability | X1C value | Filaments unlocked |
|---|---|---|
| Enclosed build volume | Yes, passive | ABS, ASA, PC, nylon (with caveats) |
| Maximum nozzle temp | 300 °C | Everything except PEEK / PEI |
| Maximum bed temp | 110 °C | PC, ABS, nylon |
| Hardened nozzle available | Yes (swap) | CF / GF blends, glow, wood, metal-fill |
| AMS multi-material | Yes (with quirks) | See section 4 |

A printer without an enclosure should not be used for ABS, ASA, PC, or large nylon parts - it can print them, but warping and layer separation will kill the result. A printer without a hardened nozzle should not be used for CF/GF/glow/wood/metal - it will eat the brass nozzle in tens of hours.

---

## 1b. Bambu Lab A1: what this printer can actually print

**This section is for the full-size Bambu Lab A1 (256³ bed slinger) with AMS Lite. Not the A1 Mini, not the X1C.** Last refreshed 2026-10-15. This plugin is not affiliated with Bambu Lab.

### Reality check

The A1 is the well-engineered, open-frame, 4-color, bed-slinger end of the Bambu lineup. **Verified** specs from Bambu Lab's tech-spec page (https://bambulab.com/en/a1/tech-specs): 256 × 256 × 256 mm build volume, all-metal hotend with a maximum nozzle temperature of 300 °C, direct-drive extruder on the toolhead, AMS Lite for 4-color printing, default 0.4 mm stainless steel nozzle, swappable to 0.2 / 0.6 / 0.8 mm and to hardened steel for abrasive materials. The heatbed is **spec'd at 100 °C** but in practice many users (and the default Bambu Studio profiles for the A1) sit around 65–80 °C - this is **Observed** from the long-running Bambu forum thread on the topic (https://forum.bambulab.com/t/new-a1-printer-max-bed-temperature/42030) and from the firmware release notes describing repeated tuning of the heatbed temperature threshold and failsafe (https://wiki.bambulab.com/en/a1/manual/a1-firmware-release-history). Treat **~70 °C as the bed temperature you can rely on**, with 80 °C reachable but slow to settle, and assume the printer will *not* deliver a stable 100 °C for the kind of long PC/ASA print that would actually need it.

**What the A1 is good at.** PLA in every variant, PETG (HF especially), TPU 95A, and decorative/CF blends with a hardened nozzle. 4-color multi-material via AMS Lite. High-speed PLA. Pretty much every "fun, functional, indoor part" use case is what this printer was designed for.

**What the A1 is NOT for.** Anything that wants an enclosure. The A1 has no chamber and no door - it is open frame by design. ABS, ASA, PC, PA (nylon), PA-CF, PC-CF, PEEK - these all exist on Bambu's compatibility table for the A1 with caveats like "warping likely without enclosure / small parts only", but in practice the open frame makes them a bad investment of time. If a part needs heat resistance > ~70 °C HDT, UV survival in direct sun, or impact resistance under sub-freezing outdoor conditions, the right answer for an A1 owner is usually either "print in PETG and accept the tradeoffs" or "send it to an X1C / P1S / service bureau."

### Compatibility table (Bambu Lab A1)

Verdict legend: **Yes** = officially supported and routinely works on A1 hardware. **Yes (caveat)** = Bambu lists it as compatible but there is a real hardware requirement (hardened nozzle, external spool only, small parts only). **Effectively no** = Bambu may list it as "compatible" but the missing enclosure / bed-temp ceiling makes it a poor fit on stock A1.

| Filament | Verdict on A1 | Nozzle (°C) | Bed (°C) | Notes |
|---|---|---|---|---|
| PLA Basic | **Yes** | 190–220 | 55–65 | The default. Use this for most prints. AMS Lite compatible. |
| PLA Matte | **Yes** | 200–220 | 55–65 | Hides layer lines. AMS Lite compatible. |
| PLA Silk | **Yes** | 210–230 | 55–65 | Metallic sheen; more stringing than Basic. |
| PLA Tough | **Yes** | 210–235 | 55–65 | Higher impact resistance. AMS Lite compatible. |
| PLA Aero (low-density) | **Yes** | 220–240 | 55–65 | Specialty for lightweight parts; print slow. |
| PLA-CF / PLA Galaxy / PLA Glow | **Yes (caveat)** | 220–240 | 55–65 | **Hardened steel nozzle required.** Brass nozzle wears out in ~20 print hours. AMS Lite OK but expect feeder wear. |
| PETG HF | **Yes** | 230–260 | 60–70 | The second filament every A1 owner should buy. AMS Lite friendly. Bambu's PETG HF was specifically tuned for AMS feeding. |
| PETG Translucent | **Yes** | 230–260 | 60–70 | Same as PETG HF. |
| PETG-CF / PETG-HGF | **Yes (caveat)** | 240–270 | 60–70 | **Hardened steel nozzle required.** |
| TPU 95A HF | **Yes** | 220–240 | 35–55 | The only TPU hardness officially compatible with AMS Lite. Softer TPU (90A and below) must bypass the AMS and feed from an external spool holder. Print slow (20–30 mm/s). |
| TPU 90A and softer | **Yes (caveat)** | 220–240 | 35–55 | External spool only; do NOT load into AMS Lite. Direct-drive on A1 helps but soft grades are still finicky. |
| PVA support | **Yes (caveat)** | 190–210 | 45–60 | Works for PLA support via AMS Lite. Pull spool back to desiccant between prints - A1 has no enclosed chamber so PVA picks up humidity fast. |
| ABS | **Effectively no** | 240–270 | 90–110 | Bambu lists "compatible" but the A1 cannot maintain the chamber heat needed to avoid warping/cracking, and the bed struggles to hold the 100 °C ABS wants. Print very small parts only, or buy an aftermarket enclosure (e.g. Printer-Box.com makes one specifically for the A1). |
| ASA / ASA-CF | **Effectively no** | 240–270 | 90–110 | Same story as ABS. Aftermarket enclosure required to get usable results - and even then the bed-temp ceiling limits what you can do. |
| PC / PC-CF / PC FR | **Effectively no** | 260–310 | 100–120 | Bambu's table marks these "compatible with caveats." In practice the A1 cannot deliver the 60–80 °C heated chamber PC really wants and the bed cannot reliably hit 100+ °C. Don't buy PC for an A1; send the part to a P1S/X1C/service bureau. |
| PA (nylon) / PAHT-CF / PA-CF / PA6-CF / PA6-GF | **Effectively no** | 260–290 | 80–100 | Same as PC: marked compatible-with-caveat on the table, but warping without enclosure plus the bed-temp ceiling means parts crack mid-print. The CF/GF variants would also need a hardened nozzle, which doesn't fix the warping. |
| PPS / PPS-CF | **Effectively no** | 280–320 | 100–120 | Bambu only lists these as fully supported on the X1E. Don't try on A1. |
| PEEK / PEI / Ultem | **No** | 360–420 | 120–160 | Not supported on any consumer Bambu. Industrial-only. |

Sources cross-referenced for the table: Bambu Lab A1 tech specs (https://bambulab.com/en/a1/tech-specs - **Verified**), Bambu Lab filament compatibility wiki (https://wiki.bambulab.com/en/general/filament-guide-material-table - **Verified** for filament categories; **Observed** for per-filament A1 verdicts since the page mixes printer models), Bambu Lab community forum and r/BambuLab discussions (**Observed**), and community open-frame ABS/ASA/PC/nylon torture tests including https://www.youtube.com/watch?v=0R7GwuFwW1A (**Observed** - that test concluded ASA worked acceptably only with an enclosure added, PC and nylon-CF were not viable without one).

### Off the menu: what it would take to print high-temp materials on an A1

If you genuinely want to print ABS, ASA, PC, or nylon on the A1, this is what's required and why it's usually the wrong move:

- **Aftermarket enclosure.** Third parties (Printer-Box.com, several Etsy makers, a few open-source designs on Printables) sell enclosures sized for the A1. With one of these, ASA becomes printable for small parts. ABS still struggles. PC and nylon still struggle because the bed can't hold the high temp those materials want.
- **Hardened steel nozzle.** Required for any CF/GF variant. Easy swap; Bambu sells it. Doesn't solve warping.
- **All-metal hotend.** Already present on the A1 - this is not the limiting factor.
- **Heated chamber.** The A1 cannot do this. Period. PC/PC-CF/PA/PA-CF/PPS/PEEK genuinely need 60–150 °C chamber temperature for good results, and no enclosure-only mod will achieve that.
- **Verdict.** For materials that need a heated chamber, the A1 is fighting the tool. For ABS/ASA on small parts with an aftermarket enclosure, it works but is an uphill battle. **Inferred** recommendation: if you find yourself wanting these materials more than occasionally, the next printer is a Bambu P1S or X1C, not an A1 mod.

### Buy these first: A1 starter set

For a brand-new A1 owner, these three spools cover ~95% of practical use cases:

1. **Bambu PLA Basic, 1 kg, neutral color (black or grey).** Tuned for the A1 profile, RFID auto-detect in the AMS Lite. This is the workhorse. ~$20.
2. **Bambu PETG HF, 1 kg, black or clear.** Specifically engineered for AMS feeding (PETG used to slip in older Bambu AMS units; the HF formulation fixes that). Use for mechanical parts, anything that lives near heat (cars, garages), and food-adjacent items. ~$25.
3. **Bambu TPU 95A HF, 1 kg, black.** The only TPU officially AMS-Lite-compatible. Use for phone cases, gaskets, drone bumpers, watch straps. Print slow. ~$30.

Skip until needed: PLA-CF and PETG-CF (need a hardened nozzle and a specific stiff-part use case), PLA Silk/Galaxy/Glow (cosmetic only - buy as one-off project purchases), TPU softer than 95A (external-spool-only on A1, finicky), and obviously skip PC/PA/ABS/ASA entirely until the next printer.

---

## 2. Major Filament Families

The numbers below are typical ranges for the unfilled base resin. Carbon-fiber and glass-fiber reinforced versions of any of these run roughly 20-40 °C hotter, more brittle, and require a hardened nozzle.

### PLA (Polylactic Acid) and variants

| Property | PLA | PLA+ | Silk PLA | Matte PLA | Tough PLA |
|---|---|---|---|---|---|
| Nozzle | 190–220 °C | 200–230 °C | 210–230 °C | 200–220 °C | 210–235 °C |
| Bed | 50–60 °C | 50–60 °C | 50–60 °C | 50–60 °C | 55–65 °C |
| Chamber | Open (cooling fan on) | Open | Open | Open | Open |
| Ease (1-5, 5=easiest) | 5 | 4 | 3 | 4 | 3 |
| Tensile strength | 50–70 MPa | 60–80 MPa | ~45–60 MPa | ~50–65 MPa | 50–70 MPa |
| Impact resistance | Brittle | Improved | Brittle | Brittle | Good (ABS-like) |
| UV / weather | Poor | Poor | Poor | Poor | Poor |
| Water absorption | Low-moderate | Low-moderate | Low-moderate | Low-moderate | Low-moderate |
| Food safety | Conditional (additives, layer voids, dyes) | Conditional | Generally not | Conditional | Generally not |
| Smell / fumes | Sweet, mild | Mild | Mild | Mild | Mild |
| Recyclability | Industrial compost; mechanical limited | Same | Same | Same | Same |
| Cost / kg (USD) | $18–30 | $22–35 | $25–40 | $22–35 | $30–50 |

**Notes.** PLA is the default for a reason - it's stiff, dimensionally accurate, low-warp, and easy on the printer. Its weaknesses are heat (anything above ~55 °C in direct sun starts to creep, and parts in a hot car will warp) and UV (it yellows and embrittles). Silk PLA contains additives that give a glossy metallic sheen but reduce strength and stringing tolerance. Matte PLA contains mineral fillers and prints with very forgiving surface finish that hides layer lines. Tough PLA is Polymaker's term for a PLA chemistry tuned for higher impact resistance, approximating ABS toughness without the printing pain.

### PETG (Polyethylene Terephthalate Glycol)

| Property | Value |
|---|---|
| Nozzle | 230–250 °C |
| Bed | 70–85 °C |
| Chamber | Open OK; enclosed helps large parts |
| Ease | 4 |
| Tensile strength | 45–70 MPa |
| Impact resistance | Good (better than PLA) |
| UV / weather | Moderate; yellows over years outdoors |
| Water absorption | Moderate (dries easily) |
| Food safety | Often labeled food-contact; verify cert |
| Smell / fumes | Very mild |
| Recyclability | Same stream as PET (in theory) |
| Cost / kg | $20–35 |

**Notes.** PETG is the second filament every printer owner should own. It is tougher and more heat-tolerant than PLA (HDT ~70 °C unfilled, vs ~55 °C for PLA), prints with no enclosure, and tolerates outdoor use better than PLA. The price is stringing and a tendency to over-adhere to PEI build plates - use a thin glue stick or a textured PEI sheet to avoid tearing chunks out of the bed.

### ABS (Acrylonitrile Butadiene Styrene)

| Property | Value |
|---|---|
| Nozzle | 230–260 °C |
| Bed | 90–110 °C |
| Chamber | Enclosed required for anything larger than ~5 cm |
| Ease | 2 |
| Tensile strength | 30–45 MPa |
| Impact resistance | Excellent |
| UV / weather | Moderate (degrades but slowly) |
| Water absorption | Low |
| Food safety | No |
| Smell / fumes | Strong; styrene fumes need ventilation |
| Recyclability | Recyclable where facilities exist |
| Cost / kg | $18–30 |

**Notes.** ABS is mostly displaced by ASA and PETG for outdoor use, but it remains the standard for parts that need to be machinable, acetone-smoothable, or solvent-welded. It warps aggressively without an enclosure and emits styrene fumes - print in a ventilated space.

### ASA (Acrylonitrile Styrene Acrylate)

| Property | Value |
|---|---|
| Nozzle | 240–260 °C |
| Bed | 90–110 °C |
| Chamber | Enclosed strongly recommended |
| Ease | 2 |
| Tensile strength | 40–55 MPa |
| Impact resistance | Good |
| UV / weather | **Excellent** - the reason to choose ASA |
| Water absorption | Low |
| Food safety | No |
| Smell / fumes | Strong, similar to ABS |
| Recyclability | Limited |
| Cost / kg | $25–40 |

**Notes.** ASA is the answer to "this part lives outdoors." Mailbox parts, garden hose fittings, Ring camera mounts, sprinkler heads - print in ASA. It is a drop-in replacement for ABS with vastly better UV stability, at a small price premium.

### TPU / TPE (Thermoplastic Polyurethane / Elastomer)

| Hardness | Nozzle | Bed | Ease | Feel | Common use |
|---|---|---|---|---|---|
| Shore 85A | 220–240 °C | 40–60 °C | 2 (very floppy, hard to feed) | Squishy, rubber-band-like | Soft gaskets, dampers |
| Shore 90A | 220–240 °C | 40–60 °C | 3 | Soft eraser | Watch straps, sandal soles |
| Shore 95A | 220–240 °C | 40–60 °C | 4 | Tire-tread firm | Phone cases, drone TPU, snap-fit hinges |
| Shore 98A / 60D | 230–245 °C | 50–60 °C | 4 | Stiff hose, just barely flexible | Bumpers, structural-flex parts |

| Other properties | Value |
|---|---|
| Chamber | Open |
| Tensile strength | 30–50 MPa (elongation 400–700% is the real metric) |
| Impact resistance | Excellent (it just deforms) |
| UV / weather | Moderate |
| Water absorption | Moderate-high; **dry before printing** |
| Food safety | No (most grades) |
| Smell / fumes | Mild |
| Cost / kg | $25–60 |

**Notes.** Shore hardness is the dial that matters: the lower the A number, the softer. Below 90A, a Bowden printer struggles to push the filament through the tube and you really want a direct-drive extruder. AMS / MMU systems are usually rated for 95A and harder only - see section 4. Print slow (20–30 mm/s) and turn cooling on for sharp features.

### Nylon (PA6, PA12, PA-CF)

| Property | PA6 | PA12 | PA-CF (carbon-filled) |
|---|---|---|---|
| Nozzle | 240–270 °C | 240–270 °C | 260–290 °C |
| Bed | 70–110 °C | 60–80 °C | 80–100 °C |
| Chamber | Enclosed | Enclosed helpful | Enclosed; chamber heat helps |
| Ease | 2 | 3 | 2 |
| Tensile strength | 60–90 MPa | 40–70 MPa | 70–120 MPa |
| Impact resistance | Excellent | Excellent | Good (more brittle than unfilled) |
| UV / weather | Moderate | Moderate | Moderate |
| Water absorption | **Very high** - saturates in hours | High | High |
| Food safety | Some grades | Some grades | No |
| Smell / fumes | Mild amine | Mild amine | Mild amine |
| Cost / kg | $30–60 | $40–80 | $70–130 |

**Notes.** Nylon is the king of mechanical parts - high impact, high fatigue life, low friction. The catch is moisture: a fresh spool exposed to a humid room for a single afternoon will pop and string when printed. Always print nylon directly from a heated dryer, not from a sealed bag. PA12 has lower moisture pickup than PA6 and is preferred when you can choose. PA-CF adds carbon fiber for stiffness and dimensional stability and is the standard for drone frames and quadcopter brackets.

### Polycarbonate (PC, PC-CF)

| Property | PC | PC-CF |
|---|---|---|
| Nozzle | 260–310 °C | 270–310 °C |
| Bed | 100–120 °C | 100–120 °C |
| Chamber | Heated chamber (60–80 °C) strongly preferred | Heated chamber required |
| Ease | 2 | 2 |
| Tensile strength | 70–100 MPa | 100–150 MPa |
| Impact resistance | Excellent | Good |
| UV / weather | Good (UV-stabilized grades) | Good |
| Water absorption | Moderate (dry before printing) | Moderate |
| Food safety | Generally no | No |
| HDT | 110–140 °C | 130+ °C |
| Cost / kg | $40–120 | $90–180 |

**Notes.** PC is the highest-strength common filament that fits on a typical consumer printer - but it really wants a heated chamber to avoid warping and layer cracking. Use this when you need transparency plus heat (clear PC), or when you need a part that survives 100 °C+ operating temperatures and high impact.

### Support materials: PVA and BVOH

| Property | PVA | BVOH |
|---|---|---|
| Nozzle | 180–210 °C | 200–220 °C |
| Bed | 45–60 °C | 45–60 °C |
| Solubility | Cold water | Cold water (faster than PVA) |
| Ease | 3 | 3 |
| Water absorption | **Extreme** (it's literally water-soluble) | Extreme |
| Pair with | PLA primarily | PLA, PETG, nylon (better high-temp tolerance) |
| Cost / kg | $40–70 | $80–150 |

**Notes.** Use only on multi-material printers (MMU, AMS, IDEX). Store in airtight desiccant containers between every print. BVOH is the upgrade if you're printing PETG or nylon and need support that doesn't get gummy at higher nozzle temps.

### HIPS (High-Impact Polystyrene)

| Property | Value |
|---|---|
| Nozzle | 230–250 °C |
| Bed | 90–110 °C |
| Chamber | Enclosed |
| Ease | 3 |
| Solubility | D-limonene (citrus solvent) |
| Pair with | ABS (similar print profile, dissolves away) |
| Cost / kg | $20–40 |

**Notes.** Mostly displaced by PVA / BVOH on modern printers. Still relevant as an ABS support material on older dual-extrusion machines.

### PEEK / PEI (Ultem): ultra-high-temp

| Property | PEEK | PEI / Ultem |
|---|---|---|
| Nozzle | 360–420 °C | 350–400 °C |
| Bed | 120–160 °C | 120–160 °C |
| Chamber | **Heated chamber 90–150 °C required** | Heated chamber required |
| Ease | 1 | 1 |
| Tensile strength | 90–110 MPa | 120–170 MPa |
| HDT | ~250 °C | 180–210 °C |
| Cost / kg | $150–500 | $150–400 |

**Notes.** Industrial-only. A normal consumer printer cannot print these. Mentioned here for completeness - if a part needs PEEK, send it to a service bureau (Markforged, Stratasys, Roboze) rather than buying a $20K printer.

### Aesthetic composites: wood-fill, metal-fill

| Property | Wood-fill PLA | Metal-fill PLA |
|---|---|---|
| Nozzle | 190–220 °C | 190–220 °C |
| Bed | 50–60 °C | 50–60 °C |
| Nozzle wear | High (hardened steel) | Very high (hardened steel) |
| Density | Slightly lower than PLA | 2-4× PLA (heavy spools) |
| Finish | Sandable, stainable | Sandable, polishable |
| Cost / kg | $25–60 | $40–80 |

**Notes.** Both are PLA-based with the additive making up 20-40% of the spool. Print like normal PLA, but use a hardened nozzle, larger nozzle diameter (0.5 mm+) to avoid clogs, and expect aesthetic-only mechanical properties - these are weaker than plain PLA.

### Carbon-fiber and glass-fiber reinforced composites

Any base polymer (PLA, PETG, ABS, nylon, PC, PPS) can be sold with chopped CF or GF added. The rules are the same for all:

- **Always use a hardened steel nozzle.** CF / GF chews through brass in 10-30 print hours.
- **Add 10-20 °C to the unfilled nozzle temp.** The fibers don't conduct heat well to the polymer.
- **Layer adhesion goes down, stiffness goes up.** These are stiff and lightweight but brittle.
- **Direct drive helps.** Bowden tubes wear faster with CF flex.
- **Surface finish is matte, with visible fiber sparkle.** Looks technical and industrial.

PPS-CF is the newer addition (2024-2025) for chemical resistance and high temperature; it competes with PA-CF for high-end functional parts and prints at 280–320 °C with a heated chamber.

---

## 3. Use-Case → Filament Matrix

| I want to print... | Top pick | Second pick | Why |
|---|---|---|---|
| Outdoor parts (sun exposure) | **ASA** | PETG (short-term), PC | ASA's acrylate backbone is genuinely UV-stable; PLA yellows in months |
| Mechanical / load-bearing | **PA12 or PA-CF** | PETG | Nylon's fatigue life and impact tolerance beat all alternatives |
| Snap-fit joint | **PETG** | Nylon (PA12) | PETG flexes without snapping; PLA cracks at the snap |
| Living hinge (thin flex bend, many cycles) | **PP (polypropylene)** | Nylon (PA12) | Both can survive thousands of cycles; PLA fails in <10 |
| Gaskets and seals | **TPU 85A–90A** | TPU 95A | Match Shore hardness to compression requirement |
| Drone frame | **PA-CF** | PETG-CF (cheaper) | Stiffness-to-weight + vibration damping |
| Decorative / aesthetic | **Matte PLA** or **Silk PLA** | Standard PLA | Matte hides layers, Silk has metallic sheen |
| Miniatures (high detail) | **Resin (SLA/MSLA)** | Standard PLA at 0.08 mm | FDM cannot match resin's surface resolution |
| Food contact | **Food-safe PETG** | Polypropylene | Verify the spool is FDA-grade; print with stainless nozzle; consider a food-safe coating (epoxy) for layer voids that harbor bacteria |
| Engine bay / under-hood | **PC or ASA** | PA-CF | HDT > 100 °C, UV-resistant |
| Dishwasher safe (top rack) | **PETG** or **PP** | ASA | PETG survives top-rack 60-70 °C; lower rack needs PC |
| Transparent | **PETG (clear)** | PC (clear) | PETG is the easy answer; PC for higher heat + better optical clarity |
| Flexible phone case | **TPU 95A** | TPU 90A | 95A snaps over the phone but flexes for drops |
| Presentation model | **Matte PLA** or **Silk PLA** | Resin (post-painted) | Customer-facing finish |
| Functional prototype (test fit, then make in metal) | **PLA or PETG** | PC-ABS | Fastest iteration; switch to PC-ABS only if you need to *use* the prototype |
| Glow-in-the-dark part | Glow PLA (hardened nozzle required) | - | The glow additive is phosphorescent powder; abrasive |
| Vase-mode lampshade | Translucent PETG or Silk PLA | - | Vase mode = single perimeter; needs predictable extrusion |

---

## 4. Print Settings Cheat Sheet

### Bed adhesion

| Material | Build plate | Adhesion aid | Notes |
|---|---|---|---|
| PLA | PEI (smooth or textured) | None usually; glue stick if needed | Textured PEI gives the nicest bottom finish |
| PETG | PEI textured, or glass | **Glue stick** (mandatory on smooth PEI to prevent tearing) | PETG bonds *too well* to bare PEI |
| ABS / ASA | PEI or glass | ABS slurry, glue stick, or hairspray | Bed at 100 °C+, brim mandatory |
| TPU | PEI smooth | None usually | Watch first-layer squish - TPU sticks like crazy |
| Nylon | **Garolite (G10/FR4)** | None | Nylon bonds chemically to garolite; PEI works in a pinch with glue |
| PC | Garolite or PEI | Glue stick, ABS slurry | Heated chamber really matters here |
| PVA / BVOH | PEI | None | Keep prints short and store the spool back in desiccant immediately |

### Cooling fan

- **PLA**: 100% after layer 2.
- **PETG**: 30-50%. Too much cooling = poor layer adhesion.
- **ABS / ASA**: 0-20%. Wants heat to bond layers; only fan small features.
- **TPU**: 30-100% depending on overhangs.
- **Nylon / PC / PEEK**: 0-10%. Cooling causes warping and delamination.

### Print speed sensitivity

| Material | Sweet spot | Notes |
|---|---|---|
| PLA | 60-300 mm/s (high-speed PLA exists) | Most forgiving |
| PETG | 40-80 mm/s | Faster = stringing |
| ABS / ASA | 40-60 mm/s | Faster = layer separation |
| TPU 95A | 20-40 mm/s | Faster = filament buckles in extruder |
| TPU 85A | 15-25 mm/s | Faster = will not extrude |
| Nylon | 30-60 mm/s | Faster = poor bonding |
| PC | 30-50 mm/s | Faster = warping |
| CF/GF blends | 30-60 mm/s | Linear advance / pressure advance tuning matters more than raw speed |

### Retraction notes

- **Direct drive**: 0.5-1.5 mm at 30-50 mm/s for most materials.
- **Bowden**: 4-7 mm at 30-50 mm/s.
- **TPU**: minimize retraction (0.5-1 mm) or disable entirely.
- **PETG**: lower retraction speed (25-30 mm/s) to avoid grinding.

### Common failure modes per material

| Material | Failure mode | Fix |
|---|---|---|
| PLA | Bed adhesion loss on cold day | Raise bed temp, clean PEI with IPA |
| PETG | Tearing chunks out of PEI | Glue stick on smooth PEI |
| PETG | Stringing | Dry filament, lower temp 5 °C, add travel-speed |
| ABS | Corners lifting | Enclosure, larger brim, lower bed-fan |
| ASA | Layer cracking mid-print | Enclosure, slower print |
| TPU | Filament buckling in extruder | Slow down, tighten extruder tension, switch to direct drive |
| Nylon | Popping / steam / stringing | **Dry the filament**, then print from dryer |
| Nylon | Warping | Garolite plate, enclosure |
| PC | Layer delamination | Heated chamber, slow first layer, dry filament |
| CF blends | Under-extrusion late in print | Hardened nozzle worn out; replace |
| Glow PLA | Same | Same - phosphorescent powder is very abrasive |
| PVA | Stringy/blistered | Wet filament; dry at 45 °C |

---

## 4b. Hardware Compatibility

### Hardened steel nozzle required

- All CF / GF reinforced filaments (PLA-CF, PETG-CF, PA-CF, PC-CF, PPS-CF)
- Glow-in-the-dark (phosphor powder)
- Wood-fill, metal-fill, marble-fill
- Most "PLA+" with mineral additives (check the TDS)

Hardened steel has lower thermal conductivity than brass, so add ~10 °C to nozzle temps when swapping from brass.

### All-metal hotend required

Any material printed above 240 °C - i.e., everything except PLA, TPU, and PVA - requires an all-metal hotend (no PTFE liner reaching the melt zone). Most 2023+ consumer printers ship with all-metal hotends by default.

### Enclosure required or strongly recommended

- ABS, ASA: enclosure mandatory for parts > 5 cm
- Nylon: enclosure recommended for parts > 10 cm
- PC: enclosure mandatory; heated chamber strongly preferred
- PEEK / PEI: heated chamber required (not just enclosure)

A passive enclosure (like the X1C) traps printer-generated heat. An active heated chamber (Qidi X-series, Bambu H2D, Voron with heater) drives chamber temperature to a target - necessary above PC and required for PEEK.

### Heated chamber thresholds

| Chamber temp target | Materials |
|---|---|
| Ambient (no enclosure) | PLA, PETG, TPU |
| 30-50 °C (passive enclosure) | ABS, ASA, small nylon parts |
| 60-90 °C (active) | PC, PC-CF, large nylon, PPS-CF |
| 90-150 °C (industrial) | PEEK, PEI/Ultem |

### AMS / MMU compatibility quirks

The Bambu Lab AMS and Prusa MMU3 share the same general gotchas:

- **TPU**: only the AMS HT (heated AMS) supports flexibles, and only down to ~95A. Soft TPU (85A) must be loaded from an external spool holder, bypassing the AMS.
- **Cardboard spools**: most AMS systems require specific spool dimensions. Bambu's reusable spool refill program exists exactly because random cardboard spools cause feeding problems.
- **Abrasive materials (CF, GF, glow, wood, metal)**: officially "not recommended" through AMS - they wear the AMS feeders. Many users do it anyway with a hardened steel hotend and just accept feeder replacement. Pure CF/GF prints should bypass the AMS.
- **PVA / BVOH**: works in AMS but the AMS is not airtight. Pull the spool back to a desiccant container between prints.
- **PETG**: the Bambu AMS has historically had grip-roller issues with PETG (the rollers slip on PETG's slick surface). Newer AMS units and AMS 2 Pro handle PETG much better; older AMS units may need PETG HF (high-flow, lower friction) specifically.

---

## 5. Storage Sensitivity

Ranked by how much moisture the material absorbs, fastest first:

| Rank | Material | Saturation time in 60% RH | Drying temp | Drying time (saturated spool) |
|---|---|---|---|---|
| 1 (worst) | PVA / BVOH | Hours - it's water-soluble | 45-50 °C | 10-12 h |
| 2 | Nylon PA6 | Hours | 70-80 °C | 12-24 h |
| 3 | Nylon PA12 | Days | 70-80 °C | 8-12 h |
| 4 | TPU | Days | 50-55 °C | 4-8 h |
| 5 | PC | Days | 80-100 °C | 6-12 h |
| 6 | PETG | Weeks | 60-65 °C | 4-8 h |
| 7 | ASA | Weeks | 60-70 °C | 4-6 h |
| 8 | ABS | Weeks-months | 60-80 °C | 4-6 h |
| 9 (best) | PLA | Months | 45-50 °C | 4-6 h |

### What wet filament looks and sounds like

- **Popping / crackling** at the nozzle (water flashing to steam inside the melt zone) - this is the classic and unmistakable signal.
- **Visible steam** from the nozzle, especially on dark filaments under good light.
- **Stringing and blobbing** that wasn't there with a fresh spool.
- **Surface roughness** - small craters or blistered texture on what should be a smooth wall.
- **Reduced layer adhesion** - parts snap apart at layer lines.
- **Bubbles in extruded test lines** - push some filament out manually and look for foam.

### Storage strategy

1. **Vacuum bag + silica gel** for long-term storage of unopened spools.
2. **Sealed bin + rechargeable desiccant** (color-changing silica is convenient) for the active library.
3. **Filament dryer on the printer** (Sunlu S2/S4, Polymaker Polydryer, Eibos, Sovol SH03) for active printing of nylon, TPU, PVA, PC. For PA, PVA, and BVOH this is basically mandatory.
4. **Re-dry before use** any spool that's been on the desk more than a week, especially nylon/TPU/PC.

A spool dried from a saturated state will start re-absorbing immediately on exposure. Drying gives you a few hours to a few days of working window depending on humidity - print right after drying, don't dry and shelve.

---

## 6. Brand Reputation Notes

These are community-consensus reputation notes, not a controlled comparison. **Inferred** - treat as starting hypotheses, not facts.

### Premium / engineering tier

- **Prusament** (Prusa Polymers, Czech Republic). Tight ±0.02 mm diameter tolerance, batch-traceable QR code, consistent color batches. Limited material catalog but every spool is what it says it is. Premium price; defensible if you run a print farm or care about repeatability.
- **Polymaker** (Shanghai). Broad catalog from value (PolyTerra, recycled-cardboard spool) through engineering (PolyMide CoPA, Fiberon PA-CF, PolyMax PC) to specialty. Generally excellent QC; the engineering lines are competitive with much more expensive industrial filaments. PolyTerra Matte is a community favorite for aesthetic prints.

### Printer-OEM tier

- **Bambu Lab**. Tuned for their own printers (RFID auto-detect in the AMS, profiles preloaded in Bambu Studio). Quality is good; price is high relative to third-party. PETG HF and PLA Basic are the workhorses. The PA-CF and PC lines are competent but expensive; many users prefer Polymaker for those.
- **Prusament**. See above - also acts as the printer-OEM tier for Prusa machines.

### Value tier (the dependable budget brands)

- **Hatchbox**. Long-standing, US-distributed, mostly Amazon. PLA and PETG are reliably good; specialty lines are hit-or-miss. Lot-to-lot variation more visible than premium brands.
- **Overture**. Mid-tier with consistent PLA and PETG. Matte PLA is a strong-value alternative to Polymaker PolyTerra. Diameter tolerance is published and credible.
- **eSun**. Broad catalog at low prices. PLA+ and ePLA-HS (high-speed) are well-regarded; specialty materials more variable. Often the entry point for engineering materials (PA, PC) at hobbyist prices.
- **Sunlu**. Budget-tier with surprising consistency in PLA and PLA Meta (their high-speed formulation). PETG and TPU are competent. Filament dryers (S1/S2/S4) are widely owned and a separate Sunlu product line worth knowing about.

### "Sketchy until proven otherwise"

- Random Amazon/AliExpress brands with no published TDS, no diameter tolerance spec, and rotating brand names. Diameter variation, dye inconsistency, and surprise additives are all common. Fine for a one-off cosmetic print; do not use for anything mechanical or food-adjacent.

### Spool format note

- **Plastic spools**: most consistent feeding, slightly more environmental waste.
- **Cardboard spools** (Polymaker PolyTerra, refill packs): lower waste, but absorb moisture themselves and can deform after vacuum-bag compression. In a humid environment, transfer to a plastic spool for storage.
- **Refill / spool-less coils** (Bambu refills, Prusa refills): cheapest per kg, but require an existing reusable spool. Worth it if you print enough volume.

---

## 7. Quick Reference: "What's in my dry box right now?"

A reasonable starter kit for an enclosed printer like the X1C:

1. **PLA** - 1 kg neutral color (white, black, or grey) for general work
2. **PETG** - 1 kg clear or black for mechanical/outdoor/food-adjacent
3. **ASA** - 1 kg black for outdoor parts
4. **TPU 95A** - 1 kg black for cases, dampers, grommets
5. **PA-CF** - 1 kg, only if you have a project that justifies it

Skip PC, PEEK, PVA, and unusual composites until a specific need arises. Buy specialty PLAs (silk, matte, wood, metal) as one-off project purchases rather than stocking them.

---

## Sources and further reading

- Bambu Lab Filament Compatibility Wiki - https://wiki.bambulab.com/en/general/filament-guide-material-table
- All3DP, Prusa, Polymaker, and MatterHackers material guides (cross-referenced for the property tables)
- r/3Dprinting community consensus on brand reliability (treated as starting hypotheses, not verified facts)
- Sigma, 3DJake, and Sovol filament drying tables (cross-referenced for the storage section)
