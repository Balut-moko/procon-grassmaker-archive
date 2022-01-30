from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * h]
ans = list(zip(*a))
for val in ans:
    print(*val)
