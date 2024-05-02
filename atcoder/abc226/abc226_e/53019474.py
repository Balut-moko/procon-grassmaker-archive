from atcoder.dsu import DSU


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
uf = DSU(N)
MOD = 998244353
for i in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
    uf.merge(u, v)

ans = 1
for g in uf.groups():
    cnt = 0
    for v in g:
        cnt += len(graph[v])
    if len(g) * 2 == cnt:
        ans = ans * 2 % MOD
    else:
        ans = 0

print(ans)
