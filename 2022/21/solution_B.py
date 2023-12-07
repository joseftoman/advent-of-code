#!/usr/bin/env python

from graphlib import TopologicalSorter
from collections import defaultdict
import math
import sys


def evaluate(resolved, rules, order):
    for node in order:
        if node == 'root':
            return resolved[rules[node][0]] - resolved[rules[node][2]]
        elif node not in resolved:
            arg1, arg2 = resolved[rules[node][0]], resolved[rules[node][2]]
            operator = rules[node][1]

            if operator == '+':
                resolved[node] = arg1 + arg2
            elif operator == '-':
                resolved[node] = arg1 - arg2
            elif operator == '*':
                resolved[node] = arg1 * arg2
            elif operator == '/':
                resolved[node] = arg1 // arg2


def main():
    resolved = {}
    rules = {}
    graph = defaultdict(set)

    for line in sys.stdin:
        tokens = line.strip().split()
        name = tokens[0][:-1]
        if len(tokens) == 2:
            resolved[name] = int(tokens[1])
        else:
            rules[name] = tokens[1:]
            graph[name].add(tokens[1])
            graph[name].add(tokens[3])

    sorter = TopologicalSorter(graph)
    order = list(sorter.static_order())

    def test(humn):
        copy_of_resolved = {**resolved}
        copy_of_resolved['humn'] = humn
        return evaluate(copy_of_resolved, rules, order)

    left, middle, right = test(-10), test(0), test(10)
    if math.copysign(1, left) != math.copysign(1, right):
        for humn in range(-10, 11):
            if test(humn) == 0:
                print(humn)
                return
    humn_sign = -1 if abs(left) < abs(right) else 1
    incr_sign = int(math.copysign(1, middle))
    
    exp = 5
    while True:
        result = test(humn_sign * 2**exp)
        if result == 0:
            print(2**exp)
            return
        if incr_sign * result < 0:
            break
        exp += 5

    exp -= 1
    humn = humn_sign * 2**exp
    while True:
        result = test(humn)
        if result == 0:
            break

        exp -= 1
        if result > 0:
            humn += incr_sign * 2**exp
        else:
            humn -= incr_sign * 2**exp

    print(humn)


if __name__ == '__main__':
    main()
