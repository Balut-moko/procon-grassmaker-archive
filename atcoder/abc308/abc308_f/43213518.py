from collections import deque
from heapq import heappop, heappush
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
P = list(map(int, readline().split()))
L = list(map(int, readline().split()))
D = list(map(int, readline().split()))
LD = []
for i in range(m):
    LD.append((L[i], D[i]))

P.sort(reverse=True)
LD.sort(reverse=True)
que = deque(LD)
hq = []
pd = [0] * n
idx = 0
for i in range(m):
    l, d = que.popleft()
    while idx < n and P[idx] >= l:
        if pd[idx] == 0:
            pd[idx] = d
            heappush(hq, d)
            break
        idx += 1
    else:
        if hq:
            val = heappop(hq)
            heappush(hq, max(val, d))

print(sum(P) - sum(hq))
