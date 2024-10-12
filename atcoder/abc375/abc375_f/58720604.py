INF = 1 << 60


class WarshallFloyd:
    def __init__(self, N):
        self.N = N
        self.hasNegativeCycle = False
        self.dist = [[INF] * N for _ in [0] * N]

    def add(self, u, v, c, undirected=True):
        self.dist[u][v] = c
        if undirected:
            self.dist[v][u] = c

    def add_edge(self, u, v, c):
        self.dist[u][v] = min(self.dist[u][v], c)
        self.dist[v][u] = self.dist[u][v]

        for k in {u, v}:
            for i in range(self.N):
                for j in range(self.N):
                    self.dist[i][j] = min(
                        self.dist[i][j], self.dist[i][k] + self.dist[k][j]
                    )

    def warshallFloydSearch(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.dist[i][j] = min(
                        self.dist[i][j], self.dist[i][k] + self.dist[k][j]
                    )
        for i in range(self.N):
            if self.dist[i][i] < 0:
                self.hasNegativeCycle = True
                break
        for i in range(self.N):
            self.dist[i][i] = 0


N, M, Q = map(int, input().split())

ABC = [tuple(map(int, input().split())) for _ in [0] * M]
query = [tuple(map(int, input().split())) for _ in [0] * Q]

stop = set()
for q in query:
    if q[0] == 1:
        stop.add(q[1] - 1)

wf = WarshallFloyd(N)

for i in range(M):
    if i not in stop:
        u, v, cost = ABC[i]
        wf.add(u - 1, v - 1, cost)

wf.warshallFloydSearch()
ans = []
for i in range(Q - 1, -1, -1):
    com, *xy = query[i]
    if com == 1:
        idx = xy[0] - 1
        u, v, cost = ABC[idx]
        wf.add_edge(u - 1, v - 1, cost)
    else:
        x, y = xy
        ans.append(wf.dist[x - 1][y - 1] if wf.dist[x - 1][y - 1] != INF else -1)

print(*ans[::-1], sep="\n")
