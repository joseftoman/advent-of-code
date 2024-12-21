#!/usr/bin/env python

from functools import lru_cache
import re
import sys

INTERMEDIARIES = 25


@lru_cache(maxsize=20000)
def expand_arrows(arrows, level):
    transitions = {
        '^A': '>',
        '^<': 'v<',
        '^v': 'v',
        '^>': 'v>',

        'A^': '<',
        'A<': 'v<<',
        'Av': '<v',
        'A>': 'v',

        '<^': '>^',
        '<A': '>>^',
        '<v': '>',
        '<>': '>>',

        'v^': '^',
        'vA': '^>',
        'v<': '<',
        'v>': '>',

        '>^': '<^',
        '>A': '^',
        '><': '<<',
        '>v': '<',
    }
    total = 0

    for chunk in re.findall('[^A]*A', arrows):
        padded = 'A' + chunk
        expanded = ''.join(transitions.get(padded[index:index + 2], '') + 'A' for index in range(len(chunk)))

        if level == 1:
            total += len(expanded)
        else:
            total += expand_arrows(expanded, level - 1)

    return total


def navigate_numbers(code):
    keypad = {
        '7': (0, 0), '8': (1, 0), '9': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '1': (0, 2), '2': (1, 2), '3': (2, 2),
                     '0': (1, 3), 'A': (2, 3),
    }

    output = ''
    pos = keypad['A']

    for char in code:
        target = keypad[char]

        if pos[0] == target[0] or pos[1] == target[1]:
            if pos[0] == target[0]:
                char = '^' if target[1] < pos[1] else 'v'
            else:
                char = '<' if target[0] < pos[0] else '>'
            output += ''.join([char] * abs(target[0] - pos[0] + target[1] - pos[1]))
            output += 'A'
            pos = target
            continue

        start_vertically = target[0] > pos[0]

        if not start_vertically and target[1] < pos[1] and pos[1] == 3 and target[0] == 0:
            start_vertically = True
        if start_vertically and target[1] > pos[1] and pos[0] == 0 and target[1] == 3:
            start_vertically = False

        if start_vertically:
            output += ''.join(['^' if target[1] < pos[1] else 'v'] * abs(target[1] - pos[1]))
        output += ''.join(['<' if target[0] < pos[0] else '>'] * abs(target[0] - pos[0]))
        if not start_vertically:
            output += ''.join(['^' if target[1] < pos[1] else 'v'] * abs(target[1] - pos[1]))

        output += 'A'
        pos = target

    return output


def complexity(code):
    arrows = navigate_numbers(code)
    length = expand_arrows(arrows, INTERMEDIARIES)

    return length * int(code[:-1])


def main():
    print(sum(complexity(_.strip()) for _ in sys.stdin))


if __name__ == '__main__':
    main()
