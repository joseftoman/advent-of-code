#!/usr/bin/env python

from collections import defaultdict
from graphlib import CycleError, TopologicalSorter
import sys


def main():
    rules = defaultdict(list)
    output = 0
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break

        before, after = [int(_) for _ in line.split('|')]
        rules[before].append((before, after))
        rules[after].append((before, after))

    for line in sys.stdin:
        pages = [int(_) for _ in line.split(',')]
        set_of_pages = set(pages)
        edges = defaultdict(set)

        for page in pages:
            for rule in rules[page]:
                if len(set(rule) & set_of_pages) == 2:
                    edges[rule[1]].add(rule[0])

        sorter = TopologicalSorter(edges)
        correct_order = list(sorter.static_order())

        if pages != correct_order:
            output += correct_order[len(correct_order) // 2]

    print(output)


if __name__ == '__main__':
    main()
