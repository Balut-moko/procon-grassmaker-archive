from sys import stdin

readline = stdin.readline
a, k = map(int, readline().split())
if k == 0:
    ans = 2 * (10**12) - a
else:
    ans = 0
    while a < 2 * (10**12):
        a += 1 + k * a
        ans += 1
print(ans)
