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
    items = [int(_) for _ in sys.stdin]
    xmas = XMAS(window or 25)
    target = None

    for num in items:
        if not xmas.add_item(num):
            target = num
            break

    start = 0
    end = 0
    agg = items[0]

    while agg != target and end + 1 < len(items):
        end += 1
        agg += items[end]
        while agg > target:
            agg -= items[start]
            start += 1

    if agg == target:
        hit = sorted(items[start:end + 1])
        print(hit[0] + hit[-1])


if __name__ == '__main__':
    main(None if len(sys.argv) < 2 else sys.argv[1])
