from collections import defaultdict, deque
from sys import stdin


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def root(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        return -self.parents[self.root(x)]

    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def members(self, x: int):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.root(member)].append(member)
        return group_members

    def __str__(self) -> str:
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


# 2grarh check
def dfs(graph, start):
    stack = deque([])
    colors = defaultdict(int)
    di = {1: 0, -1: 0}
    stack.append([start, 1])
    while stack:
        v, color = stack.pop()
        if colors[v] == 0:
            di[color] += 1
            colors[v] = color
            for to in graph[v]:
                if colors[to] == color:
                    return False, di
                if colors[to] == 0:
                    stack.append([to, -color])
    return True, di


readline = stdin.readline
n, m = map(int, readline().split())
uv = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m]
uf = UnionFind(n)
graph = [[] for _ in range(n)]
for u, v in uv:
    uf.union(u, v)
    graph[u].append(v)
    graph[v].append(u)

ans = n * (n - 1) // 2 - m
roots = uf.roots()
for root in roots:
    flg, di = dfs(graph, root)
    if not flg:
        print(0)
        exit()
    ans -= di[1] * (di[1] - 1) // 2
    ans -= di[-1] * (di[-1] - 1) // 2
print(ans)
