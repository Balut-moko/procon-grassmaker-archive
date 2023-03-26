from sys import stdin

readline = stdin.readline
n = int(readline())
s = [list(readline()[:-1]) for _ in [0] * n]

for i in range(n - 1, 0, -1):
    for j in range(2 * n - 1):
        if s[i][j] == "X":
            for k in range(-1, 2):
                if 0 <= j + k < 2 * n - 1 and s[i - 1][j + k] != ".":
                    s[i - 1][j + k] = "X"
for val in s:
    print(*val, sep="")
