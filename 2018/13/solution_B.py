#!/usr/bin/env python

import sys

J_LEFT = -1
J_STRAIGHT = 0
J_RIGHT = 1

D_LEFT = 0
D_UP = 1
D_RIGHT = 2
D_DOWN = 3

cart_mapping = {
    '^': ('|', D_UP),
    'v': ('|', D_DOWN),
    '<': ('-', D_LEFT),
    '>': ('-', D_RIGHT)
}
curve_mapping = {
    r'/': {
        D_LEFT: D_DOWN,
        D_UP: D_RIGHT,
        D_RIGHT: D_UP,
        D_DOWN: D_LEFT
    },
    '\\' : {
        D_LEFT: D_UP,
        D_UP: D_LEFT,
        D_RIGHT: D_DOWN,
        D_DOWN: D_RIGHT
    }
}

plan = {}
carts = {}
cart_index = 0

for row, line in enumerate(sys.stdin):
    for column, char in enumerate(line.rstrip()):
        if char in ('^', 'v', '<', '>'):
            plan[(row, column)] = cart_mapping[char][0]
            carts[(row, column)] = [cart_index, cart_mapping[char][1], J_LEFT]
            cart_index += 1
        else:
            plan[(row, column)] = char

while len(carts) > 1:
    order = sorted([[*pos, *cart] for pos, cart in carts.items()], key=lambda c: c[0] * 1000 + c[1])
    crashed = {}

    for cart in order:
        if cart[2] in crashed:
            continue

        if cart[3] == D_UP:
            goto = (cart[0]-1, cart[1])
        elif cart[3] == D_DOWN:
            goto = (cart[0]+1, cart[1])
        elif cart[3] == D_LEFT:
            goto = (cart[0], cart[1]-1)
        elif cart[3] == D_RIGHT:
            goto = (cart[0], cart[1]+1)

        if goto in carts:
            crashed[carts[goto][0]] = True
            del carts[goto]
            del carts[tuple(cart[0:2])]
            continue
        
        carts[goto] = carts.pop(tuple(cart[0:2]))

        if plan[goto][0] in ('/', '\\'):
            carts[goto][1] = curve_mapping[plan[goto][0]][cart[3]]
        elif plan[goto][0] == '+':
            carts[goto][1] = (cart[3] + cart[4]) % 4
            carts[goto][2] = ((cart[4] + 2) % 3) - 1

if not carts:
    print('No carts left')
else:
    last = list(carts.keys())[0]
    print(f'{last[1]},{last[0]}')
