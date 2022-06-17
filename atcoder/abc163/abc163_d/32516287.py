from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
s = n * (n + 1) // 2
ans = 0
mod = 10**9 + 7
for i in range(k, n + 2):
    lo = i * (i - 1) // 2
    hi = s - (n - i) * (n + 1 - i) // 2
    ans += hi - lo + 1
    ans %= mod
print(ans)
