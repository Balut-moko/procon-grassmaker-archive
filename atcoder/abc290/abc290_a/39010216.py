from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
ans = 0

for i in range(m):
    ans += a[b[i] - 1]
print(ans)
