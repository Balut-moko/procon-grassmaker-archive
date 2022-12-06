from sys import stdin

readline = stdin.readline
h, w, n, m = map(int, readline().split())
ab = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * n]
cd = [tuple(map(lambda x: int(x) - 1, readline().split())) for _ in [0] * m]

grid = [["."] * w for _ in [0] * h]
light = [[[False] * 2 for _ in [0] * w] for _ in [0] * h]

for c, d in cd:
    grid[c][d] = "#"
d = 0
for a, b in ab:
    if light[a][b][d]:
        continue
    dd = ((-1, 0), (1, 0))
    for (dr, dc) in dd:
        nr, nc = a, b
        while 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
            light[nr][nc][d] = True
            nr, nc = nr + dr, nc + dc
d = 1
for a, b in ab:
    if light[a][b][d]:
        continue
    dd = ((0, 1), (0, -1))
    for (dr, dc) in dd:
        nr, nc = a, b
        while 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "#":
            light[nr][nc][d] = True
            nr, nc = nr + dr, nc + dc

ans = 0
for i in range(h):
    for j in range(w):
        ans += max(light[i][j])
print(ans)
