#!/usr/bin/env python

from collections import defaultdict
import sys

def walk(start, end, using):
    if not using:
        return 1

    result = walk(using[0], end, using[1:])
    for i in [1, 2]:
        if i < len(using) and using[i] - start <= 3:
            result += walk(using[i], end, using[i+1:])

    if end - start <= 3:
        result += 1

    return result

adapters = [0] + sorted([int(_) for _ in sys.stdin])
result = 1
start = 0
end = 0

while start < len(adapters) - 1:
    end = start + 1
    while end < len(adapters) - 1 and adapters[end + 1] - adapters[end - 1] < 4:
        end += 1

    result *= walk(adapters[start], adapters[end], adapters[start+1:end])
    start = end

print(result)
