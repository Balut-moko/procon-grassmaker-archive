from sys import stdin

readline = stdin.readline
n = int(readline())

ans = 3.5
for i in range(1, n):
    tmp = 0
    for j in range(1, 7):
        tmp += max(ans, j) / 6
    ans = tmp
print(ans)
