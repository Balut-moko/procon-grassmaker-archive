from sys import stdin

readline = stdin.readline
n = int(readline())
c = sorted(map(int, readline().split()))
mod = 1000000007
ans = c[0]
for i in range(1, n):
    ans *= c[i] - i
    ans %= mod
print(ans)
