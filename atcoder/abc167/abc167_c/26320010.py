from sys import stdin

readline = stdin.readline
n, m, x = map(int, readline().split())
ca = [tuple(map(int, readline().split())) for _ in [0] * n]
ans = 1 << 60
for i in range(2**n):
    cost = 0
    skill = [0] * m
    for j in range(n):
        if (i >> j) & 1:
            cost += ca[j][0]
            for k in range(m):
                skill[k] += ca[j][k + 1]
    for s in skill:
        if s < x:
            break
    else:
        ans = min(ans, cost)
print(ans if ans != (1 << 60) else -1)
