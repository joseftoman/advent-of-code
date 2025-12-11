#!/usr/bin/env python

import sys

from scipy.optimize import linprog


def solve(target: list[int], buttons: list[set[int]]) -> int:
    # The objective function we want to minimize is a simple sum of the number of times each button is pressed
    objective = [1] * len(buttons)

    # Each joltage counter is used to form an equation.
    # Right-hand-side vector are the required joltage levels
    rhs = target

    lhs = []
    for counter in range(len(target)):
        lhs.append([1 if counter in button else 0 for button in buttons])

    result = linprog(c=objective, A_eq=lhs, b_eq=rhs, integrality=1)
    return int(result.fun)


def main() -> None:
    total = 0

    for line in sys.stdin:
        target = []
        buttons = []

        for token in line.strip().split():
            if token[0] == '{':
                target = [int(_) for _ in token[1:-1].split(',')]
            elif token[0] == '(':
                buttons.append({int(_) for _ in token[1:-1].split(',')})

        total += solve(target, buttons)

    print(total)


if __name__ == '__main__':
    main()
