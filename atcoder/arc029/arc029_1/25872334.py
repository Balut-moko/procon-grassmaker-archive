from sys import stdin

readline = stdin.readline
n = int(readline())
t = [int(readline()) for _ in [0] * n]
ans = 200
for i in range(2 ** n):
    a = 0
    b = 0
    for j in range(n):
        if ((i >> j) & 1):
            a += t[j]
        else:
            b += t[j]
    ans = min(ans, (max(a, b)))

print(ans)
