from atcoder.dsu import DSU


N = int(input())

uf = DSU(N)

for _ in range(N - 1):
    u, v = map(int, input().split())
    if u != 1:
        uf.merge(u - 1, v - 1)

print(N - max(len(g) for g in uf.groups()))
