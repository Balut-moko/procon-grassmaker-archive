from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
a = list(map(int, readline().split()))
lrv = [tuple(map(int, readline().split())) for _ in [0] * q]
ans = 0
b = [0] * n
for i in range(n - 1):
    b[i] = a[i + 1] - a[i]
    ans += abs(b[i])

for l, r, v in lrv:
    l -= 1
    r -= 1
    before = abs(b[l - 1]) + abs(b[r])
    if l >= 1:
        b[l - 1] += v
    if r < n - 1:
        b[r] -= v
    after = abs(b[l - 1]) + abs(b[r])
    ans += after - before
    print(ans)
