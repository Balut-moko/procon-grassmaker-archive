from sys import stdin

readline = stdin.readline
n = int(readline())
a = [int(readline()) for _ in [0] * n]
a = a + a
dp = [[-10**20] * n for _ in [0] * (n + 1)]

for j in range(n):
    dp[0][j] = 0
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            dp[i + 1][j] = max(dp[i][j] + a[j + i], dp[i][(j + 1) % n] + a[j])
        else:
            jj = (j + n - 1) % n
            if a[j + i] < a[jj]:
                dp[i + 1][jj] = max(dp[i + 1][jj], dp[i][j])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])


ans = max(dp[-1])
print(ans)
