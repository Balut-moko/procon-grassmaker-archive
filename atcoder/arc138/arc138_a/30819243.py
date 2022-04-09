from sys import stdin
from bisect import bisect_left

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
ak_min = [10 ** 9] * k
ak_min[k - 1] = a[k - 1]
for i in range(k - 2, -1, -1):
    ak_min[i] = min(ak_min[i + 1], a[i])

ans = 10 ** 9
for i in range(k, n):
    tmp = bisect_left(ak_min, a[i])
    if tmp == 0:
        continue

    ans = min(ans, i - tmp + 1)

print(ans if ans != 10 ** 9 else -1)
