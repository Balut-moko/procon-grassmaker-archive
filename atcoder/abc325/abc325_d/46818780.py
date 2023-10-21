from collections import deque
from heapq import heappop, heappush

N = int(input())
TD = [tuple(map(int, input().split())) for _ in [0] * N]
TD = [(t, t + d) for t, d in TD]
TD.sort()
que = deque(TD)
hq = []
now = que[0][0]
ans = 0
while que or hq:
    while que:
        t, end = que[0]
        if t <= now:
            t, end = que.popleft()
            heappush(hq, (end, t))
        else:
            if not hq:
                now = t
            break
    if hq:
        end, start = heappop(hq)
        if now <= start:
            now = start
        if now <= end:
            ans += 1
            now += 1

print(ans)
