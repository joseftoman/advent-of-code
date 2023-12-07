#!/usr/bin/python3

import sys
import re

bot = []
out = []
ready = []
r_value = re.compile('value (\d+) goes to bot (\d+)')
r_bot = re.compile('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
target = (0, 1, 2)

def extend(list, index):
    for _ in range(len(list), index + 1): list.append(None)

def fill(source, type, index, value):
    if type == 'bot':
        bot[index][0].append(value)
        if len(bot[index][0]) == 2: ready.append(index)
    else:
        extend(out, index)
        out[index] = value

    #print("Bot %d: %d -> %s %d" % (source, value, type, index))

for line in sys.stdin:
    m_obj = r_bot.match(line)
    if m_obj:
        b = int(m_obj.group(1))
        d1 = int(m_obj.group(3))
        d2 = int(m_obj.group(5))

        extend(bot, b)
        if bot[b] is None: bot[b] = [ [], None, None, None, None ]
        bot[b][1] = d1
        bot[b][2] = d2


        if m_obj.group(2) == 'bot':
            extend(bot, d1)
            bot[b][3] = 'bot'
        else:
            extend(out, d1)
            bot[b][3] = 'out'

        if m_obj.group(4) == 'bot':
            extend(bot, d2)
            bot[b][4] = 'bot'
        else:
            extend(out, d2)
            bot[b][4] = 'out'

        #print("Def", b, "->", bot[b])
        continue

    m_obj = r_value.match(line)
    if m_obj:
        v = int(m_obj.group(1))
        b = int(m_obj.group(2))
        extend(bot, b)
        if bot[b] is None: bot[b] = [ [], None, None, None, None ]
        bot[b][0].append(v)
        #print("[init]: %d -> Bot %d" % (v, b))
        if len(bot[b][0]) == 2: ready.append(b)
        continue

#print()

while ready:
    source = ready.pop()
    #print("Ready:", source, bot[source])
    v_low = min(bot[source][0])
    v_high = max(bot[source][0])
    d_low = bot[source][1]
    d_high = bot[source][2]
    fill(source, bot[source][3], bot[source][1], min(bot[source][0]))
    fill(source, bot[source][4], bot[source][2], max(bot[source][0]))

result = 1
for i in target: result *= out[i]
print(result)
