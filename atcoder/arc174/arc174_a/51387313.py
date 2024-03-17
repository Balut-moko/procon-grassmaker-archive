from heapq import heappush
from itertools import accumulate


N, C = map(int, input().split())
A = list(map(int, input().split()))
cum = list(accumulate(A, initial=0))
if C > 0:
    hq = []
    mx = -1 << 60
    mx_idx = (0, 0)
    for i in range(N):
        heappush(hq, (cum[i], i))
        tmp = cum[i + 1]
        l, li = hq[0]
        tmp -= l
        if mx < tmp:
            mx = tmp
            mx_idx = (li, i + 1)
    if mx > 0:
        l, r = mx_idx
        for i in range(l, r):
            A[i] *= C
else:
    hq = []
    mn = 1 << 60
    mn_idx = (0, 0)
    for i in range(N):
        heappush(hq, (-cum[i], i))
        tmp = cum[i + 1]
        l, li = hq[0]
        tmp += l
        if tmp < mn:
            mn = tmp
            mn_idx = (li, i + 1)
    if mn < 0:
        l, r = mn_idx
        for i in range(l, r):
            A[i] *= C

print(sum(A))
