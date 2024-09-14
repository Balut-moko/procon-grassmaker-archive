from itertools import permutations


N = int(input())
Mg = int(input())
G_uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in [0] * Mg]

Mh = int(input())
graphH = [[] for _ in range(N)]
for i in range(Mh):
    u, v = map(lambda x: int(x) - 1, input().split())
    graphH[u].append(v)
    graphH[v].append(u)

A = []
for i in range(N - 1):
    a = [0] * N + list(map(int, input().split()))
    A.append(a[-N:])

ans = 1 << 60

for val in permutations(range(N)):
    di = {v: i for i, v in enumerate(val)}
    graphG = [[] for _ in range(N)]
    for u, v in G_uv:
        graphG[di[u]].append(di[v])
        graphG[di[v]].append(di[u])
    tmp = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if j in graphG[i] and j in graphH[i]:
                continue
            if j not in graphG[i] and j not in graphH[i]:
                continue
            tmp += A[i][j]
    ans = min(ans, tmp)
print(ans)
