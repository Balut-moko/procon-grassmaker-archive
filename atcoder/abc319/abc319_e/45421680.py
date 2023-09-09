from sys import stdin

readline = stdin.readline
n, x, y = map(int, readline().split())
pt = [tuple(map(int, readline().split())) for _ in [0] * (n - 1)]
dist = []

for i in range(840):
    time = i
    for j in range(n - 1):
        p, t = pt[j]
        if time % p == 0:
            time += t
        else:
            time += t + p - time % p
    dist.append(time - i)

Q = int(readline())
for _ in range(Q):
    q = int(readline())
    ans = q + x
    ans += dist[ans % 840]
    ans += y
    print(ans)
