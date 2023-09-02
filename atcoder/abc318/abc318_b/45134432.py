from sys import stdin

readline = stdin.readline
n = int(readline())
grid = [[False] * 101 for _ in [0] * 101]

for _ in range(n):
    a, b, c, d = map(int, readline().split())
    for i in range(a, b):
        for j in range(c, d):
            grid[i][j] = True

ans = sum(map(sum, grid))
print(ans)
