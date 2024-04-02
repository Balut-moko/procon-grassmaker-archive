from collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N + M)]
for i in range(M):
    K = int(input())
    R = tuple(map(lambda x: int(x) - 1, input().split()))
    for v in R:
        graph[N + i].append(v)
        graph[v].append(N + i)

ans = [-1] * (N + M)
ans[0] = 0
que = deque([])
que.append(0)

while que:
    v = que.popleft()
    d = ans[v]
    for w in graph[v]:
        if ans[w] >= 0:
            continue
        ans[w] = d + 1
        que.append(w)


ans = [v // 2 if v >= 0 else -1 for v in ans[:N]]
print(*ans, sep="\n")
