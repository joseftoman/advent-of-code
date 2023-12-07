#!/usr/bin/env python

import sys

def read_program():
    program = []

    for line in sys.stdin:
        pair = line.strip().split()
        pair[1] = int(pair[1])
        program.append(pair)

    return program

def execute_program(program):
    acc = 0
    pos = 0
    used = set()

    while True:
        used.add(pos)

        if program[pos][0] == 'acc':
            acc += program[pos][1]

        if program[pos][0] == 'jmp':
            pos += program[pos][1]
        else:
            pos += 1

        if pos in used or pos > len(program):
            return None
        if pos == len(program):
            return acc

change_pos = 0
original = read_program()

while change_pos < len(original):
    if original[change_pos][0] in ['jmp', 'nop']:
        copy = original[:]
        copy[change_pos] = ['jmp' if original[change_pos][0] == 'nop' else 'nop', original[change_pos][1]]
        result = execute_program(copy)
        if result is not None:
            print(result)
            break

    change_pos += 1
