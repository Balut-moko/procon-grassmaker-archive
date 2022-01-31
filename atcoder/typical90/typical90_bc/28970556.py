from sys import stdin
from itertools import combinations

readline = stdin.readline
n, p, q = map(int, readline().split())
a = list(map(lambda x: int(x) % p, readline().split()))
cnt = 0
for a, b, c, d, e in combinations(a, 5):
    if a * b % p * c % p * d % p * e % p == q:
        cnt += 1
print(cnt)
