from atcoder.dsu import DSU


N = int(input())

deg = [0] * N
uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * (N - 1)]

for i in range(N - 1):
    u, v = uv[i]
    deg[u] += 1
    deg[v] += 1

uf = DSU(N)
cnt2 = [0] * N
for i in range(N - 1):
    u, v = uv[i]
    if deg[u] == deg[v] == 3:
        uf.merge(u, v)
    if deg[u] == 3 and deg[v] == 2:
        cnt2[u] += 1
    if deg[u] == 2 and deg[v] == 3:
        cnt2[v] += 1
ans = 0
for group in uf.groups():
    cnt = 0
    for v in group:
        cnt += cnt2[v]
    ans += cnt * (cnt - 1) // 2
print(ans)
