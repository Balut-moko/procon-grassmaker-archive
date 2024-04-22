N = int(input())
C = [int(input()) for _ in [0] * N]
MOD = 10**9 + 7
left = [-1] * 200001
dp = [0] * (N + 1)

dp[0] = 1

for i in range(N):
    dp[i + 1] += dp[i]
    c = C[i]
    if 0 <= left[c] < i - 1:
        dp[i + 1] += dp[left[c] + 1]
    left[c] = i
    dp[i + 1] %= MOD

print(dp[-1])
