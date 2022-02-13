from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
mod = 10**9 + 7

if n == 1:
    ans = k % mod
elif n == 2:
    ans = k * (k - 1)
    ans %= mod
else:
    if k < 3:
        ans = 0
    else:
        ans = k * (k - 1)
        ans *= pow(k - 2, n - 2, mod)
        ans %= mod
print(ans)
