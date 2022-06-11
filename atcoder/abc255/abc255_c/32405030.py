from sys import stdin

readline = stdin.readline
x, a, d, n = map(int, readline().split())

x -= a

a1 = 0
an = d * (n - 1)

ans = 1 << 62
ans = min(abs(a1 - x), abs(an - x))

if min(a1, an) <= x <= max(a1, an):
    if d != 0:
        mod = abs(x % d)
        ans = min(ans, mod, abs(d - mod), abs(d + mod))
    else:
        ans = min(ans, abs(x))
print(ans)
