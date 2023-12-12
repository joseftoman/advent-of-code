#!/usr/bin/env python

from functools import cache
import math
import sys


def min_space(groups):
    return sum(groups) + len(groups) - 1


@cache
def place(springs, groups):
    """
    All the complex optimizations are not necessary after all.
    @cache + the last else block are fast enough.
    """

    parts = springs.strip('.').split('.', 1)
    total = 0

    if set(springs) == {'?'}:
        n = len(groups) + 1
        k = len(springs) - min_space(groups)
        return int(math.factorial(n + k - 1) / math.factorial(k) / math.factorial(n - 1))
    if len(parts) == 2:
        head, tail = parts
        tail = tail.strip('.')
        head_space = 0
        tail_space = min_space(groups)
        i = 0

        while i <= len(groups):
            if i > 0:
                head_space += groups[i - 1] + (1 if i > 1 else 0)
                tail_space -= groups[i - 1] + (1 if i < len(groups) else 0)

            if head_space > len(head):
                return total
            if tail_space > len(tail) or (head_space == 0 and '#' in head) or (tail_space == 0 and '#' in tail):
                i += 1
                continue

            if i > 0:
                total += place(head, groups[:i]) * (1 if tail_space == 0 else place(tail, groups[i:]))
            else:
                total += place(tail, groups)

            i += 1
    elif (first := springs.find('#')) >= 0:
        min_group = 1
        while first + min_group < len(springs) and springs[first + min_group] == '#':
            min_group += 1

        i = 0
        head_space = 0
        tail_space = min_space(groups)

        while i < len(groups):
            while i < len(groups) and groups[i] < min_group:
                i += 1
                head_space += groups[i - 1] + (1 if i > 1 else 0)
                tail_space -= groups[i - 1] + (1 if i < len(groups) else 0)
                if head_space > first - 1:
                    return total
            if i == len(groups):
                return total

            tail_space -= groups[i] + (1 if i + 1 < len(groups) else 0)

            for j in range(min(groups[i] - min_group, first - head_space), -1, -1):
                after = first - j + groups[i]
                if after > len(springs):
                    break
                head = '' if i == 0 else springs[:first - j - 1]
                tail = springs[after + 1:]

                if tail_space > len(tail):
                    break
                if tail_space == 0 and '#' in tail:
                    continue
                if head_space > len(head):
                    continue
                if after < len(springs) and springs[after] == '#':
                    continue

                if head_space == 0:
                    total += 1 if tail_space == 0 else place(tail, groups[i + 1:])
                elif tail_space == 0:
                    total += place(head, groups[:i])
                else:
                    total += place(head, groups[:i]) * place(tail, groups[i + 1:])

            head_space += groups[i] + (1 if i > 0 else 0)
            i += 1
    else:
        minimum = sum(groups) + len(groups) - 1
        g = groups[0]
        total = 0
        i = 0

        while len(springs) - i >= minimum:
            if all(springs[_] in {'?', '#'} for _ in range(i, i + g)) and (i + g == len(springs) or springs[i + g] in {'.', '?'}):
                if len(groups) > 1:
                    total += place(springs[i + g + 1:], groups[1:])
                elif '#' not in springs[i + g + 1:]:
                    total += 1
            if springs[i] == '#':
                break

            i += 1

    return total


def main():
    total = 0

    for line in sys.stdin:
        springs, groups = line.strip().split()
        springs = '?'.join([springs] * 5)
        groups = ','.join([groups] * 5)
        groups = tuple(int(_) for _ in groups.split(','))
        total += place(springs, groups)

    print(total)


if __name__ == '__main__':
    main()
