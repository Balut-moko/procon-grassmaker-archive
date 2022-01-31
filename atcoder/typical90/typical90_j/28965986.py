from sys import stdin

readline = stdin.readline
n = int(readline())
cp = [tuple(map(int, readline().split())) for _ in [0] * n]
q = int(readline())
lr = [tuple(map(int, readline().split())) for _ in [0] * q]

cs = [[0] * 2 for i in range(n + 1)]
for i in range(1, n + 1):
    c, p = cp[i - 1]
    if c == 1:
        cs[i][0] += cs[i - 1][0] + p
        cs[i][1] += cs[i - 1][1]
    else:
        cs[i][0] += cs[i - 1][0]
        cs[i][1] += cs[i - 1][1] + p

for i in range(q):
    l, r = lr[i]
    l -= 1
    print(cs[r][0] - cs[l][0], cs[r][1] - cs[l][1])
