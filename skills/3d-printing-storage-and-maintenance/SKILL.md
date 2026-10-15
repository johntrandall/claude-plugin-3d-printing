---
name: 3d-printing-storage-and-maintenance
description: Reference knowledge on filament storage (dryboxes, desiccant, humidity targets), drying (temps/times per material), and FDM printer preventive maintenance + defect diagnosis. Auto-invoke when troubleshooting a print failure, scheduling maintenance, drying filament, or setting up storage.
last_refreshed: 2026-10-15
---

# 3D Printing: Filament Storage, Drying, and FDM Printer Maintenance

A practical reference for keeping filament dry, drying it back when it's not, and maintaining an FDM printer fleet so prints come out the way they were sliced. Companion to `3d-printing-filaments` (material selection) and `3d-printing-models-and-tools` (model sourcing, slicer tooling).

Product prices below are rough US dollar figures as of October 2026. This plugin is not affiliated with Bambu Lab.

The single most common cause of a "my printer is broken" complaint is wet filament, not a broken printer. Diagnose storage and drying first.

---

## Part 1: Filament Storage

### 1.1 Why moisture matters (per material)

All thermoplastics absorb atmospheric water; the rate and consequence vary by polymer chemistry. When wet filament hits the melt zone, water flashes to steam inside the molten plastic. That steam disrupts laminar extrusion, forms bubbles, oxidizes the polymer at high temp, and on the cold side breaks the polymer chains so the cooled part is weaker.

| Material | What wet filament does | Sensitivity |
|---|---|---|
| **PLA** | Audible popping at the nozzle, surface bubbles/zits, brittleness, ~20–30% strength loss after weeks at ambient | Low–medium |
| **PETG** | Heavy stringing, foggy/milky surface (loss of transparency), inconsistent extrusion, oozy travels | Medium |
| **Nylon (PA6, PA12, PA-CF, PA-GF)** | Catastrophic: extreme stringing, white/milky filament, weak layer adhesion, dimensional drift, surface defects. PA6 can absorb >3% water by weight within 24h at 50% RH | **Very high** |
| **TPU / flexibles** | Popping, extrusion stalls, gummy/sticky residue at nozzle, surface bubbles | High |
| **PC / Polycarbonate** | Brittle parts (it's supposed to be tough; if it snaps, it's wet), layer adhesion loss, hazy clear PC | Medium–high |
| **PVA / BVOH (support)** | Self-destructs; clumps inside the extruder; loses dissolution behavior | **Very high** |
| **ASA / ABS** | Surface bubbles, layer adhesion drop, slight stringing | Low–medium |
| **PEEK / PEI / Ultem** | Won't print correctly without industrial drying; high-temp polymers demand industrial RH control | **Extreme** |

### 1.2 RH thresholds (consensus rule of thumb)

These are operational targets, not absolutes. Use as a tiered guideline:

| RH inside storage | Status | Action |
|---|---|---|
| **< 15%** | Gold standard - equivalent to fresh-from-vacuum-bag | None; ideal for Nylon/PVA/PC |
| **< 20%** | Fine for PLA, PETG, ABS, ASA; acceptable for TPU/PC | None |
| **20–30%** | Marginal; long-term degradation begins, especially Nylon/TPU | Replace/regenerate desiccant |
| **30–50%** | Actively degrading; print quality measurably worse | Dry the filament before next print |
| **> 50%** | Damaging; treat as wet | Dry, then store properly |

Ambient indoor humidity in most North American homes runs 30–60% (higher in summer, lower in winter heating season). Coastal and basement humidity can hit 70–80%. **A filament spool left on a shelf is wet within days.**

### 1.3 Storage solutions, by tier

#### Cheap (entry, < $30/spool)

- **Vacuum bags + indicating silica gel** - Mylar or PE vacuum bags (Spacesaver, Ziploc Space Bag) plus 50–100g of orange-indicating silica gel per spool. Cheapest viable long-term storage. Caveats: vacuum bags slowly leak through valves; check every 2–4 weeks; vacuum once, not repeatedly (creases form leaks).
- **Tupperware / IRIS Airtight Cereal Container + desiccant** - Wide community endorsement of the **IRIS USA Airtight Pet Food Container** (12 qt holds a 1kg spool with desiccant; ~$15 on Amazon). Better seal than generic Tupperware. Cheap-hack famous in r/3Dprinting since ~2019.
- **5-gallon bucket + Gamma Seal lid** - Screw-top airtight bucket; holds 3–4 spools plus a tray of desiccant. ~$15 for the lid, $5 for the bucket at hardware stores. Excellent for bulk storage.
- **Mylar bags + O2 absorbers** - Borrowed from food preservation. O2 absorbers don't help with humidity per se; pair with desiccant. Reliable long-term archival storage.
- **Ziplock bags** - Inadequate for anything beyond a few days. Air exchanges through the seal.

