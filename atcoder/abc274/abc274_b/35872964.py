from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
c = [tuple(readline()) for _ in [0] * h]
ans = [0] * w

for i in range(h):
    for j in range(w):
        if c[i][j] == "#":
            ans[j] += 1
print(*ans)
