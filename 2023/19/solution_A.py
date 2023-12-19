#!/usr/bin/env python

import sys


def create_lambda(rating, op, num):
    if op == '>':
        return lambda ratings: ratings[rating] > num
    return lambda ratings: ratings[rating] < num


def main():
    workflows = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break

        name, spec = line.split('{')
        rules = []
        for part in spec[:-1].split(','):
            tokens = part.split(':')
            if len(tokens) == 1:
                rules.append((tokens[0], None))
            else:
                rules.append((tokens[1], create_lambda(tokens[0][0], tokens[0][1], int(tokens[0][2:]))))

        workflows[name] = rules

    total = 0
    
    for line in sys.stdin:
        ratings = {}
        for chunk in line.strip()[1:-1].split(','):
            ratings[chunk[0]] = int(chunk[2:])

        name = 'in'
        while True:
            for rule in workflows[name]:
                if rule[1] is None or rule[1](ratings):
                    name = rule[0]
                    break

            if name == 'R':
                break
            if name == 'A':
                total += sum(ratings.values())
                break

    print(total)


if __name__ == '__main__':
    main()
