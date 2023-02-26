from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush

readline = stdin.readline
n, m = map(int, readline().split())

in_cnt = defaultdict(int)
outs = defaultdict(list)

for _ in range(m):
    a, b = map(int, readline().split())
    in_cnt[b - 1] += 1
    outs[a - 1].append(b - 1)


def topologicalSort(in_cnt, outs):
    res = [None] * n
    hq = []
    cnt = 1
    for i in range(n):
        if in_cnt[i] == 0:
            heappush(hq, i)
    while hq:
        if len(hq) != 1:
            print("No")
            exit()
        v = heappop(hq)
        res[v] = cnt
        cnt += 1
        for v2 in outs[v]:
            in_cnt[v2] -= 1
            if in_cnt[v2] == 0:
                heappush(hq, v2)

    return res if len(res) == n else -1


ans = topologicalSort(in_cnt, outs)
print("Yes")
print(*ans)
