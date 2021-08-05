from sys import stdin

readline = stdin.readline
m,n, N = map(int, readline().split())
ans = N
while m <= N:
    div, mod = divmod(N, m)
    ans += div * n
    N = div * n + mod
print(ans)
