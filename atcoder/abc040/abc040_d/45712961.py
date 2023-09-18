from collections import deque

from atcoder.dsu import DSU


n, m = map(int, input().split())
aby = [tuple(map(int, input().split())) for _ in [0] * m]

q = int(input())
vw = [tuple([i] + list(map(int, input().split()))) for i in range(q)]

aby.sort(reverse=True, key=lambda x: x[2])
vw.sort(reverse=True, key=lambda x: x[2])
que1 = deque(aby)
que2 = deque(vw)

uf = DSU(n + 1)
ans = [None] * q
while que2:
    i, v, w = que2.popleft()
    while que1:
        a, b, y = que1[0]
        if w < y:
            uf.merge(a, b)
            que1.popleft()
        else:
            break
    ans[i] = uf.size(v)

print(*ans, sep="\n")
