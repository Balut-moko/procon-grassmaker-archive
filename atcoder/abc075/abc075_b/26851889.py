from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
grid = [readline()[:-1] for _ in [0] * h]
ans = [[0] * w for _ in range(h)]
dd = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            for r, c in dd:
                ir = i + r
                jc = j + c
                if 0 <= ir < h and 0 <= jc < w:
                    ans[ir][jc] += 1

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            ans[i][j] = '#'
for val in ans:
    print(*val, sep="")
