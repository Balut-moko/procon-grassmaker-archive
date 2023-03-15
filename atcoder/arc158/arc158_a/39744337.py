from sys import stdin


def calc():
    x = list(map(int, readline().split()))
    x.sort()
    if sum(x) % 3 != 0:
        return -1
    a = sum(x) // 3
    if a % 2 != x[0] % 2 or a % 2 != x[1] % 2 or a % 2 != x[2] % 2:
        return -1
    d = abs(x[0] - a) + abs(x[1] - a) + abs(x[2] - a)
    return d // 4


readline = stdin.readline
t = int(readline())
for _ in range(t):
    print(calc())
