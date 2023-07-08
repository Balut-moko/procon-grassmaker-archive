from sys import stdin

readline = stdin.readline
n = int(readline())
a = [readline()[:-1] for _ in [0] * n]

ans = [[None] * n for _ in [0] * n]

for i in range(1, n - 1):
    for j in range(1, n - 1):
        ans[i][j] = a[i][j]

for j in range(1, n):
    ans[0][j] = a[0][j - 1]

for i in range(1, n):
    ans[i][-1] = a[i - 1][-1]

for j in range(1, n):
    ans[-1][j - 1] = a[-1][j]

for i in range(1, n):
    ans[i - 1][0] = a[i][0]

for val in ans:
    print(*val, sep="")
