from collections import defaultdict
from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
di = defaultdict(set)
for _ in range(q):
    t, a, b = map(int, readline().split())

    if t == 1:
        di[a].add(b)
    if t == 2:
        if b in di[a]:
            di[a].remove(b)
    if t == 3:
        if a in di[b] and b in di[a]:
            print("Yes")
        else:
            print("No")
