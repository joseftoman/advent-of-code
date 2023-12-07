#!/usr/bin/python3

import sys

key_prefix = 'oundnydw'
#key_prefix = 'flqrgnkx'

def get_hash(key):
    lengths = [ ord(x) for x in key ] + [ 17, 31, 73, 47, 23 ]

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
        num = 0
        for j in range(0, block_size):
            num ^= items[(first + i + j) % item_count]
        output += bin(num)[2:].zfill(8)

    return output

used = 0

for i in range(0, 128):
    used += len([ ch for ch in get_hash(key_prefix+'-'+str(i)) if ch == '1' ])

print(used)
