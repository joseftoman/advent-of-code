#!/usr/bin/env python

import sys
top = -1
row_tr = str.maketrans('FB', '01')
seat_tr = str.maketrans('LR', '01')

for line in sys.stdin:
    row = line[:7]
    seat = line[7:]

    row = int(row.translate(row_tr), 2)
    seat = int(seat.translate(seat_tr), 2)
    seat_id = row * 8 + seat

    if seat_id > top:
        top = seat_id

print(top)
