#!/usr/bin/env python

import sys

total = 0

def evaluate(pos, expr):
    expr = expr.replace(' ', '')
    value = None
    op = None

    while pos < len(expr):
        if expr[pos] in ['+', '*']:
            op = expr[pos]
        elif expr[pos] == ')':
            return pos, value
        else:
            if expr[pos] == '(':
                pos, right = evaluate(pos + 1, expr)
            else:
                right = int(expr[pos])

            if op == '*':
                value = value * right
            elif op == '+':
                value = value + right
            else:
                value = right

        #print(pos, op, value)
        pos += 1

    return pos, value

for line in sys.stdin:
    _, value = evaluate(0, line.strip())
    total += value

print(total)
