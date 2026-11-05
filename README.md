# hjorven.github.io

Personal portfolio of [hjorven](https://github.com/hjorven) in a 1-bit dither / techno-classicism style.

Live: https://hjorven.github.io/

## Features

- Seven projects (four featured) with install commands for each one
- Live binary clock
- Light and dark theme plus 12 accent colours; every switch spreads across the page as a wave (View Transitions API)
- Animations: engravings develop dot by dot as they scroll into view, the hero icosahedron turns (24 pre-rendered frames) with scroll parallax, and taps send out a dithered ripple. All of it is off when the system asks for reduced motion.
- Wallpapers: 24 iPad Safari start-page backgrounds in all 12 colours at [/wallpapers/](https://hjorven.github.io/wallpapers/), kept in their own repository (see below)
- Favicon, home-screen icons, web manifest and a link preview image (`og.png`)
- No build step, no frameworks, no trackers. Fonts are self-hosted.

## Wallpapers

The wallpapers live in their own repository now: [hjorven/wallpapers](https://github.com/hjorven/wallpapers), served at https://hjorven.github.io/wallpapers/. GitHub Pages serves that project site under the same path, so the old link keeps working.

## Run locally

```bash
git clone https://github.com/hjorven/hjorven.github.io.git
cd hjorven.github.io
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Engravings

The images in `img/` are 1-bit alpha masks rendered with `tools/render.py` (raymarching in NumPy, then Bayer, Floyd–Steinberg or line-screen dithering). The page tints them with the current accent colour. The card images come out of the script as blue-on-navy PNGs; for the page only the blue pixels are kept as an alpha mask.

```bash
pip install numpy pillow
python3 tools/render.py out hex rack frames pixels dice temple arch easel
python3 tools/hero_layers.py out 24   # hero layers: rays, column and the 24-frame icosahedron sprite
python3 tools/hero_knock.py           # backing for the icosahedron sprite, from img/hero-ico.png
```

## Fonts

Instrument Serif, IBM Plex Mono and Inter Tight, all under the SIL Open Font License, bundled from Fontsource.
