#!/usr/bin/env python

from functools import lru_cache
import sys


def read_patterns():
    output = {'is_pattern': False, 'next': {}}

    for pattern in [_.strip() for _ in next(sys.stdin).split(',')]:
        pos = output
        for char in pattern:
            if char not in pos['next']:
                pos['next'][char] = {'is_pattern': False, 'next': {}}
            pos = pos['next'][char]
        pos['is_pattern'] = True

    return output


def main():
    grand_total = 0
    patterns = read_patterns()

    next(sys.stdin)

    @lru_cache(50_000)
    def arrangements(design):
        state = patterns
        index = 0
        hits = []
        total = 0
        
        while index < len(design) and design[index] in state['next']:
            state = state['next'][design[index]]
            if state['is_pattern']:
                if index == len(design) - 1:
                    total += 1
                else:
                    hits.append(index)
            index += 1

        for index in hits:
            total += arrangements(design[index + 1:])

        return total


    for line in sys.stdin:
        grand_total += arrangements(line.strip())

    print(grand_total)


if __name__ == '__main__':
    main()
