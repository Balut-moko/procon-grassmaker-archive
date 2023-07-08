from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))

b = sorted(a[2:])
ans = 1 << 60

for i in range(n - m - 1):
    ans = min(ans, a[0] - min(a[0], b[i]) + max(a[1], b[i + m - 1]) - a[1])
print(ans)
