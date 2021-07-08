from sys import stdin
from collections import deque


def int1(x):
    return int(x) - 1


readline = stdin.readline
h, w = map(int, readline().split())
s = list(map(int1, readline().split()))
t = list(map(int1, readline().split()))
maze = [tuple(readline()[:-1]) for _ in [0] * h]
inf = 10**6
visited = [[inf] * h * w for _ in [0] * 4]
q = deque()
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(4):
    visited[i][s[0] * w + s[1]] = 0
    q.append([s[0], s[1], i])
while q:
    y, x, m = q.popleft()
    if y == t[0] and x == t[1]:
        ans = inf
        for i in range(4):
            ans = min(ans, visited[i][t[0] * w + t[1]])
        exit(print(ans))
    now = visited[m][y * w + x]
    for i in range(4):
        if visited[i][y * w + x] <= now + 1:
            continue
        visited[i][y * w + x] = now + 1
        q.append([y, x, i])
    nxt_y, nxt_x = y + move[m][1], x + move[m][0]
    if 0 <= nxt_y < h and 0 <= nxt_x < w:
        if maze[nxt_y][nxt_x] == '.':
            if now < visited[m][nxt_y * w + nxt_x]:
                visited[m][nxt_y * w + nxt_x] = now
                q.appendleft([nxt_y, nxt_x, m])
