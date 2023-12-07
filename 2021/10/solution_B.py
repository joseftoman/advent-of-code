#!/usr/bin/env python

import statistics
import sys

start = {'(': 1, '[': 2, '{': 3, '<': 4}
end = {')': '(', ']': '[', '}': '{', '>': '<'}
scores = []

for line in sys.stdin:
    stack = []
    error = False
    for char in line.rstrip():
        if char in start:
            stack.append(char)
        else:
            if stack[-1] == end[char]:
                stack.pop()
            else:
                error = True
                break

    if stack and not error:
        score = 0
        for char in reversed(stack):
            score = score * 5 + start[char]
        scores.append(score)

print(statistics.median(scores))
