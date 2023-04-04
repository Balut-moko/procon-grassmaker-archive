from sys import stdin

readline = stdin.readline
n = int(readline())
a = []
for i in range(n):
    lst = list(map(int, readline().split()))
    a.append([0] * (i + 1) + lst)

ALL = 1 << n

score = [0] * ALL

for s in range(ALL):
    for i in range(n):
        for j in range(i + 1, n):
            if (s & (1 << i) > 0) and (s & (1 << j) > 0):
                score[s] += a[i][j]

ans = -1 << 60

for g1 in range(ALL):
    for g2 in range(ALL):
        if g1 & g2 > 0:
            continue
        g3 = ALL - (g1 | g2) - 1
        ans = max(ans, score[g1] + score[g2] + score[g3])
print(ans)
