from sys import stdin
from collections import defaultdict

readline = stdin.readline
n = int(readline())
papers = [tuple(map(int, readline().split())) for _ in [0] * n]

grid = [[0] * 1002 for _ in range(1002)]
ans_di = defaultdict(int)

for p in papers:
    lx, ly, rx, ry = p
    grid[lx][ly] += 1
    grid[lx][ry] -= 1
    grid[rx][ly] -= 1
    grid[rx][ry] += 1

for i in range(1002):
    for j in range(1, 1002):
        grid[i][j] += grid[i][j - 1]

for i in range(1, 1002):
    for j in range(1002):
        grid[i][j] += grid[i - 1][j]

for i in range(1002):
    for j in range(1002):
        ans_di[grid[i][j]] += 1

for i in range(n):
    print(ans_di[i + 1])
