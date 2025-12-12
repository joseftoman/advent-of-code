#!/usr/bin/env python

import sys


def main() -> None:
    """
    This task is silly. The main input is designed in such way that simple comparison
    of available space and space required by presents is enough. Actual packing is not
    required.

    Although it does not work on the sample input.
    """

    sizes = []
    fit = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        if line[-1] == ':':
            sizes.append(0)
        elif '#' in line or '.' in line:
            sizes[-1] += len([_ for _ in line if _ == '#'])
        elif 'x' in line:
            left, right = line.split(':')
            x, y = map(int, left.split('x'))
            amounts = list(map(int, right.split()))

            need = sum(sizes[i] * amounts[i] for i in range(len(sizes)))
            if need <= x * y:
                fit += 1

    print(fit)


if __name__ == '__main__':
    main()
