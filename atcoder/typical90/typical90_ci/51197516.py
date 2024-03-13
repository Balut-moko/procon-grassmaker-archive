class WarshallFloyd:
    def __init__(self, N):
        self.N = N
        self.hasNegativeCycle = False
        INF = 1 << 60
        self.dist = [[INF] * N for _ in [0] * N]

    def add(self, u, v, c, undirected=True):
        self.dist[u][v] = c
        if undirected:
            self.dist[v][u] = c

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


def solve(mid: int, K):
    wf = WarshallFloyd(N)
    for u in range(N):
        for v in range(N):
            c = A[u][v]
            if c == -1:
                c = mid
            wf.add(u, v, c)
    wf.warshallFloydSearch()
    cnt = 0
    for u in range(N):
        for v in range(u + 1, N):
            if wf.dist[u][v] <= P:
                cnt += 1
    return cnt >= K


def meguru_bisect(ok: int, ng: int, K):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid, K):
            ok = mid
        else:
            ng = mid
    return ok


N, P, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in [0] * N]

l = meguru_bisect(0, 1 << 60, K + 1)
r = meguru_bisect(0, 1 << 60, K)

print(r - l if r - l < 1 << 30 else "Infinity")
