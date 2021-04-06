#!/usr/bin/env python3
from collections import deque


def main():
    h, w, n = map(int, input().split())
    grid = []
    for i in range(h):
        col = input()
        grid.append(col)
        if 'S' in col:
            sy, sx = i, col.index('S')
    visited = [[-1] * w for _ in range(h)]
    queue = deque([])
    queue.append([sy, sx])
    visited[sy][sx] = 0
    ans = 0
    for i in range(n):
        while queue:
            y, x = queue.popleft()
            if grid[y][x] == str(i + 1):
                ans += visited[y][x]
                visited = [[-1] * w for _ in range(h)]
                visited[y][x] = 0
                queue = deque([[y, x]])
                break
            for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                new_y, new_x = y + j, x + k
                if 0 <= new_y < h and 0 <= new_x < w and grid[new_y][new_x] != "X" and visited[new_y][new_x] == -1:
                    visited[new_y][new_x] = visited[y][x] + 1
                    queue.append([new_y, new_x])
    print(ans)


if __name__ == "__main__":
    main()
