from sys import stdin


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
mod = 998244353
ans = 0

for i in range(1, n + 1):
    dp = [[[0] * (i + 1) for _ in [0] * (i + 1)] for _ in [0] * (n + 1)]
    dp[0][0][0] = 1

    for j in range(n):
        for k in range(i + 1):
            for l in range(i):
                dp[j + 1][k][l] += dp[j][k][l]
                if k != i:
                    dp[j + 1][k + 1][(l + a[j]) % i] += dp[j][k][l]
    ans += dp[n][i][0]
    ans %= mod
print(ans)
