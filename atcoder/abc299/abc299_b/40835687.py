from sys import stdin

readline = stdin.readline
n, t = map(int, readline().split())
c = list(map(int, readline().split()))
r = list(map(int, readline().split()))

max_t = 0
max_f = r[0]
win = 0
win_f = 1
for i in range(n):
    if c[i] == t:
        if max_t < r[i]:
            max_t = r[i]
            win = i + 1
    elif c[i] == c[0]:
        if max_f < r[i]:
            max_f = r[i]
            win_f = i + 1

if win != 0:
    print(win)
else:
    print(win_f)
