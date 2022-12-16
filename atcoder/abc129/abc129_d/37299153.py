from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
grid = [readline()[:-1] for _ in [0] * h]

ans_col = [[1] * w for _ in [0] * h]
ans_row = [[1] * w for _ in [0] * h]

for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            if 0 <= j - 1 < w:
                ans_row[i][j] = ans_row[i][j - 1] + 1
        else:
            ans_row[i][j] = 0
for i in range(h):
    for j in range(w - 1, -1, -1):
        if grid[i][j] == ".":
            if 0 <= j + 1 < w and grid[i][j + 1] == ".":
                ans_row[i][j] = ans_row[i][j + 1]
for j in range(w):
    for i in range(h):
        if grid[i][j] == ".":
            if 0 <= i - 1 < h:
                ans_col[i][j] = ans_col[i - 1][j] + 1
        else:
            ans_col[i][j] = 0
for j in range(w):
    for i in range(h - 1, -1, -1):
        if grid[i][j] == ".":
            if 0 <= i + 1 < h and grid[i + 1][j] == ".":
                ans_col[i][j] = ans_col[i + 1][j]
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, ans_row[i][j] + ans_col[i][j] - 1)
print(ans)
