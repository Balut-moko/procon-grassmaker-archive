from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
ans = 0
while k < n:
    n = n - k + 1
    ans += 1
if n != 0:
    ans += 1
print(ans)
