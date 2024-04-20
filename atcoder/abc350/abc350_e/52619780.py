from functools import cache


N, A, X, Y = map(int, input().split())


@cache
def f(N):
    if N == 0:
        return 0
    resX = X + f(N // A)
    resY = Y * 6 / 5 + sum(f(N // b) for b in range(2, 7)) / 5
    return min(resX, resY)


print(f(N))
