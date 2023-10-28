from collections import deque
from itertools import permutations
from copy import deepcopy


def check(grid):
    for i in range(N):
        cnt = [0] * 4
        s = "."
        for j in range(N):
            cnt[grid[i][j]] += 1
            if s == ".":
                s = di[grid[i][j]]
        for k in range(1, 4):
            if cnt[k] > 1:
                return False
        if s != "." and R[i] != s:
            return False

    for j in range(N):
        cnt = [0] * 4
        t = "."
        for i in range(N):
            cnt[grid[i][j]] += 1
            if t == ".":
                t = di[grid[i][j]]
        for k in range(1, 4):
            if cnt[k] > 1:
                return False
        if t != "." and C[j] != t:
            return False
    return True


def print_ans(grid):
    for i in range(N):
        for j in range(N):
            grid[i][j] = di[grid[i][j]]
    print("Yes")
    for val in grid:
        print(*val, sep="")
    exit()


N = int(input())
R = input()
C = input()
di = {0: ".", 1: "A", 2: "B", 3: "C"}

grid = [[0] * N for _ in range(N)]
li = list(permutations(range(N), 3))
que = deque([[grid, 0]])

while que:
    grid, row = que.pop()
    for val in li:
        for i in range(N):
            grid[row][i] = 0
        for i, v in enumerate(val):
            grid[row][v] = i + 1
        if check(grid):
            if row == N - 1:
                print_ans(grid)
            else:
                new = deepcopy(grid)
                que.append([new, row + 1])

print("No")
