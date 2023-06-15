from itertools import permutations
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
for val in permutations(range(1, n)):
    pre = 0
    for v in val:
        if v not in graph[pre]:
            break
        pre = v
    else:
        ans += 1

print(ans)
