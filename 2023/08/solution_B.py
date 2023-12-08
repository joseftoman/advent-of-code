#!/usr/bin/env python

import math
import sys
from typing import Iterator


def directions(fragment: str) -> Iterator[int]:
    pos = 0
    while True:
        yield {'L': 0, 'R': 1}[fragment[pos]]
        pos = (pos + 1) % len(fragment)


def main():
    fragment = next(sys.stdin).strip()
    next(sys.stdin)

    nodes = {}
    for line in sys.stdin:
        name, next_pair = line.strip().split('=')
        nodes[name.strip()] = tuple(_.strip() for _ in next_pair.strip()[1:-1].split(','))

    cycles = []
    for node in [_ for _ in nodes if _[-1] == 'A']:
        steps = 0
        for index in directions(fragment):
            steps += 1
            node = nodes[node][index]
            if node[-1] == 'Z':
                cycles.append(steps)
                break
    
    print(math.lcm(*cycles))


if __name__ == '__main__':
    main()
