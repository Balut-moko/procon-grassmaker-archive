from sys import stdin

readline = stdin.readline
h, w = map(int, readline().split())
s = [readline()[:-1] for _ in [0] * h]
ans = 1
mod = 998244353
for i in range(h):
    ii = i
    jj = 0
    color = '.'
    while 0 <= ii < h and 0 <= jj < w:
        if s[ii][jj] == 'R':
            if color == 'B':
                print(0)
                exit()
            color = 'R'
        elif s[ii][jj] == 'B':
            if color == 'R':
                print(0)
                exit()
            color = 'B'
        ii -= 1
        jj += 1
    if color == '.':
        ans *= 2
        ans %= mod

for j in range(1, w):
    ii = h - 1
    jj = j
    color = '.'
    while 0 <= ii < h and 0 <= jj < w:
        if s[ii][jj] == 'R':
            if color == 'B':
                print(0)
                exit()
            color = 'R'
        elif s[ii][jj] == 'B':
            if color == 'R':
                print(0)
                exit()
            color = 'B'
        ii -= 1
        jj += 1
    if color == '.':
        ans *= 2
        ans %= mod

print(ans)
