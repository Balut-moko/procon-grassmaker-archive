from itertools import combinations
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]
ans = 0
for down in combinations(range(h + w - 2), h - 1):
    r, c = 0, 0
    tmp = set()
    tmp.add(a[r][c])
    for i in range(h + w - 2):
        if i in down:
            r += 1
        else:
            c += 1
        tmp.add(a[r][c])
    if len(tmp) == h + w - 1:
        ans += 1
print(ans)
