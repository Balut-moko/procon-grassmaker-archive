from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())
s = readline()[:-1]
start = 0
for _ in range(q):
    t, x = map(int, readline().split())
    if t == 1:
        start = (start - x) % n
    else:
        print(s[(start + x - 1) % n])
