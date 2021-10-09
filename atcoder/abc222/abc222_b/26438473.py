from sys import stdin

readline = stdin.readline
n, p = map(int, readline().split())
a = list(map(int, readline().split()))
ans = 0
for i in range(n):
    if a[i] < p:
        ans += 1
print(ans)
