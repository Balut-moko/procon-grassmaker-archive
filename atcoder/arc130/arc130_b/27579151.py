from sys import stdin
from collections import defaultdict

readline = stdin.readline
h, w, c, q = map(int, readline().split())
m = map(int, stdin.read().split())
query = tuple(zip(m, m, m))
row = set()
col = set()
ans = [0] * c
for ti, ni, ci in query[::-1]:
    if ti == 1 and ni not in row:
        row.add(ni)
        ans[ci - 1] += w - len(col)
    if ti == 2 and ni not in col:
        col.add(ni)
        ans[ci - 1] += h - len(row)
print(*ans)
