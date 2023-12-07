#!/usr/bin/env python

import sys


five_to_ten = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
ten_to_five = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}

numbers = [line.strip()[::-1] for line in sys.stdin]
max_power = max(len(_) for _ in numbers)
output = ''
power = 0
carry_on = 0

while power < max_power or carry_on:
    power_sum = sum(0 if len(item) <= power else five_to_ten[item[power]] for item in numbers) + carry_on
    output += ten_to_five[power_sum % 5]
    carry_on = (power_sum + 2) // 5
    power += 1

print(output[::-1])
