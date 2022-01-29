from sys import stdin

readline = stdin.readline
n, l, w = map(int, readline().split())
a = list(map(int, readline().split())) + [l]
dist_li = [a[i + 1] - (a[i] + w) for i in range(n) if a[i + 1] - (a[i] + w) > 0]
ans = 0
if a[0] != 0:
    ans += a[0] // w
    if a[0] % w != 0:
        ans += 1
for val in dist_li:
    ans += val // w
    if val % w != 0:
        ans += 1

print(ans)
