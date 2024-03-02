N = int(input())

A = [tuple(map(int, input().split())) for _ in [0] * N]

graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            graph[i].append(j + 1)

for g in graph:
    print(*sorted(g))
