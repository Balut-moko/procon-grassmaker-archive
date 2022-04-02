from sys import stdin

readline = stdin.readline
a, b = map(int, readline().split())
x = a / (a ** 2 + b ** 2) ** 0.5
y = b / (a ** 2 + b ** 2) ** 0.5
print(x, y)
