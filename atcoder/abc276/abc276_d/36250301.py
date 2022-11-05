from sys import stdin
from collections import defaultdict


def factorization(n):
    di = defaultdict(int)
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            di[i] += cnt

    if temp != 1:
        di[temp] = 1

    if not di:
        di[n] = 1

    return di


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

min_2 = 1 << 60
min_3 = 1 << 60

for val in a:
    di = factorization(val)
    min_2 = min(min_2, di[2])
    min_3 = min(min_3, di[3])

ans = 0

di = factorization(a[0])
di[2] = min_2
di[3] = min_3

num = 1
for k, v in di.items():
    num *= k ** v

for val in a:
    di = factorization(val)
    ans += di[2] - min_2
    ans += di[3] - min_3
    di[2] = min_2
    di[3] = min_3
    tmp = 1
    for k, v in di.items():
        tmp *= k ** v
    if num != tmp:
        print(-1)
        exit()
print(ans)
