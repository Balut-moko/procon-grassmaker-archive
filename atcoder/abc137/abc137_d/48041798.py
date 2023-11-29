from collections import deque
from heapq import heappop, heappush


N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in [0] * N]
AB.sort()
que = deque(AB)
hq = []
ans = 0
cnt = 1
while cnt <= M:
    while que:
        a, b = que[0]
        if a <= min(cnt, M):
            que.popleft()
            heappush(hq, -b)
        else:
            break
    if hq:
        ans -= heappop(hq)
    cnt += 1

print(ans)
