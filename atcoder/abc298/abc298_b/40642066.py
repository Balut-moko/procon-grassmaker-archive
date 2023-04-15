from itertools import product
from sys import stdin

readline = stdin.readline
n = int(readline())
a = [tuple(map(int, readline().split())) for _ in [0] * n]
b = [tuple(map(int, readline().split())) for _ in [0] * n]

for k in range(4):
    flag = True
    tmp = [[None] * n for _ in [0] * n]
    for i, j in product(range(n), range(n)):
        tmp[i][j] = a[n - 1 - j][i]
    for i, j in product(range(n), range(n)):
        if tmp[i][j] == 1:
            if tmp[i][j] != b[i][j]:
                flag = False
                break
    if flag:
        print("Yes")
        exit()
    a = tmp
print("No")
