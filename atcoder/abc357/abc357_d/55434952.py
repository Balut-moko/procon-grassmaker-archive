N = int(input())
MOD = 998244353
ans = 1
x = N
while x:
    x //= 10
    ans *= 10
    ans %= MOD

inv = pow(ans - 1, -1, MOD)
ans = N * ((pow(ans, N, MOD) - 1) * inv) % MOD
print(ans)
