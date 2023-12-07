#!/usr/bin/python3

import sys

steps = {
    '1': { 'D': '3' },
    '2': { 'R': '3', 'D': '6' },
    '3': { 'L': '2', 'R': '4', 'U': '1', 'D': '7' },
    '4': { 'L': '3', 'D': '8' },
    '5': { 'R': '6' },
    '6': { 'L': '5', 'R': '7', 'U': '2', 'D': 'A' },
    '7': { 'L': '6', 'R': '8', 'U': '3', 'D': 'B' },
    '8': { 'L': '7', 'R': '9', 'U': '4', 'D': 'C' },
    '9': { 'L': '8' },
    'A': { 'R': 'B', 'U': '6' },
    'B': { 'L': 'A', 'R': 'C', 'U': '7', 'D': 'D' },
    'C': { 'L': 'B', 'U': '8' },
    'D': { 'U': 'B' }
}
pos = '5'
code = ''

for line in [ l.rstrip() for l in sys.stdin ]:
    for dir in line:
        if dir in steps[pos]: pos = steps[pos][dir]

    code += pos

print(code)
