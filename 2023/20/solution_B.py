#!/usr/bin/env python

from collections import defaultdict
from dataclasses import dataclass
from enum import StrEnum, auto
import math
import sys


class PulseType(StrEnum):
    LOW = auto()
    HIGH = auto()


@dataclass
class Pulse:
    kind: PulseType
    source: str
    dest: str


class Module:
    def __init__(self, name, outputs):
        self.name: str = name
        self.outputs: list[str] = outputs

    def _send(self, pulse: PulseType):
        for item in self.outputs:
            yield Pulse(pulse, self.name, item)


class Broadcaster(Module):
    def receive(self, pulse: Pulse):
        yield from self._send(pulse.kind)


class FlipFlop(Module):
    def __init__(self, *args):
        super().__init__(*args)
        self.on = False

    def receive(self, pulse: Pulse):
        if pulse.kind == PulseType.HIGH:
            return

        to_send = PulseType.LOW if self.on else PulseType.HIGH
        self.on = not self.on
        yield from self._send(to_send)


class Conjunction(Module):
    def __init__(self, inputs, *args):
        super().__init__(*args)
        self.memory = {_: PulseType.LOW for _ in inputs}

    def receive(self, pulse: Pulse):
        self.memory[pulse.source] = pulse.kind
        to_send = PulseType.HIGH if any(_ == PulseType.LOW for _ in self.memory.values()) else PulseType.LOW
        yield from self._send(to_send)


def main():
    inputs = defaultdict(set)
    raw_modules = []

    for line in sys.stdin:
        left, right = line.strip().split(' -> ')
        right = [_.strip() for _ in right.split(',')]
        kind = left[0] if left[0] in {'%', '&'} else ''
        name = left if kind == '' else left[1:]
        for module in right:
            inputs[module].add(name)
        raw_modules.append((kind, name, right))

    modules = {}
    for item in raw_modules:
        args = [item[1], item[2]]
        if item[0] == '':
            modules[item[1]] = Broadcaster(*args)
        elif item[0] == '%':
            modules[item[1]] = FlipFlop(*args)
        else:
            modules[item[1]] = Conjunction(inputs[item[1]], *args)

    press = 0

    # By analyzing the input:
    # Each of these conjuntion modules constitues an independent sub-network
    # and sends a low pulse every N-th cycle.
    # When all of them send low pulse at the same cycle, in the end, rx receives low pulse.
    slots = {name: None for name in ['qr', 'lz', 'ft', 'lk']}

    while True:
        pulses = [Pulse(PulseType.LOW, '_button', 'broadcaster')]
        press += 1

        while pulses:
            next_round = []
            for incoming_pulse in pulses:
                if incoming_pulse.dest == 'rx' and incoming_pulse.kind == PulseType.LOW:
                    # Never going to happen, takes too long, see optimization below
                    print(press)
                    return

                if incoming_pulse.dest not in modules:
                    continue

                for pulse in modules[incoming_pulse.dest].receive(incoming_pulse):
                    if incoming_pulse.dest in {'qr', 'lz', 'ft', 'lk'} and pulse.kind == PulseType.LOW:
                        if slots[incoming_pulse.dest] is None:
                            slots[incoming_pulse.dest] = press
                            if all(_ is not None for _ in slots.values()):
                                print(math.lcm(*slots.values()))
                                return

                    next_round.append(pulse)

            pulses = next_round


if __name__ == '__main__':
    main()
