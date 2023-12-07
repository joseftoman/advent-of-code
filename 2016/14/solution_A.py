#!/usr/bin/python3

import hashlib

def test_digest(digest):
    three = None
    five = set()
    buf_len = 0

    for i in range(0, len(digest)):
        if i == 0 or digest[i] == digest[i-1]:
            buf_len += 1
            if three is None and buf_len == 3: three = digest[i]
            if buf_len == 5: five.add(digest[i])
        else:
            buf_len = 1

    return (three, five)

salt = "jlmsuwbz"
goal = 64
index = -1
queue = []
found = 0
window_size = 1000

while found < goal:
    index += 1
    if queue and queue[0][1] < index - window_size and not queue[0][0]:
        #print("Drop:", queue[0][1])
        queue.pop(0)

    digest = hashlib.md5((salt+str(index)).encode("utf-8")).hexdigest()
    matches = test_digest(digest)

    if len(matches[1]):
        #print("Hit:", index, matches[1], digest)
        for item in queue:
            if item[0]: continue
            if item[2] in matches[1]:
                item[0] = True
                #print("->", item[1], item[2])

    if matches[0] is not None:
        queue.append([False, index, matches[0]])
        #print("Add:", index, matches[0], digest)

    while queue and queue[0][0]:
        found += 1
        #print("Use:", str(queue[0][1]), '['+str(found)+'/'+str(goal)+']')
        if found == goal:
            print(queue[0][1])
            queue = []
        else:
            queue.pop(0)
