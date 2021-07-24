from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())

print((a - b) / 3 + b)
