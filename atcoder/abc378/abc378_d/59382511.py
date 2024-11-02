from sys import setrecursionlimit

setrecursionlimit(100000)


def dfs(r, c, cnt):
    if cnt == K:
        return 1
    used[r][c] = True
    res = 0
    for dr, dc in dd:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < H and 0 <= nc < W) or grid[nr][nc] == "#":
            continue
        if used[nr][nc] is True:
            continue
        res += dfs(nr, nc, cnt + 1)

    used[r][c] = False
    return res


H, W, K = map(int, input().split())
grid = [input() for _ in [0] * H]
used = [[False] * W for _ in range(H)]
dd = ((-1, 0), (0, 1), (1, 0), (0, -1))

ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            ans += dfs(i, j, 0)
print(ans)
