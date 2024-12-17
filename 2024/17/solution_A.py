#!/usr/bin/env python

import sys


def main():
    reg = [0, 0, 0]
    for i in range(3):
        reg[i] = int(next(sys.stdin).split()[-1])
    next(sys.stdin)
    program = [int(_) for _ in next(sys.stdin).split()[1].split(',')]
    pointer = 0
    out = []

    def combo(value):
        if value <= 3:
            return value
        return reg[value - 4]

    while pointer < len(program):
        jump = False
        op = program[pointer + 1]

        match program[pointer]:
            case 0:
                reg[0] = reg[0] // (2 ** combo(op))
            case 1:
                reg[1] = reg[1] ^ op
            case 2:
                reg[1] = combo(op) % 8
            case 3:
                if reg[0]:
                    jump = True
                    pointer = op
            case 4:
                reg[1] = reg[1] ^ reg[2]
            case 5:
                out.append(combo(op) % 8)
            case 6:
                reg[1] = reg[0] // (2 ** combo(op))
            case 7:
                reg[2] = reg[0] // (2 ** combo(op))

        if not jump:
            pointer += 2

    print(','.join(str(_) for _ in out))


if __name__ == '__main__':
    main()
