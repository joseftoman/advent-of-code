#!/usr/bin/env python

from collections import defaultdict
import sys


def main():
    rules = defaultdict(lambda: {'before': set(), 'after': set()})
    output = 0
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break

        before, after = [int(_) for _ in line.split('|')]
        rules[before]['after'].add(after)
        rules[after]['before'].add(before)

    for line in sys.stdin:
        pages = [int(_) for _ in line.split(',')]
        correct = True

        for i in range(len(pages)):
            for j in range(i):
                if pages[i] in rules[pages[j]]['before']:
                    correct = False
                    break
            if not correct:
                break

            for j in range(i + 1, len(pages)):
                if pages[i] in rules[pages[j]]['after']:
                    correct = False
                    break
            if not correct:
                break

        if correct:
            output += pages[len(pages) // 2]

    print(output)


if __name__ == '__main__':
    main()
