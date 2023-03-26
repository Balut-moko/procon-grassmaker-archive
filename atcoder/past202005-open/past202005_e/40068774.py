from sys import stdin

readline = stdin.readline
n, m, q = map(int, readline().split())

graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x) - 1, readline().split())
    graph[a].append(b)
    graph[b].append(a)

c = list(map(int, readline().split()))

for _ in range(q):
    que = list(map(int, readline().split()))
    x = que[1] - 1

    if que[0] == 1:
        print(c[x])
        for e in graph[x]:
            c[e] = c[x]
    else:
        print(c[x])
        c[x] = que[2]
