from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * n]

print(*sorted(s[:k]), sep="\n")
