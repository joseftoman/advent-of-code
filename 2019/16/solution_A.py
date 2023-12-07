#!/usr/bin/env python

import sys

def get_coef(output_pos, input_pos):
    return (0, 1, 0, -1)[((input_pos + 1) // (output_pos + 1)) % 4]

signal = [int(_) for _ in sys.stdin.readline().strip()]

for step in range(100):
    new_signal = []

    for i in range(len(signal)):
        total = 0
        for j, digit in enumerate(signal):
            total += digit * get_coef(i, j)
        new_signal.append(abs(total) % 10)

    signal = new_signal

print(''.join(str(_) for _ in signal[:8]))
