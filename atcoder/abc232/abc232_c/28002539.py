from sys import stdin
from itertools import permutations

readline = stdin.readline
n, m = map(int, readline().split())
graph_a = [set() for _ in range(n)]
for i in range(m):
    a, b = map(int, readline().split())
    graph_a[a - 1].add(b - 1)
    graph_a[b - 1].add(a - 1)

graph_b = [set() for _ in range(n)]
for i in range(m):
    a, b = map(int, readline().split())
    graph_b[a - 1].add(b - 1)
    graph_b[b - 1].add(a - 1)

for val in permutations(range(n)):
    d = {i: v for i, v in enumerate(val)}
    graph_c = [set() for _ in range(n)]
    for i in range(n):
        tmp_li = list(graph_b[i])
        for t in tmp_li:
            graph_c[d[i]].add(d[t])
    if graph_a == graph_c:
        print('Yes')
        exit()
print('No')
