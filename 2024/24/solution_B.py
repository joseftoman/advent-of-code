#!/usr/bin/env python

r"""
Schema of the N-th step of the adder:

      xN |   | yN
         |   |
         |   |
        /\  / \
       |  \/  |
       |  /\  |
       | /  \ |
       |/    \|
     /---\  /---\
     |AND|  |XOR|
     \---/  \---/                    |
       |      |  ______ carry(N-1) <--
       |     / \/     /
       |    /  /\    /
       |   /  /  \  /
       |   | /   | /
       |   |/    |/
       | /---\ /---\
       | |AND| |XOR|
       | \---/ \---/
       |   |     |
       |   /     | zN
       |  /
       | /
       |/
     /---\
     |OR |
     \---/
       |
       | carry(N)
     <--

We are looking for places where the input structure does not match the expected schema.
"""

from collections import defaultdict
import sys

EXPECTED_MISPLACED_WIRES = 8


def main():
    output_to_gate = {}
    input_to_gate = defaultdict(dict)
    width = 0
    wrong = set()

    read_gate = False

    for line in sys.stdin:
        line = line.strip()

        if not line:
            read_gate = True
            continue
        if not read_gate:
            continue

        input1, gate, input2, _, output = line.split()
        output_to_gate[output] = (input1, input2, gate)
        input_to_gate[input1][gate] = (input2, output)
        input_to_gate[input2][gate] = (input1, output)

        for wire in [input1, input2]:
            if wire[0] == 'x':
                width = max(width, int(wire[1:]))

    carry = input_to_gate['x00']['AND'][1]

    for pos in range(1, width + 1):
        x_wire = f'x{pos:02}'
        z_wire = f'z{pos:02}'

        top_and_output = input_to_gate[x_wire]['AND'][1]
        top_xor_output = input_to_gate[x_wire]['XOR'][1]
        bottom_and_output = None

        if len(input_to_gate[top_and_output]) != 1 or list(input_to_gate[top_and_output])[0] != 'OR':
            # print(f'Problem [{pos:02}]: Top AND output ({top_and_output}) not followed by OR')
            wrong.add(top_and_output)
            top_and_output = None

        if len(input_to_gate[top_xor_output]) != 2 or set(input_to_gate[top_xor_output].keys()) != {'AND', 'XOR'}:
            # print(f'Problem [{pos:02}]: Top XOR output ({top_xor_output}) not forking into AND + XOR')
            wrong.add(top_xor_output)
            top_xor_output = None

        if output_to_gate[z_wire][2] != 'XOR' or output_to_gate[z_wire][0][0] in {'x', 'y'}:
            # print(f'Problem [{pos:02}]: Z-wire is misplaced')
            wrong.add(z_wire)

        if carry is not None:
            correct = top_xor_output is not None
            xor_operand = input_to_gate[carry].get('XOR', (None, None))[0]
            and_operand = input_to_gate[carry].get('AND', (None, None))[0]

            if xor_operand != and_operand:
                # print(f'Problem [{pos:02}]: {carry=} + operand mismatch')
                wrong.add(carry)
                correct = False
            if correct and xor_operand != top_xor_output:
                # print(f'Ambiguous problem [{pos:02}]: carry operand {xor_operand} != top XOR output {top_xor_output}')
                correct = False
            if correct and z_wire not in wrong and {xor_operand, carry} != set(output_to_gate[z_wire][:2]):
                # print(f'Ambiguous problem [{pos:02}]: Z-wire operands mismatch')
                correct = False

            if correct:
                bottom_and_output = input_to_gate[top_xor_output]['AND'][1]
                if len(input_to_gate[bottom_and_output]) != 1 or list(input_to_gate[bottom_and_output])[0] != 'OR':
                    # print(f'Problem [{pos:02}]: Bottom AND output ({bottom_and_output}) not followed by OR')
                    wrong.add(bottom_and_output)
                    bottom_and_output = None

                bottom_xor_output = input_to_gate[xor_operand]['XOR'][1]
                if bottom_xor_output != z_wire:
                    # print(f'Problem [{pos:02}]: {bottom_xor_output} produced instead of a z-wire')
                    wrong.add(bottom_xor_output)

        if top_and_output is None and bottom_and_output is not None:
            missing = input_to_gate[bottom_and_output]['OR'][0]
            # print(f'Problem [{pos:02}]: {missing} expected as top AND output but missing')
            wrong.add(missing)
            top_and_output = missing

        carry = None
        if top_and_output is not None and bottom_and_output is not None:
            test_against, carry = input_to_gate[top_and_output]['OR']
            if test_against != bottom_and_output:
                # print(f'Ambiguous problem [{pos:02}]: Carry operands mismatch')
                carry = None
            if carry in wrong:
                carry = None
        if carry is None and top_and_output is not None:
            carry = input_to_gate[top_and_output]['OR'][1]
            if carry in wrong:
                carry = None
        if carry is None and bottom_and_output is not None:
            carry = input_to_gate[bottom_and_output]['OR'][1]
            if carry in wrong:
                carry = None

    if len(wrong) == EXPECTED_MISPLACED_WIRES:
        print(','.join(sorted(wrong)))
    else:
        print('Not good enough')


if __name__ == '__main__':
    main()