#### Mid-tier (active or semi-active container, $50–$150)

- **PolyDryer (Polymaker)** - Modular stackable dry box system; can run heated as a dryer or passive with desiccant as storage. Each module holds one spool. PTFE feed-through for printing from the box. Often the best balance of storage + drying for prosumers.
- **Sunlu FilaDryer S1/S2** (used passively) - Heater off, lid sealed; works as a dry storage box. Add desiccant for actual RH control (the units don't include effective desiccant out of the box).
- **EIBOS Easdry / smaller EIBOS units** - Similar form factor; some include indicator hygrometers.
- **Bambu AMS storage racks** (third-party 3D-printed) - Wall- or shelf-mount Mylar bag holders that integrate with AMS feed paths.

#### Active dryboxes: heat + airflow, store and print from the same unit

| Unit | Spools (1kg) | Maximum temp | Notes |
|---|---|---|---|
| **Sunlu S1** | 1 | 50 °C | Entry, no humidity readout |
| **Sunlu S2** | 1 | 70 °C | Most common consumer dryer, PTFE feed-through |
| **Sunlu S4** | 4 | 70 °C | Multi-spool, large footprint |
| **Sunlu E2** | 2 | 70 °C | Compact 2-spool |
| **Polymaker PolyDryer (heated module)** | 1 per module, stackable | 75 °C | Best modular system; PTFE feed-through; HygroSense humidity sensor |
| **EIBOS Cyclopes** | 2 | 70 °C | Convection + fan; print-from-drybox via PTFE |
| **EIBOS Polyphemus** | 4 | 70 °C | Large capacity; popular for production |
| **EIBOS Easdry** | 1 | 55 °C | Entry-level |
| **PrintDry PRO3** | 2 | 70 °C | Long-time enthusiast favorite; replaces discontinued PrintDry Pro |
| **Creality Filament Dryer Box 2.0** | 1 | 70 °C | Budget; humidity readout |
| **Comgrow Filament Dryer** | 2 | 70 °C | Budget multi-spool |
| **Sovol SH01 / SH02** | 1–2 | 70 °C | SH02 has touchscreen + RH readout |

**Print-while-drying** is the holy grail. Look for: PTFE feed-through ports, heater that maintains temp continuously without timeout (some have 24h auto-off), built-in fan (convection-only takes hours to recover after opening), and a humidity sensor inside the chamber (not just on the door).

#### DIY (proven community builds)

- **Food dehydrator hack** - Pull out the stacked trays, set the spool on the base. Presto 06301, Magic Mill, and Cosori are the popular bases. Pros: huge capacity (up to 4 spools), accurate-ish thermostat, cheap (~$50). Cons: no humidity control, often runs hot, must be on a level surface, drying-only (no print-from-dryer).
- **Ikea SAMLA tote + rechargeable Eva-Dry desiccant + Govee hygrometer** - ~$25 build. 22L SAMLA tote holds 2–3 spools. Snap-shut lid is reasonably airtight if you swap the stock gasket. Common DIY recipe.
- **Custom heated cabinet** - PTC heater + thermostat + fan in an Ikea or food-grade plastic cabinet. r/3Dprinting and r/voroncorexy have detailed build threads. Best for large fleets.
- **Server-rack style multi-spool builds** - Heated 19" rack inserts with PTFE feed-throughs to a print farm. Industrial scale only.

#### AMS and multi-color systems: what they actually do

- **Bambu AMS (original)** - Seals spools and monitors humidity with a single internal sensor; **does not heat or actively dry**. Add Bambu's silica gel rolls (or generic equivalents) and check RH on the printer screen. Treat as dry *storage*, not drying.
- **Bambu AMS HT** (single-spool, higher-temp materials) - Heats to ~65 °C; suitable as a passive drying unit during print for moisture-sensitive materials like PA-CF, PETG-CF.
- **Bambu AMS 2 Pro** (announced 2025) - Active heating to dry inside the AMS; closer to a true integrated dryer.
- **Prusa MMU3 / Prusa CORE One MMU** - No humidity control or sealing; relies entirely on external storage/drying. CORE One's heated chamber can passively help during long prints.
- **Anycubic ACE Pro** - Similar to AMS; heated drying inside the multi-spool unit.

### 1.4 Desiccant management

#### Silica gel

- **Orange-indicating silica gel** - Orange when dry, green/dark when saturated. Preferred over older blue cobalt-chloride indicator (cobalt chloride is a suspected carcinogen and banned in EU REACH). Buy in 1–5kg bulk from Amazon, Uline, or McMaster-Carr.
- **Capacity** - Silica gel adsorbs ~20–40% of its own weight in water at high RH. Practical sizing: **~50–100g of fresh silica gel per liter of container** for filament. A 1kg spool in a 12qt (~11L) IRIS container wants 100–200g of desiccant.
- **Regeneration** - Spread thin on a sheet pan, 120 °C (250 °F) in a conventional oven for 2–3 hours. Confirm full color return to orange. **Do not microwave indicator silica** - it can melt the indicator dye and the bag. Plain non-indicator silica beads can microwave at low power but it's risky.

#### Molecular sieves

- **3A vs 4A** - Pore size in Ångströms. **3A** (3 Å pore) admits only water molecules - preferred for filament because it won't adsorb other organics. **4A** (4 Å pore) admits water plus larger molecules (e.g., CO2, ethanol); cheaper but less specific. For filament dry boxes, **3A is the right choice**.
- **Why use them** - Molecular sieves drive RH lower than silica gel can (silica plateaus around 10–20% RH; 3A can hit single-digit RH). Use 3A on top of silica when you need <15% RH for Nylon/PVA/PEEK.
- **Regeneration** - 200–250 °C (400–480 °F) for 2–4 hours in a conventional oven (not toaster oven - temperature accuracy matters). They cannot be microwaved.

#### Indicator strips and color-change packs

- Bambu Lab and Polymaker sell indicating desiccant pucks/rolls with color windows. Convenient for AMS bays. Lifespan: a few weeks to months depending on ambient RH and how often the lid opens.

### 1.5 Hygrometers

- **Cheap reliable models:**
  - **Govee H5100 / H5104 / H5179** - Bluetooth, app-loggable, ~$12 each. The most-recommended hobby hygrometer; multi-pack to seed every storage container and dryer.
  - **ThermoPro TP49 / TP50 / TP55** - Standalone digital, no app. ~$10. Cheap multi-pack for headless monitoring.
  - **SensorPush** - Higher-accuracy Bluetooth with optional gateway; $50+. Overkill for hobby but excellent for production.
- **Two-point calibration matters.** Cheap hygrometers can read ±5–10% RH out of the box. Calibrate with a **Boveda One-Step Calibration Kit** (75% RH salt pack - most kits ship with 75% only; some have 32% too). Procedure: seal hygrometer in a Ziploc with the Boveda pack for 24h, then check reading vs the pack's stated RH. Apply offset in the device (Govee allows this in-app) or note it manually. Better: two-point calibration with both 32% and 75% packs to catch nonlinearity.
- **Placement** - Inside the drybox/container, mid-height, away from desiccant (you'll read the desiccant's micro-environment, not the spool's), away from direct fan airflow in active dryers.

---

## Part 2: Filament Drying

### 2.1 When to dry: symptoms

Before adjusting retraction or temp, ask "have I dried this spool?" If no, dry first, retest, then tune.

**Universal symptoms (any material):**
- **Audible popping, crackling, or snapping at the nozzle** - water flashing to steam. The single most diagnostic symptom.
- **Visible steam, wisps, or condensation** near the nozzle in a cool room.
- **Filament snaps in your hand** with a clean break (worst in PLA and PA-CF).
- **Surface roughness, blobs, zits, oozing during travels** that wasn't there with a fresh spool.
- **Layer adhesion drops** - parts delaminate under hand force that should be tough.
- **First-layer adhesion goes weird** even with good bed prep.

**Material-specific tells:**
- **Nylon** - goes from translucent to **opaque white**; brittle filament; "fuzz" along extruded line.
- **PETG** - prints look **glassy/foggy** instead of clear; heavy stringing on a material that's already string-prone but should be tunable.
- **TPU** - gets **gummy** at nozzle, sticks to itself in the spool, popping during retraction.
- **PLA** - surface zits, brittle filament, occasional snap on the spool, slight popping.
- **PC** - finished parts are **brittle** (PC is supposed to be tough); hazy clear PC.
- **ABS/ASA** - surface bubbles, faint popping; symptoms milder than PETG/Nylon.

### 2.2 Drying temperatures and times

Authoritative ranges, consolidated from filament manufacturers (Polymaker, Bambu Lab, Prusament, ColorFabb, Hatchbox) and dedicated dryer manuals (PrintDry, Sunlu S2, EIBOS, PolyDryer):

| Material | Temp | Time | Notes |
|---|---|---|---|
| **PLA** | 40–50 °C | 4–8 h | **Glass transition (Tg) ~55–60 °C** - exceed it and the spool deforms or filament fuses. Stay ≤50 °C. |
| **PLA+ / Tough PLA** | 45–55 °C | 4–8 h | Higher Tg than standard PLA, slightly more headroom. |
| **PETG** | 60–65 °C | 4–6 h | Standard. Some brands tolerate 70 °C. |
| **ABS / ASA** | 65–80 °C | 4–6 h | Watch for spool warp at the high end. |
| **Nylon (PA6)** | 70–80 °C | 12–16 h | Highly hygroscopic - long dry. Severe cases: 24h+. |
| **Nylon (PA12)** | 70–80 °C | 8–12 h | Less hygroscopic than PA6. |
| **PA-CF / PA-GF** | 80–90 °C | 8–16 h | Carbon/glass fill traps water; dry longer. |
| **TPU / TPE** | 45–55 °C | 4–8 h | TPU also softens at high temp; don't push past 55 °C. |
| **PC / Polycarbonate** | 80–100 °C | 6–10 h | Most consumer dryers top out at 70–80 °C - undersized for PC. Use food dehydrator with high range. |
| **PVA** | 45 °C | 6–10 h | **Heat-sensitive; >50 °C degrades it.** Don't try to speed-dry. |
| **BVOH** | 50–55 °C | 4–6 h | Similar to PVA, slightly more heat-tolerant. |
| **HIPS** | 60–65 °C | 4–6 h | |
| **PEEK / PEI / Ultem** | 120–150 °C | 4–6 h | Industrial dryers only. |

**The single most important caveat:** consumer filament-dryer thermostats commonly run **5–15 °C cold** versus their setpoint. A "70 °C" Sunlu S2 may actually be 55–60 °C inside. **Verify with a separate thermometer/hygrometer in the chamber** - a Govee or ThermoPro slipped onto the spool tells you the truth. Adjust setpoint upward accordingly.

**Better than fixed time: dry until the chamber RH stops dropping** (target <15% RH at temperature). This is the real endpoint; the times above are conservative defaults assuming you can't measure.

### 2.3 Drying methods compared

#### Dedicated filament dryers
**Pros:** purpose-built airflow, presets per material, often have PTFE feed-throughs to print from the dryer, humidity readout on the better models.
**Cons:** cost ($50–$200), limited spool count, thermostats often run cold (see caveat above), some auto-off after 24h (Nylon needs longer).
**Best picks (2025):** Polymaker PolyDryer (modular), Sunlu S2/S4 (best price/perf), EIBOS Cyclopes/Polyphemus (best convection + multi-spool), PrintDry PRO3 (premium, two spools), Sovol SH02 (budget with touchscreen + RH readout).

#### Food dehydrator (hack)
**Pros:** ~$50 for high capacity, generally accurate thermostat across the range (Presto 06301 goes to 71 °C, Magic Mill to 75 °C, Cosori to 75 °C), fits 3–4 spools.
**Cons:** no humidity readout, drying-only (no print-from), uneven (rotate spools or run longer), some run hot at low settings.
**Setup:** remove all trays except the bottom one, set spool flat, run at material's target temp + 5 °C to compensate for indirect contact.

#### Conventional oven
**Risky.** Most ovens don't go below 75 °C; many residential ovens have ±15 °C hotspots and cycle aggressively. Real risk of melting PLA spools (the spool itself, not the filament - many spools are PLA or PETG plastic and will deform at 60 °C). Only acceptable for **high-temp materials** (Nylon, PC, PEEK), with a verified-accurate oven thermometer and a sheet pan to spread heat, and the spool on a cardboard or wood riser. Even then, dedicated dryers are safer.

#### In-printer drying

- **Bambu AMS HT** - Heats to ~65 °C inside the single-spool HT unit; suitable for PA-CF, PETG-CF, ASA. Lets you keep the spool dry across long prints.
- **Bambu A1 / A1 mini "dry spool" mode** - Uses the heatbed to dry a spool placed on it (see "X1/P1/H2 bed-dry hack" below - Bambu officially supports this on A1 series).
- **Bambu X1C / P1S / H2D bed-as-dryer** - Community/official hack: place spool on the heated bed inside the enclosure, set bed to 60–65 °C, close lid, run 6–8h. Bambu published an official guide for this in 2024. Works because the enclosed chamber holds heat.
- **Prusa CORE One heated chamber** - Active chamber heat (up to ~55 °C ambient) keeps filament dry during print but isn't aggressive enough as a primary dryer.
- **Anycubic Kobra S1 Combo** - Has a dryer-integrated ACE Pro.

#### Run-while-printing
The single biggest workflow improvement for moisture-sensitive materials. Dryers that support it via PTFE feed-through: **Sunlu S2/S4**, **EIBOS Cyclopes/Polyphemus**, **Polymaker PolyDryer**, **PrintDry PRO3**, **Sovol SH02**. The dryer sits next to the printer; PTFE tubing routes the filament. Eliminates the "dry then immediately rehydrate while printing" problem.

### 2.4 Verifying dryness

- **Weight-loss method** - Weigh the spool before drying, then every 2 hours during drying. Stop when weight stops dropping. Typical loss for a moderately wet kg-spool: **5–30g**; severely wet Nylon: **30–50g+**. Most accurate objective check.
- **Hygrometer in chamber** - Target **<10–15% RH at drying temperature**. If RH won't drop below 20%, your desiccant pack inside the dryer (if any) is saturated, or the unit is leaking, or the spool is much wetter than expected.
- **Watch extrusion** - After drying, purge a line. Listen (no popping), look (smooth glossy strand, no bubbles, no steam), feel (filament has its expected stiffness).
- **Test print** - Single-wall vase or retraction tower. Empirical proof; takes 30 minutes.
- **"Spool snap test" - DON'T.** A common bit of bad advice: "snap a piece of filament; if it snaps clean it's wet, if it bends it's dry." This is unreliable (PLA and PA-CF can be brittle when dry from age or formulation), wastes filament, and tells you less than 5 minutes of test-printing would. Skip it.

---

## Part 3: FDM Printer Maintenance

### 3.1 Daily / per-print

- **Bed cleaning** - Print surface determines cleaner:
  - **PEI smooth (Bambu engineered plate, Prusa Satin)** - 91%+ isopropyl alcohol (IPA), microfiber cloth.
  - **PEI textured (Prusa textured, Bambu textured)** - **Dish soap + warm water in the kitchen sink** (IPA spreads oils on textured surfaces rather than removing them; not effective).
  - **Glass** - Windex with ammonia, or IPA. Glue stick reapply for ABS.
  - **G10 / FR4 (Garolite)** - IPA. Used for Nylon.
- **Never touch the print surface with bare fingers.** Skin oils are the #1 cause of mysterious first-layer adhesion failures. Use the corner tab to handle.
- **Visual nozzle check** before each print - look for plastic buildup, leaks around the heater block (cold leak), loose silicone sock.
- **First-layer monitor** - eyeball or printer camera. Abort within the first 5 layers if adhesion is wrong; an aborted print costs 5 minutes, a failed 18-hour print costs 18 hours.
- **Filament path check** - spool turns freely, no tangle, no dust collection on filament passing through guides.

### 3.2 Weekly / ~50 print hours

**Lubrication.** The most common operator error. Wrong lubricant = damaged rails, gummed bearings, attracted dust.

| Where | Right lubricant | Wrong (do not use) |
|---|---|---|
| Linear rails (MGN9/12 - Bambu, Voron, Prusa MK4) | **Super Lube 21030 synthetic PTFE grease** (community consensus); **Krytox GPL 205** (premium) | WD-40, white lithium, Vaseline, motor oil |
| Lead screws (Z-axis) | Super Lube 21030 or PTFE-safe grease; some printers use lead-screw nut grease pre-applied by manufacturer | WD-40, dry graphite |
| Smooth rods (older Enders, MK3-style) | Light machine oil (3-in-1, sewing machine oil) - sparingly | Vaseline (attracts dust + degrades plastics), thick grease |
| Extruder gear / pulleys | Nothing - keep clean and dry | Any lubricant (attracts filament shavings) |
| POM V-wheels (Ender 3 family) | Nothing - clean only; some users apply a microscopic Super Lube film | Anything that swells POM |

**Banned:**
- **WD-40** - it's a *degreaser*, not a lubricant. Strips existing grease, attracts dust, evaporates leaving residue. Never appropriate for printer mechanics.
- **Vaseline / petroleum jelly** - Attracts dust, swells/degrades many plastics (POM, ABS) over time, doesn't stay where applied at print temps.
- **White lithium grease** - incompatible with many plastics; can damage POM wheels, polycarbonate parts.
- **Cooking oils, olive oil** - go rancid, attract dust, no lubrication value.

**Belt tension** - should feel taut with a clean "pluck" tone. Tools:
- **Gates carbon tension meter** - precision, ~$45.
- **Phone tuner app** (Insta-Tuner, Pano Tuner) - pluck the belt, read the resonance frequency. Voron community standard: **~110 Hz** for the A/B belts on a Voron 2.4 with stock belts. Bambu and Prusa: refer to the manufacturer's stated tension or feel-based ("taut, not tight").
- **Feel** - should not be so tight it deflects the gantry inward; should not be so loose it sags or makes a buzzing sound.

**Frame screw retorque** (V-slot extrusion printers especially - Ender, Voron) - vibration loosens. Quick once-over with the printer-supplied hex set.

**Dust wipe** - microfiber cloth over rails, frame, bed underside. Dust mixed with grease = lapping compound.

### 3.3 Monthly / ~200 print hours

- **Cold pull (atomic pull)** - diagnostic and clog-prevention.
  1. Heat to print temperature (e.g., 220 °C for PLA, 245 °C for PETG).
  2. Push filament through manually until it extrudes cleanly.
  3. Cool to ~90 °C for PLA, ~110 °C for ABS/PETG.
  4. Yank filament out firmly. The end should show a clean negative impression of the nozzle interior. Black gunk = old clog being pulled out.
  5. Repeat with fresh filament 2–3 times until the pulled tip is clean.
- **Nozzle change** - replace if visibly worn (oblong opening), after every ~50 hours of CF/GF filament for brass nozzles, after a definitive clog that survives a cold pull.
- **PTFE Bowden tube inspection** - pull both ends, look for discoloration (charred = burned PTFE, hazardous), kinks, short sections inside the hotend (cut clean square ends). Replace if any issue. Cheap part; replace annually as preventive on Bowden printers.
- **Extruder drive gear** - open the extruder cover (printer-specific). Brush out filament shavings (an old toothbrush or compressed air). Shavings = filament slipping = wet filament, wrong tension, or worn idler.
- **Bed level / mesh recalibration** - most modern printers auto-mesh; re-run the mesh after moving the printer, changing the print sheet, or any time first layer starts going sideways.
- **Hot-tighten the nozzle** - Heat the hotend to printing temperature, then with **two wrenches** (one holding the heater block to prevent twisting wires loose, one torquing the nozzle), give the nozzle ~1/4 turn of tightening. This seats the nozzle against the heat break and prevents the "cold leak" where molten plastic creeps up around the threads and oozes around the heater block. Do this on every nozzle change and at least monthly otherwise.

### 3.4 As-needed

- **Hotend disassembly** (full clog that survives cold pull) - remove heater block, cold-soak in acetone if PLA-clogged (overnight), use thin pin (0.4mm acupuncture needle is the community trick) to clear bore. Replace heat break if cold-side clog (charred ring inside the throat).
- **Replace nozzle** - see §3.5 for lifespan.
- **Replace heat break** - every ~1 year heavy use or after first stripped/galled installation. Failure mode: cold-side clog (filament jams above the melt zone).
- **Replace heater cartridge** - typically 2–5 year lifespan; fails as PID swings or unable to reach temp. Cheap part.
- **Replace thermistor** - fails as temp readings go to MAXTEMP or random values, printer aborts. Cheap part, easy swap.
- **Replace PEI sheet** - when scratched (impacts first-layer aesthetic) or dished (impacts first-layer adhesion). Heavy use = 1–2 years. Smooth PEI dishes faster than textured.
- **Stepper motor diagnostics** - overheating to the touch (running too hot current), missed steps under load (current too low or mechanical bind), unusual whine (current/microstepping config). Tune via firmware (Klipper, Marlin TMC settings).
- **Z-offset drift** - typically creeps +/-0.05mm over weeks as the bed mounts settle, the PEI sheet relaxes, or the probe drifts. Re-baby-step into spec.

### 3.5 Abrasive filament protocol

Carbon fiber, glass fiber, glow-in-the-dark, wood-fill, metal-fill, and most "engineering" composite filaments are abrasive. A brass nozzle running PA-CF can be ovaled in **10–50 hours**.

| Nozzle material | Brass | Hardened steel | Ruby-tipped | Tungsten carbide |
|---|---|---|---|---|
| Standard PLA/PETG/ABS life | 1000+ h | 1000+ h | 1000+ h | 1000+ h |
| CF/GF life | 10–50 h | ~500 h | 1000+ h | 1000+ h |
| Cost | $1–3 | $5–15 | $90+ | $40–80 |
| Heat transfer | Excellent | Reduced (compensate +5–10 °C) | Reduced | Reduced |
| When | Default | Any CF/GF | Print farm with CF | Heavy continuous CF |

**Heat break:** swap PTFE-lined for **all-metal titanium heatbreak** when printing at temps >245 °C (PTFE degrades and outgasses HF) or with abrasive high-temp materials (PA-CF, PC, PEI).

**Extruder gear:** hardened-steel extruder gears (BMG-style, Bondtech) wear less than brass-coated steel when feeding abrasives.

### 3.6 Print defect → cause/fix matrix

The most usable form for quick triage:

| Defect | Most likely causes (in order) | First fix to try |
|---|---|---|
| **Stringing** | Wet filament; retraction too low; hotend too hot; travel too slow | **Dry filament first**; then bump retraction by 0.5mm and re-tune |
| **Stringing in walls only** (inner perimeters) | Coasting off; wipe-on-retract off; temp too high | Enable coasting and wipe; drop temp 5 °C |
| **Layer shifts** | Loose pulley grub-screw; belt tension; print head collided with print; accel too high | Tighten pulley grubs, recheck belt tension, lower print accel |
| **Warping** | Bed temp too low; no enclosure for ABS/ASA; draft from window/AC; poor adhesion | Increase bed temp; add brim; enclose printer for ABS/ASA; eliminate drafts |
| **Elephant's foot** (first layer wider than rest) | First layer too squished; bed temp too high for material; no first-layer compensation | Raise Z-offset 0.02–0.05mm; reduce bed temp 5 °C; enable first-layer horizontal expansion compensation in slicer |
| **Under-extrusion** | Partial nozzle clog; extruder skipping (tension or wet filament); print temp too low; flow too low | Cold pull; check extruder tension; bump temp 5 °C; verify e-steps / flow rate |
| **Over-extrusion** (blobs, dimensional growth) | Flow rate too high; e-steps wrong; temp too high | Calibrate flow with single-wall test; recalibrate e-steps |
| **Ghosting / ringing** (echo of features) | Print/travel speed too high; accel too high; belt tension too low; weak frame; input shaping not tuned | Drop accel; retension belts; **run input-shaping calibration** (Klipper, Bambu, Marlin 2.1+) |
| **Poor bridging** | Part cooling fan too low; bridge speed too high; flow too high on bridges | Bump part-cooling fan to 100%; reduce bridge speed; reduce bridge flow to 95% |
| **First-layer adhesion failure** | Bed dirty (oils); Z-offset too high; bed temp wrong; wrong cleaner for surface | Clean bed with appropriate cleaner; re-baby-step Z; verify bed temp |
| **Holes in top layer (pillowing)** | Top layer count too low; cooling insufficient; infill too sparse | Increase top layers to 5–6; bump part cooling; increase infill |
| **Z-banding / Z-wobble** | Bent lead screw; binding Z; lead screw coupler too tight | Inspect and replace coupler; check Z rails for bind |
| **Salmon skin** (LCD/resin only) | LCD pixel issues, exposure variation | LCD replacement, exposure re-tune (mentioned for completeness; FDM doesn't get salmon skin) |

### 3.7 Printer-specific maintenance notes

**Bambu Lab (X1C, X1E, P1S, P1P, A1, A1 mini, H2D)**
- **Quick-swap hotend** (X1/P1/H2 series): designed for ~1 minute swap. Swap when changing nozzle size or material class.
- **AMS humidity sensor** cleaning - wipe with dry microfiber; condensation can throw readings.
- **Carbon rod lubrication** (X1/P1 X-axis): Bambu recommends a light film of their supplied grease every ~300h. **Do not over-grease** - excess attracts dust onto the toolhead.
- **Lidar calibration** (X1C/X1E): runs at the start of prints; manual lidar calibration in settings if it drifts.
- **Eco mode** - reduces fan/light power during long prints; doesn't affect print quality.
- **AMS PTFE tubes** - replace if you see filament shavings near the AMS feeders.
- **External spool alongside AMS Lite (A1/A1 mini)** - the toolhead hub is passive and firmware doesn't map hub ports to AMS trays, so a spare hub port can take a permanent PTFE tube from an external spool (drybox feed, TPU): run the AMS Lite on 3 ports, dedicate the 4th to Ext. Community-proven (*Observed*): load via touchscreen Filament → Ext → Load with manual feed to the extruder; retract the ext filament past the hub merge zone after use or AMS loads jam; the matching AMS slot must stay empty; **AMS + Ext can never combine in one print job** (firmware maps a job to one source). Aftermarket "5-way" hubs for the A1 are 4-input (the name counts the output); genuine 5-input printable hubs exist on MakerWorld (model 1310652).

**Prusa (MK4, MK4S, CORE One, XL, MK3S+)**
- **Nextruder loadcell calibration** (MK4 family): re-run after any heater/hotend work. The loadcell is the Z-touch sensor; out-of-cal = bad first layer.
- **MMU2/MMU3 maintenance** - selector lubrication (Prusa-specific Plastilube or similar), idler tension, FINDA sensor cleaning.
- **Input Shaping (IS) calibration** - run from the printer menu after belt changes or major mechanical work.
- **IR filament sensor** (MK3S+, MK4) - dust accumulation causes false runouts; wipe with dry microfiber every ~200h.
- **Print sheet warpage** - Prusa textured PEI sheets can warp slightly with heavy use; rotate orientation periodically.

**Voron (2.4, V0, Trident, V2)**
- **CAN bus connectors** - vibration loosens; check toolhead CAN connector monthly.
- **A/B belt tension parity** - A and B belts on CoreXY *must* match within a few Hz of each other (use phone tuner app, target 110 Hz with stock belts). Mismatched = skew issues.
- **Gantry squaring / racking** - recheck quarterly; loose belt = racked gantry.
- **Screws-to-belt skew calibration** - Klipper has `SKEW_PROFILE` for measured skew; print a skew calibration cube and apply correction.
- **TAP probe calibration** (if equipped) - recheck after toolhead changes.

**Creality (Ender 3 family, K1, K1C, K2 Plus)**
- **Ender 3 family eccentric nut adjustment** - POM V-wheels ride in slot extrusion via eccentric nuts. Adjust until wheel just spins under finger pressure but bed/gantry can't be wiggled by hand. Re-check monthly.
- **POM wheel wear** - replace if you see flat spots or grooves; symptoms are stuttery moves and ghosting.
- **K1 / K1C silicone sock** - falls off occasionally and gets cooked into a mess. Check before each print.
- **K1 / K1C carbon rods** - sparingly lubricate per Creality recommendation.
- **K2 Plus AI camera** - clean lens monthly; AI defect detection accuracy depends on clean optics.

**Anycubic (Kobra 2 family, Photon Mono X, Kobra S1)**
- **Auto-leveling sensor (LeviQ)** - clean nozzle before each level; sensor measures from the nozzle tip, so plastic snot throws results.
- **Leveling springs** (older Kobra) - replace if compressed/sagged.
- **Kobra S1 ACE Pro dryer** - internal desiccant rolls need replacement/regeneration; mirror to AMS workflow.

**Elegoo (Neptune 4, Centauri Carbon, Saturn for resin)**
- **Centauri Carbon** - quick-swap hotend like Bambu; automatic bed leveling.
- **Neptune 4 family** - Klipper-based; same input-shaping and PID tuning workflow as Voron.

---

## Quick reference card

**RH targets:** <15% gold, <20% fine, >30% degrading, >50% damaging.

**Drying defaults** (verify chamber temp):
PLA 45 °C/6h · PETG 65 °C/5h · ABS 70 °C/5h · Nylon 80 °C/12h · TPU 50 °C/6h · PC 80 °C/8h · PVA 45 °C/8h.

**Wet-filament tell:** popping at nozzle → dry the spool before troubleshooting anything else.

**Lubricant:** Super Lube 21030 on linear rails. **Never** WD-40, Vaseline, white lithium on plastics.

**Bed cleaner:** smooth PEI → IPA; textured PEI → dish soap + water; glass → Windex or IPA.

**Abrasive filament:** hardened steel nozzle minimum; all-metal heatbreak if also high-temp.

**Hot-tighten the nozzle** on every nozzle change. Use two wrenches.

**Calibrate hygrometers** with Boveda salt packs before trusting them.

---

## Sources

- Manufacturer drying guides: Polymaker PolyDryer manual; Bambu Lab Wiki (filament drying on X1/P1/H2 heatbed); Prusament material data sheets; ColorFabb material guides; Hatchbox storage recommendations.
- Dryer comparisons: Sovol 2025 dryer guide; All3DP 2024–2025 dryer roundups; CNC Kitchen filament-drying tests; community comparisons on r/3Dprinting and r/voroncorexy.
- Maintenance and defect diagnosis: Teaching Tech (calibration guides), CNC Kitchen (mechanical testing), Thomas Sanladerer (nozzle wear), Prusa blog (printer maintenance), Bambu Lab Wiki, Voron documentation (V2.4/Trident manuals), Creality wiki.
- Lubrication consensus: Voron community wiki, BIQU/Bondtech docs, Bambu official maintenance guide. WD-40/Vaseline anti-recommendations are universal across hobby and industrial sources.
- Hygrometer calibration: Boveda 75% RH One-Step Calibration Kit instructions; cigar-humidor and reptile-keeping communities (the same salt-pack method).
