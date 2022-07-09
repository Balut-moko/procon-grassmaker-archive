from sys import stdin

readline = stdin.readline
n, m, x, t, d = map(int, readline().split())

if x <= m <= n:
    print(t)
    exit()
for i in range(x, -1, -1):
    if m == i:
        print(t)
        exit()
    t -= d
