from random import uniform
from math import cos, sin, pi, dist, floor

def sim_walk(steps):
    dt = 1 / steps
    xpos = 0
    ypos = 0
    for _ in range(steps):
        theta = uniform(0, 1)
        xpos += dt * cos(2 * pi * theta)
        ypos += dt * sin(2 * pi * theta)
    return dist((0, 0), (xpos, ypos))

STEPS = 10000
BINS = 100

WALKS = 1000

bins = [0] * BINS

for _ in range(WALKS):
    index = floor(BINS * sim_walk(STEPS))
    bins[index] += 1

print("step, frequency")

for i, freq in enumerate(bins):
    print(f"{i / BINS}, {freq}")
