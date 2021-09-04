from sys import stdin
from collections import deque
import heapq
readline = stdin.readline
q = int(readline())
que = deque([])
hq = []
ans = []
for _ in [0] * q:
    query = list(map(int, readline().split()))
    if query[0] == 1:
        que.append(query[1])
    elif query[0] == 2:
        if len(hq):
            ans.append(heapq.heappop(hq))
        else:
            ans.append(que.popleft())
    else:
        for val in que:
            heapq.heappush(hq, val)
        que.clear()
print(*ans, sep='\n')
