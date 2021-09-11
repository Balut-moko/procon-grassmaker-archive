from sys import stdin
from itertools import combinations
readline = stdin.readline
n = int(readline())
xy = [tuple(map(int, readline().split())) for _ in [0] * n]
xy_set = set(xy)
ans = 0
for a, b in combinations(xy, 2):
    if a[0] != b[0] and a[1] != b[1]:
        c = (a[0], b[1])
        d = (b[0], a[1])
        if c in xy_set and d in xy_set:
            ans += 1

print(ans // 2)
