#!/usr/bin/python3

limit = 7 * 365
num = 0

while num < limit:
    if num % 2 == 0:
        num = 2 * num + 1
    else:
        num *= 2

print(num - limit)
