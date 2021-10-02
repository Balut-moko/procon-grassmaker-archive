from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())

print(32**(a - b))
