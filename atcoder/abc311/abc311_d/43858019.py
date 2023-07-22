from collections import deque
from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
grid = [readline()[:-1] for _ in [0] * n]

used = [[0] * m for _ in [0] * n]
stop = [[-1] * m for _ in [0] * n]
used[1][1] = 1
stop[1][1] = 1


def bfs():
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    que = deque([(1, 1)])
    while que:
        r, c = que.popleft()
        for dr, dc in dd:
            nr = r + dr
            nc = c + dc
            while grid[nr][nc] != "#":
                used[nr][nc] = 1
                nr = nr + dr
                nc = nc + dc
            nr = nr - dr
            nc = nc - dc
            if stop[nr][nc] == -1:
                stop[nr][nc] = 1
                que.append((nr, nc))


bfs()
print(sum(map(sum, used)))
