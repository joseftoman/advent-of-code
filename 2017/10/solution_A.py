#!/usr/bin/python3

import sys

lengths = [ int(x) for x in sys.stdin.readline().rstrip().split(',') ]

item_count = 256
items = list(range(0, item_count))
first = 0
skip = 0

for length in lengths:
    items = list(reversed(items[0:length])) + items[length:]
    items = items[(length+skip)%item_count:] + items[:(length+skip)%item_count]
    first = (first - length - skip) % item_count
    skip += 1

print(items[first] * items[(first+1)%item_count])
