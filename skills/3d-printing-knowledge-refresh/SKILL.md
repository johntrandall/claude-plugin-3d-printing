---
name: 3d-printing-knowledge-refresh
description: Monthly refresh procedure for the five 3d-printing-* knowledge skills. Per-skill URL manifest, "scout for what's NEW in the industry" prompts, diff-edit pattern, and parallel-spawn procedure. Auto-invoke when any 3d-printing-* skill is >30 days stale, when the user asks to refresh 3d-printing knowledge, or when a scheduled refresh fires.
last_refreshed: 2026-10-15
---

# 3D Printing: Knowledge Refresh Procedure

The five `3d-printing-*` reference skills are a snapshot of the industry at a point in time. They go stale: vendors change prices and shipping policies, new filament chemistries enter the consumer market, AI mesh tools improve monthly, take-back programs come and go, and Bambu/Polymaker/Prusa ship hardware that shifts what's recommended.

This skill is the canonical procedure to refresh them. Use it monthly, or whenever a skill's `last_refreshed:` is more than 30 days old.

**Don't refresh blindly.** A skill that is technically 32 days old but covers material chemistry that doesn't change in months is fine. A skill covering "current AI mesh tools" or "current vendor prices" needs more attention. Each section of each skill has its own decay rate - pay attention to which sections are most likely drifting.

## Decision: refresh now, defer, or skip

Before spawning any subagent, ask:

1. **Has anything material happened since last refresh?** Scan the user's recent context for: "new Bambu printer announced," "PolyTerra changed shipping," "Hunyuan3D 4 dropped," "Prusament price increase," counterfeit complaints. If yes, refresh the affected skill specifically - don't run the full five.
2. **Is this a passive refresh tick or a real research need?** If a user is about to make a $200 filament purchase decision and the sourcing skill is 35 days old, refresh sourcing first, then proceed. If they're just asking about PLA properties, defer.
3. **Does the user want it now?** If they're mid-task, note the refresh as a follow-up for later rather than blocking their request.

## Per-skill refresh manifest

Each entry lists: what's likely to have drifted, the URLs to re-scrape, and the "scout for NEW" categories specific to that domain. URLs that 404 on refresh should be removed from the skill; don't keep dead references.

### `3d-printing-filaments`

**Likely drift:**
- New filament chemistries entering consumer market (PPS-CF appeared in 2025, PAHT-CF, recycled-blend variants)
- Bambu's official compatibility table for the A1
- Hardened nozzle / heat-creep workarounds becoming standard
- Brand-tier reputation (e.g. a brand goes downhill or a new premium player enters)

**URLs to fetch / re-verify:**
- https://bambulab.com/en-us/filament - current catalog
- https://bambulab.com/en-us/filament/printers/a1 - A1 compatibility matrix
- https://wiki.bambulab.com/en/filament-acc/filament - official guide
- https://us.polymaker.com - catalog and material spec pages
- https://www.prusa3d.com/category/prusament/ - Prusament additions
- https://www.matterhackers.com/c/3d-printer-filaments - broad market scan

**Scout for NEW (the unknown unknowns):**
- Any filament family not currently in the skill? (Sample list to challenge: PPS, PAHT, PPSU, PEKK, recycled-content PETG, biocomposite PHA, conductive variants, magnetic, color-changing thermochromic, UV-reactive, fiber-glass-reinforced PA)
- New TPU shore hardness brackets becoming common
- New abrasive composites requiring a hardened nozzle category
- Any "high-flow" or "high-speed" variant becoming the default (e.g. PETG HF)
- Material safety reclassifications (PFAS bans, new fume warnings)

**Use:** web search for "new FDM filament 2026" and "[new material name] consumer release"; fetch the vendor pages above.

---

### `3d-printing-filament-sourcing`

**Likely drift:** **High.** This skill ages fastest.
- Vendor prices (refresh every 30 days)
- Free-shipping thresholds
- Sale calendar - Black Friday/Prime Day/anniversary
- Counterfeit incidents on Amazon
- New vendors entering the US market
- Vendor shutting down (it happens - small shops disappear yearly)

**URLs to fetch / re-verify:**
- https://us.store.bambulab.com/products/pla-basic-refill - sample-price for PLA Basic
- https://us.store.bambulab.com/collections/3d-printer-filament - full Bambu catalog
- https://us.polymaker.com/collections/all-filaments - Polymaker catalog
- https://www.printedsolid.com/collections/prusament - Prusament pricing via Printed Solid
- https://www.matterhackers.com/c/3d-printer-filaments - MatterHackers catalog
- https://www.microcenter.com/search/search_results.aspx?Ntt=filament - Inland in-store pricing snapshot
- https://www.amazon.com/stores/Polymaker/page/... - Polymaker Amazon storefront (check for new third-party seller infiltration)
- https://www.reddit.com/r/3Dprintingdeals/top/?t=month - community-curated deals
- https://3dprintingdeals.com - aggregator
- Sunlu's own counterfeit-warning page: https://store.sunlu.com/pages/sunlu-official-online-store-statement

