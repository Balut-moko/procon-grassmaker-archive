from sys import stdin

readline = stdin.readline
n, k, q = map(int, readline().split())
a = list(map(int, readline().split())) + [n + 1]
l = list(map(int, readline().split()))

for val in l:
    if a[val - 1] + 1 != a[val]:
        a[val - 1] += 1
print(*a[:-1])
