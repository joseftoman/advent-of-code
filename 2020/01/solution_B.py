#!/usr/bin/env python

import sys

numbers = [int(_) for _ in sys.stdin]
sums_of_two = dict()

for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if i == j:
            continue
        sums_of_two[2020 - numbers[i] - numbers[j]] = (numbers[i], numbers[j])

for num in numbers:
    if num in sums_of_two:
        print(num * sums_of_two[num][0] * sums_of_two[num][1])
        break
