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
            if self._unite(v - 1, w - 1):
                continue
            else:
                if c > 0:
                    min_cost += c
        return min_cost


readline = stdin.readline
n, m = map(int, readline().split())
abc = [tuple(map(int, readline().split())) for _ in [0] * m]
edge = [(c, a, b) for a, b, c in abc]
kruskal = KruskalAlgorithm(n, edge)
cost = kruskal.make_min_span_tree()
print(cost)
