from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
a = list(map(int, readline().split()))
ans = 0
if x < a[0]:
    ans += a[0] - x
    a[0] = x

for i in range(1, n):
    if x < a[i - 1] + a[i]:
        ans += a[i - 1] + a[i] - x
        a[i] -= a[i - 1] + a[i] - x

print(ans)
