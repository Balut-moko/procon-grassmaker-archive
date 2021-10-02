from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
print(k * (k - 1)**(n - 1))
