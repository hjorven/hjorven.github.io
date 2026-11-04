# Portfolio

Personal portfolio of [hjorven](https://github.com/hjorven) in a 1-bit dither / techno-classicism style.

Live: https://hjorven.github.io/jorven.github.io/ (or https://hjorven.github.io/ once the repository is renamed to `hjorven.github.io`)

## Features

- Six featured projects with install commands for each one
- Live binary clock
- Light and dark theme plus 12 accent colours; every switch spreads across the page as a wave (View Transitions API)
- No build step, no frameworks, no trackers. Fonts are self-hosted.

## Run locally

```bash
git clone https://github.com/hjorven/jorven.github.io.git
cd jorven.github.io
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Engravings

The images in `img/` are 1-bit alpha masks rendered with `tools/render.py` (raymarching in NumPy, then Bayer, Floyd–Steinberg or line-screen dithering). The page tints them with the current accent colour. The card images come out of the script as blue-on-navy PNGs; for the page only the blue pixels are kept as an alpha mask.

```bash
pip install numpy pillow
python3 tools/render.py out hero hex rack torus armillary dice temple arch
```

## Fonts

Instrument Serif, IBM Plex Mono and Inter Tight, all under the SIL Open Font License, bundled from Fontsource.
