#!/usr/bin/env python

import sys


def find_split(pattern):
    for split in range(1, len(pattern)):
        ok = True
        for i in range(split):
            if split + i == len(pattern):
                break
            if pattern[split - i - 1] != pattern[split + i]:
                ok = False
        if ok:
            return split

    return None


def find_reflection(pattern):
    split = find_split(pattern)
    if split is not None:
        return 100 * split

    rotated = []
    for col in range(len(pattern[0])):
        rotated.append(''.join(pattern[row][col] for row in range(len(pattern))))

    return find_split(rotated)


def main():
    total = 0
    pattern = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            total += find_reflection(pattern)
            pattern = []
            continue
        pattern.append(line)
        
    total += find_reflection(pattern)

    print(total)


if __name__ == '__main__':
    main()
