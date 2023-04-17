from sys import stdin

readline = stdin.readline
n, m, q = map(int, readline().split())

p = [[] for _ in range(n)]
score = [n] * m

for _ in range(q):
    t, *nm = map(int, readline().split())
    if t == 1:
        ans = 0
        for val in p[nm[0] - 1]:
            ans += score[val]
        print(ans)
    if t == 2:
        ni, mi = nm
        p[ni - 1].append(mi - 1)
        score[mi - 1] -= 1
