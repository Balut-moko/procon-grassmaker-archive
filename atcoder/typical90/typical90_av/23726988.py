from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
ab = []
for _ in [0] * n:
    a, b = map(int, readline().split())
    ab.append(b)
    ab.append(a - b)
ab.sort(reverse=True)

print(sum(ab[:k]))
