#!/usr/bin/python3

import sys

lengths = [ ord(x) for x in sys.stdin.readline().rstrip() ] + [ 17, 31, 73, 47, 23 ]

rounds = 64
item_count = 256
block_size = 16

items = list(range(0, item_count))
first = 0
skip = 0

for i in range(0, 64):
    for length in lengths:
        items = list(reversed(items[0:length])) + items[length:]
        items = items[(length+skip)%item_count:] + items[:(length+skip)%item_count]
        first = (first - length - skip) % item_count
        skip += 1

output = ''
for i in range(0, item_count, block_size):
    char = 0
    for j in range(0, block_size):
        char ^= items[(first + i + j) % item_count]
    output += '%02x' % char

print(output)
