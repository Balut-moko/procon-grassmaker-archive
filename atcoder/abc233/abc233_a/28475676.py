from sys import stdin

readline = stdin.readline
x, y = map(int, readline().split())

print(max(0, (y - x - 1) // 10 + 1))
