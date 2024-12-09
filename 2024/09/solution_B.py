#!/usr/bin/env python

import sys


def main():
    files = []
    blanks = []
    vacancy = {}
    pos = 0

    for i, size in enumerate(int(_) for _ in next(sys.stdin).strip()):
        if i % 2:
            for i in range(1, size + 1):
                if i not in vacancy:
                    vacancy[i] = len(blanks)
            blanks.append((pos, size))
        else:
            files.append((pos, size))
        pos += size

    checksum = 0

    for file_id in range(len(files) - 1, 0, -1):
        pos, size = files[file_id]
        if size not in vacancy or blanks[vacancy[size]][0] > pos:
            # There's no better spot for this file. Calculate it's checksum and go on.
            checksum += (((size - 1) * size) // 2 + pos * size) * file_id
            continue

        # Grab a better spot from the vacancy index and calculate the checksum increment.
        blank_index = vacancy[size]
        checksum += (((size - 1) * size) // 2 + blanks[blank_index][0] * size) * file_id

        # Chosen blank space was reduced and can not accomodate higher file sizes any longer.
        # Find the interval of file sizes we need to reindex.
        min_replace = blanks[blank_index][1] - size + 1
        max_replace = blanks[blank_index][1]
        for v in range(max_replace - 1, min_replace - 1, -1):
            if vacancy[v] < blank_index:
                min_replace = v + 1
                break

        # Save the reduced blank space.
        blanks[blank_index] = (blanks[blank_index][0] + size, blanks[blank_index][1] - size)

        # Remap the vacancy index. There's no point looking for a blank space beyond
        # the original spot of the file we have just moved.
        for i in range(blank_index + 1, file_id):
            if blanks[i][1] >= min_replace:
                for v in range(min_replace, min(blanks[i][1], max_replace) + 1):
                    vacancy[v] = i
                min_replace = blanks[i][1] + 1

                if min_replace > max_replace:
                    break

        # It's possible there's no blank space avalable for some file sizes.
        for v in range(min_replace, max_replace + 1):
            del vacancy[v]

    print(checksum)


if __name__ == '__main__':
    main()
