#!/usr/bin/env python

import sys


def find_split(pattern, ignore=None):
    for split in range(1, len(pattern)):
        ok = True
        for i in range(split):
            if split + i == len(pattern):
                break
            if pattern[split - i - 1] != pattern[split + i]:
                ok = False
        if ok and split != ignore:
            return split

    return None


def find_reflection(pattern, ignore=None):
    split = find_split(pattern, None if ignore is None or ignore < 100 else ignore // 100)
    if split is not None:
        return 100 * split

    rotated = []
    for col in range(len(pattern[0])):
        rotated.append(''.join(pattern[row][col] for row in range(len(pattern))))

    split = find_split(rotated, None if ignore is None or ignore >= 100 else ignore)
    if split is not None:
        return split

    return None


def find_smudge(pattern):
    old = find_reflection(pattern)

    for row in range(len(pattern)):
        for col in range(len(pattern[0])):
            fixed = pattern[:]
            fixed[row] = fixed[row][:col] + ('.' if fixed[row][col] == '#' else '#') + fixed[row][col + 1:]
            refl = find_reflection(fixed, old)
            if refl is not None:
                return refl


def main():
    total = 0
    pattern = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            total += find_smudge(pattern)
            pattern = []
            continue
        pattern.append(line)
        
    total += find_smudge(pattern)

    print(total)


if __name__ == '__main__':
    main()
