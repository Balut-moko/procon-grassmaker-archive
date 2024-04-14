from atcoder.dsu import DSU


N, M = map(int, input().split())
P = list(map(int, input().split()))
XY = [tuple(map(int, input().split())) for _ in [0] * M]

di = {v: i for i, v in enumerate(P)}
uf = DSU(N + 1)

for x, y in XY:
    uf.merge(x, y)

ans = 0
for i in range(N):
    if uf.same(P[i], i + 1):
        ans += 1

print(ans)
