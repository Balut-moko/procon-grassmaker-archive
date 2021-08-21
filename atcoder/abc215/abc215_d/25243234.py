from sys import stdin
from math import gcd
from functools import reduce


def lcm(x, y):
    return (x * y) // gcd(x, y)


def lcm_any(*numbers):
    return reduce(lcm, numbers, 1)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
tmp_set = set()
for v in a:
    tmp = factorization(v)
    for t in tmp:
        tmp_set.add(t[0])
ans_li = [True] * (m + 1)
ans_li[0] = False
for v in list(tmp_set):
    if v == 1:
        continue
    k = 1
    while v * k <= m:
        ans_li[v * k] = False
        k += 1
ans_num = [i for i, b in enumerate(ans_li) if b]
print(len(ans_num))
print(*ans_num, sep='\n')
