from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())


def f(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return 1 ^ n
    if n % 4 == 3:
        return 0


print(f(a - 1) ^ f(b))
