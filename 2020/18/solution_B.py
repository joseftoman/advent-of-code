#!/usr/bin/env python

import sys

total = 0

def eval_simple(parts):
    new_parts = []
    num = parts[0]
    pos = 1

    while pos < len(parts):
        if parts[pos] == '*':
            new_parts.append(num)
            num = parts[pos + 1]
        else:
            num += parts[pos + 1]

        pos += 2

    new_parts.append(num)
    
    value = 1
    for num in new_parts:
        value *= num

    return value


def evaluate(pos, expr):
    expr = expr.replace(' ', '')
    parts = []

    while pos < len(expr):
        if expr[pos] == '(':
            pos, value = evaluate(pos + 1, expr)
            parts.append(value)
        elif expr[pos] == ')':
            return pos, eval_simple(parts)
        elif expr[pos] in ['+', '*']:
            parts.append(expr[pos])
        else:
            parts.append(int(expr[pos]))

        pos += 1

    return pos, eval_simple(parts)

for line in sys.stdin:
    _, value = evaluate(0, line.strip())
    total += value

print(total)
