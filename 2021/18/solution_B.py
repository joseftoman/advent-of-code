#!/usr/bin/env python

import json
import sys


def drill_down(pair, index, value):
    if isinstance(pair[index], int):
        pair[index] += value
    else:
        drill_down(pair[index], index, value)


def explode(num, level = 1):
    if isinstance(num[0], int) and isinstance(num[1], int):
        return None if level <= 4 else num[:]
    
    if not isinstance(num[0], int):
        explosion = explode(num[0], level + 1)
        if explosion is not None:
            if explosion[0] is not None and explosion[1] is not None:
                num[0] = 0
            if explosion[1] is not None:
                if isinstance(num[1], int):
                    num[1] += explosion[1]
                else:
                    drill_down(num[1], 0, explosion[1])
                explosion[1] = None
            return explosion

    if not isinstance(num[1], int):
        explosion = explode(num[1], level + 1)
        if explosion is not None:
            if explosion[0] is not None and explosion[1] is not None:
                num[1] = 0
            if explosion[0] is not None:
                if isinstance(num[0], int):
                    num[0] += explosion[0]
                else:
                    drill_down(num[0], 1, explosion[0])
                explosion[0] = None
            return explosion

    return None


def split(num):
    if isinstance(num[0], int):
        if num[0] >= 10:
            num[0] = [num[0] // 2, num[0] // 2 + num[0] % 2]
            return True
    elif split(num[0]):
        return True

    if isinstance(num[1], int):
        if num[1] >= 10:
            num[1] = [num[1] // 2, num[1] // 2 + num[1] % 2]
            return True
    elif split(num[1]):
        return True

    return False


def reduce(num):
    go_on = True

    while go_on:
        go_on = False
        if explode(num) is not None:
            go_on = True
            continue
        go_on = split(num)


def magnitude(num):
    if isinstance(num, int):
        return num

    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


numbers = [line.rstrip() for line in sys.stdin]
best = 0

for index_a, line_a in enumerate(numbers):
    for index_b, line_b in enumerate(numbers):
        if index_a == index_b:
            continue

        number = [json.loads(line_a), json.loads(line_b)]
        reduce(number)
        best = max(best, magnitude(number))

print(best)
