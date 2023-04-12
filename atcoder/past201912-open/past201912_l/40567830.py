from itertools import product
from math import sqrt
from sys import stdin
from heapq import heappush, heappop, heapify


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
            min_cost += cv
            for w, c in self.graph[v]:
                if used[w]:
                    continue
                heappush(que, (c, w))
        return min_cost


readline = stdin.readline
N, M = map(int, readline().split())
xyc_n = [tuple(map(int, readline().split())) for _ in [0] * N]
xyc_m = [tuple(map(int, readline().split())) for _ in [0] * M]

ALL = 1 << M


def has_bit(n, i):
    return n & (1 << i) > 0


def calc_cost(p1, p2):
    dist = sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    if p1[2] != p2[2]:
        dist *= 10
    return dist


ans = 1 << 60
for m in range(ALL):
    mc = bin(m).count("1")
    prim = PrimAlgorithm(N + mc)
    for i, j in product(range(N), range(N)):
        if i == j:
            continue
        c = calc_cost(xyc_n[i], xyc_n[j])
        prim.add(i, j, c)
    bit_count = 0
    for i in range(M):
        if has_bit(m, i):
            for j in range(N):
                c = calc_cost(xyc_m[i], xyc_n[j])
                prim.add(N + bit_count, j, c)

            bit_count_j = 0
            for j in range(M):
                if i == j:
                    bit_count_j += 1
                    continue
                if has_bit(m, j):
                    c = calc_cost(xyc_m[i], xyc_m[j])
                    prim.add(N + bit_count, N + bit_count_j, c)
                    bit_count_j += 1
            bit_count += 1
    tmp = prim.make_min_span_tree()
    ans = min(ans, tmp)

print(ans)
