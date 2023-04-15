from collections import deque
from sys import stdin

readline = stdin.readline
Q = int(readline())
mod = 998244353
que = deque([1])
s = 1
for _ in range(Q):
    t, *x = map(int, readline().split())

    if t == 1:
        s = (s * 10 + x[0]) % mod
        que.append(x[0])
    if t == 2:
        digit = len(que)
        num = que.popleft()
        s -= num * pow(10, digit - 1, mod)
    if t == 3:
        print(s % mod)
