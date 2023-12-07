#!/usr/bin/python3

import sys
import re

regs = { 'a': 7, 'b': 0, 'c': 0, 'd': 0 }
program = []
pos = 0

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

    m_obj = re.match('tgl (.)', line)
    if m_obj:
        program.append(['tgl', m_obj.group(1)])
        continue

    print("Unknown instruction:", line)

while pos < len(program):
    #print(pos, program)
    #print(regs)
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
    elif i[0] == 'tgl':
        rel = regs[i[1]] if i[1].isalpha() else int(i[1])
        target = pos + rel
        if target >= 0 and target < len(program):
            i = program[target]
            if i[0] == 'cpy':
                i[0] = 'jnz'
            elif i[0] == 'inc':
                i[0] = 'dec'
            elif i[0] == 'dec':
                i[0] = 'inc'
            elif i[0] == 'tgl':
                i[0] = 'inc'
            elif i[0] == 'jnz':
                i[0] = 'cpy'
    elif i[0] == 'jnz':
        test = regs[i[1]] if i[1].isalpha() else int(i[1])
        if test != 0:
            rel = regs[i[2]] if i[2].isalpha() else int(i[2])
            pos += rel
            continue

    pos += 1

#print(pos, program)
#print(regs)
print(regs['a'])
