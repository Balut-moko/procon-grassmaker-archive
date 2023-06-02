from sys import stdin


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

    def make_min_span_tree(self) -> int:
        min_cost = 0
        for c, v, w in self.edge:
            if self._unite(v, w):
                min_cost += c
        return min_cost


class MstPlus(KruskalAlgorithm):
    def __init__(self, n, edge, q) -> None:
        super().__init__(n, edge)
        self.ans = ["No"] * q

    def calc_query(self):
        for w, u, v, i in self.edge:
            if self._root(u) != self._root(v):
                if i == -1:
                    self._unite(u, v)
                else:
                    self.ans[i] = "Yes"


readline = stdin.readline
n, m, q = map(int, readline().split())

cab = []
for _ in range(m):
    a, b, c = map(int, readline().split())
    cab.append((c, a - 1, b - 1, -1))

wuv = []
for i in range(q):
    u, v, w = map(int, readline().split())
    wuv.append((w, u - 1, v - 1, i))

que = cab + wuv

ans = MstPlus(n, que, q)
ans.calc_query()

print(*ans.ans, sep="\n")
