# 強連結成分分解(Strongly Connected Components)
from sys import setrecursionlimit


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


N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

scc = SCC_graph(N)
ans = 0

for i in range(N):
    scc.add_edge(i, A[i])
    if i == A[i]:
        ans += 1

groups = scc.scc()
ans += sum(len(g) for g in groups if len(g) >= 2)
print(ans)
