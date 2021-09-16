from sys import stdin


def calc_dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**.5


readline = stdin.readline
txty = list(map(int, readline().split()))
n = int(readline())
a = [tuple(map(int, readline().split())) for _ in [0] * n]

s = (txty[0], txty[1])
g = (txty[2], txty[3])
t = txty[4]
v = txty[5]
ans = 'NO'
for i in range(n):
    if calc_dist(s, a[i]) + calc_dist(a[i], g) <= (t * v):
        ans = 'YES'
print(ans)
