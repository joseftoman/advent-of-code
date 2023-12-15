#!/usr/bin/env python

from collections import defaultdict
import sys


def hash_algo(label):
    value = 0
    for char in label:
        value = ((value + ord(char)) * 17) % 256
    return value


def locate(label, box):
    for i in range(len(box)):
        if box[i][0] == label:
            return i
    return -1


def main():
    boxes = defaultdict(list)

    for step in [_ for _ in next(sys.stdin).strip().split(',')]:
        if step[-1] == '-':
            label = step[:-1]
            box_no = hash_algo(label)
            box = boxes[box_no]
            pos = locate(label, box)
            if pos >= 0:
                boxes[box_no] = box[:pos] + box[pos + 1:]
        else:
            label, focal_length = step.split('=')
            focal_length = int(focal_length)
            box_no = hash_algo(label)
            box = boxes[box_no]
            pos = locate(label, box)
            
            if pos >= 0:
                box[pos][1] = focal_length
            else:
                boxes[box_no].append([label, focal_length])

    total = 0
    for box_no, box in boxes.items():
        for pos, lens in enumerate(box, 1):
            total += (box_no + 1) * pos * lens[1]

    print(total)


if __name__ == '__main__':
    main()
