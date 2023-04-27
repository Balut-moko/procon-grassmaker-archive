from sys import stdin

readline = stdin.readline
n = int(readline())
lr = [tuple(map(int, readline().split())) for _ in [0] * n]
ans = 0

for i in range(n):
    li, ri = lr[i]
    for j in range(i):
        lj, rj = lr[j]
        for k in range(li, ri + 1):
            ans += max(0, rj - max(k, lj - 1)) / ((ri - li + 1) * (rj - lj + 1))

print(ans)
