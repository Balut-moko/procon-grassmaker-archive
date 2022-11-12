from sys import stdin

readline = stdin.readline
n, x = map(int, readline().split())
p = list(map(int, readline().split()))

for i in range(n):
    if p[i] == x:
        print(i + 1)
