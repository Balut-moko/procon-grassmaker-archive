from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

print(sum([a[i + 1] - a[i] for i in range(n - 1)]) / (n - 1))
