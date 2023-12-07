#!/usr/bin/python3

import sys
from collections import deque

key_prefix = 'oundnydw'
#key_prefix = 'flqrgnkx'
grid_size = 128
hash_rounds = 64

def get_hash(key):
    lengths = [ ord(x) for x in key ] + [ 17, 31, 73, 47, 23 ]

    item_count = 2 * grid_size
    block_size = 16

    items = list(range(0, item_count))
    first = 0
    skip = 0

    for i in range(0, hash_rounds):
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

regions = 0
grid = []

def mark_region(x, y):
    queue = deque([(x, y)])
    diffs = ( (-1, 0), (1, 0), (0, -1), (0, 1) )

    while queue:
        pos = queue.popleft()
        grid[pos[0]][pos[1]] = '0'

        for d in diffs:
            x = pos[0] + d[0]
            y = pos[1] + d[1]
            if x >= 0 and x < grid_size and y >= 0 and y < grid_size and grid[x][y] == '1':
                queue.append((x, y))

for i in range(0, grid_size):
    grid.append([ ch for ch in get_hash(key_prefix+'-'+str(i)) ])

for x in range(0, grid_size):
    for y in range(0, grid_size):
        if grid[x][y] == '1':
            regions += 1
            mark_region(x, y)

print(regions)
