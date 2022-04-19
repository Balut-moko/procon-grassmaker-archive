from sys import stdin
from bisect import bisect_left

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
idx_li = [[] for _ in range(n + 1)]
for i, val in enumerate(a):
    idx_li[val].append(i + 1)

q = int(readline())
for _ in range(q):
    l, r, x = map(int, readline().split())
    print(bisect_left(idx_li[x], r + 1) - bisect_left(idx_li[x], l))
