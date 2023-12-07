#!/usr/bin/env python

import sys

digits = (9, 8, 7, 6, 5, 4, 3, 2, 1)

for w1 in digits:
    z1 = w1 + 13

    for w2 in digits:
        z2 = z1 * 26 + w2 + 16

        for w3 in digits:
            z3 = z2 * 26 + w3 + 2

            for w4 in digits:
                z4 = z3 * 26 + w4 + 8

                for w5 in digits:
                    z5 = z4 * 26 + w5 + 11

                    z6 = z5 // 26
                    w6 = z5 % 26 - 11
                    if w6 < 1 or w6 > 9:
                        continue

                    for w7 in digits:
                        z7 = z6 * 26 + w7 + 12

                        z8 = z7 // 26
                        w8 = z7 % 26 - 16
                        if w8 < 1 or w8 > 9:
                            continue

                        z9 = z8 // 26
                        w9 = z8 % 26 - 9
                        if w9 < 1 or w9 > 9:
                            continue

                        for w10 in list(digits):
                            z10 = z9 * 26 + w10 + 15

                            z11 = z10 // 26
                            w11 = z10 % 26 - 8
                            if w1 < 1 or w11 > 9:
                                continue

                            z12 = z11 // 26
                            w12 = z11 % 26 - 8
                            if w12 < 1 or w12 > 9:
                                continue

                            z13 = z12 // 26
                            w13 = z12 % 26 - 10
                            if w13 < 1 or w13 > 9:
                                continue

                            z14 = z13 // 26
                            w14 = z13 % 26 - 9
                            if w14 < 1 or w14 > 9:
                                continue

                            print(''.join(str(_) for _ in [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14]))
                            sys.exit(0)
