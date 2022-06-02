from sys import stdin

readline = stdin.readline
n = int(readline())
csf = [tuple(map(int, readline().split())) for _ in [0] * n]

for i in range(n):
    now = 0
    for j in range(i, n - 1):
        c, s, f = csf[j]
        if now <= s:
            now = s + c
        else:
            if (now - s) % f == 0:
                now = now + c
            else:
                now = now + f - (now - s) % f + c
    print(now)
