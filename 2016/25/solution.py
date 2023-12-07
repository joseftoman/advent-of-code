#!/usr/bin/python3

import sys
import re
import itertools

program = []

for line in sys.stdin:
    m_obj = re.match('cpy (\S+) (.)', line)
    if m_obj:
        program.append(['cpy', m_obj.group(1), m_obj.group(2)])
        continue

    m_obj = re.match('(inc|dec) (.)', line)
    if m_obj:
        program.append([m_obj.group(1), m_obj.group(2)])
        continue

    m_obj = re.match('jnz (\S+) (\S+)', line)
    if m_obj:
        program.append(['jnz', m_obj.group(1), m_obj.group(2)])
        continue

    m_obj = re.match('out (.)', line)
    if m_obj:
        program.append(['out', m_obj.group(1)])
        continue

    m_obj = re.match('mlt (.) (\S+) (.) (.)', line)
    # R1 += R2 * R3; R3 = R4 = 0
    if m_obj:
        program.append(['mlt', m_obj.group(1), m_obj.group(2), m_obj.group(3), m_obj.group(4)])
        continue

    print("Unknown instruction:", line)

for init in itertools.count():
    regs = { 'a': init, 'b': 0, 'c': 0, 'd': 0 }
    pos = 0
    next_out = 0
    ok = 0

    while ok < 100 and pos < len(program):
        i = program[pos]

        if i[0] == 'cpy':
            if i[2].isalpha():
                if i[1].isalpha():
                    regs[i[2]] = regs[i[1]]
                else:
                    regs[i[2]] = int(i[1])
        elif i[0] == 'inc':
            if i[1].isalpha():
                regs[i[1]] += 1
        elif i[0] == 'dec':
            if i[1].isalpha():
                regs[i[1]] -= 1
        elif i[0] == 'mlt':
            q = regs[i[2]] if i[2].isalpha() else int(i[2])
            regs[i[1]] += q * regs[i[3]];
            regs[i[3]] = regs[i[4]] = 0
        elif i[0] == 'out':
            if regs[i[1]] == next_out:
                ok += 1
                next_out = (next_out + 1) % 2
            else:
                break
        elif i[0] == 'jnz':
            test = regs[i[1]] if i[1].isalpha() else int(i[1])
            if test != 0:
                rel = regs[i[2]] if i[2].isalpha() else int(i[2])
                pos += rel
                continue

        pos += 1

    if ok >= 100:
        print(init)
        break
