from sys import stdin

readline = stdin.readline
h, w, c = map(int, readline().split())
a = [list(map(int, readline().split())) for _ in [0] * h]
inf = 1 << 60
ans = inf
for k in range(2):
    if k == 1:
        a = [val[::-1] for val in a]
    dp = [[inf] * w for _ in [0] * h]
    X = [[inf] * w for _ in [0] * h]
    dp[0][0] = a[0][0]
    for i in range(h):
        for j in range(w):
            if i != 0:
                ans = min(ans, dp[i - 1][j] + c + a[i][j])
                dp[i][j] = min(a[i][j], dp[i][j], dp[i - 1][j] + c)
            if j != 0:
                ans = min(ans, dp[i][j - 1] + c + a[i][j])
                dp[i][j] = min(a[i][j], dp[i][j], dp[i][j - 1] + c)
print(ans)
