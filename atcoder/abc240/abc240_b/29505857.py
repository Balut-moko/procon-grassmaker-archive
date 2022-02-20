from sys import stdin

readline = stdin.readline
n = int(readline())
a = set(map(int, readline().split()))
print(len(a))
