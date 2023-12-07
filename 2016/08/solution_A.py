#!/usr/bin/python3

import sys
import re

width = 50
height = 6
d = [ [0] * width for i in range(0, height) ]

for line in sys.stdin:
    m_obj = re.match('rect (\d+)x(\d+)', line)
    if m_obj:
        for row in range(0, int(m_obj.group(2))):
            for col in range(0, int(m_obj.group(1))):
                d[row][col] = 1;
        continue

    m_obj = re.match('rotate row y=(\d+) by (\d+)', line)
    if m_obj:
        new = [0] * width
        for col in range(0, width):
            new[(col + int(m_obj.group(2))) % width] = d[int(m_obj.group(1))][col]
        d[int(m_obj.group(1))] = new
        continue

    m_obj = re.match('rotate column x=(\d+) by (\d+)', line)
    if m_obj:
        new = [0] * height
        for row in range(0, height):
            new[(row + int(m_obj.group(2))) % height] = d[row][int(m_obj.group(1))]
        for row in range(0, height):
            d[row][int(m_obj.group(1))] = new[row]
        continue

sum = 0

for row in range(0, height):
    for col in range(0, width):
        sum += d[row][col]

print(sum)
