from sys import stdin

readline = stdin.readline
x, k = map(int, readline().split())

for i in range(k):
    x = int(round(x + 0.5, -i - 1))
print(x)
