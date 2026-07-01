# People 404™ Work Health Check — Offer System

A launch-ready, buyer-facing offer + fulfillment system for the **People 404™ Work
Health Check** ($3,500 launch price) — a workforce infrastructure diagnostic within
the Sustineri ecosystem.

This is a self-contained **static site** (no build step) plus the fulfillment,
sample-deliverable, sales, and tracker artifacts needed to run the offer.

## What's here

```
people-404-work-health-check/
├── index.html            # Buyer-facing offer page (hero → problem → … → FAQ)
├── intake.html           # Diagnostic intake form (static; integration required)
├── sample.html           # Rendered anonymized sample deliverable (noindex)
├── assets/styles.css     # Locked Sustineri brand kit + Feng Shui layout system
├── config/
│   └── booking-payment.config.json   # Booking / payment / form placeholders
├── deliverables/
│   └── people-404-work-health-summary.md   # Sample deliverable (markdown source)
├── internal/
│   └── fulfillment-sop.md            # Internal delivery SOP + stage checklists
├── sales/
│   └── sales-copy-snippets.md        # LinkedIn / email / CTA / one-liners
├── trackers/
│   ├── master-output-index.md
│   ├── master-change-log.md
│   └── people-404-tracker.md
├── netlify.toml          # Netlify static deploy config
└── README.md
```

## Local preview

It's plain HTML/CSS — open `index.html` in a browser, or serve the folder:

```bash
cd people-404-work-health-check
python3 -m http.server 8080
# visit http://localhost:8080
```

## Deploy to Netlify

No build step is required.

**Option A — deploy this subfolder (recommended):**
1. In Netlify, create a site from this repo.
2. Set **Base directory** to `people-404-work-health-check`.
3. Set **Publish directory** to `.` (the base directory), **Build command** empty.
4. Deploy. `netlify.toml` provides headers and friendly `/offer`, `/intake`, `/sample` routes.

**Option B — drag-and-drop:** zip this folder and drop it into the Netlify UI.

> Do **not** mark the offer "live" until a deploy has actually succeeded and the URL loads.

## Before you can take money / bookings (required integrations)

Nothing is faked. Three integrations must be connected before launch — all tracked in
`config/booking-payment.config.json`:

| Marker | Where | What to do |
| --- | --- | --- |
| **BOOKING LINK REQUIRED** | `index.html` (`data-cta="booking"` + "Book" buttons) | Add a live scheduling link and set it as the button `href`. |
| **PAYMENT LINK REQUIRED** | booking/confirmation flow | Add a live checkout link (Stripe/Square/PayPal) for $3,500. |
| **FORM INTEGRATION REQUIRED** | `intake.html` `<form>` | Wire to Netlify Forms / Formspree / CRM (see the comment in `intake.html`). |
| **FOUNDER BIO REQUIRED** | `index.html` founder section | Replace placeholder with real name, photo, proof points. |

### Quick path: Netlify Forms for intake
In `intake.html`, add `name="people-404-intake" netlify netlify-honeypot="bot-field"`
to the `<form>` tag and a hidden `<input type="hidden" name="form-name" value="people-404-intake" />`.
Re-enable native submission (remove the `preventDefault` handler). Netlify will capture submissions.

## Brand + layout

The site uses the **locked Sustineri brand kit** (Navy `#012564`, Gold `#ab8834`,
Light gold `#e6bb54`, Steel `#496699`, Gray `#dbdbdb`, off-white) and the **locked
Feng Shui layout system** (clear entry path → problem → why now → who → what's
reviewed → what you receive → process → price → CTA → FAQ → trust). System fonts
only — no external font imports. See `assets/styles.css`.
