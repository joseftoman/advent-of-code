#!/usr/bin/env python

import re
import sys

sheet = set()

while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    x, y = line.split(',')
    sheet.add((int(x), int(y)))

match = re.match('fold along (x|y)=(\d+)', sys.stdin.readline())

new_sheet = set()
for dot in sheet:
    fold = int(match.group(2))
    if match.group(1) == 'y':
        if dot[1] > fold:
            new_sheet.add((dot[0], fold - (dot[1] - fold)))
        else:
            new_sheet.add(dot)
    else:
        if dot[0] > fold:
            new_sheet.add((fold - (dot[0] - fold), dot[1]))
        else:
            new_sheet.add(dot)

print(len(new_sheet))
