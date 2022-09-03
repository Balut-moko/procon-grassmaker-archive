from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
graph = [[] for _ in range(n)]
costs = [0] * n
for i in range(m):
    u, v = map(lambda x: int(x) - 1, readline().split())
    graph[u].append(v)
    graph[v].append(u)
    costs[u] += a[v]
    costs[v] += a[u]


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        s = deque([])
        flg = [False] * n
        cnt = 0
        tmp_cost = costs.copy()
        for i, val in enumerate(tmp_cost):
            if val <= mid:
                s.append(i)
                flg[i] = True
                cnt += 1
        while s:
            idx = s.pop()
            for e in graph[idx]:
                tmp_cost[e] -= a[idx]
                if flg[e] == False and tmp_cost[e] <= mid:
                    s.append(e)
                    flg[e] = True
                    cnt += 1
        if cnt == n:
            return True
        return False

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(1 << 60, -1))
