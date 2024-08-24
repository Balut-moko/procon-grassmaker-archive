import sys

sys.setrecursionlimit(10**7)

N, K = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

V = list(map(lambda x: int(x) - 1, input().split()))
SV = set(V)
flag = [False] * N


def dfs(v, p):
    if len(graph[v]) == 0 and v not in SV:
        flag[v] = True
        return True
    res = True
    for nv in graph[v]:
        if nv == p:
            continue
        res &= dfs(nv, v)
    if res and v not in SV:
        flag[v] = True
        return True
    return False


dfs(V[0], -1)

print(N - sum(flag))
