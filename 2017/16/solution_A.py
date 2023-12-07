#!/usr/bin/python3

import string
import sys
import re

dancers = 16
progs = list(string.ascii_lowercase[:dancers]) 
dance = sys.stdin.readline().rstrip().split(',')

for move in dance:
    m = re.match(r's(\d+)$', move)
    if m:
        num = int(m.group(1))
        progs = progs[-num:] + progs[:-num]
        continue
    
    m = re.match(r'x(\d+)/(\d+)$', move)
    if m:
        pos = [ int(x) for x in m.groups() ]
        prog = progs[pos[0]]
        progs[pos[0]] = progs[pos[1]]
        progs[pos[1]] = prog
        continue

    m = re.match(r'p(\w)/(\w)$', move)
    if m:
        for i in range(0, dancers):
            if progs[i] == m.group(1):
                progs[i] = m.group(2)
            elif progs[i] == m.group(2):
                progs[i] = m.group(1)

print(''.join(progs))
