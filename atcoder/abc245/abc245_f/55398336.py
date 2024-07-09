from sys import setrecursionlimit
import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")


class SCC_graph:
    def __init__(self, N: int) -> None:
        self.N = N
        self.graph = [[] for _ in range(self.N)]
        self.reverse_ordered_graph = [[] for _ in range(self.N)]
        setrecursionlimit(10**7)

    def add_edge(self, frm: int, to: int):
        self.graph[frm].append(to)
        self.reverse_ordered_graph[to].append(frm)

    def scc_ids(self):
        order = []
        used = [0] * self.N
        ids = [-1] * self.N

        def _dfs(i: int):
            used[i] = 1
            for t in self.graph[i]:
                if not used[t]:
                    _dfs(t)
            order.append(i)

        def _reverse_ordered_dfs(i: int, col: int):
            ids[i] = col
            used[i] = 1
            for t in self.reverse_ordered_graph[i]:
                if not used[t]:
                    _reverse_ordered_dfs(t, col)

        for i in range(self.N):
            if not used[i]:
                _dfs(i)

        used = [0] * self.N
        group_num = 0

        for s in reversed(order):
            if not used[s]:
                _reverse_ordered_dfs(s, group_num)
                group_num += 1
        return group_num, ids

    def scc(self):
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i in range(self.N):
            groups[ids[i]].append(i)
        return groups

    def construct(self):
        group_num, ids = self.scc_ids()
        # 縮約後のグラフを構築
        G0 = [set() for _ in range(group_num)]
        GP = [[] for _ in range(group_num)]
        for v in range(self.N):
            lbs = ids[v]
            for w in self.graph[v]:
                lbt = ids[w]
                if lbs == lbt:
                    continue
                G0[lbs].add(lbt)
            GP[lbs].append(v)
        return G0, GP


N, M = map(int, input().split())

g = SCC_graph(N)
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    g.add_edge(u, v)

gc, gp = g.construct()
gr = [[] for _ in range(len(gc))]
for i in range(len(gc)):
    for v in gc[i]:
        gr[v].append(i)

reach = [None] * len(gc)


def rec(i, p, d):
    if len(gp[i]) > 1:
        reach[i] = True
        return True
    if reach[i] is not None:
        return reach[i]
    res = False
    for x in gc[i]:
        if x != p:
            res |= rec(x, i, d + 1)
    reach[i] = res
    return res


for i in range(len(gc)):
    if reach[i] is None:
        rec(i, -1, 0)
ans = 0
for i in range(len(gc)):
    if reach[i]:
        ans += len(gp[i])

print(ans)
