from collections import Counter
from sys import stdin
from atcoder import dsu

readline = stdin.readline
n, k, L = map(int, readline().split())
uf_r = dsu.DSU(n)
uf_t = dsu.DSU(n)
for i in range(k):
    p, q = map(lambda x: int(x) - 1, readline().split())
    uf_r.merge(p, q)
for i in range(L):
    r, s = map(lambda x: int(x) - 1, readline().split())
    uf_t.merge(r, s)

pairs = [(uf_r.leader(i), uf_t.leader(i)) for i in range(n)]

cnt = Counter(pairs)

ans = [cnt[pairs[i]] for i in range(n)]
print(*ans)
