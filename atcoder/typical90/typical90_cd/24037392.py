from sys import stdin

readline = stdin.readline
l, r = map(int, readline().split())
ans = 0
mod = 1000000007
for i in range(1, len(str(r)) + 1):
    if l <= r:
        ans += (r - l + 1) * (2 * l + (r - l)) // 2
        ans %= mod
    l = max(l, 10**i)

print(ans)
