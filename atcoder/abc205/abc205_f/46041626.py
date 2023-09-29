from collections import deque

H, W, N = map(int, input().split())
V = H + W + N * 2 + 2
G = [[] for _ in range(V)]
X = H + W + N * 2
Y = H + W + N * 2 + 1


def add_edge(u, v, c):
    G[u].append([v, c, len(G[v])])
    G[v].append([u, 0, len(G[u]) - 1])


def bfs(s):
    D = [-1] * V
    D[s] = 0
    que = deque([s])
    while que:
        u = que.popleft()
        for next, capacity, _ in G[u]:
            if capacity > 0 and D[next] < 0:
                D[next] = D[u] + 1
                que.append(next)
    return D


def dfs(v, t, f, removed, D):
    if v == t:
        return f
    while removed[v] < len(G[v]):
        next, capacity, rev = G[v][removed[v]]
        if capacity > 0 and D[v] < D[next]:
            flow = dfs(next, t, min(f, capacity), removed, D)
            if flow > 0:
                G[v][removed[v]][1] -= flow
                G[next][rev][1] += flow
                return flow
        removed[v] += 1
    return 0


def calc_max_flow(s, t):
    flow = 0
    while True:
        D = bfs(s)
        if D[t] < 0:
            return flow
        removed = [0] * V
        while True:
            f = dfs(s, t, 1e10, removed, D)
            if f == 0:
                break
            flow += f


for i in range(N):
    A, B, C, D = map(lambda x: int(x) - 1, input().split())
    for r in range(A, C + 1):
        add_edge(r, H + W + i, 1)
    for c in range(B, D + 1):
        add_edge(H + W + N + i, H + c, 1)

for r in range(H):
    add_edge(X, r, 1)

for c in range(W):
    add_edge(H + c, Y, 1)

for i in range(N):
    add_edge(H + W + i, H + W + N + i, 1)

max_flow = calc_max_flow(X, Y)
print(max_flow)
