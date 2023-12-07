#!/usr/bin/env python

import sys

raw_scanners = {}
aligned_scanners = {}
scanner = None


def rotate_beacon(b):
    """ See https://stackoverflow.com/a/16467849 """
    def roll(b): return (b[0], b[2], -b[1])
    def turn(b): return (-b[1], b[0], b[2])
    
    for _ in range(2):
        for _ in range(3):
            b = roll(b)
            yield(b)
            for _ in range(3):
                b = turn(b)
                yield(b)

        b = roll(turn(roll(b)))


def rotate_scanner(s):
    return zip(*[rotate_beacon(_) for _ in s])


def align_scanners(base, candidate):
    for sample_a in base:
        for sample_b in candidate:
            diff = tuple(sample_a[_] - sample_b[_] for _ in range(3))
            beacons = {(b[0] + diff[0], b[1] + diff[1], b[2] + diff[2]) for b in candidate}

            if len(base & beacons) >= 12:
                return (diff, beacons)

    return None


for line in sys.stdin:
    if line[:4] == '--- ':
        scanner = int(line[12:][:-4])
        raw_scanners[scanner] = set()
    elif len(line) > 1:
        raw_scanners[scanner].add(tuple(int(_) for _ in line.split(',')))

aligned_scanners[0] = ((0, 0, 0), raw_scanners.pop(0))

while raw_scanners:
    hit = False

    for key_raw in raw_scanners.keys():
        for r in rotate_scanner(raw_scanners[key_raw]):
            for key_aligned in aligned_scanners.keys():
                aligned = align_scanners(aligned_scanners[key_aligned][1], list(r))
                if aligned is not None:
                    hit = True
                    del raw_scanners[key_raw]
                    aligned_scanners[key_raw] = aligned
                    print(f'{key_aligned} -> {key_raw}: {aligned[0]}')
                    break
            if hit: break
        if hit: break

scanners = [_[0] for _ in aligned_scanners.values()]
best = 0

for s1 in scanners:
    for s2 in scanners:
        distance = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2])
        if distance > best:
            best = distance

print(best)
