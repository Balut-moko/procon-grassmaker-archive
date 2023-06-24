from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = [0] * n
for i in range(n):
    for j in range(7):
        ans[i] += a[i * 7 + j]

print(*ans)
