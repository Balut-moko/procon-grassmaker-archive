from sys import stdin
from collections import deque, defaultdict
from heapq import heappop, heappush

readline = stdin.readline
n, m = map(int, readline().split())
ab = []
for _ in range(m):
    ab.append(tuple(map(int, input().split())))

in_cnt = defaultdict(int)
outs = defaultdict(list)
for a, b in ab:
    in_cnt[b - 1] += 1
    outs[a - 1].append(b - 1)

res = []
hq = []
for i in range(n):
    if in_cnt[i] == 0:
        heappush(hq, i)
while hq:
    v = heappop(hq)
    res.append(v + 1)
    for v2 in outs[v]:
        in_cnt[v2] -= 1
        if in_cnt[v2] == 0:
            heappush(hq, v2)
if len(res) == n:
    print(*res)
else:
    print(-1)
