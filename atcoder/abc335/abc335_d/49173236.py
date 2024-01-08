N = int(input())

grid = [[None] * N for _ in range(N)]
dd = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

x, y = 0, 0
cur = 1
cnt = 1
grid[(N + 1) // 2 - 1][(N + 1) // 2 - 1] = "T"
grid[x][y] = cnt
while cnt < N * N - 1:
    dx, dy = dd[cur]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] is None:
        cnt += 1
        grid[nx][ny] = cnt
        x, y = nx, ny
        continue
    cur = (cur + 1) % 4

for row in grid:
    print(*row)
