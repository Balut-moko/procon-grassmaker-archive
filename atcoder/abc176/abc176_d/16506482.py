#!/usr/bin/env python3
from collections import deque
from math import inf


def bfs(maze, visited, Ch, Cw, Dh, Dw, H, W):
    queue = deque([[Ch, Cw]])
    visited[Ch][Cw] = 0

    while queue:
        y, x = queue.popleft()
        if [y, x] == [Dh, Dw]:
            break
        for j in range(-2, 3):
            for k in range(-2, 3):
                new_y, new_x = y + j, x + k
                if 0 <= new_y < H and 0 <= new_x < W:
                    if maze[new_y][new_x] == "." and j**2 + k**2 == 1 and visited[y][x] < visited[new_y][new_x]:
                        visited[new_y][new_x] = visited[y][x]
                        queue.appendleft([new_y, new_x])
                    elif maze[new_y][new_x] == "." and visited[new_y][new_x] == inf:
                        visited[new_y][new_x] = visited[y][x] + 1
                        queue.append([new_y, new_x])
    return visited[Dh][Dw]


def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    maze = [input() for i in range(H)]
    visited = [[inf] * W for i in range(H)]

    dist = bfs(maze, visited, Ch - 1, Cw - 1, Dh - 1, Dw - 1, H, W)
    print(dist if dist != inf else -1)


if __name__ == "__main__":
    main()
