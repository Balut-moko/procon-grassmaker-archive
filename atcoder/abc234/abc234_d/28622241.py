from sys import stdin
from heapq import heapify, heappop, heappush

readline = stdin.readline
n, k = map(int, readline().split())
p = list(map(int, readline().split()))
heap = p[:k]
heapify(heap)
ans = heappop(heap)
print(ans)
for i in range(k, n):
    if p[i] > ans:
        heappush(heap, p[i])
        ans = heappop(heap)
    print(ans)
