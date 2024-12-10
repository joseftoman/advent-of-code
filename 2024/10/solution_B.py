#!/usr/bin/env python

import sys


def main():
    topo = {}
    trailheads = []

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        for x, height in enumerate(line):
            topo[(y, x)] = int(height)
            if height == '0':
                trailheads.append({(y, x): 1})

    for step in range(1, 10):
        one_step_ahead = []

        for trailhead in trailheads:
            expanse = {}

            for pos, rating in trailhead.items():
                for diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    next_pos = (pos[0] + diff[0], pos[1] + diff[1])
                    if topo.get(next_pos) == step:
                        if next_pos in expanse:
                            expanse[next_pos] += rating
                        else:
                            expanse[next_pos] = rating

            one_step_ahead.append(expanse)

        trailheads = one_step_ahead

    print(sum(rating for trailhead in trailheads for _, rating in trailhead.items()))


if __name__ == '__main__':
    main()
