N = int(input())
S = input()
MOD = 10**9 + 7
dp = [[0] * N for _ in [0] * N]
for j in range(N):
    dp[0][j] = 1

for i in range(N - 1):
    cum = [0] * (N + 1)
    for j in range(N - i):
        cum[j + 1] = (cum[j] + dp[i][j]) % MOD

    if S[i] == "<":
        for j in range(N - i):
            dp[i + 1][j] = (cum[N - i] - cum[j + 1]) % MOD
    else:
        for j in range(N - i):
            dp[i + 1][j] = cum[j + 1]
print(dp[-1][0])
