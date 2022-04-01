from sys import stdin
import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n ** 0.5) // 1)) + 1):
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
a, b = map(int, readline().split())
ab = math.gcd(a, b)
ans = 1
if ab != 1:
    arr = factorization(ab)
    ans = len(arr) + 1
print(ans)
