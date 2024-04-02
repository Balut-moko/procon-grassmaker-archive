from atcoder.dsu import DSU


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


N, M = map(int, input().split())
CLR = [tuple(map(int, input().split())) for _ in [0] * M]

edge = [(c, l - 1, r) for c, l, r in CLR]
uf = DSU(N + 1)
for _, u, v in edge:
    uf.merge(u, v)

if uf.size(0) != N + 1:
    print(-1)
    exit()

graph = KruskalAlgorithm(N + 1, edge)
print(graph.make_min_span_tree())
