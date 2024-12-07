H, W, D = map(int, input().split())
S = [input() for _ in [0] * H]


def manhattan_distance(xr, xc, yr, yc):
    return abs(xr - yr) + abs(xc - yc)


def count(xr, xc, yr, yc):
    cnt = 0
    for r in range(H):
        for c in range(W):
            if S[r][c] == "#":
                continue
            if (
                manhattan_distance(xr, xc, r, c) <= D
                or manhattan_distance(yr, yc, r, c) <= D
            ):
                cnt += 1
    return cnt


ans = 0
for xr in range(H):
    for xc in range(W):
        if S[xr][xc] == "#":
            continue
        for yr in range(H):
            for yc in range(W):
                if S[yr][yc] == "#":
                    continue
                if xr == yr and xc == yc:
                    continue
                ans = max(ans, count(xr, xc, yr, yc))

print(ans)
