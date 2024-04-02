from collections import defaultdict, deque


N, M = map(int, input().split())

group_d = defaultdict(set)
di = dict()
for i in range(M):
    K = int(input())
    R = tuple(map(lambda x: int(x) - 1, input().split()))
    di[i] = R
    for r in R:
        group_d[r].add(i)

INF = 1 << 60
ans = [INF] * N
ans[0] = 0
used = set()
que = deque([])
for v in group_d[0]:
    que.append(v)

while que:
    idx = que.popleft()
    used.add(idx)
    p = di[idx]
    mn = INF
    for v in p:
        mn = min(mn, ans[v])
    nxt = set()
    for v in p:
        if ans[v] >= INF:
            ans[v] = mn + 1
            nxt |= group_d[v]
    for n in nxt.difference(used):
        que.append(n)

ans = [v if v < INF else -1 for v in ans]
print(*ans, sep="\n")
