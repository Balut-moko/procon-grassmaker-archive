from lib2to3.pgen2 import grammar
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, readline().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
cnt = 0
for i, e in enumerate(graph):
    tmp = 0
    for v in e:
        if v < i:
            tmp += 1
    if tmp == 1:
        cnt += 1
print(cnt)
