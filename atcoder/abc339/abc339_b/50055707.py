H, W, N = map(int, input().split())

grid = [["."] * W for _ in [0] * H]
r, c = 0, 0
muki = 0
dd = ((-1, 0), (0, 1), (1, 0), (0, -1))
for _ in range(N):
    if grid[r][c] == "#":
        grid[r][c] = "."
        muki -= 1
        muki %= 4
        r += dd[muki][0]
        r %= H
        c += dd[muki][1]
        c %= W
    else:
        grid[r][c] = "#"
        muki += 1
        muki %= 4
        r += dd[muki][0]
        r %= H
        c += dd[muki][1]
        c %= W

for v in grid:
    print(*v, sep="")
