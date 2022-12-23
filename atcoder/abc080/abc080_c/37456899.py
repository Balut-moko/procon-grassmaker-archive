from sys import stdin

readline = stdin.readline
n = int(readline())
f = [tuple(map(int, readline().split())) for _ in [0] * n]
p = [tuple(map(int, readline().split())) for _ in [0] * n]
ans = -1 << 60
for flg in range(1, 1 << 10):
    tmp = 0
    for i in range(n):
        cnt = 0
        for j in range(10):
            if f[i][j] == 1 and (flg >> j) & 1:
                cnt += 1
        tmp += p[i][cnt]
    ans = max(ans, tmp)

print(ans)
