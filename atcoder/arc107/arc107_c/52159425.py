from math import perm
from atcoder.dsu import DSU


N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * N]
MOD = 998244353
uf_c = DSU(N)
uf_r = DSU(N)

for x in range(N):
    for y in range(N):
        if x == y:
            continue
        flag = True
        for i in range(N):
            if A[i][x] + A[i][y] > K:
                flag = False
        if flag:
            uf_c.merge(x, y)

        flag = True
        for i in range(N):
            if A[x][i] + A[y][i] > K:
                flag = False
        if flag:
            uf_r.merge(x, y)
ans = 1
for v in uf_c.groups():
    ans *= perm(len(v))
    ans %= MOD

for v in uf_r.groups():
    ans *= perm(len(v))
    ans %= MOD

print(ans)
