#!/usr/bin/env python

import sys


def place(springs, groups):
    minimum = sum(groups) + len(groups) - 1
    g = groups[0]
    total = 0
    i = 0

    while len(springs) - i >= minimum:
        if all(springs[_] in {'?', '#'} for _ in range(i, i + g)) and (i + g == len(springs) or springs[i + g] in {'.', '?'}):
            if len(groups) > 1:
                total += place(springs[i + g + 1:], groups[1:])
            elif '#' not in springs[i + g + 1:]:
                total += 1
        if springs[i] == '#':
            break
            
        i += 1
   
    return total


def main():
    total = 0

    for line in sys.stdin:
        springs, groups = line.strip().split()
        groups = [int(_) for _ in groups.split(',')]
        total += place(springs, groups)

    print(total)


if __name__ == '__main__':
    main()
