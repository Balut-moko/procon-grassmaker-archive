from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))
ans = 1 << 60
idx_n = p.index(n)
idx_1 = p.index(1)
if idx_1 == 0 and idx_n == n - 1:
    ans = 0
if idx_1 < idx_n:
    ans = min(ans, p[0] + 1)
    ans = min(ans, n - p[-1] + 2)
else:
    ans = min(ans, n - p[0] + 1)
    ans = min(ans, p[-1] + 2)

print(ans)
