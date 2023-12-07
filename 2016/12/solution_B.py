#!/usr/bin/python3

import sys
import re

regs = { 'a': 0, 'b': 0, 'c': 1, 'd': 0 }
program = []
pos = 0

for line in sys.stdin:
    m_obj = re.match('cpy (\S+) (.)', line)
    if m_obj:
        if m_obj.group(1).isdigit():
            program.append(('cpy_num', int(m_obj.group(1)), m_obj.group(2)))
        else:
            program.append(('cpy_reg', m_obj.group(1), m_obj.group(2)))
        continue

    m_obj = re.match('(inc|dec) (.)', line)
    if m_obj:
        program.append((m_obj.group(1), m_obj.group(2)))
        continue

    m_obj = re.match('jnz (\S+) (-?\d+)', line)
    if m_obj:
        if m_obj.group(1).isdigit():
            program.append(('jnz_num', int(m_obj.group(1)), int(m_obj.group(2))))
        else:
            program.append(('jnz_reg', m_obj.group(1), int(m_obj.group(2))))

        continue

    print("Unknown instruction:", line)

while pos < len(program):
    i = program[pos]

    if i[0] == 'cpy_num':
        regs[i[2]] = i[1]
    elif i[0] == 'cpy_reg':
        regs[i[2]] = regs[i[1]]
    elif i[0] == 'inc':
        regs[i[1]] += 1
    elif i[0] == 'dec':
        regs[i[1]] -= 1
    else:
        test = i[1] if i[0] == 'jnz_num' else regs[i[1]]
        if test != 0:
            pos += i[2]
            continue

    pos += 1

print(regs['a'])
