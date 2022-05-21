from itertools import combinations
from sys import stdin

readline = stdin.readline
n, w = map(int, readline().split())
a = list(map(int, readline().split()))
w_li = [0] * (10**6 + 1)
for i in range(3):
    for val in combinations(a, i + 1):
        if sum(val) <= 10**6:
            w_li[sum(val)] = 1
print(sum(w_li[: w + 1]))
