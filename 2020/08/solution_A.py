#!/usr/bin/env python

import sys

def read_program():
    program = []

    for line in sys.stdin:
        pair = line.strip().split()
        pair[1] = int(pair[1])
        program.append(pair)

    return program

acc = 0
pos = 0
used = set()
program = read_program()

while True:
    used.add(pos)

    if program[pos][0] == 'acc':
        acc += program[pos][1]

    if program[pos][0] == 'jmp':
        pos += program[pos][1]
    else:
        pos += 1

    if pos in used:
        print(acc)
        break
