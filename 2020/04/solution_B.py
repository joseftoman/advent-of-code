#!/usr/bin/env python

import re
import sys


hcl_regex = re.compile(r'^#[0-9a-f]{6}$')
pid_regex = re.compile(r'^\d{9}$')
eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

left = required.copy()
valid = 0


def check_field(field, value):
    if field == 'byr':
        return len(value) == 4 and 1920 <= int(value) <= 2002

    if field == 'iyr':
        return len(value) == 4 and 2010 <= int(value) <= 2020

    if field == 'eyr':
        return len(value) == 4 and 2020 <= int(value) <= 2030

    if field == 'hgt':
        if len(value) < 3:
            return False
        unit = value[-2:]
        num = int(value[:-2])
        return (unit == 'cm' and 150 <= num <= 193) or (unit == 'in' and 59 <= num <= 76)

    if field == 'hcl':
        return bool(hcl_regex.match(value))

    if field == 'ecl':
        return value in eye_colors

    if field == 'pid':
        return bool(pid_regex.match(value))

    return False


for line in sys.stdin:
    line = line.strip()
    if not line:
        if not left:
            valid += 1
        left = required.copy()
        continue

    for token in line.split():
        field, value = token.split(':')
        if field == 'cid':
            continue

        if check_field(field, value):
            left.remove(field)

if not left:
    valid += 1

print(valid)
