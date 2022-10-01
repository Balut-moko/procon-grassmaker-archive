from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
l = [tuple(map(int, readline().split())) for _ in [0] * n]
st = [tuple(map(int, readline().split())) for _ in [0] * q]

for s,t in st:
    print(l[s-1][t])