**Scout for NEW:**
- Any vendor running a permanent free-shipping policy (currently Polymaker)? Flag the shift.
- Has a vendor changed their AMS-Lite spool format? (Cardboard core adapters change - the Printables model numbers in the current skill may not be the latest.)
- New take-back / refill program (Bambu refillable, Polymaker PolyTerra, etc.)?
- Any vendor now requiring account/login to see pricing?
- New deal sites, new Reddit subs for deals, new Slickdeals tags?
- Has Bambu changed firmware in a way that affects third-party-filament use? (They've done this before.)

**Use:** fetch each URL; record current $/kg per representative SKU into the skill's pricing tables. Mark prices as **Observed today** with the date. Web-search "[vendor] shipping change 2026" and "Amazon filament counterfeit 2026."

---

### `3d-printing-storage-and-maintenance`

**Likely drift:** **Low to medium.** Material science doesn't change monthly, but the dryer/storage product ecosystem does.

**URLs to fetch / re-verify:**
- https://www.sunlu.com/collections/filament-dryer - current Sunlu dryer lineup
- https://www.eibos3d.com - EIBOS Cyclopes / Polyphemus updates
- https://us.polymaker.com/collections/polydryer - PolyDryer line
- https://wiki.bambulab.com - AMS HT / AMS 2 Pro behavior, in-printer drying
- https://www.printables.com/model/search?q=drybox - community DIY drybox designs
- Bambu A1 maintenance page: https://wiki.bambulab.com/en/a1/manual/maintenance

**Scout for NEW:**
- New dryer with higher maximum temp (the 80→90→100°C creep matters for nylon/PC)
- Dryers that support **printing-while-drying** (this was rare in 2024, common in 2025+)
- AMS firmware adding humidity-active drying (AMS Lite currently does not; AMS HT does)
- New A1-specific maintenance recall or firmware fix
- New "abrasive" detection - has the field added ruby/tungsten nozzle alternatives at consumer price?
- Common-wisdom corrections (e.g. "PLA dries at 50°C" was revised down for PLA+ variants)

**Use:** web search for "FDM dryer review 2026" and "Bambu A1 firmware maintenance change." Fetch the Bambu wiki maintenance page in case it has been restructured.

---

### `3d-printing-recycling-and-waste`

**Likely drift:** **High.** Take-back programs come and go yearly; greenwashing assessment can rot.

**URLs to fetch / re-verify:**
- Polymaker PolyTerra "plant a tree" page (verify program still active and check the metrics)
- https://www.terracycle.com - search "3D printing" / "filament"
- https://reflowfilament.com - Reflow recycled-content
- https://www.greengate3d.com - GreenGate3D status
- https://www.filamentive.com - Filamentive program
- https://www.matterhackers.com (Refill program page)
- https://www.printedsolid.com - refill spool offerings
- https://filabot.com - Filabot extruder line + current pricing
- https://3devo.com - Composer/Precision pricing
- https://www.protocycler.com - ProtoCycler current status (this one has been unreliable)

**Scout for NEW:**
- New take-back / mail-in program
- Existing program quietly discontinued (verify each before sending people there)
- New pellet-extrusion consumer printer (Mahor, Piocreat) that changes the home-recycling economics
- New refillable-spool standard from a major brand
- Updated PLA composting reality (industrial-facility availability changes regionally)
- New local drop-off options near the user (university makerspaces, public-library makerspaces, FabLabs)

**Use:** fetch each program URL and check the actual "currently accepting submissions" status (not just that the page loads). For each program: alive / dormant / dead - and update the skill. Web search for "3D printing filament take-back program 2026."

---

### `3d-printing-models-and-tools`

**Likely drift:** **Very high for AI tools. Medium for everything else.** AI mesh generation improves monthly.

**URLs to fetch / re-verify:**
- https://www.printables.com - sample browse + latest top-of-month
- https://makerworld.com - MakerWorld activity
- https://www.thingiverse.com - verify still alive (it limps along)
- https://cults3d.com - verify
- https://www.myminifactory.com - paid-minis market
- https://www.thangs.com - Thangs meta-search status
- https://www.tripo3d.ai - Tripo AI capability
- https://www.meshy.ai - Meshy AI capability
- https://www.csm.ai - CSM
- https://hyper3d.ai - Rodin
- https://hunyuan3d.tencent.com (or wherever Hunyuan3D's current home is)
- https://github.com/microsoft/TRELLIS - Trellis open-source status
- https://github.com/CadQuery/cadquery - CadQuery activity
- https://github.com/gumyr/build123d - build123d activity (newer CadQuery successor)
- https://github.com/SoftFever/OrcaSlicer - OrcaSlicer releases (the de facto OSS slicer as of 2026)
- https://github.com/prusa3d/PrusaSlicer - PrusaSlicer release cadence
- Bambu Studio release notes (whatever URL the wiki points to)

**Scout for NEW:**
- New AI mesh tool that's actually usable for printing (the bar: under 15 minutes of post-cleanup from prompt to printable)
- New AI image-to-3D that works on common hand-drawn sketches
- New CAD entrant or major release (OnShape, Fusion, Shapr3D, Plasticity)
- New Blender release with relevant 3D-print toolbox changes
- A slicer feature that changes the default recommendation (e.g. "OrcaSlicer added X, now best choice for use case Y")
- New file format gaining traction (3MF subtype, etc.)
- A model-sourcing site shutting down (Thingiverse has nearly died several times - verify it's still functional)
- New aggregator / meta-search

**Use:** web search for "best 3D model AI generation 2026" and "FDM slicer release 2026"; fetch each tool page; for the GitHub repos, check the latest release tag and the README's "what's new" section.

## The "what's NEW" scout (universal)

Across all five skills, run these scout queries with web search once per refresh, and propagate findings to the relevant skill:

1. **"What new 3D printing technology / filaments / tools were announced in the last 3 months that a consumer FDM hobbyist would care about?"** Look for things the current skills don't mention.
2. **"What are common 3D printing techniques in 2026 that were not common in 2024?"** Captures workflow drift (e.g. "input shaping at home became default with Bambu/Klipper").
3. **"What 3D printing vendor / service / program shut down in the last year?"** Captures the "dead reference" risk.
4. **"What new Bambu Lab printer or accessory was released that affects the A1 user's decisions?"** If the user has an A1, new sibling products (X1E, P2S, AMS HT-Lite, etc.) shift the upgrade conversation.

Each finding gets routed to the appropriate skill section. If it doesn't fit any existing section, that's a signal a new section (or a new skill) is needed - flag to the user, don't silently invent.

## Diff-edit, don't rewrite

When refreshing, read the existing skill first. Edit in place:
- **Updated** facts (price changed, URL moved) → Edit the line, preserve surrounding context, bump `last_refreshed:`.
- **New** facts (new product, new program) → Insert in the appropriate section. If no section fits, add one but match the surrounding style.
- **Removed** facts (vendor died, program dormant) → Delete the line or mark with a brief inline note like "*(Verified discontinued 2026-06)*" so future readers know why something's missing.
- **Unchanged** sections → Don't touch. Especially don't reformat for the sake of it; diff noise hides real changes.

Do NOT rewrite the whole skill. The original `name:` and `description:` fields are stable identifiers - change them only when the skill's actual scope changes, not as part of a refresh.

## Claim confidence during refresh

Maintain the Verified / Observed / Inferred discipline:

| Refresh source | Confidence tag |
|---|---|
| Official vendor product page, today | **Verified** for the stated fact (price, spec, policy) |
| Bambu wiki | **Verified** for the printer/AMS behavior described |
| Reddit, Hacker News, YouTube creator claims | **Observed** at best - say "community-reported" |
| Search-engine or AI research synthesis | **Inferred** unless backed by a Verified citation; treat as a research lead |

Never write a previously-Verified claim back as Inferred just because the URL temporarily 404'd - chase the new URL first. Verified claims should only become Inferred when the underlying source is genuinely gone.

## The parallel-spawn pattern

When more than one skill needs refresh, spawn one `general-purpose` subagent per skill, in parallel, each with a self-contained prompt:

> The skill at `${CLAUDE_PLUGIN_ROOT}/skills/<NAME>/SKILL.md` is N days stale. Read it. Open `${CLAUDE_PLUGIN_ROOT}/skills/3d-printing-knowledge-refresh/SKILL.md` for the per-skill URL manifest and the "scout for NEW" categories that apply to this skill. Fetch each listed URL. Run the relevant web searches. Diff-edit the skill - preserve unchanged sections, update changed facts, insert new findings, mark dead references. Tag updates with Verified / Observed / Inferred. Bump `last_refreshed:` to today. Return a short changelog of what you updated.

After all subagents return, aggregate the changelogs, summarize to the user, and commit with a single message attributing the refresh date (if the skills live in a git checkout you control).

## Reporting back

The refresh's final output to the user is a tight summary:

```
3D-printing knowledge refresh complete (2026-MM-DD)

filaments:        +1 PPS-CF section, updated Bambu A1 nozzle-temp ceiling
sourcing:         price refresh on 6 SKUs, Polymaker free-ship still active,
                  removed dead reference to [vendor X]
storage:          AMS HT firmware update added active drying - noted
recycling:        ProtoCycler discontinued - marked, added Voxelfill Labs
                  (new mail-in program)
models-and-tools: Hunyuan3D-5 released, updated capability assessment;
                  OrcaSlicer 2.4 default for non-Bambu printers

Committed: <SHA>
```

Don't dump full diffs into chat. The skills themselves are the artifact; the user reads diffs in git if they want them.

## Refresh cadence triggers

Auto-fire this skill when:
- Any of the five `3d-printing-*` skills has `last_refreshed:` more than 30 days old.
- User asks "refresh 3D printing knowledge" or similar.
- A scheduled monthly refresh fires (only if the user has set one up).
- A session reveals a fact that contradicts what a skill currently states (in that case, refresh only the affected skill immediately, don't wait for the cycle).

Do NOT auto-fire from within a tight loop, a shopping flow, or during an active print-troubleshooting session - refresh costs research-agent time and search calls; defer to after the user's current task is settled.
