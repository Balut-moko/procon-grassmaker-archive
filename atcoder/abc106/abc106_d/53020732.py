from atcoder.fenwicktree import FenwickTree


N, M, Q = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in [0] * M]
pq = [tuple(map(int, input().split())) for _ in [0] * Q]

bits = [FenwickTree(N + 1) for _ in [0] * (N + 1)]
for l, r in LR:
    bits[l].add(r, 1)

ans = [[0] * (N + 1) for _ in [0] * (N + 1)]
for i in range(1, N + 1):
    for j in range(i, N + 1):
        for k in range(i, j + 1):
            ans[i][j] += bits[k].sum(k, j + 1)

for p, q in pq:
    print(ans[p][q])
