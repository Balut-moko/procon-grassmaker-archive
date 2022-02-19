from sys import stdin
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


readline = stdin.readline
a, b, c, d = map(int, readline().split())
b += 1
d += 1
ans = "Aoki"
for i in range(a, b):
    for j in range(c, d):
        if is_prime(i + j):
            break
    else:
        ans = "Takahashi"

print(ans)
