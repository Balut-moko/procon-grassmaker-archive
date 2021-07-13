from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
a = list(map(int, readline().split()))
for i in range(1, n, 2):
    a[i] -= 1

print('Yes' if sum(a) <= x else 'No')
