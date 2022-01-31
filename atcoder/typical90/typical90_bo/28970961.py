from sys import stdin


def base2tenint(value, base):
    if int(value // base):
        return base2tenint(int(value // base), base) + str(value % base)
    return str(value % base)


def ten2baseint(value: str, n):
    return int(value, n)


readline = stdin.readline
n, k = map(int, readline().split())

for _ in range(k):
    n = ten2baseint(str(n), 8)
    n = base2tenint(n, 9)
    n = n.replace("8", "5")
print(n)
