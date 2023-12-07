#!/usr/bin/env python

import sys


def transform_factory(line):
    _, formula = line.split('=')
    tokens = formula.strip().split()

    def inner(value: int, reducer: int) -> int:
        nonlocal tokens
        result = 0

        op1 = value if tokens[0] == 'old' else int(tokens[0])
        op2 = value if tokens[2] == 'old' else int(tokens[2])

        if tokens[1] == '+':
            result = op1 + op2
        elif tokens[1] == '-':
            result = op1 - op2
        elif tokens[1] == '*':
            result = op1 * op2

        return result % reducer

    return inner


def throw_factory(lines):
    params = [int(line.split()[-1]) for line in lines]

    def inner(value: int) -> int:
        nonlocal params
        return params[1] if value % params[0] == 0 else params[2]

    return params[0], inner
    

def main():
    monkeys = []
    reducer = 1

    while True:
        new_monkey = sys.stdin.readline()
        if not new_monkey:
            break

        items = [int(_.strip()) for _ in sys.stdin.readline().split(':')[-1].split(',')]
        transform = transform_factory(sys.stdin.readline())
        divisor, throw = throw_factory([sys.stdin.readline() for _ in range(3)])

        reducer *= divisor
        monkeys.append({'items': items, 'transform': transform, 'throw': throw, 'activity': 0})
        sys.stdin.readline()

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['activity'] += 1
                item = monkey['transform'](item, reducer)
                target = monkey['throw'](item)
                monkeys[target]['items'].append(item)
            monkey['items'] = []

    monkeys.sort(key=lambda monkey: -monkey['activity'])
    print(monkeys[0]['activity'] * monkeys[1]['activity'])


if __name__ == '__main__':
    main()
