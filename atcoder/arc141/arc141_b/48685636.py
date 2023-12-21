N, M = map(int, input().split())
MOD = 998244353
if N > 60:
    print(0)
    exit()

dp = [[0] * 61 for _ in [0] * N]
for j in range(60):
    low = 1 << j
    up = min(M + 1, 1 << (j + 1))
    dp[0][j] = max(0, up - low)

for i in range(1, N):
    for j in range(i, 60):
        low = 1 << j
        up = min(M + 1, 1 << (j + 1))
        for k in range(j):
            dp[i][j] += dp[i - 1][k]
        dp[i][j] *= max(0, up - low)
        dp[i][j] %= MOD
ans = 0
for j in range(60):
    ans += dp[N - 1][j]
    ans %= MOD

print(ans)
