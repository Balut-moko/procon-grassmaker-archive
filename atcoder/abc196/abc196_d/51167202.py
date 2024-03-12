def dfs(r, c, a):
    if r == H:
        return a == 0
    if c == W:
        return dfs(r + 1, 0, a)
    if used[r][c]:
        return dfs(r, c + 1, a)
    res = 0
    if r + 1 < H and not used[r + 1][c] and a > 0:
        used[r][c] = True
        used[r + 1][c] = True
        res += dfs(r, c + 1, a - 1)
        used[r][c] = False
        used[r + 1][c] = False
    if c + 1 < W and not used[r][c + 1] and a > 0:
        used[r][c] = True
        used[r][c + 1] = True
        res += dfs(r, c + 1, a - 1)
        used[r][c] = False
        used[r][c + 1] = False
    res += dfs(r, c + 1, a)
    return res


H, W, A, B = map(int, input().split())
used = [[False] * W for _ in [0] * H]

print(dfs(0, 0, A))
