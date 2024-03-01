N = int(input())
LR = [tuple(map(int, input().split())) for _ in [0] * N]
ans = 0
for i in range(N):
    for j in range(i):
        li, ri = LR[i]
        lj, rj = LR[j]
        ALL = (ri - li + 1) * (rj - lj + 1)
        for k in range(li, ri + 1):
            ans += max(0, rj - max(k, lj - 1)) / ALL

print(ans)
