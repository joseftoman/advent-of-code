#!/usr/bin/env python

import re
import sys

def get_adjacent(index):
    row = index // 5
    col = index % 5

    response = []
    if col > 0:
        response.append(index - 1)
    if col < 4:
        response.append(index + 1)
    if row > 0:
        response.append(index - 5)
    if row < 4:
        response.append(index + 5)

    return response


def get_rating(layout):
    rating = 0

    for index, space in enumerate(layout):
        if space == '#':
            rating += 2 ** index

    return rating


def print_bugs(layout):
    print(layout[:5])
    print(layout[5:10])
    print(layout[10:15])
    print(layout[15:20])
    print(layout[20:])
    print()


bugs = ''
for line in sys.stdin:
    bugs += line.strip()
known = {get_rating(bugs)}

while True:
    new_bugs = ''
    for index, space in enumerate(bugs):
        bugs_around = len([True for _ in get_adjacent(index) if bugs[_] == '#'])
        if (space == '#' and bugs_around == 1) or (space == '.' and 1 <= bugs_around <= 2):
            new_bugs += '#'
        else:
            new_bugs += '.'

    bugs = new_bugs
    rating = get_rating(bugs)
    if rating in known:
        print(rating)
        break
    else:
        known.add(rating)
