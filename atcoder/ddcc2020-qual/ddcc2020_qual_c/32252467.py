from sys import stdin

readline = stdin.readline
h, w, k = map(int, readline().split())
grid = [readline()[:-1] for _ in [0] * h]

ans = [[0] * w for _ in range(h)]
cnt = 0
for r in range(h):
    for c in range(w):
        if grid[r][c] == "#":
            cnt += 1
        ans[r][c] = cnt
for r in range(h):
    if grid[r].count("#") == 0:
        continue
    cc = grid[r].index("#")
    if cc != 0:
        for c in range(cc):
            ans[r][c] = ans[r][cc]
for r in range(h - 2, -1, -1):
    if grid[r].count("#") == 0:
        for c in range(w):
            ans[r][c] = ans[r + 1][c]
for r in range(1, h):
    if grid[r].count("#") == 0:
        for c in range(w):
            ans[r][c] = ans[r - 1][c]
for a in ans:
    print(*a)
