from sys import stdin

readline = stdin.readline
n = int(readline())
a = [tuple(readline()[:-1]) for _ in [0] * n]

dd = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))
ans = 0
for i in range(n):
    for j in range(n):
        for dx, dy in dd:
            ii = i
            jj = j
            tmp = a[ii][jj]
            for k in range(n - 1):
                ii += dx
                ii %= n
                jj += dy
                jj %= n
                tmp += a[ii][jj]
            ans = max(ans, int(tmp))
print(ans)
