#!/usr/bin/env python

import sys

"""
This is what the system is actually doing:
- register #3 is the instruction pointer
- registers #2 and #5 are low-level intermediate storage
- register #4 is a loop variable
- registers #1 is being mutated over time and yields a sequence of integers
- system halts when a new integer yielded from register #1 matches register #0, which stays constant.

Below are important parts using this notation - "<#instruction>: operation".
Square brackets are registers.

-----
5: [1] = 0

6: [4] = [1] | 65536
7: [1] = 3798839

8-9: [1] += [4] & 255 # [1] += [4] % (2 ** 8)
10: [1] &= 16777215   # [1] %= 2 ** 24
11: [1] *= 65899
12: [1] &= 16777215   # [1] %= 2 ** 24

while [4] >= 256:
    [4] //= 256
    run 8..12

YIELD [1]
skip to instruction no. 6
-----

To solve the task, we need to keep the system going until it starts repeating itself.
"""


def mutate(a, b):
    return (((a + (b % 256)) % 16777216) * 65899) % 16777216


def main():
    producer = 0
    iterator = 0

    seen = set()
    last = 0

    while True:
        iterator = producer | 65536
        producer = mutate(3798839, iterator)

        while iterator >= 256:
            iterator //= 256
            producer = mutate(producer, iterator)

        if producer in seen:
            print(last)
            break
        seen.add(producer)
        last = producer


if __name__ == '__main__':
    main()
