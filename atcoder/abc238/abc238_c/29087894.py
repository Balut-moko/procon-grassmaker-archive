from sys import stdin

readline = stdin.readline
n = int(readline())
mod = 998244353
ans = 0
digit = len(str(n))
for i in range(digit - 1):
    tmp = 9 * 10 ** i
    ans += (tmp * (tmp + 1)) // 2
    ans %= mod
last = n - (10 ** (digit - 1)) + 1
ans += (last * (last + 1)) // 2
ans %= mod
print(ans)
