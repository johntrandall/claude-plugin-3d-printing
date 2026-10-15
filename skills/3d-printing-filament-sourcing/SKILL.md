---
name: 3d-printing-filament-sourcing
description: Where to buy 1.75mm PLA/PETG/TPU (Bambu A1-relevant), vendor catalog, comparison-shopping procedure (per-spool landed cost), sale cycles, and Amazon-counterfeit warnings. Auto-invoke when buying filament, comparing prices, deciding which brand/spool format to order, or planning bulk purchases.
last_refreshed: 2026-10-15
printer_specific: [bambu-a1]
---

# Filament Sourcing: Bambu Lab A1 (1.75mm PLA / PETG / TPU)

This is the **purchasing companion** to `3d-printing-filaments` (material reference) and `3d-printing-storage-and-maintenance` (post-purchase care). Where to buy, how to comparison-shop, and what to watch out for.

**Scope assumption:** Bambu Lab A1 (open-frame) with AMS Lite. That constrains the universe to **PLA, PETG, and TPU 95A+**. ABS / ASA / Nylon / PC are out of scope - if a user asks for those, the answer is "the A1 can't print this; use PETG-CF or a different printer." Don't waste research budget on those families.

Prices are US dollars **as of June 2026** (Observed). This plugin is not affiliated with Bambu Lab or any vendor named here. Filament pricing moves often - re-check before committing. Vendor policies (refill programs, tolerance specs, free-shipping thresholds) are **Verified** when the vendor publishes them on a permanent page; treat unsourced policy claims as **Inferred**.

---

## 1. Decision Tree (Read This First)

```
What does the user want?
│
├── "Fill the AMS with 4 workhorse colors of PLA"
│       → Bambu PLA Basic 4-pack with-spool ($80-92) OR
│         Bambu PLA Basic 4-pack refill + 1 spool ($72-80) OR
│         Polymaker PolyLite/PolyTerra 4-pack ($72-84) - section 5.1
│
├── "One spool of basic PLA, fast"
│       → Amazon Overture or Hatchbox brand storefront (~$15-18 + Prime) - section 5.2
│       → Or Microcenter Inland if local pickup ($13-15) - section 5.2
│
├── "One spool of PETG to try"
│       → Polymaker direct (PolyLite PETG $19.99 + free ship) - section 5.3
│       → Or Bambu PETG HF if AMS use is primary
│
├── "TPU for a flexible part"
│       → Bambu TPU for AMS 95A - only A1-safe TPU path (section 5.4)
│       → Avoid: TPU 85A and softer; AMS Lite will jam
│
├── "Fun matte / silk / dual color"
│       → Bambu PLA Matte (broadest palette, AMS-native)
│       → Polymaker PolyTerra Matte (eco messaging, cardboard spool)
│
├── "Cheapest workhorse $/kg, bulk"
│       → Microcenter Inland in-store ($12-14/kg)
│       → Push Plastic direct bulk ($14-18/kg @ 5+ rolls)
│       → Hatchbox Amazon bundle when on Prime Day
│
├── "Food safe"
│       → STOP. See `3d-printing-filaments` §"Food contact". No FDM filament
│         is truly food-safe. Suggest food-safe silicone coating or buy a
│         silicone mold instead.
│
├── "ABS to repair Lego / something tough"
│       → STOP. A1 can't print ABS (open frame, no enclosure). Offer:
│         PETG-CF for stiffness, or send to a Bambu X1C / makerspace.
│
└── "Carbon fiber"
        → A1 supports Bambu PLA-CF / PETG-CF (needs hardened nozzle -
          confirm A1 has one before recommending; stock A1 ships with
          stainless, not hardened-for-abrasives)
```

---

## 2. Vendor Catalog (US-focused)

Organized by class. Star (★) = "default pick" for the listed material on an A1.

### 2.1 House-brand / manufacturer-direct

#### ★ Bambu Lab Store: `us.store.bambulab.com`

**Catalog scope (A1-relevant):** PLA Basic, PLA Matte, PLA Silk+, PLA-CF, PLA Galaxy, PLA Marble, PETG HF, PETG-CF, PETG Translucent, TPU for AMS 95A, TPU 95A HF. Bambu does NOT sell ABS-replacement materials targeted at the A1 (they assume X1/P1 for those).

