from itertools import permutations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    u, v, cost = map(int, readline().split())
    graph[u - 1].append((v - 1, cost))
    graph[v - 1].append((u - 1, cost))
ans = 0
for val in permutations(range(n)):
    tmp = 0
    for i in range(1, n):
        for nv, c in graph[val[i - 1]]:
            if nv == val[i]:
                tmp += c
                break
        else:
            ans = max(ans, tmp)
            break
    else:
        ans = max(ans, tmp)


print(ans)
