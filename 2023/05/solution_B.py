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

    while seeds:
        start, amount = seeds.pop()

        while pos < len(mapping) and start >= mapping[pos][1] + mapping[pos][2]:
            pos += 1

        if pos >= len(mapping):
            new_seeds.append((start, amount))
        else:
            if start + amount < mapping[pos][1]:
                new_seeds.append((start, amount))
            elif start < mapping[pos][1]:
                new_seeds.append((start, mapping[pos][1] - start))
                seeds.append((mapping[pos][1], amount - (mapping[pos][1] - start)))
            elif start < mapping[pos][1] + mapping[pos][2]:
                capacity = mapping[pos][2] - (start - mapping[pos][1])
                new_seeds.append((mapping[pos][0] + (start - mapping[pos][1]), min(amount, capacity)))
                if amount > capacity:
                    seeds.append((mapping[pos][1] + mapping[pos][2], amount - capacity))

    return sorted(new_seeds, key=lambda pair: pair[0], reverse=True)


def main():
    raw = [int(_) for _ in next(sys.stdin).split(':')[1].split()]
    seeds = []
    for index in range(0, len(raw), 2):
        seeds.append((raw[index], raw[index + 1]))
    seeds.sort(key=lambda pair: pair[0], reverse=True)
    
    for mapping in mappings():
        seeds = remap(seeds, mapping)

    print(seeds[-1][0])

if __name__ == '__main__':
    main()
