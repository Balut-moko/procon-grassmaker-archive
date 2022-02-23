from sys import stdin

readline = stdin.readline
l, r = map(int, readline().split())
l_digit = len(str(l))
r_digit = len(str(r))
ans = 0
mod = 10**9 + 7
for i in range(l_digit, r_digit + 1):
    lo = max(10 ** (i - 1), l)
    hi = min(int("9" * i), r)
    if hi - lo + 1 > 0:
        ans += i * (hi * (hi + 1) // 2 - (lo - 1) * lo // 2)
        ans %= mod
print(ans)
