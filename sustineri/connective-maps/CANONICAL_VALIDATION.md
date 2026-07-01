# ROOT / Canonical Validation — Connective Map Workflow

**Status:** PROVISIONAL — a canonical Sustineri brand workflow **does exist** in ROOT.
**Validated by:** Claude, on behalf of Angeline Stephens (Angie@sustinericonsulting.com)
**ROOT reachable this session:** Yes — Microsoft 365 / SharePoint / OneDrive.

## What was found in ROOT (contradicts "no workflow exists")

A quick-search of the Sustineri OS canonical vault surfaced an established system.
This graphic is **not** greenfield and must reconcile with the following:

| Canonical artifact | Path | Bearing on this work |
|---|---|---|
| **Sustineri Claude Design Brand Kit** (rank-1 authority, D-BRAND-001) | `00_System_Core/AI_Operating_System/07_Templates/Brand/Sustineri_Brand_Kit.md` | The single controlling visual authority. Must be loaded by path before any branded build. |
| **`sustineri-brand-system` skill** | `02_Prompt_Architecture/01_Skills/sustineri-brand-system/SKILL.md` | Parent brand-system skill; points at the kit. |
| **`sustineri-house-ui` / `Sustineri_House_UI_Skill`** | (skill) | The execution/build skill that loads the kit. This is the intended builder. |
| **Brand Inception Gate** | `05_Governance/Brand_Inception_Gate.md` | Mandatory pre-build PASS gate. Not run for the current draft. |
| **Connective-map series (existing)** | `.../04_Trackers/13_System_Maps/Sustineri_Connective_Map_001_Entity_Ownership_v1.md` (`MAP-ENTITY-001`) | An established naming/ID convention: `Sustineri_Connective_Map_00N_*`. This asset should slot into that series, not invent its own. |
| **Connective Node Registry** | `.../03_Connective_Node_Registry/` | Existing connective-map infrastructure. |
| **Invisible Ecosystem Campaign** | `Website Development/Invisible_Ecosystem_Campaign/02_Netlify_Package/` | The campaign this post belongs to (connective app, whitepaper, index). |
| **Trackers** | `Master_Output_Index.md`, `Master_Change_Log.md` | Every output + reusable asset is logged. This deliverable is not yet logged. |

**Conclusion:** Do **not** promote this repo folder to canonical. It is a
PROVISIONAL build produced in an isolated repo without loading the canonical kit
by path or running the Brand Inception Gate.

## Brand-fidelity check against the canonical kit (PASS/FAIL is the kit's own rule)

Validated the delivered PNGs against `Sustineri_Brand_Kit.md` §2–§6. Deviations found:

1. **Logo — FAIL (hard rule).** The kit treats the Sustineri logo as a *protected
   asset*: "never substitute a wordmark or text — use the cached PNG or flag and
   stop." The current draft **invents an "S" roundel monogram + "Sustineri"
   wordmark lockup**. This must be replaced with the real cached logo asset or the
   logo slot must be flagged as a gap. The invented mark ships in the current PNGs.
2. **Typography — deviation.** Kit: **serif** for display/headlines. The draft
   sets the headline in **sans**. Headline should be the editorial serif.
3. **Gradients / shadows — deviation.** Kit §2: "Never used: … gradients, drop
   shadows." The draft uses a radial page gradient, a navy gradient on the core
   node, and card drop-shadows. Cards should be flat white + `1px --light-gray`.
4. **Fabricated tokens — deviation.** `#e6bb54` ("gold-bright") and the desaturated
   grays used for Zone C are not in the locked palette. Use only navy/gold/steel/
   light-gray/stone/gold-tint; for "what broke," desaturate within light-gray.
5. **Background neutral — deviation.** Section neutral should be **Stone `#F5F2EC`**
   (warm), not the cool blue-grey paper used. Social-card spec further calls for a
   **navy** background with a gold rule.
6. **Social-card copy density — deviation.** Kit social-card rule: "Headline only —
   no taglines, no CTAs … body copy lives in the LinkedIn post, not on the image."
   The connective map is intentionally denser — but note the kit classifies this as
   a **surface not yet covered** (§11), which should be *routed back as a gap* to be
   added to the kit, not silently shipped.
7. **Process — deviation.** Brand Inception Gate not run; kit not loaded by path;
   output not logged to Master Output Index / Change Log.

**Net:** The palette is correct, but the current draft would **not pass** the kit's
pass/fail brand gate as-is. It is usable as a provisional concept for founder
review; it is not brand-final.

## Brand-compliant rebuild (brandv2) — status after founder direction

Founder chose **"rebuild fully brand-compliant."** A brand-compliant set was produced
(`*_brandv2*`) that loads the real design system extracted from ROOT:

- **Fonts:** real brand families embedded from the header inject — **Source Serif 4**
  (headlines), **Public Sans** (body), **JetBrains Mono** (eyebrows), Latin woff2
  base64 in `source/fonts_embedded.css`. ✔ resolves deviation #2.
- **Flat surfaces:** no gradients, no drop shadows; white cards, `1px solid --lgray`,
  square corners; navy core + navy footer band. ✔ resolves deviation #3.
