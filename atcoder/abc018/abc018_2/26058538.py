from sys import stdin


def int1(x):
    return int(x) - 1


readline = stdin.readline
s = readline()[:-1]
n = int(readline())
lr = [tuple(map(int1, readline().split())) for _ in [0] * n]

for l, r in lr:
    s = s[:l] + s[l:r + 1][::-1] + s[r + 1:]
print(s)
