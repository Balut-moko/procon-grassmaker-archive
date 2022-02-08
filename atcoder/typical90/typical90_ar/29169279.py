from sys import stdin
from collections import deque

readline = stdin.readline
n, q = map(int, readline().split())
a = deque(map(int, readline().split()))
txy = [tuple(map(int, readline().split())) for _ in [0] * q]

for t, x, y in txy:
    x -= 1
    y -= 1
    if t == 1:
        a[x], a[y] = a[y], a[x]
    if t == 2:
        tmp = a.pop()
        a.appendleft(tmp)
    if t == 3:
        print(a[x])
