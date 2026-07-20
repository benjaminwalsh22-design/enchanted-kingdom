# Enchanted Kingdom — Design System

The "Whimsical & Enchanted Kingdom" visual system for the ages 4–6 app. All of
this lives inline in `index.html` (single self-contained PWA) — this doc is the
reference map.

## Color tokens (CSS custom properties, in `:root`)

**Core palette — vibrant, high-contrast**

| Token | Value | Use |
|---|---|---|
| `--pink` / `--magenta` | `#ff5fae` / `#ff3d9a` | primary actions, princess accent |
| `--purple` / `--violet` / `--lilac` | `#8a3ffb` / `#a15bff` / `#cbb0ff` | bubble buttons, unicorn accent |
| `--aqua` / `--aqua-deep` / `--aqua-soft` | `#19c6e6` / `#0aa6c9` / `#a6f2ff` | mermaid/cove accent, water |
| `--mint` / `--mint-soft` | `#33e0ac` / `#bafce6` | forest/glow accents |
| `--gold` / `--gold-deep` / `--gold-soft` | `#ffc22e` / `#f5a300` / `#ffe9a8` | stars, tiara, rewards |
| `--ink` / `--ink-soft` | `#2b1a63` / `#6a53b0` | text (never pure black) |

**Realm accents**: `--castle #ff5fae`, `--forest #57cf3f`, `--cove #19c6e6`.

**Background** (body): layered radial glows + a rainbow linear gradient
(pink → lilac → sky-blue → mint) for the "dreamlike" feel.

> Legacy aliases (`--bubblegum`, `--peri`, `--amethyst`, `--seafoam`, …) are
> remapped to vibrant values so the two mini-games restyle automatically.

## Metrics

- `--hit: 78px` — jumbo minimum touch target (big for little hands).
- `--radius: 30px` — friendly rounded corners everywhere.
- Generous card gaps (22–34px) so targets never crowd.

## Components (class → what it is)

- **`.brand` + `.badge`** — title lockup with the inline **shield-crest emblem**
  (`EMBLEM_BADGE` SVG: gold tiara + unicorn horn + mermaid tail). The app icon is
  the same crest, rasterized to PNG.
- **`.starjar`** — the reward counter: a glowing jar SVG that fills with gold
  stars. Each completed activity drops **+3 stars** in the jar (`Ledger.complete`).
- **`.realm`** — floating realm island on the hub. Custom `sceneSVG()` per realm
  (Crystal Castle cloud-castle, Enchanted Forest rainbow-woods, Coral Cove reef),
  with a `floatRealm` idle bob + `shine` sweep. Shows an `⭐ N` badge once earned.
- **`.activity`** — jumbo glossy card inside a realm: gradient fill, `.sheen`
  highlight, bobbing `.glow-orb` icon, big title. `soon ✨` chip when locked.
- **`.bubble-btn`** — glossy round bubble button (back / nav) that squishes on tap.
- **`.bigbtn`** — primary pill button, now glossy pink→magenta.
- **`.tappable`** — any element that should squish on press (`:active` scale) and
  emit a burst of ⭐/✨ particles under the finger (global `pointerdown` handler).

## Interaction & feedback rules (ages 4–6)

- **Icon-first**: realms and activities lead with a big emoji/icon; text is short.
- **Instant feedback on every tap**: CSS `:active` squish + a star/sparkle burst
  (`Sparkles.burst`) + a soft WebAudio chime. No tap goes unrewarded.
- **No fail states, no timers** (carried through from the games): wrong moves get
  a gentle nudge, never a buzzer.
- **High contrast**: saturated card gradients sit on the soft rainbow background;
  white borders + drop shadows lift every interactive element off the page.

## Where the art comes from (all asset-free / vector)

- App icon + title emblem: authored as SVG (`emblem.html`), rasterized to
  `icon-180/192/512.png`, inlined as data-URIs. One file, no image dependencies.
- Realm scenes, star jar, shape glyphs: inline SVG generated in JS.
- Characters/props: emoji (🐚 🏰 🦄 💎 👑 🌈 🧜‍♀️) for instant, colorful, familiar icons.

## Structure recap

`index.html` → `:root` tokens · component CSS · `REALMS`/`GAMES` model ·
`Ledger` (stars + pearls, persisted) · `HubScreen` / `RealmScreen` · the two
playable games (Bubble Sort Reef, Counting Clam Beds) · reward banner.
