#!/usr/bin/env python

import sys
from textwrap import wrap


def get_start_chunk(chunks: list[int]) -> int:
    for chunk in chunks[1:]:
        if chunk < chunks[0]:
            return chunks[0]
        if chunk > chunks[0]:
            return chunks[0] + 1

    return chunks[0]


def main():
    known = set()
    output = 0

    for interval in next(sys.stdin).strip().split(','):
        start, end = interval.split('-', maxsplit=1)
        # print(f'\n{start} -> {end}')

        for chunk_length in range(1, len(end) // 2 + 1):
            if len(start) % chunk_length:
                minimum = [10 ** (chunk_length - 1), max(2, len(start) // chunk_length + 1)]
            else:
                chunks = [int(_) for _ in wrap(start, chunk_length)]
                minimum = [get_start_chunk(chunks), max(2, len(start) // chunk_length)]

            if len(end) % chunk_length:
                maximum = [10 ** chunk_length - 1, len(end) // chunk_length]
            else:
                chunks = [-1 * int(_) for _ in wrap(end, chunk_length)]
                maximum = [-1 * get_start_chunk(chunks), len(end) // chunk_length]

            # print(f'- {chunk_length}: {minimum[0]}[{minimum[1]}] -> {maximum[0]}[{maximum[1]}]')

            while minimum[1] <= maximum[1]:
                for item in range(minimum[0], maximum[0] + 1 if  minimum[1] == maximum[1] else 10 ** chunk_length):
                    invalid = int(''.join([str(item)] * minimum[1]))
                    if invalid not in known:
                        output += invalid
                        known.add(invalid)
                        # print(f'* {invalid}')

                minimum[0] = 10 ** (chunk_length - 1)
                minimum[1] += 1

    print(output)

if __name__ == '__main__':
    main()
