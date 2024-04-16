N, K, L = map(int, input().split())
MOD = 998244353

ans = 1

for i in range(1, N + 1):
    if i <= N - K:
        ans *= max(0, L + 1 - i)
    else:
        ans *= max(0, L - (N - K))
    ans %= MOD

print(ans)
