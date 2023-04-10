from itertools import product
from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [readline()[:-1] for _ in [0] * h]
mod = 10 ** 9 + 7
dp = [[0] * w for _ in [0] * h]

for i in range(h):
    if a[i][0] == "#":
        break
    dp[i][0] = 1
for j in range(w):
    if a[0][j] == "#":
        break
    dp[0][j] = 1

for i, j in product(range(1, h), range(1, w)):
    if a[i][j] == ".":
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

print(dp[-1][-1])
