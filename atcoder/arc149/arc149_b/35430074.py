from sys import stdin
from bisect import bisect_left


def calc_LIS(li):
    lis = [li[0]]
    for i in range(len(li)):
        if lis[-1] < li[i]:
            lis.append(li[i])
        else:
            lis[bisect_left(lis, li[i])] = li[i]
    return lis


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
a_di = {key: val for key, val in zip(a, b)}
bb = []
for i in range(1, n + 1):
    atob = a_di[i]
    bb.append(atob)

lis = calc_LIS(bb)
print(n + len(lis))
