from sys import stdin
from atcoder import dsu

readline = stdin.readline
n, m = map(int, readline().split())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m]
c = list(map(int, readline().split()))

uf = dsu.DSU(n * 2)

for i in range(m):
    a, b = ab[i]
    if c[a] != c[b]:
        uf.merge(a + c[a] * n, b + c[b] * n)

flag = False
for i in range(m):
    a, b = ab[i]
    if c[a] == c[b] and uf.same(a + c[a] * n, b + c[b] * n):
        flag = True

print("Yes" if flag else "No")
