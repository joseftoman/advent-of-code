#!/usr/bin/env python

from math import copysign
import numpy as np
import sys


#limits = [7, 27]
limits = [200000000000000, 400000000000000]


def intersect(h1, h2):
    x, _, rank = np.linalg.lstsq(np.array([h1[1], -h2[1]]).T, h2[0] - h1[0], rcond=None)[:3]
    if rank != 2:
        return None

    return h1[1] * x[0] + h1[0]


def main():
    hailstones = []
    for line in sys.stdin:
        point, velocity = line.strip().split('@')
        point = [int(_) for _ in point.split(',')]
        velocity = [int(_) for _ in velocity.split(',')]
        hailstones.append((np.array([point[0], point[1]]).T, np.array([velocity[0], velocity[1]]).T))

    total = 0

    for a in range(len(hailstones)):
        for b in range(a + 1, len(hailstones)):
            cross = intersect(hailstones[a], hailstones[b])
            if cross is None:
                # no intersection
                continue

            if not (limits[0] <= cross[0] <= limits[1] and limits[0] <= cross[1] <= limits[1]):
                # out of range
                continue

            future = (
                copysign(1, cross[0] - hailstones[a][0][0]) == copysign(1, hailstones[a][1][0])
                and copysign(1, cross[0] - hailstones[b][0][0]) == copysign(1, hailstones[b][1][0])
            )
            if future:
                total += 1

    print(total)


if __name__ == '__main__':
    main()
