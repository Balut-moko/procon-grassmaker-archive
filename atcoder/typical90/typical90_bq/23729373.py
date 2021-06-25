from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
mod = 1000000007
if n == 1:
    ans = k
else:
    ans = k * (k - 1)
if 3 <= n:
    ans *= pow(k - 2, n - 2, mod)
    ans %= mod
print(ans)
