from sys import stdin

readline = stdin.readline
a, b, c = map(int, readline().split())
a %= 10
b = b % 4 + 4
bc = pow(b, c, 4) + 4
print(pow(a, bc, 10))
