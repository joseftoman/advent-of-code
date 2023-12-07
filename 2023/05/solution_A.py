#!/usr/bin/env python

import sys


def mappings():
    ranges = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            if ranges:
                yield ranges
                ranges = []
            continue
        if line.endswith(' map:'):
            continue

        range_spec = [int(_) for _ in line.split()]
        ranges.append(range_spec)

    if ranges:
        yield ranges
        

def remap(seeds, mapping):
    mapping.sort(key=lambda item: item[1])
    new_seeds = []
    pos = 0

    for item in seeds:
        while pos < len(mapping) and item >= mapping[pos][1] + mapping[pos][2]:
            pos += 1

        if pos < len(mapping) and mapping[pos][1] <= item < mapping[pos][1] + mapping[pos][2]:
            new_seeds.append(mapping[pos][0] + (item - mapping[pos][1]))
        else:
            new_seeds.append(item)

    return sorted(new_seeds)


def main():
    seeds = sorted(int(_) for _ in next(sys.stdin).split(':')[1].split())
    
    for mapping in mappings():
        seeds = remap(seeds, mapping)

    print(seeds[0])

if __name__ == '__main__':
    main()
