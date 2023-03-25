from sys import stdin

readline = stdin.readline
r, c = map(int, readline().split())
b = [tuple(readline()[:-1]) for _ in [0] * r]

ans = [["#"] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if b[i][j] == ".":
            ans[i][j] = "."

for i in range(r):
    for j in range(c):
        if b[i][j] != "." and b[i][j] != "#":
            for ii in range(r):
                for jj in range(c):
                    if abs(i - ii) + abs(j - jj) <= int(b[i][j]):
                        ans[ii][jj] = "."

for val in ans:
    print(*val, sep="")
