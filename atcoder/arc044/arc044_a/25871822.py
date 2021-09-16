from sys import stdin
import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


def digit_sum(n):
    return sum(map(int, str(n)))


readline = stdin.readline
n = int(readline())
ans = 'Not Prime'
if n == 1:
    pass
elif is_prime(n):
    ans = 'Prime'
elif n % 2 != 0 and n % 5 != 0 and digit_sum(n) % 3 != 0:
    ans = 'Prime'

print(ans)
