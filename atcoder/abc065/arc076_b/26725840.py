from sys import stdin
from heapq import heappush, heappop, heapify


class KruskalAlgorithm:
    def __init__(self, n, edge) -> None:
        self.p = list(range(n))
        self.edge = sorted(edge)

    def _root(self, x) -> int:
        if x == self.p[x]:
            return x
        self.p[x] = y = self._root(self.p[x])
        return y

    def _unite(self, x, y):
        px = self._root(x)
        py = self._root(y)
        if px == py:
            return 0
        if px < py:
            self.p[py] = px
        else:
            self.p[px] = py
        return 1

    def makeminspantree(self) -> int:
        mincost = 0
        for c, v, w in self.edge:
            if self._unite(v, w):
                mincost += c
        return mincost


readline = stdin.readline
n = int(readline())
point = [[i] + list(map(int, readline().split())) for i in range(n)]
edge = []

point = sorted(point, key=lambda x: x[1])
for j in range(n - 1):
    i1, a, b = point[j]
    i2, c, d = point[j + 1]
    cost = min(abs(a - c), abs(b - d))
    edge.append([cost, i1, i2])

point = sorted(point, key=lambda x: x[2])
for j in range(n - 1):
    i1, a, b = point[j]
    i2, c, d = point[j + 1]
    cost = min(abs(a - c), abs(b - d))
    edge.append([cost, i1, i2])

print(KruskalAlgorithm(n, edge).makeminspantree())
