from sys import stdin


def func(x):
    str_x = str(x)
    res = 0
    for s in str_x:
        res += int(s)
    res += x
    res %= 10**5
    return res


readline = stdin.readline
n, k = map(int, readline().split())
num = [None] * 100000
num[0] = n
tmp = 0
for i in range(k):
    n = func(n)
    if n == 0:
        exit(print(0))
    if n not in num:
        num[i] = n
    else:
        tmp = k % (i - num.index(n))
        tmp -= num.index(n) + 1
        while tmp < 0:
            tmp += i - num.index(n)
        break
for i in range(tmp):
    n = func(n)
print(n)
