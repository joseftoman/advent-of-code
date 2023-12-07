#!/usr/bin/env python

from collections import defaultdict
import sys


class Hand:
    card_strength = {
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'J': 10,
        'Q': 11,
        'K': 12,
        'A': 13,
    }

    def __init__(self, line: str) -> None:
        hand, bid = line.strip().split()
        self._hand = hand
        self.bid = int(bid)

        groups = defaultdict(int)
        for card in list(hand):
            groups[card] += 1

        cardinalities = defaultdict(int)
        for amount in groups.values():
            cardinalities[amount] += 1

        top = max(cardinalities)
        if top > 3:
            self._power = top + 2
        elif top == 3:
            if 2 in cardinalities:
                self._power = 5
            else:
                self._power = 4
        elif top == 2:
            self._power = cardinalities[2] + 1
        else:
            self._power = 1

        self._cards = [self.card_strength[_] for _ in hand]

    def vector(self) -> tuple[int]:
        return (self._power, *self._cards)

    def __str__(self) -> str:
        return str(self._hand)


def main():
    winnings = 0
    for rank, hand in enumerate(sorted([Hand(_) for _ in sys.stdin], key=lambda hand: hand.vector()), 1):
        winnings += rank * hand.bid
    print(winnings)


if __name__ == '__main__':
    main()
