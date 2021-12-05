from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
grid = [list(readline()[:-1]) for _ in [0] * h]
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
color_set = {'1', '2', '3', '4', '5'}
for r in range(h):
    for c in range(w):
        if grid[r][c] == '.':
            nxt = set()
            for dr, dc in dd:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    if grid[nr][nc] != '.':
                        nxt.add(grid[nr][nc])
            color = color_set - nxt
            if len(color):
                grid[r][c] = color.pop()
            else:
                grid[r][c] = '1'
for val in grid:
    print(*val, sep='')
