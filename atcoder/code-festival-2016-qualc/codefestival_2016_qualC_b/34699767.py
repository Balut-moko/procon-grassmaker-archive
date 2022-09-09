from heapq import heapify, heappop, heappush
from sys import stdin

readline = stdin.readline
k, t = map(int, readline().split())
a = list(map(int, readline().split()))

que = [(-val, i) for i, val in enumerate(a)]
pre = -1
ans = 0
heapify(que)
while que:
    cnt, idx = heappop(que)
    if pre != idx:
        cnt += 1
        pre = idx
        if cnt != 0:
            heappush(que, (cnt, idx))
    else:
        if que:
            cnt2, idx2 = heappop(que)
            cnt2 += 1
            pre = idx2
            if cnt != 0:
                heappush(que, (cnt, idx))
            if cnt2 != 0:
                heappush(que, (cnt2, idx2))
        else:
            cnt += 1
            pre = idx
            ans += 1
            if cnt != 0:
                heappush(que, (cnt, idx))
print(ans)
