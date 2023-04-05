from collections import defaultdict
from sys import stdin


def has_bit(n, i):
    return n & (1 << i) > 0


readline = stdin.readline
N, x = map(int, readline().split())
w = [int(readline()) for _ in [0] * N]

n1 = N // 2
w1 = w[:n1]
w2 = w[n1:]

ALL = 1 << n1
dic = defaultdict(int)
for n in range(ALL):
    s = 0
    for i in range(n1):
        if has_bit(n, i):
            s += w[i]
    dic[s] += 1

ans = 0
for n in range(1 << len(w2)):
    s = 0
    for i in range(len(w2)):
        if has_bit(n, i):
            s += w2[i]
    ans += dic[x - s]

print(ans)
