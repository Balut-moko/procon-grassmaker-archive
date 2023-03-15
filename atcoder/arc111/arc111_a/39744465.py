from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
print(pow(10, n, m * m) // m % m)
