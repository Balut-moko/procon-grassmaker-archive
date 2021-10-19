from sys import stdin
from collections import defaultdict


class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)] for i in range(N)]

    def add(self, u, v, c, directed=False):
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        hasNegativeCycle = False
        for i in range(self.N):
            if self.d[i][i] < 0:
                hasNegativeCycle = True
                break
        for i in range(self.N):
            self.d[i][i] = 0
        return hasNegativeCycle, self.d


readline = stdin.readline
h, w = map(int, readline().split())
graph = WarshallFloyd(10)
for i in range(10):
    cost = list(map(int, readline().split()))
    for j in range(10):
        if i != j:
            graph.add(i, j, cost[j], directed=True)
hasNegativeCycle, d = graph.WarshallFloyd_search()
nums = defaultdict(int)
for _ in [0] * h:
    num_li = list(map(int, readline().split()))
    for num in num_li:
        if num != -1:
            nums[num] += 1
ans = 0
for i in range(10):
    ans += d[i][1] * nums[i]
print(ans)
