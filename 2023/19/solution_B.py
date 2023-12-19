#!/usr/bin/env python

import sys


def apply_condition(ratings, category, op, value, invert=False):
    output = {}

    if invert:
        if op == '<':
            op = '>'
            value -= 1
        else:
            op = '<'
            value += 1

    for c, r in ratings.items():
        if r is None:
            output[c] = None
        elif c != category:
            output[c] = r[:]
        else:
            if op == '<':
                if value < r[0]:
                    output[c] = None
                else:
                    output[c] = [r[0], min(value - 1, r[1])]
            else:
                if value > r[1]:
                    output[c] = None
                else:
                    output[c] = [max(value + 1, r[0]), r[1]]

    return output


def get_acceptance(workflows, name, ratings):
    output = 0

    if name == 'R':
        return 0
    if name == 'A':
        output = 1
        for item in ratings.values():
            output *= 0 if item is None else (item[1] - item[0] + 1)
        return output

    for rule in workflows[name]:
        if rule[1] is None:
            output += get_acceptance(workflows, rule[0], ratings)
        else:
            output += get_acceptance(workflows, rule[0], apply_condition(ratings, *rule[1]))
            ratings = apply_condition(ratings, *rule[1], True)

    return output


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
                rules.append((tokens[1], (tokens[0][0], tokens[0][1], int(tokens[0][2:]))))

        workflows[name] = rules

    print(get_acceptance(workflows, 'in', {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}))


if __name__ == '__main__':
    main()
