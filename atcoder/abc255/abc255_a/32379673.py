from sys import stdin

readline = stdin.readline
r, c = map(lambda x: int(x) - 1, readline().split())
a = [tuple(map(int, readline().split())) for _ in [0] * 2]

print(a[r][c])
