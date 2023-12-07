#!/usr/bin/env python

import math
import sys

numbers = [[int(_.strip()), False] for _ in sys.stdin]
pos = 0
#print(numbers)

for _ in range(len(numbers)):
    numbers[pos][1] = True
    if numbers[pos][0] == 0:
        #print('--- zero ---')
        pos += 1
    else:
        shift = numbers[pos][0]
        shift += int(math.copysign(abs(shift) // len(numbers), shift))
        new_pos = (pos + shift) % len(numbers)
        if numbers[pos][0] > 0:
            new_pos = (new_pos + 1) % len(numbers)

        #print(pos, ':', numbers[pos][0], '->', new_pos)

        if new_pos >= pos:
            numbers = numbers[:pos] + numbers[pos + 1:new_pos] + [numbers[pos]] + numbers[new_pos:]
        else:
            numbers = numbers[:new_pos] + [numbers[pos]] + numbers[new_pos:pos] + numbers[pos + 1:]
            pos += 1

    while pos < len(numbers) and numbers[pos][1]:
        pos += 1
    #print(numbers)

numbers = [_[0] for _ in numbers]
zero = numbers.index(0)
result = 0
for index in [1000, 2000, 3000]:
    result += numbers[(zero + index) % len(numbers)]
print(result)
