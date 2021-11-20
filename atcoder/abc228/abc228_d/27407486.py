from sys import stdin
from collections import defaultdict

readline = stdin.readline
q = int(readline())
mod = 2**20
a = defaultdict(lambda: -1)
nxt = list(range(mod))


def find(x):
    h = nxt[x]
    if h == x:
        return h
    else:
        nxt[x] = find(h)
    return nxt[x]


for i in range(q):
    t, x = map(int, readline().split())
    h = x % mod
    if t == 1:
        h = find(h)
        a[h] = x
        nxt[h] = find((h + 1) % mod)
    else:
        print(a[h])
