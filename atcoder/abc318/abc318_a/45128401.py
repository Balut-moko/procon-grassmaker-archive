from sys import stdin

readline = stdin.readline
n, m, p = map(int, readline().split())
ans = 0
for i in range(m - 1, n, p):
    ans += 1

print(ans)
