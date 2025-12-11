#!/usr/bin/env python

from collections import deque
import sys


def solve(target: list[bool], buttons: list[set[int]]) -> int:
    queue = deque([(0, [False] * len(target))])

    while queue:
        steps, lights = queue.popleft()
        for group in buttons:
            next_lights = lights[:]
            for button in group:
                next_lights[button] = not next_lights[button]

            if next_lights == target:
                return steps + 1
            queue.append((steps + 1, next_lights))

    return -1  # Unreachable


def main() -> None:
    total = 0

    for line in sys.stdin:
        target = []
        buttons = []

        for token in line.strip().split():
            if token[0] == '[':
                target = [True if _ == '#' else False for _ in token[1:-1]]
            elif token[0] == '(':
                buttons.append([int(_) for _ in token[1:-1].split(',')])

        total += solve(target, buttons)

    print(total)


if __name__ == '__main__':
    main()
