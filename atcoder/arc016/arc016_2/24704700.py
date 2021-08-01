from sys import stdin

readline = stdin.readline
n = int(readline())
x = [readline()[:-1] for _ in range(n)]
ans = x[0].count('x') + x[0].count('o')

for i in range(1, n):
    for j in range(9):
        if x[i][j] == 'x':
            ans += 1
        if x[i][j] == 'o' and x[i - 1][j] != 'o':
            ans += 1
print(ans)
