#!/usr/bin/env python

import re
import sys

re_before = re.compile(r'Before:\s+\[(\d+), (\d+), (\d+), (\d+)\]')
re_after = re.compile(r'After:\s+\[(\d+), (\d+), (\d+), (\d+)\]')
hits = 0

ADDR = 0
ADDI = 1
MULR = 2
MULI = 3
BANR = 4
BANI = 5
BORR = 6
BORI = 7
SETR = 8
SETI = 9
GTIR = 10
GTRI = 11
GTRR = 12
EQIR = 13
EQRI = 14
EQRR = 15

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
            match += 1

    if match >= 3:
        hits += 1

print(hits)
