from heapq import heappush, heappop, heapify

from atcoder.dsu import DSU


class PrimAlgorithm:
    def __init__(self, n) -> None:
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add(self, u, v, cost, undirected=True) -> None:
        self.graph[u].append((v, cost))
        if undirected:
            self.graph[v].append((u, cost))

    def make_min_span_tree(self) -> int:
        used = [0] * self.n
        used[0] = 1
        que = [(c, w) for w, c in self.graph[0]]
        heapify(que)

        min_cost = 0
        while que:
            cv, v = heappop(que)
            if used[v]:
                continue
            used[v] = 1
            if v < N:
                min_cost += cv
            for w, c in self.graph[v]:
                if used[w]:
                    continue
                heappush(que, (c, w))
        return min_cost


N, M = map(int, input().split())
prim = PrimAlgorithm(N + M)
uf = DSU(N + M)
for i in range(M):
    K, C = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))
    for a in A:
        uf.merge(a, i + N)
        prim.add(a, i + N, C)

if uf.size(0) != N + M:
    print(-1)
    exit()

ans = prim.make_min_span_tree()
print(ans)
