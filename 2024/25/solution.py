#!/usr/bin/env python

from collections import defaultdict
import sys

PINS = 5
PIN_SIZE = 5


def main():
    locks = defaultdict(int)
    keys = defaultdict(int)
    fits = 0

    while True:
        rows = [next(sys.stdin).strip() for _ in range(PIN_SIZE + 2)]
        is_lock = rows[0][0] == '#'

        vector = tuple(map(lambda col: max(row for row in range(PIN_SIZE + 1) if rows[row][col] == rows[0][0]), (_ for _ in range(PINS))))
        if not is_lock:
            vector = tuple(PIN_SIZE - _ for _ in vector)

        (locks if is_lock else keys)[vector] += 1

        try:
            next(sys.stdin)
        except StopIteration:
            break

    for key, key_amount in keys.items():
        for lock, lock_amount in locks.items():
            if max(key[_] + lock[_] for _ in range(PINS)) <= PIN_SIZE:
                fits += key_amount * lock_amount

    print(fits)


if __name__ == '__main__':
    main()
