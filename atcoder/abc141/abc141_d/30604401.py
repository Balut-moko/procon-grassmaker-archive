from sys import stdin
from heapq import heapify, heappop, heappush

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(lambda x: -int(x), readline().split()))
heapify(a)

for _ in range(m):
    val = heappop(a)
    val += 1
    val //= 2
    heappush(a, val)

print(-sum(a))
