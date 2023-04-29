from sys import stdin

readline = stdin.readline
n, a, b = map(int, readline().split())
c = list(map(int, readline().split()))

for i in range(n):
    if a + b == c[i]:
        print(i + 1)
        break
