#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import sys


def main():
    nodes = defaultdict(set)
    edges = set()
    best = None

    for line in sys.stdin:
        pair = line.strip().split('-')
        nodes[pair[0]].add(pair[1])
        nodes[pair[1]].add(pair[0])
        edges.add(tuple(pair))
        edges.add(tuple(reversed(pair)))

    for node, other in nodes.items():
        hit = False
        for size in range(len(other), 1 if best is None else len(best) - 1, -1):
            for group in combinations(other, size):
                if set(tuple(_) for _ in combinations(group, 2)) <= edges:
                    best = sorted([*group, node])
                    hit = True
                    break

            if hit:
                break

    print(','.join(best))


if __name__ == '__main__':
    main()
