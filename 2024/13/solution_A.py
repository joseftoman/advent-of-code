#!/usr/bin/env python

import sys


def machines():
    machine = {}
    mapping = {'Button A': 'a', 'Button B': 'b', 'Prize': 'p'}

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        name, numbers = line.split(':')
        x, y = [int(_.strip()[2:]) for _ in numbers.split(',')]
        machine[mapping[name]] = (x, y)
        if name == 'Prize':
            yield machine


def main():
    tokens = 0

    for machine in machines():
        a_x, a_y = machine['a']
        b_x, b_y = machine['b']
        p_x, p_y = machine['p']

        b = (p_y * a_x - p_x * a_y) // (a_x * b_y - a_y * b_x)
        a = (p_x - b_x * b) // a_x

        if a * a_x + b * b_x == p_x and a * a_y + b * b_y == p_y:
            tokens += a * 3 + b

    print(tokens)


if __name__ == '__main__':
    main()
