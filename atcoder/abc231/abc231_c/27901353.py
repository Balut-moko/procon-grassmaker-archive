from sys import stdin
from bisect import bisect_left
readline = stdin.readline
n, q = map(int, readline().split())
a = sorted(map(int, readline().split()))
x = [int(readline()) for _ in [0] * q]

for i in range(q):
    print(n - bisect_left(a, x[i]))
