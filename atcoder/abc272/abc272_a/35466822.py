from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
print(sum(a))
