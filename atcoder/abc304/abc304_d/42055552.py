from bisect import bisect_left
from collections import defaultdict
from sys import stdin

readline = stdin.readline
W, H = map(int, readline().split())
N = int(readline())
pq = [tuple(map(int, readline().split())) for _ in [0] * N]
A = int(readline())
a = list(map(int, readline().split()))
B = int(readline())
b = list(map(int, readline().split()))

cnt = 0
dic = defaultdict(int)

for p, q in pq:
    pa = bisect_left(a, p)
    qb = bisect_left(b, q)
    if dic[(pa, qb)] == 0:
        cnt += 1
    dic[(pa, qb)] += 1
m = 0
if cnt == (A + 1) * (B + 1):
    m = min(dic.values())
M = max(dic.values())
print(m, M)
