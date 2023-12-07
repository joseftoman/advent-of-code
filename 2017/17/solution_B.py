#!/usr/bin/python3

steps = 386
last = int(5e7)
after_zero = None
curr = 1
pos = 0

while curr <= last:
    pos = ((pos + steps) % curr)
    if pos == 0:
        after_zero = curr
    pos += 1
    curr += 1

print(after_zero)
