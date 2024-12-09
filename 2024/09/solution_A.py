#!/usr/bin/env python

import sys


def main():
    disk_map = [int(_) for _ in next(sys.stdin).strip()]
    checksum = 0
    pos = 0
    block_no = 0

    while True:
        if pos >= len(disk_map):
            break

        if pos % 2 == 0:
            file_id = pos // 2
            for i in range(disk_map[pos]):
                checksum += file_id * (block_no + i)
            block_no += disk_map[pos]
        else:
            while disk_map[pos]:
                file_id = len(disk_map) // 2
                shift = min(disk_map[pos], disk_map[-1])
                for i in range(shift):
                    checksum += file_id * (block_no + i)
                block_no += shift
                disk_map[pos] -= shift
                disk_map[-1] -= shift
                if disk_map[-1] == 0:
                    disk_map.pop()
                    if pos + 1 == len(disk_map):
                        disk_map[pos] = 0
                    else:
                        disk_map.pop()

        pos += 1

    print(checksum)


if __name__ == '__main__':
    main()
