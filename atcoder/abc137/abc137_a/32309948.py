from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
print(max(a + b, a - b, a * b))
