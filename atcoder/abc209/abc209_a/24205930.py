from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
print(b - a + 1 if 0 < b - a + 1 else 0)
