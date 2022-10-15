from sys import stdin


def f(x):
    if x == 0:
        return 1
    return x * f(x - 1)


readline = stdin.readline
n = int(readline())
print(f(n))
