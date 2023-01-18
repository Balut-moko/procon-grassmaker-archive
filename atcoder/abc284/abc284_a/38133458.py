from sys import stdin

readline = stdin.readline
n = int(readline())
s = [readline()[:-1] for _ in [0] * n]

print(*s[::-1], sep="\n")
