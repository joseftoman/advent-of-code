#!/usr/bin/env python

import sys


def is_true(test_value, numbers):
    if len(numbers) == 1:
        return test_value == numbers[0]

    return (
        is_true(test_value, [numbers[0] + numbers[1], *numbers[2:]])
        or is_true(test_value, [numbers[0] * numbers[1], *numbers[2:]])
        or is_true(test_value, [int(f'{numbers[0]}{numbers[1]}'), *numbers[2:]])
    )


def main():
    total = 0

    for line in sys.stdin:
        left, right = line.split(':')
        test_value = int(left)
        numbers = list(map(int, right.split()))

        if is_true(test_value, numbers):
            total += test_value
    
    print(total)


if __name__ == '__main__':
    main()
