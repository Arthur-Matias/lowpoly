# -*- coding: utf-8 -*-
"""low_poly.ipynb

Original file is located at
    https://colab.research.google.com/drive/1hLPAsCUFBzqy2V90xuA-fNHVFCnaeonm
"""

import os
import sys
import numpy as np
import pygame
import pygame.gfxdraw
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from scipy.ndimage import gaussian_filter
from collections import defaultdict

# Load Image
target = sys.argv[1]
inp = pygame.surfarray.pixels3d(pygame.image.load(f"input/{target}.jpg"))
perceptual_weight = np.array([0.2126, 0.7152, 0.0722])
grayscale = (inp * perceptual_weight).sum(axis=-1)
# plt.imshow(grayscale.T)

# Highlight Details
x = gaussian_filter(grayscale, 2, mode="reflect")
x2 = gaussian_filter(grayscale, 30, mode="reflect")

diff = (x-x2)
diff[diff < 0] *= 0.1
diff = np.sqrt(np.abs(diff)/diff.max())
# plt.imshow(diff.T)


def get_points_from_image(ref, n=1000000):
    np.random.seed(0)
    w, h = x.shape
    xs = np.random.randint(0, w, size=n)
    ys = np.random.randint(0, h, size=n)
    value = ref[xs, ys]
    accept = np.random.random(size=n) < value
    points = np.array([xs[accept], ys[accept]])
    return points.T, value[accept]


# Plotting points
samples, v = get_points_from_image(diff)
# plt.scatter(samples[:, 0], -samples[:, 1], c=v, s=0.2, edgecolors="none", cmap="viridis")


def get_triangle_color(tri, image):
    colors = defaultdict(lambda: [])
    w, h, _ = image.shape
    for i in range(0, w):
        for j in range(0, h):
            index = tri.find_simplex((i, j))
            colors[int(index)].append(inp[i, j, :])

    for index, array in colors.items():
        colors[index] = np.array(array).mean(axis=0)

    return colors


def draw(tri, colors, screen, upscale):
    s = screen.copy()
    for key, c in colors.items():
        t = tri.points[tri.simplices[key]]
        pygame.gfxdraw.filled_polygon(s, t * upscale, c)
        pygame.gfxdraw.polygon(s, t * upscale, c)
    return s


w, h, _ = inp.shape
upscale = 2
screen = pygame.Surface((w * upscale, h * upscale))
screen.fill(inp.mean(axis=(0, 1)))
corners = np.array([(0, 0), (0, h - 1), (w - 1, 0), (w - 1, h - 1)])
points = np.concatenate((corners, samples))

outdir = f"output/{target}/"
os.makedirs(outdir, exist_ok=True)

for i in range(0, 100):
    print(f"{target}/{i}")
    n = 5 + i + 2 * int(i**2)
    tri = Delaunay(points[:n, :])
    colors = get_triangle_color(tri, inp)
    s = draw(tri, colors, screen, upscale)
    s = pygame.transform.smoothscale(s, (w, h))
    pygame.image.save(s, f"{outdir}{i:04d}.png")
