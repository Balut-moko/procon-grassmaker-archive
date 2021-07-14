from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = set(map(int, readline().split()))
b = set(map(int, readline().split()))
sd = sorted(a ^ b)
print(*sd)