**Typical $/kg (Observed 2026-06):**
- PLA Basic with spool: $22.99
- PLA Basic refill (no spool): $19.99 - designed to reuse the cardboard spool
- PLA Matte: $24.99 with spool
- PETG HF: $24.99 with spool / $21.99 refill
- TPU for AMS 95A: $34.99
- 4-roll bulk PLA Basic: typically $80-92 (saves ~$8-12 vs single-spool)

**Shipping:** Free over $89. Below $89, flat ~$8 ground. Remote states (HI, AK, PR) need $199 for free shipping. Ships from US warehouse - usually 2-4 day delivery to the US East Coast. (Verified from product pages.)

**Sale cadence:**
- **Black Friday / Cyber Monday** - biggest drop of year, 20-30% off filament + bundle promos (Observed pattern 2023-2025)
- **Summer Sale** (June-July) - filament-bulk-sale page goes live, 10-15% off
- **"Buy 4 refills get a free spool"** - runs intermittently
- **New printer launch** - adjacent filament discounts (e.g., H2D launch)
- **Newsletter signup** - occasional $5-10 off coupon

**AMS spool format:** Cardboard (refill) + plastic reusable spool ecosystem. **This is the gold standard for AMS Lite compatibility** - RFID chip in spool, perfect dimensions, no rolling-resistance issues.

**Recycled / refill program:** Yes - refill packs explicitly designed to reuse the Bambu spool. RFID chip is on the refill, so AMS still auto-detects material.

**Why pick them:** Default for A1 - most predictable AMS behavior, RFID auto-detect, fastest spool changes. **First-choice for AMS-resident colors.**

---

#### Polymaker: `us.polymaker.com` (redirects to `shop.polymaker.com`)

**Catalog scope (A1-relevant):**
- **PolyTerra PLA** - matte, mineral-loaded, cardboard spool, sustainability messaging
- **PolyLite PLA** - basic PLA, formerly $19.99, broad color range
- **PolyLite PLA Pro** ($22.99) - tougher PLA+
- **Polymaker PETG (new formula)** - $19.99
- **PolyMax PLA** - high-impact engineering PLA
- **PolyFlex TPU95** - flexible

**Typical $/kg (Observed 2026-06):**
- Panchroma Matte PLA: $19.99
- PolyLite PLA Pro: $22.99
- Polymaker PETG: $19.99
- Panchroma CoPE: $19.99
- Refill spools: ~$2-4 less than with-spool versions

**Shipping:** **FREE SHIPPING ON ALL ORDERS** (Verified site banner 2026-06-07). This makes single-spool orders extremely competitive vs Bambu (where shipping kicks in below $89).

**Sale cadence:**
- Black Friday - usually 15-25% off site-wide
- New product launches - early-bird discount
- Newsletter signup - typically 10% off first order

