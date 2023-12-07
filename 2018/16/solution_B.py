#!/usr/bin/env python

import re
import sys

re_before = re.compile(r'Before:\s+\[(\d+), (\d+), (\d+), (\d+)\]')
re_after = re.compile(r'After:\s+\[(\d+), (\d+), (\d+), (\d+)\]')

ADDR = 2**0
ADDI = 2**1
MULR = 2**2
MULI = 2**3
BANR = 2**4
BANI = 2**5
BORR = 2**6
BORI = 2**7
SETR = 2**8
SETI = 2**9
GTIR = 2**10
GTRI = 2**11
GTRR = 2**12
EQIR = 2**13
EQRI = 2**14
EQRR = 2**15

mapping = {opcode: 2**16 - 1 for opcode in range(0, 16)}

def perform(regs, op):
    if op[0] == ADDR:
        regs[op[3]] = regs[op[1]] + regs[op[2]]
    elif op[0] == ADDI:
        regs[op[3]] = regs[op[1]] + op[2]
    elif op[0] == MULR:
        regs[op[3]] = regs[op[1]] * regs[op[2]]
    elif op[0] == MULI:
        regs[op[3]] = regs[op[1]] * op[2]
    elif op[0] == BANR:
        regs[op[3]] = regs[op[1]] & regs[op[2]]
    elif op[0] == BANI:
        regs[op[3]] = regs[op[1]] & op[2]
    elif op[0] == BORR:
        regs[op[3]] = regs[op[1]] | regs[op[2]]
    elif op[0] == BORI:
        regs[op[3]] = regs[op[1]] | op[2]
    elif op[0] == SETR:
        regs[op[3]] = regs[op[1]]
    elif op[0] == SETI:
        regs[op[3]] = op[1]
    elif op[0] == GTIR:
        regs[op[3]] = 1 if op[1] > regs[op[2]] else 0
    elif op[0] == GTRI:
        regs[op[3]] = 1 if regs[op[1]] > op[2] else 0
    elif op[0] == GTRR:
        regs[op[3]] = 1 if regs[op[1]] > regs[op[2]] else 0
    elif op[0] == EQIR:
        regs[op[3]] = 1 if op[1] == regs[op[2]] else 0
    elif op[0] == EQRI:
        regs[op[3]] = 1 if regs[op[1]] == op[2] else 0
    elif op[0] == EQRR:
        regs[op[3]] = 1 if regs[op[1]] == regs[op[2]] else 0
    else:
        raise Exception('Unknown operation ' + op)

def match_line(regex):
    line = sys.stdin.readline().rstrip()
    match = regex.match(line)
    if not match: return None

    return [int(x) for x in match.groups()]

while True:
    before = match_line(re_before)
    if before is None: break

    op = [int(x) for x in sys.stdin.readline().split()]
    after = match_line(re_after)
    sys.stdin.readline()

    match = 0

    for opcode in (ADDR, ADDI, MULR, MULI, BANR, BANI, BORR, BORI, SETR, SETI, GTIR, GTRI, GTRR, EQIR, EQRI, EQRR):
        work = before.copy()
        perform(work, (opcode, *op[1:]))
        if work == after:
            match |= opcode

    mapping[op[0]] &= match

final_mapping = {}

while mapping:
    hit = None

    for opcode, mask in mapping.items():
        possible = 0
        for x in (ADDR, ADDI, MULR, MULI, BANR, BANI, BORR, BORI, SETR, SETI, GTIR, GTRI, GTRR, EQIR, EQRI, EQRR):
            if x & mask:
                possible += 1

        if possible == 1:
            hit = [opcode, mask]
            break

    final_mapping[hit[0]] = hit[1]
    del mapping[hit[0]]

    for opcode in mapping:
        mapping[opcode] &= ~hit[1]

registers = [0] * 4

for line in sys.stdin:
    op = [int(x) for x in line.rstrip().split()]
    if len(op) == 0:
        continue

    op[0] = final_mapping[op[0]]
    perform(registers, op)

print(registers[0])
