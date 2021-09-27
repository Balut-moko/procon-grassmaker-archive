from sys import stdin

readline = stdin.readline
n, t = map(int, readline().split())
ts = list(map(int, readline().split()))
ans, tmp = 0, 0
for i in range(n):
    if ts[i] < tmp:
        ans -= tmp - ts[i]
    ans += t
    tmp = ts[i] + t

print(ans)
