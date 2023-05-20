from collections import defaultdict
from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
query = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * q]
groups = n
cnt = [0] * n
graph = defaultdict(set)
for que in query:
    if que[0] == 0:
        u = que[1]
        v = que[2]
        if cnt[u] == 0:
            groups -= 1
        if cnt[v] == 0:
            groups -= 1
        cnt[u] += 1
        cnt[v] += 1
        graph[u].add(v)
        graph[v].add(u)
        print(groups)
    else:
        v = que[1]
        if cnt[v] != 0:
            groups += 1
        cnt[v] = 0
        for u in graph[v]:
            graph[u].discard(v)
            cnt[u] -= 1
            if cnt[u] == 0:
                groups += 1
        graph[v].clear()
        print(groups)
