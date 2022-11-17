from sys import stdin


def f(level, x):
    if level == 0:
        return 1
    length = (1 << (level + 1)) - 3
    p = (1 << level) - 1

    if x == 1:
        return 0
    elif x <= length + 1:
        return f(level - 1, x - 1)
    elif x <= length + 2:
        return p + 1
    elif x <= (length + 1) * 2:
        return p + 1 + f(level - 1, x - length - 2)
    else:
        return p * 2 + 1


readline = stdin.readline
n, x = map(int, readline().split())

print(f(n, x))
