from sys import stdin
from collections import Counter
readline = stdin.readline
n = int(readline())
c = [list(map(int, readline().split())) for _ in [0] * n]
min_c = 10**9
min_i = 0
min_j = 0
for i in range(n):
    for j in range(n):
        if c[i][j] <= min_c:
            min_c = c[i][j]
            min_i = i
            min_j = j
a = [None] * n
b = [None] * n
for i in range(n):
    a[i] = c[i][min_j] - c[min_i][min_j]
for j in range(n):
    b[j] = c[min_i][j] - a[min_i]
for i in range(n):
    for j in range(n):
        if c[i][j] != a[i] + b[j]:
            print('No')
            exit()
print('Yes')
print(*a)
print(*b)
