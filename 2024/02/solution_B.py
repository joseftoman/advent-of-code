#!/usr/bin/env python

from collections import defaultdict
import sys


def cmp(a, b):
    if a == b:
        return 0
    return -1 if a < b else 1


def scan(levels: list[int], target: int | None = None) -> tuple[bool, int | None]:
    mono = defaultdict(int)
    has_gap = False
    
    for i in range(1, len(levels)):
        pair_test = cmp(levels[i - 1], levels[i])
        has_gap |= abs(levels[i - 1] - levels[i]) > 3
        if target is not None and (target != pair_test or has_gap):
            return False, None
        mono[pair_test] += 1

    is_safe = (len(mono) == 1 and 0 not in mono and not has_gap)
    if target is not None or is_safe:
        return is_safe, None

    mono.pop(0, None)
    return is_safe, sorted(mono.items(), key=lambda pair: pair[1], reverse=True)[0][0]


def main():
    total_safe = 0

    for line in sys.stdin:
        levels = [int(_) for _ in line.split()]
        is_safe, target = scan(levels)
        if is_safe:
            total_safe += 1
            continue

        for i in range(len(levels)):
            altered_levels = levels[:]
            altered_levels.pop(i)
            is_safe, _ = scan(altered_levels, target)
            if is_safe:
                total_safe += 1
                break

    print(total_safe)
    

if __name__ == '__main__':
    main()
