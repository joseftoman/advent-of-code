#!/usr/bin/env python

import sys


def main():
    topo = {}
    trailheads = []

    for y, line in enumerate(_.strip() for _ in sys.stdin):
        for x, height in enumerate(line):
            topo[(y, x)] = int(height)
            if height == '0':
                trailheads.append({(y, x)})

    for step in range(1, 10):
        one_step_ahead = []

        for trailhead in trailheads:
            expanse = set()

            for pos in trailhead:
                for diff in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    next_pos = (pos[0] + diff[0], pos[1] + diff[1])
                    if topo.get(next_pos) == step:
                        expanse.add(next_pos)

            one_step_ahead.append(expanse)

        trailheads = one_step_ahead

    print(sum(len(_) for _ in trailheads))


if __name__ == '__main__':
    main()
