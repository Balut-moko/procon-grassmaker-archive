from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())


def f(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return n ^ (n - 1)
    if n % 4 == 2:
        return n ^ (n - 1) ^ (n - 2)
    if n % 4 == 3:
        return 0


print(f(a - 1) ^ f(b))
