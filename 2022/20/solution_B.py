#!/usr/bin/env python

import sys

dkey = 811589153


def mix(order, numbers):
    for index, item in enumerate(order):
        if item == 0:
            continue

        pos = numbers.index((item, index))
        new_pos = (pos + item) % (len(numbers) - 1)
        if new_pos > pos:
            new_pos += 1

        if new_pos >= pos:
            numbers = numbers[:pos] + numbers[pos + 1:new_pos] + [numbers[pos]] + numbers[new_pos:]
        else:
            numbers = numbers[:new_pos] + [numbers[pos]] + numbers[new_pos:pos] + numbers[pos + 1:]

    return numbers


def main():
    order = [int(line.strip()) * dkey for line in sys.stdin]
    numbers = list(zip(order, range(len(order))))

    for _ in range(10):
        numbers = mix(order, numbers)

    numbers = [_[0] for _ in numbers]
    zero = numbers.index(0)
    result = 0
    for index in [1000, 2000, 3000]:
        result += numbers[(zero + index) % len(numbers)]
    print(result)


if __name__ == '__main__':
    main()
