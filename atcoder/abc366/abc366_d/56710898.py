N = int(input())
grid = [[] * N for _ in [0] * N]
for x in range(N):
    for y in range(N):
        z = tuple(map(int, input().split()))
        grid[x].append(z)

cs = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

for x in range(N):
    for y in range(N):
        for z in range(N):
            cs[x + 1][y + 1][z + 1] = (
                cs[x][y + 1][z + 1]
                + cs[x + 1][y + 1][z]
                + cs[x + 1][y][z + 1]
                - cs[x + 1][y][z]
                - cs[x][y + 1][z]
                - cs[x][y][z + 1]
                + cs[x][y][z]
                + grid[x][y][z]
            )

Q = int(input())
for _ in range(Q):
    lx, rx, ly, ry, lz, rz = tuple(map(int, input().split()))
    lx -= 1
    ly -= 1
    lz -= 1

    ans = (
        cs[rx][ry][rz]
        - cs[rx][ry][lz]
        - cs[lx][ry][rz]
        - cs[rx][ly][rz]
        + cs[lx][ly][rz]
        + cs[lx][ry][lz]
        + cs[rx][ly][lz]
        - cs[lx][ly][lz]
    )
    print(ans)
