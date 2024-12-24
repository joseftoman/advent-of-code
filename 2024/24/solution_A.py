#!/usr/bin/env python

from graphlib import TopologicalSorter
import sys


def main():
    wires = {}
    gates = {}
    sorter = TopologicalSorter()

    read_value = True

    for line in sys.stdin:
        line = line.strip()
        if not line:
            read_value = False
            continue

        if read_value:
            wire, value = line.split(':')
            wires[wire] = int(value)
        else:
            input1, func, input2, _, output = line.split()
            gates[output] = (input1, input2, func)
            sorter.add(output, input1, input2)

    for wire in sorter.static_order():
        if wire not in gates:
            continue

        input1, input2, func = gates[wire]

        match func:
            case 'AND': wires[wire] = wires[input1] & wires[input2]
            case 'OR': wires[wire] = wires[input1] | wires[input2]
            case 'XOR': wires[wire] = wires[input1] ^ wires[input2]

    print(int('0b' + ''.join(map(lambda wire: str(wires[wire]), sorted((_ for _ in wires if _[0] == 'z'), reverse=True))), 2))


if __name__ == '__main__':
    main()
