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
        que = [(c, w) for w, c in self.g[0]]
        heapify(que)

        while que:
            cv, v = heappop(que)
            if used[v]:
                continue
            used[v] = 1
            mincost += cv
            for w, c in self.g[v]:
                if used[w]:
                    continue
                heappush(que, (c, w))
        return mincost


readline = stdin.readline
n = int(readline())
point = [[i] + list(map(int, readline().split())) for i in range(n)]
mst = PrimAlgorithm(n)

point = sorted(point, key=lambda x: x[1])
for j in range(n - 1):
    i1, a, b = point[j]
    i2, c, d = point[j + 1]
    cost = min(abs(a - c), abs(b - d))
    mst.add(i1, i2, cost)

point = sorted(point, key=lambda x: x[2])
for j in range(n - 1):
    i1, a, b = point[j]
    i2, c, d = point[j + 1]
    cost = min(abs(a - c), abs(b - d))
    mst.add(i1, i2, cost)

print(mst.makeminspantree())
