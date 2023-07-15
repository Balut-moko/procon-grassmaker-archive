from sys import stdin

readline = stdin.readline
n, p,q = map(int, readline().split())
d = list(map(int, readline().split()))

ans = p

for i in range(n):
    ans = min(ans,d[i]+q)

print(ans)