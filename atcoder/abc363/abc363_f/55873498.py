from functools import cache


@cache
def rec(n: int):
    if "0" not in str(n) and str(n) == str(n)[::-1]:
        return str(n)

    for x in range(2, int(n**0.5) + 2):
        if n % x == 0 and "0" not in str(x):
            rx = int(str(x)[::-1])
            if n // x % rx == 0 and len(rec(n // x // rx)) != 0:
                return str(x) + "*" + rec(n // x // rx) + "*" + str(rx)
    return ""


N = int(input())
print(-1 if len(rec(N)) == 0 else rec(N))
