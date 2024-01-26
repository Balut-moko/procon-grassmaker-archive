N = int(input())
A = [tuple(map(int, input().split())) for _ in [0] * N]
MOD = 10**9 + 7

ALL = 1 << N
dp = [0] * ALL

dp[0] = 1

for s in range(1, ALL):
    i = bin(s).count("1")
    for j in range(N):
        if A[i - 1][j] == 1 and (s & (1 << j)) > 0:
            dp[s] += dp[s & ~(1 << j)]
            dp[s] %= MOD

print(dp[-1])
