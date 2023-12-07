#!/usr/bin/env python

import sys

signal = sys.stdin.readline().strip()
offset = int(signal[:7])

tail_len = len(signal) * 10000 - offset
tail = signal * (((tail_len - 1) // len(signal)) + 1)
tail = [int(_) for _ in tail[-tail_len:]]
tail.reverse()

for step in range(100):
    new_tail = [tail[0]]
    for digit in tail[1:]:
        new_tail.append((digit + new_tail[-1]) % 10)
    tail = new_tail

print(''.join(str(_) for _ in reversed(tail[-8:])))
