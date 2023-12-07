#!/usr/bin/python3

import sys
input = int(sys.argv[1])

init = [ 1, 2, 4, 4, 5, 10, 10, 10, 10, 10, 11, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 25, 25 ]

if input < len(init):
    print(init[input])
    exit()

prev = [ 1, 2, 4, 5, 10, 11, 23, 25 ]
curr = []
e = 4

while True:
    for q in range(0, 4):
        for i in range(0, e):
            p = q * (e - 2) + i

            if q == 0 and i == 0:
                curr.append(prev[0] + prev[-1])
            elif q == 0 and i == 1:
                curr.append(prev[0] + prev[1] + prev[-1] + curr[-1])
            elif q == 3 and i == e - 2:
                curr.append(prev[p-1] + prev[p-2] + curr[-1] + curr[0])
            elif q == 3 and i == e - 1:
                curr.append(prev[p-2] + curr[-1] + curr[0])
            elif i == 0:
                curr.append(prev[p] + prev[p-1] + curr[-1] + curr[-2])
            elif i == e - 2:
                curr.append(prev[p-1] + prev[p-2] + curr[-1])
            elif i == e - 1:
                curr.append(prev[p-2] + curr[-1])
            else:
                curr.append(prev[p] + prev[p-1] + prev[p-2] + curr[-1])

            if curr[-1] > input:
                print(curr[-1])
                exit()

    e += 2
    prev = curr
    curr = []
