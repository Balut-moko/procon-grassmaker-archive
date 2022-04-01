from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a.sort()
mod = 998244353
ans = 0
now = 0
for i in range(n):
    if i == 0:
        ans += a[i] * a[i]
    else:
        tmp = now
        tmp += a[i] + a[i - 1]
        tmp *= a[i]
        tmp %= mod
        ans += tmp
        ans %= mod
        now += a[i - 1]
        now *= 2
        now %= mod
print(ans % mod)
