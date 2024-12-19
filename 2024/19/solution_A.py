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
    possible = 0
    patterns = read_patterns()

    next(sys.stdin)

    @lru_cache(50_000)
    def is_possible(design):
        state = patterns
        index = 0
        hits = []
        
        while index < len(design) and design[index] in state['next']:
            state = state['next'][design[index]]
            if state['is_pattern']:
                if index == len(design) - 1:
                    return True
                hits.append(index)
            index += 1

        for index in reversed(hits):
            if is_possible(design[index + 1:]):
                return True

        return False


    for line in sys.stdin:
        if is_possible(line.strip()):
            possible += 1

    print(possible)


if __name__ == '__main__':
    main()
