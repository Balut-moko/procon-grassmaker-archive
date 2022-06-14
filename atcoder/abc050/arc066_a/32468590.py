from collections import defaultdict
from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
mod = 10**9 + 7
di = defaultdict(set)
for i in range(n):
    if a[i] % 2 == n % 2:
        print(0)
        exit()
    left = (n - 1 + a[i]) // 2
    di[left].add(i)
    di[n - left - 1].add(i)
ans = 1
for i in range(n // 2):
    if len(di[i]) == 2:
        ans *= len(di[i])
    elif len(di[i]) == 1 and i == n // 2 - 1:
        pass
    else:
        ans = 0
    ans %= mod
print(ans)
