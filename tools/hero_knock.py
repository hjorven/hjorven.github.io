# Aufruf aus dem Repo: python3 tools/hero_knock.py  (erzeugt img/hero-ico-knock.png aus img/hero-ico.png)
"""Unterlage fürs drehende Ikosaeder: Striche plus kleine eingeschlossene Lücken füllen,
große Lücken (zwischen Ring und Körper) offen lassen, damit die Strahlen dort durchscheinen."""
import os, sys; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')); sys.path.insert(0, 'tools'); sys.argv = ['x', '/tmp']
from PIL import Image; import numpy as np; import render as R
def labels(free):
    H, W = free.shape; BIG = H * W + 1
    lab = np.where(free, np.arange(H * W).reshape(H, W), BIG)
    while True:
        n = lab.copy()
        n[1:] = np.minimum(n[1:], lab[:-1]); n[:-1] = np.minimum(n[:-1], lab[1:])
        n[:, 1:] = np.minimum(n[:, 1:], lab[:, :-1]); n[:, :-1] = np.minimum(n[:, :-1], lab[:, 1:])
        n = np.where(free, n, BIG)
        if (n == lab).all(): return lab, BIG
        lab = n
spr = np.array(Image.open('img/hero-ico.png').getchannel('A')) > 127
N = 24; fw = spr.shape[1] // N; out = []
for k in range(N):
    g = R.binary_dilation(spr[:, k*fw:(k+1)*fw], iterations=1)
    g[0, :] = g[-1, :] = g[:, 0] = g[:, -1] = False
    lab, BIG = labels(~g)
    ids, cnt = np.unique(lab[lab < BIG], return_counts=True)
    keep = np.isin(lab, ids[cnt > 2500])
    out.append(R.binary_dilation(~keep, iterations=2))
    print(k, end=' ', flush=True)
k = np.concatenate(out, axis=1)
a = np.where(k, 255, 0).astype(np.uint8)
Image.merge('LA', (Image.new('L', (k.shape[1], k.shape[0]), 0), Image.fromarray(a))).save('img/hero-ico-knock.png', optimize=True)
