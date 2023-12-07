#!/usr/bin/env python

import sys

start = {'(', '[', '{', '<'}
end = {')': ('(', 3), ']': ('[', 57), '}': ('{', 1197), '>': ('<', 25137)}
score = 0

for line in sys.stdin:
    stack = []
    for char in line.rstrip():
        if char in start:
            stack.append(char)
        else:
            if stack[-1] == end[char][0]:
                stack.pop()
            else:
                score += end[char][1]
                break

print(score)
