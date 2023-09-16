from collections import deque


n, m = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in [0] * m]
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, x, y = info[i]
    graph[a - 1].append((b - 1, x, y))
    graph[b - 1].append((a - 1, -x, -y))

ans = [None] * n

ans[0] = (0, 0)


def bfs():
    que = deque([0])  # root
    while que:
        v = que.popleft()
        for w, dx, dy in graph[v]:
            if ans[w] is not None:
                continue
            x, y = ans[v]
            ans[w] = (x + dx, y + dy)
            que.append(w)
    return


bfs()

for val in ans:
    if val is None:
        print("undecidable")
    else:
        print(*val)
