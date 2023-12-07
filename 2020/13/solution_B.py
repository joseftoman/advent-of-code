#!/usr/bin/env python

import math
import sys

sys.stdin.readline()
buses = [(offset, int(bus)) for offset, bus in enumerate(sys.stdin.readline().strip().split(',')) if bus != 'x']
time = 0
period = buses[0][1]

for target_offset, interval in buses[1:]:
    local_period = max(period, interval)
    local_mod = min(period, interval)
    local_offset = target_offset % local_mod
    mult = 0

    if interval > period:
        increment = interval % period
    else:
        increment = math.ceil(period / interval) * interval - period
    offset = math.ceil(time / interval) * interval - time

    if interval > period and offset > 0:
        mult = 1
    if offset > local_mod:
        time += math.floor(offset / local_mod) * local_mod
        offset %= local_mod

    #print(f'Bus {interval}/{target_offset}->{local_offset}: INC = {increment}, PER = {local_period}, OFF = {offset}, TIM = {time}, MUL = {mult}')

    while offset != local_offset:
        mult += 1
        offset = (offset + increment) % local_mod

    if interval > period:
        time = mult * interval - target_offset
    else:
        time += mult * local_period

    period *= interval
    #print(f'HIT = {time}')

print(time)
