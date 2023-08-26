from sys import stdin

readline = stdin.readline
n, h, x = map(int, readline().split())
p = list(map(int, readline().split()))

for i in range(n):
    if x <= h + p[i]:
        print(i + 1)
        break
