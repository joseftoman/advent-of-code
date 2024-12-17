#!/usr/bin/env python

import sys

# Fast solution probably does not exist for all possible inputs.
# This is how it works:
# - analyse what the input program is actually doing
# - build a program that works for a single input only
# - this specific input program is running start-to-end loops, doing this:
#   - shifts A by 3 bits to the right
#   - outputs a single 3-bit digit
#   - loops back to start
#
# Given special properties of bitwise operations carried out by the program,
# it's possible to construct the required register value iteratively, one base-8 digit
# per program position.
# Sadly, a single isolated step can be ambiguous. We need to explore the whole
# state space. Also, there are multiple solutions. We need to find them all and pick
# the lowest.


def get_next(register, digit):
    for guess in range(8):
        b = ((register * 8 + guess) % 8) ^ 2
        c = (register * 8 + guess) >> b
        if (b ^ c ^ 7) % 8 == digit:
            yield guess


def main():
    program = [2, 4, 1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]
    stack = [[]]
    output = None

    while stack:
        exps = stack.pop()
        reg_a = 0
        for i, exp in enumerate(exps):
            reg_a += exp * (8 ** (len(exps) - i - 1))

        for guess in get_next(reg_a, program[-1 * (len(exps) + 1)]):
            if len(exps) == len(program) - 1:
                final_value = reg_a * 8 + guess
                output = min(output or final_value, final_value)
            else:
                stack.append([*exps, guess])

    print(output)


if __name__ == '__main__':
    main()
