#!/usr/bin/env python

import sys
row_tr = str.maketrans('FB', '01')
seat_tr = str.maketrans('LR', '01')

seat_ids = []

for line in sys.stdin:
    row = line[:7]
    seat = line[7:]

    row = int(row.translate(row_tr), 2)
    seat = int(seat.translate(seat_tr), 2)
    seat_ids.append(row * 8 + seat)

seat_ids.sort()

for i in range(1, len(seat_ids)):
    if seat_ids[i-1] < seat_ids[i] - 1:
        print(seat_ids[i] - 1)
        break
