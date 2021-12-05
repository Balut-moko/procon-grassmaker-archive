from sys import stdin

readline = stdin.readline
n, m, p = map(int, readline().split())
print(pow(n, p, m))