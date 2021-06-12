#!/usr/bin/env python3
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def size(self, x):
        return -self.root[self.Find_Root(x)]

    def members(self, x):
        root = self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    h, w = map(int, input().split())
    grid = [[0] * w for _ in range(h)]
    UF = UnionFind(h * w)
    q = int(input())
    for _ in range(q):
        que = list(map(int, input().split()))
        que[1] -= 1
        que[2] -= 1
        if que[0] == 1:
            x = que[1] * w + que[2]
            grid[que[1]][que[2]] = 1
            move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for m in move:
                y = (que[1] + m[0]) * w + que[2] + m[1]
                if 0 <= que[1] + m[0] < h and 0 <= que[2] + m[1] < w:
                    if grid[que[1] + m[0]][que[2] + m[1]] == 1:
                        UF.Unite(x, y)
        else:
            que[3] -= 1
            que[4] -= 1
            x = que[1] * w + que[2]
            y = que[3] * w + que[4]
            if grid[que[1]][que[2]] == 1 and grid[que[3]][que[4]] == 1 and UF.isSameGroup(x, y):
                print('Yes')
            else:
                print('No')


if __name__ == "__main__":
    main()
