from collections import Counter
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def scc(N, G, RG):
    order = []
    used = [0] * N
    group = [None] * N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)

    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n)]
graph_r = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph_r[b].append(a)

_, group = scc(n, graph, graph_r)
cnt = Counter(group)
ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2

print(ans)
