from sys import stdin
from heapq import heappush, heappop, heapify


class PrimAlgorithm:
    def __init__(self, n) -> None:
        self.n = n
        self.g = [[] for _ in range(n)]

    def add(self, a, b, cost, directed=False) -> None:
        if directed is False:
            self.g[a].append((b, cost))
            self.g[b].append((a, cost))
        else:
            self.g[a].append((b, cost))

    def makeminspantree(self) -> int:
        used = [0] * self.n
        used[0] = 1
        mincost = 0
        cost_li = []
        que = [(c, w) for w, c in self.g[0]]
        heapify(que)

        while que:
            cv, v = heappop(que)
            if used[v]:
                continue
            used[v] = 1
            mincost += cv
            heappush(cost_li, -cv)
            for w, c in self.g[v]:
                if used[w]:
                    continue
                heappush(que, (c, w))
        return mincost, cost_li


readline = stdin.readline
n, m, k = map(int, readline().split())
mst = PrimAlgorithm(n)
for _ in range(m):
    a, b, c = map(int, readline().split())
    mst.add(a - 1, b - 1, c)
ans, cost_li = mst.makeminspantree()
for _ in range(k - 1):
    ans += heappop(cost_li)
print(ans)
