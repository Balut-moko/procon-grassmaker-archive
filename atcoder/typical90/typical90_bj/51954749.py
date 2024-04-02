from collections import deque


N = int(input())
AB = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * N]

que = deque([])
white = [False] * N
ans = []
graph = [[] for _ in range(N)]
for i in range(N):
    a, b = AB[i]
    graph[a].append(i)
    graph[b].append(i)
    if a == i or b == i:
        que.append(i)
        if not white[i]:
            ans.append(i + 1)
        white[i] = True

while que:
    v = que.popleft()
    if not white[v]:
        ans.append(v + 1)
    white[v] = True
    for w in graph[v]:
        if white[w]:
            continue
        que.append(w)

if len(ans) == N:
    print(*ans[::-1], sep="\n")
else:
    print(-1)
