#!/usr/bin/python3

steps = 386
last = 2017
buff = [0]
curr = 1
pos = 0

while curr <= last:
    pos = ((pos + steps) % curr)
    buff = buff[0:pos+1] + [curr] + buff[pos+1:]
    pos += 1
    curr += 1

print(buff[(pos + 1) % curr])
