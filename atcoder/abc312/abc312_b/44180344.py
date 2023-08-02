from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]


def check(r, c):
    for dr in range(3):
        for dc in range(3):
            if s[r + dr][c + dc] != "#":
                return False
    for dr in range(4):
        if s[r + dr][c + 3] != ".":
            return False
    for dc in range(4):
        if s[r + 3][c + dc] != ".":
            return False
    for dr in range(3):
        for dc in range(3):
            if s[r + dr + 6][c + dc + 6] != "#":
                return False
    for dr in range(4):
        if s[r + dr + 5][c + 5] != ".":
            return False
    for dc in range(4):
        if s[r + 5][c + dc + 5] != ".":
            return False
    return True


for i in range(n - 8):
    for j in range(m - 8):
        if check(i, j):
            print(i + 1, j + 1)