**AMS spool format:** **Mixed and important.** PolyTerra ships on a **cardboard spool**. Cardboard spools can shed dust into the AMS - community workarounds include (a) printing the "Polymaker Cardboard Spool Adapter" from Printables (model #575220 / #542307), (b) wrapping spool edges in electrical tape, or (c) transferring filament to a reusable Bambu spool. Polymaker now sells **refill** versions (since ~2025) for several lines, intended for a Bambu-spool-style master spool - this is the cleanest AMS path.

**Recycled / refill program:** Yes - Polymaker switched all products to 100% recycled spools (per their 2022 announcement, still in effect). Refill program rolled out for major PLA/PETG SKUs. PolyTerra has a tree-planting commitment per spool.

**Why pick them:** Best alternative to Bambu when you want a slightly different palette (especially matte PLA), eco messaging, or free shipping on a small order. **First-choice for one-off PLA color, single PETG spool.**

---

#### Prusament (via Printed Solid: US distributor): `printedsolid.com`

**Catalog scope (A1-relevant):** Prusament PLA, Prusament PETG, Prusament PVB (drop-not-supported on A1 - skip). Larger 2kg spools for power users.

**Typical $/kg (Observed 2026-06 at Printed Solid):**
- Prusament PLA / PETG 1kg: $35.99
- Prusament "Made in USA" refill (no spool): $26.99
- 2kg spools: $49.99 ($24.99/kg - best per-kg deal in the Prusament line)

**Tolerance spec:** ±0.02mm diameter (Verified - Prusa publishes this). Best tolerance in this catalog. Matters most for vase mode, transparents, and first-layer-critical functional prints.

**Shipping:** Wilmington, DE - fast to the US Northeast (often next-day ground). Local pickup available. Free shipping threshold ~$50-75 (Inferred from typical small-shop policy; verify at checkout).

**Sale cadence:** Modest. Occasional Prusament promo windows. Printed Solid newsletter sometimes runs 10% off.

**AMS spool format:** Prusament cardboard spool, 1.75mm. Fits AMS Lite but watch for cardboard dust (same advisory as PolyTerra - use adapter or transfer to reusable spool). RFID is Prusa-format, NOT Bambu - AMS won't auto-detect material; you set it manually in Bambu Studio.

**Recycled / refill program:** "Made in USA" Prusament refills exist (intended for the Prusa MK4S filament holder, but reusable on Bambu spools too).

**Why pick them:** **Tightest tolerance** filament in the US channel. Pick when first-layer perfection or transparents matter. Not the everyday-AMS default - too pricey for a workhorse spool.

---

#### Proto-Pasta: `proto-pasta.com`

**Catalog scope (A1-relevant):** HTPLA (high-temp PLA, anneal to make heat-tolerant), conductive PLA, magnetic iron PLA, glow-in-the-dark PLA, color-shifting PLA. Specialty only - they don't try to compete on workhorse PLA.

**Typical $/kg (Observed pattern 2025-2026):** $35-55 for HTPLA, $50-75 for conductive/magnetic. Premium tier.

**Shipping:** US-based (Vancouver, WA). Standard ground; flat fee typical, no aggressive free-shipping threshold.

**AMS spool format:** Plastic reusable spool (older runs may have been cardboard - verify). Magnetic and metal-fill require a **hardened nozzle** - A1 stock nozzle is stainless, not hardened. Wear-out in tens of hours. Do not recommend metal-fill to a stock A1 without warning.

**Why pick them:** Specialty experiments. Glow-PLA for a kid's project. Magnetic iron for a refrigerator magnet. **Not for everyday printing.**

---

#### Atomic Filament: `atomicfilament.com`

**Catalog scope (A1-relevant):** US-made premium PLA and PETG. Limited but high-quality colorways. No TPU.

**Typical $/kg:** $28-38/kg PLA, $30-40 PETG (Observed pattern).

**Shipping:** US-made, ships domestically. Standard ground.

**AMS spool format:** Plastic spool, standard dimensions - AMS Lite compatible.

**Why pick them:** When user wants **US-made premium** and is willing to pay a small premium over Bambu/Polymaker. Niche pick.

---

#### Push Plastic: `pushplastic.com`

**Catalog scope (A1-relevant):** US-made bulk PLA and PETG. Sold in 1kg, but the value tier is 5kg+ bulk packs.

**Typical $/kg:** $14-22 at 1kg, drops to $14-16/kg in 5-roll bulk (Observed pattern).

**Shipping:** Ships from Arkansas. Flat-rate or free-over-threshold (varies).

**AMS spool format:** Plastic spool, standard 200mm - AMS Lite compatible.

**Why pick them:** **Bulk workhorse PLA.** If user wants 10kg of "any white PLA" for a print farm or large project, this is the cost-effective domestic-source answer.

---

### 2.2 Resellers / multi-brand

#### MatterHackers: `matterhackers.com`

**Catalog scope (A1-relevant):** Build Series (house brand budget - PLA, PETG, ABS, TPU), Pro Series (premium house brand), MatterHackers brand specialty, plus resold Bambu, Polymaker, Prusament, eSun, Hatchbox, Polymaker, Proto-Pasta.

**Typical $/kg (Observed 2026-06):**
- Build Series PLA: ~$20-24
- Build Series PETG: $19.31 to $38.34 (color/promo dependent)
- TPU: $50-115 (premium tier - note this is higher than Bambu TPU)
- Pro Series: $30-45

**Shipping:** Free over $35 (Verified site policy as of 2026-06-07). Excellent threshold - pretty much any 2-spool order ships free.

**Sale cadence:** Constant rotation. "Filament on sale" category always has 10-20+ items. Pre-Black Friday, Black Friday, Cyber Monday, Christmas, Memorial Day, Labor Day, October "Make Month."

**Price-match policy:** They have one but it's manual and slow - call/email support with the competitor link. (Inferred from community reports; verify if pursuing.)

**Refill program:** MH Refill is a thing - they list 240+ "refill" SKUs in the filament category. Functions like the Bambu/Polymaker refill - cardboard inner core, reuse a master spool.

**Why pick them:** **Broadest one-stop catalog** + reliable free-shipping threshold. Pick when consolidating an order across brands (e.g., 1 Bambu + 1 Polymaker + 1 specialty would hit $35+ for free shipping and avoid 3 separate shipping fees).

---

#### Printed Solid: `printedsolid.com`

Covered above as Prusament US distributor. They also sell Polymaker, Bambu, eSun, Atomic, and others. Small-shop quality control. Wilmington, DE = excellent shipping speed to the US Northeast.

---

#### Filaments.ca / 3DJake (EU / Canada: slow shipping to US)

**Skip unless niche product not available US-side.** Customs + 2-4 week shipping makes these unattractive for a US buyer.

---

### 2.3 Amazon channel (handle honestly)

Brands sold via Amazon with brand-owned storefronts: Hatchbox, Overture, eSun, Sunlu, Inland (Microcenter cross-listing), Polymaker (official storefront), Bambu (official storefront).

**Typical $/kg (Observed 2026-06):**
- Hatchbox PLA: $18-22
- Overture PLA: $15-20 (often cheapest fast-Prime option)
- eSun PLA+: $18-22
- Sunlu PLA: $14-20

**Pros:**
- Prime shipping (1-2 day) - best for "I need filament now"
- Easy returns - beats every direct vendor's return policy
- Frequent lightning deals + Prime Day discounts
- CamelCamelCamel price history available

**Cons (these are real, not theoretical):**
- **Counterfeit / commingled inventory.** Amazon mixes stock from multiple sellers under one ASIN - even buying "from Sunlu storefront" can ship a counterfeit spool because of FBA commingling. (Sources: r/3Dprinting "Do not purchase Sunlu PLA" thread, SUNLU's own "Avoid Fake SUNLU Stores" advisory page on store.sunlu.com, multiple community reports through 2025.)
- Listings disappear / change ASIN - link rot on price-tracking.
- Inconsistent batches - fine 6 months ago might be different now.
- Color match across spools is unreliable batch-to-batch.

**Rule of thumb for Amazon filament:**
1. **Only buy from brand-owned storefronts.** Hatchbox: "Sold by HATCHBOX 3D Filaments." Bambu: "Sold by Bambu Lab." Polymaker: "Sold by Polymaker." If "Sold by [random Chinese-sounding name]" - pass.
2. **Avoid commingled-FBA risk by checking the seller AND fulfillment.** "Sold by Brand, Shipped by Amazon" can still be commingled. Brand-direct "Sold and shipped by Brand" is safer.
3. **For Sunlu specifically** - buy from store.sunlu.com direct if at all possible. The counterfeit problem is worst with Sunlu (highest community-reported volume).
4. **Don't trust review counts.** Many high-review Amazon filament listings are review-merged across products.

---

### 2.4 Specialty / one-offs

#### AliExpress

Bambu-style spools cheaper but slow shipping (3-6 weeks), customs/tariff risk, no warranty path. Skip unless deliberately experimenting with no-name PLA. Don't recommend for production work.

#### Microcenter (in-store + online): `microcenter.com`

**Inland** is Microcenter's house brand. Manufactured by overseas suppliers but quality is consistently rated near the top of "budget PLA" tier.

**Typical $/kg (Observed 2026-06):**
- Inland PLA 1kg: $12-15 in-store (the loss-leader - Microcenter uses cheap filament to drive foot traffic)
- Inland PLA+ 1kg: $15-18
- Tolerance: ±0.03mm (Verified per Inland product spec)

**Spool format:** Cardboard 1kg (Verified - Microcenter PLA+ spec page lists "1kg Cardboard Spool"). Same AMS-Lite advisory as Polymaker PolyTerra - works but watch for cardboard dust.

**Why pick them:** **Best $/kg for workhorse PLA if a Micro Center is local.** If the nearest store is a long drive away it is not an everyday source, and Amazon Overture is more practical. Mention only if the user is already going to a Micro Center for other reasons.

#### Local 3D-printer shops

Rare to be price-competitive, but useful for "I need it today and don't want to drive to a big-box store." Check what a nearby makerspace or local printer shop stocks.

---

## 3. Price Comparison Procedure (Operational)

When user asks "where should I buy X?":

### Step 1: Normalize the ask

Capture three variables before doing any pricing:

| Variable | Question | Typical answers |
|---|---|---|
| **Quantity** | How many spools? | 1 (sample), 4 (fill AMS), 10+ (bulk) |
| **Color tolerance** | Any [color]? Specific Pantone? Matte vs glossy? | "Any red" → flexible; "match THIS red" → narrow |
| **Urgency** | Prime tomorrow? OK to wait? | "Today" → Amazon; "this week" → any direct vendor |

A spool of "any white PLA, no rush" is a totally different question than "PolyTerra Banana Yellow matte, urgent."

### Step 2: Decide candidate vendors

Heuristic (3-5 candidates at most - don't burn tokens on 10 quotes):

| Pattern | Candidates |
|---|---|
| 4 spools to fill AMS, basic colors | Bambu direct, Polymaker direct, MatterHackers Build Series |
| 1 spool, fast | Amazon Hatchbox/Overture, Polymaker direct (free ship) |
| 1 spool of PETG | Polymaker direct, Bambu direct |
| 1 spool of TPU | Bambu direct (only safe AMS-Lite path) |
| Bulk workhorse | Microcenter (if local), Push Plastic direct, Amazon Hatchbox bundle |
| Specialty (glow, magnetic) | Proto-Pasta direct |
| Tight tolerance need | Printed Solid (Prusament) |
| Eco / refill priority | Polymaker direct (PolyTerra) or Bambu refill packs |

### Step 3: Pull current prices

| Vendor type | Tool |
|---|---|
| Bambu, Polymaker, Printed Solid, Atomic, Push Plastic, Proto-Pasta direct | Fetch the collection or product page |
| MatterHackers | Fetch the product search; they have many SKUs so be specific |
| Amazon | Web search for current price + Prime status; fetch the product page only if a specific ASIN is known. Cross-reference with CamelCamelCamel: `https://camelcamelcamel.com/product/<ASIN>` |
| Deal aggregators | Web search for: "site:reddit.com/r/3Dprintingdeals [brand] [year]" or "site:3dprintingdeals.com" or "site:slickdeals.net 3d printing filament" |

Size the effort to the purchase (under $30 = one search; $30-200 = focused comparison; $200+ = full table).

### Step 4 - Payment, address and tax

Use whatever payment method and ship-to address the user prefers, and state the sales tax rate for their state (the example table below uses 6.625 percent). For amounts over $50, or a new brand or material the user has not tried, confirm the choice with the user before ordering.

### Step 5: Compute total-landed-cost

The #1 mistake: comparing $/kg before shipping. **Always show landed total.**

Comparison table format:

| Vendor | SKU | Qty | Unit | Subtotal | Shipping | Tax (example 6.625%) | **Total** | $/kg | ETA |
|---|---|---|---|---|---|---|---|---|---|
| Bambu direct | PLA Basic White refill | 1 | $19.99 | $19.99 | $8.00 | $1.86 | **$29.85** | $29.85 | 3 day |
| Polymaker direct | PolyLite PLA White | 1 | $19.99 | $19.99 | FREE | $1.32 | **$21.31** | $21.31 | 5 day |
| Amazon Overture | White PLA 1.75 | 1 | $17.99 | $17.99 | FREE Prime | $1.19 | **$19.18** | $19.18 | next day |

A single spool from Bambu is almost never cost-optimal vs Polymaker/Amazon - Bambu's $89 free-ship threshold kills small orders. **Bambu wins when the order is 4+ spools.** Show this math, don't assume.

### Step 6: Non-price signals

After the table, surface these qualitative factors:

| Factor | Why it matters | Where it lives |
|---|---|---|
| **Spool format** | Cardboard sheds dust in AMS Lite; plastic reusable spools are cleaner | `3d-printing-filaments` AMS notes |
| **Tolerance spec** | ±0.02 (Prusament) > ±0.03 (Inland) > ±0.05 (typical) - matters for first-layer-critical prints | Vendor product pages |
| **Recycled content / refill** | Polymaker refills + 100% recycled spools; Bambu refill packs. Matters if the user cares about waste | `3d-printing-recycling-and-waste` |
| **Brand reputation** | Community quality consensus | `3d-printing-filaments` §brand notes |
| **AMS RFID** | Bambu RFID auto-detects material; Polymaker/Prusament/Inland do not - manual select in Studio | Vendor-specific |

### Step 7 - Decide on a confirmation level

- **Total < $50**: present the recommendation with the table, suggest the winner, ask one confirm question
- **Total $50-200**: offer 2-3 options (winner, alternative, "wait for a sale")
- **Total > $200** or a new brand: show the full table and get an explicit go-ahead

### Step 8 - Log the order

If the user keeps a filament log, append: date, vendor, SKU, color, quantity, landed $/kg, spool format and expected use. When a spool arrives, record it as on hand; when it is used up, record the date so spool lifetime and burn rate can be computed. Keep receipts with the log.

---

## 4. Common Buying Patterns (Cheat Sheet)

### 4.1 "I need 4 spools of basic PLA to fill the AMS"

**Recommend:** Bambu PLA Basic 4-pack with-spool OR Polymaker PolyLite 4-pack.

| Option | Approx total | $/kg | Why |
|---|---|---|---|
| Bambu 4-pack with-spool | ~$80-92 free ship | $20-23 | AMS RFID auto-detect, cleanest spool format |
| Bambu refill 4-pack + 1 reusable spool (one-time) | ~$72-80 + spool | $18-20 ongoing | Best long-run if reusing the master spool |
| Polymaker PolyLite 4-pack | ~$72-84 free ship | $18-21 | Free shipping no threshold |
| MatterHackers Build Series 4-pack | varies, free ship over $35 | $18-22 | Consolidate if also buying tools |

**Default pick:** Bambu refill 4-pack + reusable spool - best $/kg over a year of printing, native AMS, cardboard waste minimized.

### 4.2 "One spool of black PETG to test"

**Recommend:** Polymaker PETG direct.

- Polymaker PETG: $19.99 + FREE SHIP = **$19.99 + tax** total
- Bambu PETG HF single: $24.99 + $8 ship = $32.99 + tax (kills the single-spool case)
- Amazon Overture PETG: ~$18 Prime - fast and cheap but lower-tier brand reputation

Polymaker wins on landed cost + brand reputation.

### 4.3 "TPU for a phone case"

**Recommend:** Bambu TPU for AMS 95A.

The A1 + AMS Lite is **fragile for TPU.** AMS Lite has limited tolerance for very soft TPU - anything below 95A shore hardness risks jams in the AMS rollers. Even 95A is borderline.

- Bambu TPU for AMS 95A: $34.99 - formulated specifically for AMS feeding, **only filament I'd recommend through AMS Lite**
- Bambu TPU 95A HF: $32.99 - high-flow variant
- Direct-feed from spool (bypass AMS): opens up Polymaker PolyFlex 95A, eSun TPU 95A, others. But user loses AMS multi-material.

If user insists on TPU through AMS, Bambu's AMS-specific TPU is the only safe-default answer.

### 4.4 "I broke a Lego: need ABS to repair it"

**STOP.** A1 cannot print ABS - open frame, no enclosure, parts will warp and delaminate. Options:

1. PETG-CF - stiffer than PETG, A1 supports it with a hardened nozzle. Closest the A1 can come.
2. Print on someone else's enclosed printer - X1C, K1 family, or a local makerspace
3. Send the STL to a print service (CraftCloud, JLCPCB 3D)

Do NOT recommend buying ABS for an A1 - it'll print badly and frustrate the user.

### 4.5 "I want a fun color"

**Recommend (in order):**
1. **Bambu PLA Matte** - broadest matte palette, native AMS, $24.99 with spool
2. **Bambu PLA Silk Dual Color / Tri Color** - multicolor-in-one-spool, $30-35
3. **Polymaker PolyTerra Matte** - eco angle, $19.99, but cardboard spool advisory
4. **Bambu PLA Galaxy / Marble** - sparkle/marble effects
5. **Proto-Pasta HTPLA color-shifting** - premium, niche

### 4.6 "Cheapest workhorse PLA per kg"

| Source | $/kg | Notes |
|---|---|---|
| Micro Center Inland (in-store) | $12-15 | If a Micro Center is local |
| Push Plastic 5-roll bulk | $14-16 | US-made, ships from Arkansas |
| Hatchbox Amazon 5-roll bundle on Prime Day | $14-18 | Time-sensitive |
| Amazon Overture 1-spool | $15-20 | Best fast-default |

**Default pick when no Micro Center is nearby:** Amazon Overture single spool or Push Plastic bulk if buying 5+.

### 4.7 "I need food safe"

**STOP.** Reference `3d-printing-filaments` food-safety section. The short answer: no FDM filament is truly food-safe because of layer voids that harbor bacteria, dye toxicity uncertainty, and uncertified additives. Options:

1. Print the *shape* in PETG, then food-safe-coat (Smooth-On XTC-3D or food-safe epoxy)
2. Print a mold in PETG, cast in food-safe silicone
3. Buy a silicone version of whatever the user is making

Do not recommend "food safe PLA" - the label is mostly marketing.

---

## 5. Sale Cycles + Deal Sources

### 5.1 When to wait vs buy now

| Window | Vendors that participate | Typical discount | Wait if... |
|---|---|---|---|
| **Black Friday / Cyber Monday** (late Nov) | Bambu, Polymaker, MatterHackers, Amazon brands | 15-30% off, bundle bonuses | Order is non-urgent and >$50 |
| **Prime Day** (mid-July + Oct prime-day) | Amazon brands (Sunlu, Overture, Hatchbox, eSun) - Bambu/Polymaker storefronts also participate | 10-25% off | Buying Amazon-channel anyway |
| **Manufacturer anniversaries** (Polymaker Birthday, Bambu launch events) | Bambu, Polymaker direct | 10-20% off | Subscribed to their newsletter |
| **Newsletter signup** | Polymaker, MatterHackers, Bambu (occasionally) | 5-15% off first order | First-time buyer |
| **Multi-spool bundles** (year-round) | Most direct vendors | 10-15% per-kg savings | Buying ≥4 spools anyway |
| **Year-end clearance** (Jan) | MatterHackers especially | Up to 50% on discontinued colors | OK with off-palette colors |

**Don't wait when:** print is blocking other work, or savings <$20 absolute. Time-to-print > savings most of the time.

### 5.2 Deal-watching sources (still active 2026)

- **r/3Dprintingdeals** (Reddit) - community-curated; check before any non-urgent purchase
- **3DPrintingDeals.com** - aggregator; less reliable signal but catches some vendor-direct codes
- **Slickdeals "3D printing" tag** - `slickdeals.net/computer-deals/3d-printer/` - broader and Amazon-heavy
- **CamelCamelCamel** - `camelcamelcamel.com` - Amazon price history; essential for spotting fake "sale" prices that just returned to baseline
- **Polymaker, Bambu, MatterHackers newsletters** - direct-source promo codes
- **Honey / Rakuten** - auto-coupon plugins; lightweight but occasionally produce a working code at Bambu/Polymaker direct

---

## 6. Pitfalls + Honest Warnings

### 6.1 Amazon counterfeit risk

Sunlu has the worst public counterfeit problem - Sunlu themselves publish a "Avoid Fake SUNLU Stores" advisory on `store.sunlu.com/pages/sunlu-official-online-store-statement` listing their verified domains. Polymaker and Bambu have less but non-zero counterfeit risk on Amazon. Rule: **brand-owned storefronts only**, prefer brand-direct shipping where possible, and **prefer the brand's own website over Amazon for any non-urgent buy** unless the Amazon price is materially better after factoring in shipping.

### 6.2 Fake "sale" prices

Common Amazon pattern: list price quietly rises 30%, then "sale" returns to baseline. CamelCamelCamel reveals this - always check price history before buying anything claimed-on-sale on Amazon.

### 6.3 TPU shipping hazmat

Mostly a non-issue for 1kg hobby quantities, but some couriers refuse certain TPU formulations in bulk. Hazmat surcharges are rare for filament. **Filament dryers shipped with batteries** (e.g., portable dryers like the Sunlu S2/S4) DO have lithium-shipping rules and can ship slower / require ground.

### 6.4 International shipping

Polymaker EU site, AliExpress - customs + 2-4 week ETA. Skip for time-sensitive work. Only worth it for SKUs not available US-side.

### 6.5 Filament weight ≠ spool weight

A "1kg spool" is 1kg of filament + 200-300g of plastic/cardboard spool = 1.2-1.3kg shipped. This affects flat-rate shipping cost from vendors like Push Plastic / Atomic when you're calculating bulk economics. For Bambu refills (no plastic spool), shipped weight is ~1.1kg - modestly cheaper to ship.

### 6.6 Cardboard spools + AMS Lite

Polymaker PolyTerra, Inland, Prusament all ship cardboard. They work in AMS Lite **but**:
- Cardboard dust can deposit in the AMS over time
- Cardboard edges can fray and cause rolling resistance
- **Mitigations:** (a) Bambu AMS adapter print (Printables #575220), (b) electrical tape around spool edges, (c) transfer filament to a reusable Bambu spool
- Refill versions (filament-only, no spool) sidestep this entirely if you have a reusable master spool

### 6.7 RFID auto-detect is Bambu-only

Bambu spools have RFID chips that AMS reads to auto-set material profile. Polymaker, Prusament, Inland, Amazon brands all require manual material selection in Bambu Studio. Not a deal-breaker - just one extra step per spool load.

### 6.8 Color batch consistency

Direct from manufacturer is more consistent batch-to-batch. Amazon channel can vary because of commingled FBA inventory. If color match across spools matters (large multi-spool print), buy all spools in one direct-vendor order.

### 6.9 Tolerance numbers are not all equal

±0.02 (Prusament Verified) > ±0.03 (Inland, many premium PLAs) > ±0.05 (typical budget). Matters for: vase mode, transparent prints, first-layer-critical functional parts. Doesn't matter for: most cosmetic / fit-tolerant work.

### 6.10 Drying state matters more than the price

A $30/kg PLA dried correctly outperforms a $15/kg PLA that's been sitting in a humid garage. Reference `3d-printing-storage-and-maintenance` - desiccant storage and pre-print drying are the single biggest quality lever, and they cost nothing once set up.

---

## 7. Integration with Other Skills

| When you... | Use... |
|---|---|
| Selecting which material for a part | `3d-printing-filaments` |
| Storing the spool when it arrives | `3d-printing-storage-and-maintenance` |
| Disposing of empty spools / scrap | `3d-printing-recycling-and-waste` |

---

## Refresh Notes

Last refreshed 2026-10-15 (prices still as of June 2026). Refresh triggers:
- **Quarterly** - pricing moves; reconfirm Bambu/Polymaker base prices
- **Pre-Black-Friday** (mid Nov) - verify sale dates and discount percentages
- **When a new vendor enters** the conversation (e.g., a new US-made manufacturer)
- **When a counterfeit-warning incident** is reported in r/3Dprinting (update §6.1)
- **If Bambu changes shipping threshold** (was $89 as of June 2026)

When refreshing, mark all prices as Observed with the new date, re-Verify any policy claims, and flag changes in a brief "Changes since last refresh" subsection.
