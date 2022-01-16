from sys import stdin

readline = stdin.readline
t = int(readline())


def f(t):
    return t * t + 2 * t + 3


print(f(f(f(t) + t) + f(f(t))))
