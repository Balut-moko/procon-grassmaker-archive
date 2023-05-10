from sys import stdin


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


readline = stdin.readline
n, p, K = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in [0] * n]

idx_lst = []

for i in range(n):
    for j in range(n):
        if a[i][j] == -1:
            idx_lst.append((i, j))


def meguru_bisect(ok: int, ng: int):
    def solve(mid: int):
        wf = WarshallFloyd(n)
        for i in range(n):
            for j in range(n):
                wf.add(i, j, a[i][j])
        for i, j in idx_lst:
            wf.add(i, j, mid)
        wf.warshallFloydSearch()
        cnt = 0
        for i in range(n):
            for j in range(i + 1, n):
                if wf.dist[i][j] <= p:
                    cnt += 1

        return cnt <= K

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


l = meguru_bisect(1 << 60, 0)
K -= 1
r = meguru_bisect(1 << 60, 0)

if r - l < 1 << 50:
    print(r - l)
else:
    print("Infinity")
