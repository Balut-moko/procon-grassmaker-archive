from collections import defaultdict
from sys import stdin


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
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
n = int(readline())
di = defaultdict(int)
mod = 10**9 + 7
for i in range(1, n + 1):
    arr = factorization(i)
    for num, cnt in arr:
        di[num] += cnt

ans = 1
di[1] = 0
for val in di.values():
    ans *= val + 1
    ans %= mod
print(ans)
