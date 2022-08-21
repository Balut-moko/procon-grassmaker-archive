from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
g = [list(readline()[:-1]) for _ in [0] * h]

i, j = 0, 0
cnt = 0
while cnt < 300000:
    if g[i][j] == "U":
        if i == 0:
            break
        i -= 1
    if g[i][j] == "D":
        if i == h - 1:
            break
        i += 1
    if g[i][j] == "L":
        if j == 0:
            break
        j -= 1
    if g[i][j] == "R":
        if j == w - 1:
            break
        j += 1
    cnt += 1

if cnt == 300000:
    print(-1)
else:
    print(i + 1, j + 1)
