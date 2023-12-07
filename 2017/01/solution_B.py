#!/usr/bin/python3

import sys

line = sys.stdin.readline().rstrip()
length = len(line)
sum = 0

for i in range(0, length):
    if line[i] == line[(i+(length >> 1)) % length]: sum += int(line[i])

print(sum)
