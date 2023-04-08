from sys import stdin

readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]


sab = [(a + b, a, b) for a, b in ab]
sab.sort(reverse=True)

takahashi = 0
aoki = 0

for i in range(n):
    _, a, b = sab[i]
    if i % 2 == 0:
        takahashi += a
    else:
        aoki += b

print(takahashi - aoki)
