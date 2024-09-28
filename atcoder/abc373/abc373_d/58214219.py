from collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(M):
    u, v, cost = map(int, input().split())
    graph[u - 1].append((v - 1, cost))
    graph[v - 1].append((u - 1, -cost))


ans = [None] * N


for i in range(N):
    if ans[i] is not None:
        continue
    que = deque([i])
    ans[i] = 0
    while que:
        v = que.popleft()
        d = ans[v]
        for w, c in graph[v]:
            if ans[w] is not None:
                continue
            ans[w] = c + d
            que.append(w)

print(*ans)
