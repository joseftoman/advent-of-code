#!/usr/bin/env python

from collections import defaultdict
import sys
from typing import Iterator


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
        'J': 0,
        'Q': 11,
        'K': 12,
        'A': 13,
    }

    @classmethod
    def _possible_powers(cls, partial_groups: dict[str, int], jokers: int) -> Iterator[int]:
        if jokers == 0:
            cardinalities = defaultdict(int)
            for amount in partial_groups.values():
                cardinalities[amount] += 1

            top = max(cardinalities)
            if top > 3:
                yield top + 2
            elif top == 3:
                yield 5 if 2 in cardinalities else 4
            elif top == 2:
                yield cardinalities[2] + 1
            else:
                yield 1
        else:
            for card in cls.card_strength:
                if card == 'J':
                    continue
                groups = defaultdict(int, **partial_groups)
                groups[card] += 1
                yield from cls._possible_powers(groups, jokers - 1)

    def __init__(self, line: str) -> None:
        hand, bid = line.strip().split()
        self._hand = hand
        self.bid = int(bid)

        groups = defaultdict(int)
        jokers = 0
        for card in list(hand):
            if card == 'J':
                jokers += 1
            else:
                groups[card] += 1

        self._power = 0
        for power in self._possible_powers(groups, jokers):
            if power > self._power:
                self._power = power

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
