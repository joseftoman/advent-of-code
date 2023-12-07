#!/usr/bin/python3

import sys
input = int(sys.argv[1])

if input == 1:
    print(0)
    exit()

prev = 1
edge = 2

while input > prev + 4 * edge:
    prev += 4 * edge
    edge += 2

pos = (input - prev - 1) % edge
steps = int(abs(pos - (edge / 2 - 1)) + edge / 2)

print(steps)
