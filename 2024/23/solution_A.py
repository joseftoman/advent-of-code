#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import sys


def main():
    nodes = defaultdict(set)
    edges = set()
    known_triples = set()
    total = 0

    for line in sys.stdin:
        pair = line.strip().split('-')
        nodes[pair[0]].add(pair[1])
        nodes[pair[1]].add(pair[0])
        edges.add(tuple(pair))
        edges.add(tuple(reversed(pair)))

    for node, other in nodes.items():
        for pair in combinations(other, 2):
            if tuple(pair) in edges:
                triple = tuple(sorted([node, *pair]))
                if triple in known_triples:
                    continue
                known_triples.add(triple)
                if any(_[0] == 't' for _ in triple):
                    total += 1

    print(total)


if __name__ == '__main__':
    main()
