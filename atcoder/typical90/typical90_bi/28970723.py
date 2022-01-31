from sys import stdin
from collections import deque

readline = stdin.readline
q = int(readline())
tx = [tuple(map(int, readline().split())) for _ in [0] * q]
que = deque()
for t, x in tx:
    if t == 1:
        que.appendleft(x)
    elif t == 2:
        que.append(x)
    else:
        print(que[x - 1])
