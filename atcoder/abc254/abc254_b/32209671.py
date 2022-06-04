from sys import stdin

readline = stdin.readline
n = int(readline())
a = [1]
print(*a)
for i in range(1, n):
    tmp = [1] * i
    for j in range(1, i):
        tmp[j] = a[j - 1] + a[j]
    tmp += [1]
    a = tmp
    print(*a)
