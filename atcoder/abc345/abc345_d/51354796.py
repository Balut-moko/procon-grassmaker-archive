from itertools import permutations


def check():
    for r in range(H):
        for c in range(W):
            if not grid[r][c]:
                return False
    return True


def check_tile(r, c, a, b):
    global grid
    ng = [g[:] for g in grid]
    for i in range(a):
        for j in range(b):
            nr = r + i
            nc = c + j
            if not (0 <= nr < H and 0 <= nc < W):
                return False
            if grid[nr][nc]:
                return False
            ng[nr][nc] = True
    grid = ng
    return True


def dfs(tiles: list, r, c):
    global grid
    while grid[r][c]:
        c += 1
        if c == W:
            r += 1
            c = 0
        if r == H:
            break
    if r == H:
        global ans
        ans = True
        return
    if len(tiles) == 0:
        return
    t = tiles[:]
    a, b = t.pop()
    pre = [g[:] for g in grid]
    if check_tile(r, c, a, b):
        dfs(t, r, c)
        tiles = t[:]
        grid = pre
    if a != b and check_tile(r, c, b, a):
        dfs(t, r, c)
        tiles = t[:]
        grid = pre
    return


N, H, W = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in [0] * N]

ans = False
for val in permutations(AB):
    val = list(val)
    grid = [[False] * W for _ in [0] * H]

    dfs(val, 0, 0)
    if check():
        ans = True
print("Yes" if ans else "No")
