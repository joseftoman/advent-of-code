#!/usr/bin/python3

import sys

line = sys.stdin.readline().rstrip()
line = line + line[0]
sum = 0

for i in range(0, len(line) - 1):
    if line[i] == line[i+1]: sum += int(line[i])

print(sum)
