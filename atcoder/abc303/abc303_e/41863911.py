from collections import deque
from sys import stdin

readline = stdin.readline
n = int(readline())

graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = n
ans = []

for i in range(n):
    if len(graph[i]) >= 3:
        ans.append(len(graph[i]))
        cnt -= len(graph[i]) + 1

ans.sort()
ans = [2] * (cnt // 3) + ans
print(*ans)
