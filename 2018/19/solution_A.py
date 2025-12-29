#!/usr/bin/env python

import sys


def perform(regs, op):
    if op[0] == 'addr':
        regs[op[3]] = regs[op[1]] + regs[op[2]]
    elif op[0] == 'addi':
        regs[op[3]] = regs[op[1]] + op[2]
    elif op[0] == 'mulr':
        regs[op[3]] = regs[op[1]] * regs[op[2]]
    elif op[0] == 'muli':
        regs[op[3]] = regs[op[1]] * op[2]
    elif op[0] == 'banr':
        regs[op[3]] = regs[op[1]] & regs[op[2]]
    elif op[0] == 'bani':
        regs[op[3]] = regs[op[1]] & op[2]
    elif op[0] == 'borr':
        regs[op[3]] = regs[op[1]] | regs[op[2]]
    elif op[0] == 'bori':
        regs[op[3]] = regs[op[1]] | op[2]
    elif op[0] == 'setr':
        regs[op[3]] = regs[op[1]]
    elif op[0] == 'seti':
        regs[op[3]] = op[1]
    elif op[0] == 'gtir':
        regs[op[3]] = 1 if op[1] > regs[op[2]] else 0
    elif op[0] == 'gtri':
        regs[op[3]] = 1 if regs[op[1]] > op[2] else 0
    elif op[0] == 'gtrr':
        regs[op[3]] = 1 if regs[op[1]] > regs[op[2]] else 0
    elif op[0] == 'eqir':
        regs[op[3]] = 1 if op[1] == regs[op[2]] else 0
    elif op[0] == 'eqri':
        regs[op[3]] = 1 if regs[op[1]] == op[2] else 0
    elif op[0] == 'eqrr':
        regs[op[3]] = 1 if regs[op[1]] == regs[op[2]] else 0
    else:
        raise Exception('Unknown operation ' + op)


def main():
    registers = [0] * 6
    instructions = []
    ip = 0
    ip_binding = None

    for line in sys.stdin:
        tokens = line.strip().split()
        if tokens[0] == '#ip':
            ip_binding = int(tokens[1])
        else:
            instructions.append((tokens[0], *[int(_) for _ in tokens[1:]]))

    while 0 <= ip < len(instructions):
        registers[ip_binding] = ip
        perform(registers, instructions[ip])
        ip = registers[ip_binding]
        ip += 1

    print(registers[0])


if __name__ == '__main__':
    main()
