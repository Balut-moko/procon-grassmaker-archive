from collections import Counter
from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
mod = 10**9 + 7
cnt = Counter(s)
ans = 1

for val in cnt.values():
    ans *= val + 1
    ans %= mod
ans -= 1
print(ans)
