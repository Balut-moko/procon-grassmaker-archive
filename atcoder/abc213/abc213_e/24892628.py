from sys import stdin
from collections import deque

readline = stdin.readline
h, w = map(int, readline().split())
inf = 10**10
maze = [readline()[:-1] for _ in [0] * h]
visited = [[inf] * w for _ in [0] * h]
queue = deque([[0, 0]])
visited[0][0] = 0
nxt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
warp = []
for i in range(-2, 3):
    for j in range(-2, 3):
        if abs(i) + abs(j) < 4:
            warp.append([i, j])
while queue:
    y, x = queue.popleft()
    if [y, x] == [h - 1, w - 1]:
        break
    for j, k in nxt:
        new_y, new_x = y + j, x + k
        if 0 <= new_y < h and 0 <= new_x < w:
            if maze[new_y][new_x] == "." and visited[y][x] < visited[new_y][new_x]:
                visited[new_y][new_x] = visited[y][x]
                queue.appendleft([new_y, new_x])
    for j, k in warp:
        new_y, new_x = y + j, x + k
        if 0 <= new_y < h and 0 <= new_x < w:
            if visited[new_y][new_x] == inf:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])
print(visited[-1][-1])
