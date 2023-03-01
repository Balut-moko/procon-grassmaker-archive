from sys import stdin

readline = stdin.readline
n = int(readline())
ab = [tuple(map(int, readline().split())) for _ in [0] * n]

li = sorted([(a + b, a, b) for a, b in ab], reverse=True)

takahashi = 0
aoki = 0
flag = True
for s, a, b in li:
    if flag:
        takahashi += a
        flag = not flag
    else:
        aoki += b
        flag = not flag
print(takahashi - aoki)
