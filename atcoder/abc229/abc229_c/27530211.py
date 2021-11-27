from sys import stdin

readline = stdin.readline
n, w = map(int, readline().split())
ab = sorted([tuple(map(int, readline().split())) for _ in [0] * n], reverse=True)
ans = 0
for i in range(n):
    if ab[i][1] <= w:
        ans += ab[i][0] * ab[i][1]
        w -= ab[i][1]
    else:
        ans += ab[i][0] * w
        break
print(ans)
