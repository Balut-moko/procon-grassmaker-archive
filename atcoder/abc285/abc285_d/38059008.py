from sys import stdin
from collections import defaultdict
from heapq import heappop, heappush

readline = stdin.readline
n = int(readline())
st = [readline().split() for _ in [0] * n]

s_set = set()

for s, t in st:
    s_set.add(s)
    s_set.add(t)

n = len(s_set)
s_di = {val: i for i, val in enumerate(s_set)}


in_cnt = defaultdict(int)
outs = defaultdict(list)

for s, t in st:
    s = s_di[s]
    t = s_di[t]

    in_cnt[t] += 1
    outs[s].append(t)


def topologicalSort(in_cnt, outs):
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

    return res if len(res) == n else -1


print("Yes" if topologicalSort(in_cnt, outs) != -1 else "No")
