from collections import deque

N, M = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
B = list(map(lambda x: int(x) - 1, input().split()))

graph = [[] for _ in range(N)]
for i in range(M):
    graph[A[i]].append(B[i])
    graph[B[i]].append(A[i])

color = [0 for _ in range(N)]


def bfs(s):
    que = deque([s])  # root
    while que:
        v = que.popleft()
        for w in graph[v]:
            if color[w] == 0:
                color[w] = -color[v]
                que.append(w)
            elif color[w] == color[v]:
                return False
    return True


for i in range(N):
    if color[i] == 0:
        color[i] = 1
        flag = bfs(i)
        if not flag:
            print("No")
            exit()

print("Yes")
