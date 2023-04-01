from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())

if n * n < m:
    print(-1)
    exit()

if m <= n:
    print(m)
    exit()
ans = 1 << 60
for a in range(1, n + 1):
    x = (m + a - 1) // a
    if x <= n:
        ans = min(ans, a * x)
    if x < a:
        break
print(ans if ans != 1 << 60 else -1)
