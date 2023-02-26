from sys import stdin

readline = stdin.readline
n = int(readline())
x = list(map(int, readline().split()))

x.sort()

print(sum(x[n:-n]) / (3 * n))
