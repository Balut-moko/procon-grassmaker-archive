from sys import stdin

readline = stdin.readline
h1, w1 = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h1]
h2, w2 = map(int, readline().split())
b = [tuple(map(int, readline().split())) for _ in [0] * h2]


def check(i: int, j: int):
    if bin(i).count("1") != h2 or bin(j).count("1") != w2:
        return False
    row = -1
    for r in range(h1):
        col = -1
        if (i >> r) & 1:
            row += 1
            for c in range(w1):
                if (j >> c) & 1:
                    col += 1
                    if a[r][c] != b[row][col]:
                        return False
    return True


ans = "No"
for i in range(1 << h1):
    for j in range(1 << w1):
        if check(i, j):
            ans = "Yes"
print(ans)
