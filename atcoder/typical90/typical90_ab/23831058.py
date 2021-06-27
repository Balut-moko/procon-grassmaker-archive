from sys import stdin

readline = stdin.readline
n = int(readline())
xy = [[0] * 1001 for _ in [0] * 1001]

for _ in [0] * n:
    lx, ly, rx, ry = map(int, readline().split())
    xy[ry][lx] -= 1
    xy[ry][rx] += 1
    xy[ly][lx] += 1
    xy[ly][rx] -= 1

for i in range(1001):
    for j in range(1, 1001):
        xy[i][j] += xy[i][j - 1]
for j in range(1001):
    for i in range(1, 1001):
        xy[i][j] += xy[i - 1][j]
paper = [0] * (n + 1)
for i in range(1001):
    for j in range(1001):
        paper[xy[i][j]] += 1
print(*paper[1:], sep='\n')
