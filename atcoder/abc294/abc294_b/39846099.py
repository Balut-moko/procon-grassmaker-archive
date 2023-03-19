from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]

for i in range(h):
    ans = []
    for j in range(w):
        if a[i][j] == 0:
            ans.append(".")
        else:
            ans.append(chr(ord("A") + a[i][j] - 1))
    print(*ans, sep="")
