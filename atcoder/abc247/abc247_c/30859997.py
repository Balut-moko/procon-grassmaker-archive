from sys import stdin


def f(n):
    if n == 1:
        return [str(1)]
    return f(n - 1) + [str(n)] + f(n - 1)


readline = stdin.readline
n = int(readline())
ans = f(n)
print(*ans)
