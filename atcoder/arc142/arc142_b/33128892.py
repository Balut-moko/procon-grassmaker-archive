from sys import stdin

readline = stdin.readline
n = int(readline())
ans = []
for i in range(n):
    tmp = []
    half = (n + 1) // 2
    for j in range(1, half + 1):
        tmp.append(i * n + j)
        if i * n + j + half <= (i + 1) * n:
            tmp.append(i * n + j + half)
    ans.append(tmp)

for val in ans:
    print(*val)
