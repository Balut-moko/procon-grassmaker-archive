from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
a = list(map(int, readline().split()))

print(sum([val for i, val in enumerate(a) if (x >> i) & 1 == 1]))
