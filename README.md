# facelift

**Give your pwnagotchi a facelift.** A tiny plugin that replaces the
classic text face `( ⚆_⚆)` in the web UI with a picture — any picture,
a different one for every mood.

![how it works](https://img.shields.io/badge/pwnagotchi-plugin-blue)

## How it works

Stock pwnagotchi faces are text glyphs drawn by a `Text` widget. On
`ui_setup`, facelift swaps that one widget for a `FaceImage` widget.
Every time the UI sets a new face, the widget reverse-maps the glyph to
its state name (`AWAKE`, `SLEEP`, `EXCITED`, ...) and pastes
`/root/coco2-faces/<STATE>.png` onto the canvas instead. No fork source
is modified — disable the plugin and the classic face is back.

- Picture is pasted at (0, 14) at 108x108, so the top status bar
  (CH / APS / UP) stays visible.
- Missing or broken images fall back to drawing the text glyph.
- Works with the dark-mode CSS invert trick (the picture inverts too).

## Install

1. Copy `facelift.py` to your pwnagotchi's custom plugins folder:
   `/usr/local/share/pwnagotchi/custom-plugins/`
2. Create `/root/coco2-faces/` and drop in your face PNGs
   (see `faces/README.md` for names and format).
3. Enable it in `/etc/pwnagotchi/config.toml`:

   ```toml
   main.plugins.facelift.enabled = true
   ```

4. Restart pwnagotchi. The log should say
   `[facelift] face widget swapped for picture face`.

## Making faces

Any image works. Crop square, convert to greyscale, resize to 108x108,
dither to 1-bit black & white, save as `<STATE>.png`. Anime, memes,
your cat — bold line art reads best at 108px. One pose per mood:
something sleepy for SLEEP/SLEEP2, something smug for COOL, and so on.

## Compatibility

Built and tested on the aluminum-ice fork (Raspberry Pi Zero 2 W,
headless, web UI). Should work on any build with the standard
`pwnagotchi.ui` package and plugin system.

## Donations

facelift is free. If it made your gotchi cuter and you feel like tipping:

**Monero (XMR)**
`4875Mj3ZVyXYiwhvcjnbNMWpqocBzyXDnL3bsBmkpJXcYLu4C6epuHwi4HyLwh9AJoJFNjfdxiKQnEHGQB5PKb5hK58mrro`

## Licence

GPL3
