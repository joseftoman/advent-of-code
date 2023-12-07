#!/usr/bin/env python

import sys

end = 2020

class Game():
    def __init__(self, start):
        self._mem = {}
        self._turn = 0
        self._future = None

        for num in start:
            self._add(num)

    def _add(self, num):
        self._turn += 1
        first = num not in self._mem
        self._future = 0 if first else self._turn - self._mem[num]
        self._mem[num] = self._turn

    def next(self):
        if self._turn == end - 1:
            print(self._future)
            return False

        self._add(self._future)
        return True


game = Game([int(_) for _ in next(sys.stdin).strip().split(',')])
while game.next():
    pass
