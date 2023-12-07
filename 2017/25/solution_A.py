#!/usr/bin/python3

import sys
import re

program = {}

m = re.match(r'Begin in state ([A-Z]+)', sys.stdin.readline())
state = m.group(1)

m = re.match(r'Perform a diagnostic checksum after (\d+)', sys.stdin.readline())
steps = int(m.group(1))

while sys.stdin.readline():
    m = re.match(r'In state ([A-Z]+)', sys.stdin.readline())
    s = m.group(1)

    sys.stdin.readline()
    m = re.search(r'Write the value (0|1)', sys.stdin.readline())
    w0 = int(m.group(1))
    m = re.search(r'Move one slot to the (left|right)', sys.stdin.readline())
    m0 = -1 if m.group(1) == 'left' else 1
    m = re.search(r'Continue with state ([A-Z]+)', sys.stdin.readline())
    s0 = m.group(1)

    sys.stdin.readline()
    m = re.search(r'Write the value (0|1)', sys.stdin.readline())
    w1 = int(m.group(1))
    m = re.search(r'Move one slot to the (left|right)', sys.stdin.readline())
    m1 = -1 if m.group(1) == 'left' else 1
    m = re.search(r'Continue with state ([A-Z]+)', sys.stdin.readline())
    s1 = m.group(1)

    program[s] = ( (w0, m0, s0), (w1, m1, s1) )

pos = 0
data = {}

while steps > 0:
    steps -= 1
    if pos not in data: data[pos] = 0
    i = program[state][data[pos]]

    data[pos] = i[0]
    pos += i[1]
    state = i[2]

print(sum(data.values()))
