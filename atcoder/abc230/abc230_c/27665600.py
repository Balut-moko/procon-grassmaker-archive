from sys import stdin

readline = stdin.readline
n, a, b = map(int, readline().split())
p, q, r, s = map(int, readline().split())
ans = [['.'] * (s - r + 1) for _ in range(q - p + 1)]
for i in range(q - p + 1):
    for j in range(s - r + 1):
        ii = i + p
        jj = j + r
        if ii - a == jj - b:
            if max(1 - a, 1 - b) <= ii - a <= min(n - a, n - b):
                ans[i][j] = '#'
        if ii - a == b - jj:
            if max(1 - a, b - n) <= ii - a <= min(n - a, b - 1):
                ans[i][j] = '#'

for val in ans:
    print(*val, sep='')
