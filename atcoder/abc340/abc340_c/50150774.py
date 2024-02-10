from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10**7)
N = int(input())


@lru_cache(maxsize=None)
def calc(x):
    if x == 1:
        return 0
    res = x // 2
    res += (x + 1) // 2
    res += calc(x // 2) + calc((x + 1) // 2)
    return res


print(calc(N))
