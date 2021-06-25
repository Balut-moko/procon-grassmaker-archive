#!/usr/bin/env python3
from sys import stdin
from collections import deque

readline = stdin.readline
n, q = map(int, readline().split())
a = deque(tuple(map(int, readline().split())))
for _ in [0] * q:
    t, x, y = map(int, readline().split())
    if t == 1:
        a[x - 1], a[y - 1] = a[y - 1], a[x - 1]
    elif t == 2:
        tmp = a.pop()
        a.appendleft(tmp)
    else:
        print(a[x - 1])
