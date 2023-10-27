N, X = map(int, input().split())
T = list(map(int, input().split()))

dp = [0] * (X + 1)
mod = 998244353
inv_N = pow(N, -1, mod)
ans = 0

dp[0] = 1
if T[0] > X:
    ans += dp[0] * inv_N

for i in range(1, X + 1):
    for j in range(N):
        if T[j] <= i:
            dp[i] += dp[i - T[j]]
            dp[i] %= mod
    dp[i] *= inv_N
    dp[i] %= mod
    if i + T[0] > X:
        ans += dp[i] * inv_N
        ans %= mod
print(ans)
