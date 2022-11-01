from sys import stdin

readline = stdin.readline
n = int(readline())
h = list(map(int, readline().split()))
max_h = max(h)
print(h.index(max_h) + 1)
