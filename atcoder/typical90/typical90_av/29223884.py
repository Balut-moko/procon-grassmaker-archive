from sys import stdin
from heapq import heappop, heappush

readline = stdin.readline
n, k = map(int, readline().split())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]
h = []
for i, val in enumerate(ab):
    heappush(h, [-val[1], i])
ans = 0
while k > 0:
    p, i = heappop(h)
    ans += p
    k -= 1
    if i != -1:
        heappush(h, [ab[i][1] - ab[i][0], -1])

print(-ans)
