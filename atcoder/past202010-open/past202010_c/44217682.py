from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]

ans = [[0] * m for _ in [0] * n]


def check(r, c):
    dd = ((0, 0), (-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1))
    for dr, dc in dd:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if s[nr][nc] == "#":
            ans[r][c] += 1


for i in range(n):
    for j in range(m):
        check(i, j)


for val in ans:
    print(*val, sep="")
