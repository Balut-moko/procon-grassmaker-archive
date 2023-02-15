from sys import stdin

readline = stdin.readline
n = int(readline())
a = [sum(map(int, readline().split())) for _ in [0] * n]

print(*a, sep="\n")
