from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))

MOD = 998244353
A_sum = list(accumulate(A, initial=0))
ans = 0
for j in range(1, N):
    sm = A_sum[j] % MOD
    ans += sm * pow(10, len(str(A[j])), MOD)
    ans %= MOD
    ans += A[j] * j
    ans %= MOD

print(ans)
