from sys import stdin
from collections import defaultdict


def f(x: int):
    digit_sum = sum(map(int, str(x)))
    return (x + digit_sum) % 100000


readline = stdin.readline
n, k = map(int, readline().split())

num_di = defaultdict(int)
num_di[n] += 1
cnt1 = 0
origin = n
for i in range(k):
    n = f(n)
    cnt1 += 1
    num_di[n] += 1
    if num_di[n] == 2:
        break

cnt2 = 0
while origin != n:
    origin = f(origin)
    cnt2 += 1
    k -= 1

if cnt1 - cnt2 != 0:
    k %= cnt1 - cnt2

for i in range(k):
    n = f(n)
print(n)