- **Tokens:** only locked tokens (`--navy/--gold/--steel/--lgray/--paper/--stone`)
  from `00_HEADER_INJECT.html`; dropped `#e6bb54` and ad-hoc grays. ✔ resolves #4/#5.
- **Type system:** serif H1 + gold 64×2 rule, mono letter-spaced eyebrows, sans body,
  serif zone titles, `SECTION · NN` mono indices. ✔ resolves #2.
- **Wordmark:** the real serif **"Sustineri"** lockup (Source Serif 4), as the live
  nav/footer render it — no invented "S" monogram. ✔ resolves the fabrication in #1.

**One item still open (deviation #1, partial):** the protected **logo mark image**
(`assets/sustineri-mark.png` / `sustineri-logo-trans.png`) could **not be exported**
through the read-only Microsoft Graph connector (binary `/content` returns 400; no
download URL). The brandv2 set therefore uses the **wordmark-only** lockup and leaves
the mark slot open rather than fabricating one. To finish: composite the real
`sustineri-mark.png` into the header/footer lockup (drop-in), or authorize a path to
export the binary.

Still outstanding regardless of art: **Brand Inception Gate** run, kit loaded by path
in-session, and **tracker logging** (Master Output Index / Change Log) — these are
ROOT-side governance steps, not repo steps.

The earlier provisional set (`*_watermarked.png`, `_alt`, `_sharp`, `_tight`) is
**retained, not deleted**. The `*_brandv2*` set is the brand-aligned recommendation.

## 2026-07-01 — Founder correction & final-candidate lock

**Brand direction ACCEPTED by founder (Angeline Stephens).** brandv2 is the approved
direction. Primary = portrait, Alt = square. Confirmations requested, answered honestly:

1. **Visible logo is the real protected asset — ❌ NOT met (blocked).** The protected
   mark (`assets/sustineri-mark.png` / `sustineri-logo-trans.png`) could not be exported
   through the available **read-only** Microsoft Graph connector (binary `/content`
   → `400 invalidRequest`; no download URL). No SVG exists; no inline base64 copy exists
   in any readable text file (the archived `sustineri-brand-kit.html` is text-wordmark
   only); the Canva brand-kit list is empty. brandv2 therefore uses the **official serif
   "Sustineri" wordmark** (Source Serif 4, as the live nav/footer render it) as an
   **interim** lockup, with the mark slot flagged. **The mark image must be composited
   before publish** by a session with binary-export or write access. This asset is
   **final-pending-logo**, not publish-final.
2. **Watermark uses approved brand pattern only — ✔ met.** The background watermark is the
   brand **hero-comp diagonal grid** pattern (per `00_HEADER_INJECT.html`
   `.scg-hero-comp__grid`). The earlier concentric-ring motif (not a brand asset) was
   **removed**. No logo asset is used as a watermark (kit forbids recolor/opacity-alter).
3. **No invented "S" monogram / unofficial logo remains — ✔ met** in the final-candidate
   (brandv2) set. The invented "S" roundel exists only in the ARCHIVED provisional set.
   Note: brandv2 still shows the **wordmark** (see #1) — the official wordmark, not an
   invented mark, but it is a stand-in until the protected mark image is dropped in.
4. **Provisional version archived & marked non-canonical — ✔ met.**
   `output/_ARCHIVED_provisional_noncanonical/` and
   `source/_ARCHIVED_provisional_noncanonical/` each carry `DO_NOT_USE.md`.
5. **brandv2 files are the only final candidates — ✔ met.** `output/` contains only the
   two brandv2 PNGs; all v1/sharp/tight moved to the archive folder.
6. **CANONICAL_VALIDATION updated — ✔ (this section).**

### ROOT write-back — ❌ NOT possible in this session
The founder requested writing outputs + appending tracker rows in the canonical ROOT
(`.../00_System_Core/AI_Operating_System/`). This **cannot be performed here**:
- The available Microsoft 365 connector is **read/search only** — it exposes no
  file-create / upload / update capability for OneDrive/SharePoint.
- The path given (`/Users/angeline/Library/CloudStorage/OneDrive-.../`) is a **local
  macOS path**, not reachable from this cloud container.
- GitHub write scope is limited to `sustineri-consulting/streamlit`.

A ready-to-paste write-back payload (tracker rows + exact paths) is staged at
`ROOT_WRITEBACK_PAYLOAD.md` for an authorized/write-enabled session to apply.

## Recommended reconciliation (for founder decision — do not action without approval)

- Rebuild via **`sustineri-house-ui`**, loading `Sustineri_Brand_Kit.md` by path,
  through the **Brand Inception Gate**.
- Serif headline; flat surfaces (no gradients/shadows); Stone or navy background per
  the social-card rule; drop `#e6bb54` and ad-hoc grays.
- Replace the invented monogram with the **real protected logo** (cached base64 PNG
  in `00_HEADER_INJECT.html`) — or flag the logo slot and stop.
- Register the connective-map *social graphic* as a **new surface/gap** in the kit.
- Name + log under the existing series (e.g. `Sustineri_Connective_Map_002_AI_Work_
  Architecture_*`) and add rows to Master Output Index + Master Change Log.

_No writes were made to ROOT / SharePoint / OneDrive during this validation — read-only._
