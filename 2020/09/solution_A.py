#!/usr/bin/env python

from collections import deque, defaultdict
import sys


class XMAS():
    def __init__(self, window):
        self._window = int(window)
        self._sums = defaultdict(int)
        self._preamble = deque()

    def add_item(self, num):
        if len(self._preamble) == self._window:
            if num not in self._sums:
                return False

            item = self._preamble.popleft()
            for x in self._preamble:
                self._sums[item + x] -= 1
                if not self._sums[item + x]:
                    del self._sums[item + x]

        for x in self._preamble:
            self._sums[num + x] += 1
        self._preamble.append(num)

        return True


def main(window):
    xmas = XMAS(window or 25)

    for num in [int(_) for _ in sys.stdin]:
        if not xmas.add_item(num):
            print(num)
            break


if __name__ == '__main__':
    main(None if len(sys.argv) < 2 else sys.argv[1])
