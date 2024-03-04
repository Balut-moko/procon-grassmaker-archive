from collections import deque
from atcoder.dsu import DSU


N = int(input())
Q = int(input())
query = [tuple(map(int, input().split())) for _ in [0] * Q]

A = [[] for _ in range(N)]

for q in range(Q):
    T, X, Y, V = query[q]
    X, Y = X - 1, Y - 1
    if T == 0:
        A[X].append((Y, V))


dist = [None] * len(A)
for i in range(N):
    if dist[i] is None:
        que = deque([i])  # root
        dist[i] = 0
        while que:
            v = que.popleft()
            d = dist[v]
            for w, c in A[v]:
                if dist[w] is not None:
                    continue
                dist[w] = c - d
                que.append(w)

uf = DSU(N)
for q in range(Q):
    T, X, Y, V = query[q]
    X, Y = X - 1, Y - 1
    if T == 0:
        uf.merge(X, Y)
        continue
    if not uf.same(X, Y):
        print("Ambiguous")
        continue
    ans = dist[Y]
    d = V - dist[X]
    if (X - Y) % 2 == 0:
        ans += d
    else:
        ans -= d
    print(ans)
