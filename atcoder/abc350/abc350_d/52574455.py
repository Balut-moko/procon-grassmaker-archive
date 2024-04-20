from atcoder.dsu import DSU


N, M = map(int, input().split())
uf = DSU(N)
graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
    uf.merge(u, v)

ans = 0
for i in range(N):
    member = uf.size(i)
    ans += member - len(graph[i]) - 1

print(ans // 2)
