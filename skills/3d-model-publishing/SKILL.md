---
name: 3d-model-publishing
type: procedure
description: "Publish a finished 3D model (STEP/STL/3MF) to model-sharing sites - Printables, MakerWorld, Thingiverse. Auto-invoke when the user says 'post this model', 'upload to Printables/MakerWorld/Thingiverse', 'share this print', or after a reverse-engineered replacement part is finished and the user wants it published. Covers the listing.md package format, per-site accounts and login handoff, upload flows, tagging, and licensing defaults."
tags: [3d-printing, publishing]
freshness:
  last_refreshed_at: 2026-10-15
  auto_refresh_cadence: quarterly
---

# 3D Model Publishing

Publish a finished model to 3D printing model sites with consistent copy, tags,
images, and license.

## 1. Prepare the listing package first

Before touching any site, assemble a `listing.md` in the model's project folder:

```markdown
# Listing copy for 3D printing sites
## Title           : "<Brand> <thing>: <OEM part number> Replacement" for repair parts
## Summary (short) : 1-2 lines
## Description     : what it replaces, compatible models, how it was made,
                      strength/design notes worth knowing
## Print settings  : material, infill, walls, layer height, orientation, supports
## Files           : STEP preferred + STL (upload both when the site allows)
## Tags            : see Tagging below
## Category        : closest to Home / Appliance / Replacement Parts
## License         : default CC BY (Creative Commons Attribution); ask the user before
                      choosing NC/ND variants
## Images (in order): hero first: printed part next to the original if it exists
```

Images: real photos of THE PRINT outperform everything - sites reward print
photos, and buyers want to see what the printed result looks like, not the OEM
part being replaced. Order: (1) the print installed/in use, (2) the print
alone from 2 angles, (3) print-vs-original comparison (label which is which),
(4) at most ONE OEM/reference photo, (5) render last. If print photos don't
exist yet, ask for them before publishing - a listing that is mostly OEM
photos misrepresents the model.

### Tagging

Include ALL of: brand names (every compatible brand - e.g. thermador, bosch,
gaggenau), the appliance type, the component words (drawer, rail, clip), the OEM
part number(s) - these are the highest-value search terms for repair parts -
plus "replacement part", "appliance repair", "spare part".

## 2. Accounts

Each site needs its own account (Printables uses a Prusa account, MakerWorld uses a Bambu Lab account, Thingiverse, Thangs, Cults3D and MyMiniFactory each have their own sign-up).

The agent must NOT create accounts or type credentials. If the user has no account on a site, prepare the sign-up details (a suggested username and a plus-address email alias if their mail provider supports one) and hand the actual sign-up and login to the user. Store the credentials in the user's password manager, never in the listing package or the conversation.

## 3. Login handoff

Preferred flow: **the user logs in, the agent drives the rest**.

1. Open the site in a browser tab the user is already signed in to (for example through a browser-automation extension that works in the user's own browser).
2. If logged out, ask the user to log in, and notify them if they may have stepped away.
3. After login, the agent completes the entire upload flow in that tab.

Do NOT paste passwords through browser-automation tools. For interactive sessions the user-login handoff is simpler and safer than any scripted login.

## 4. Per-site upload flow

All three follow the same shape: Create/Upload → files → images → title/
description → category → tags → print settings → license → publish.

- **Printables**: `+ Create` → Upload model. Accepts STEP + STL. Has explicit
  print-settings fields (nozzle, layer height, infill, supports) - fill them
  from listing.md. Category tree: Home → Kitchen (or Spare Parts).
- **MakerWorld**: Upload → 3D Model. Prefers 3MF with embedded print profile -
  uploading the STEP/STL works but consider slicing once in Bambu Studio and
  uploading the 3MF print profile alongside (MakerWorld rewards profiles).
  License picker on the right rail.
- **Thingiverse**: Create → Upload a Thing. STL only (no STEP) - upload STL,
  mention in the description that STEP lives on Printables.
- **MakerWorld gotcha**: the tag input accumulates synthetic keystrokes across
  Enter presses (every chip gets the whole buffer). Enter tags via JS instead:
  native value setter + dispatch 'input' + KeyboardEvent Enter per tag; delete
  bad chips by clicking `.tagItem-deleteIcon`. Verify chips with
  `.tagItem-content` textContent before publishing.

## 4.5 Registry of registries

The canonical map of 3D-model sites: what each is good for, both for SEARCHING
(when hunting for an existing model) and for PUBLISHING (when sharing one).
When sourcing a model, fan out across the meta-search engines FIRST, then hit
individual sites the metas don't index well. When publishing, work down the
publish column in priority order.

| Site | Search value | Publish value |
|------|--------------|---------------|
| **yeggi.com** | META-SEARCH - indexes most sites below; always start here | n/a (aggregator) |
| **stlfinder.com** | META-SEARCH - second sweep; catches some yeggi misses | n/a (aggregator) |
| **3dmdb.com** | META-SEARCH - third option; includes commercial CAD sites | n/a (aggregator) |
| **printables.com** | strong; quality models, good part-number search | #1 - best community, Prusameter rewards, accepts STEP |
| **makerworld.com** | strong; huge volume since 2023, Bambu-slicer integrated | #2 - biggest audience, rewards print profiles (3MF) |
| **thingiverse.com** | huge LEGACY archive - best for pre-2022 models | #3 - declining but still heavily searched; STL only |
| **thangs.com** | GEOMETRIC search (search by shape/mesh) - unique capability | #4 - free, indexes well |
| **cults3d.com** | good for artistic/commercial models | optional - free listings, large audience |
| **myminifactory.com** | curated, miniatures-heavy | optional - low repair-part traffic |
| **grabcad.com** | engineering CAD (STEP/native), industrial parts | niche - engineers only |
| **crealitycloud.com** | some unique uploads, weak search | skip - low traffic per model |
| **Google w/ part number** | for repair parts, searching the OEM part number directly often beats every model site | n/a |

Search procedure for a wanted model: (1) yeggi + stlfinder with descriptive
terms AND OEM part numbers, (2) thangs if you have similar geometry to match,
(3) printables/makerworld/thingiverse native search, (4) plain web search with
the part number + "stl". Verify visual match against photos before trusting a
hit - model titles lie (in one search, three "matching" appliance clips
were three different parts).

Reddit channels that drive repair-part traffic (read each community's posting
rules first): r/functionalprint (best fit), r/appliancerepair, r/3Dprinting.

After publishing each, record the live URLs at the bottom of `listing.md`.

## 5. Cross-linking and closeout

- Add each published URL to `listing.md` under a `## Published` section.
- If the part replaces an OEM part, the description should name every
  cross-reference number found (e.g. 00633652 / 00604665 / AP5953399 /
  PS10060851) - people search by whichever number their parts site showed them.
