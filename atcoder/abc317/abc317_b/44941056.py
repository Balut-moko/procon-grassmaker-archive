from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
a.sort()

for i in range(1, n):
    if a[i - 1] + 1 != a[i]:
        print(a[i - 1] + 1)
        break
