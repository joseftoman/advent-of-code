#!/usr/bin/env python

import sys

from intervaltree import IntervalTree


def main():
    tree = IntervalTree()
    fresh = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break

        left, right = [int(_) for _ in line.split('-')]
        tree[left:right + 1] = None

    tree.merge_overlaps()
    for interval in tree:
        fresh += interval.end - interval.begin

    print(fresh)


if __name__ == '__main__':
    main()
