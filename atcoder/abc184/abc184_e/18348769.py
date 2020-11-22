#!/usr/bin/env python3
from collections import deque
from math import inf


def main():
    h, w = map(int, input().split())
    maze = [input() for _ in range(h)]
    visited = [[inf] * w for _ in range(h)]
    azlist = [[] for _ in range(26)]
    warped = [0] * 26
    for i in range(h):
        if 'S' in maze[i]:
            start = [i, maze[i].index('S')]
        if 'G' in maze[i]:
            goal = [i, maze[i].index('G')]
        for j in range(w):
            if maze[i][j] != 'S' and maze[i][j] != 'G' and maze[i][j] != '.' and maze[i][j] != '#':
                azlist[ord(maze[i][j]) - ord('a')].append([i, j])

    queue1 = deque([start])
    queue2 = deque()
    visited[start[0]][start[1]] = 0
    cnt = 1
    while queue1:
        y, x = queue1.popleft()
        for j in range(-1, 2):
            for k in range(-1, 2):
                new_y, new_x = y + j, x + k
                if 0 <= new_y < h and 0 <= new_x < w and maze[new_y][new_x] != '#' and j**2 + k**2 == 1 and visited[new_y][new_x] > cnt:
                    visited[new_y][new_x] = cnt
                    queue2.appendleft([new_y, new_x])
        if maze[y][x] != 'S' and maze[y][x] != 'G' and maze[y][x] != '.' and maze[y][x] != '#' and warped[ord(maze[y][x]) - ord('a')] == 0:
            warped[ord(maze[y][x]) - ord('a')] = 1
            for p in azlist[ord(maze[y][x]) - ord('a')]:
                if (p[0] != y or p[1] != x) and visited[p[0]][p[1]] > cnt:
                    visited[p[0]][p[1]] = cnt
                    queue2.appendleft(p)
        if len(queue1) == 0:
            queue1 = deque(list(queue2))
            queue2.clear()
            cnt += 1
    print(visited[goal[0]][goal[1]] if visited[goal[0]][goal[1]] != inf else -1)


if __name__ == "__main__":
    main()
