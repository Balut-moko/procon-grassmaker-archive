from sys import stdin

readline = stdin.readline
n = int(readline())
a = [0] + list(map(int, readline().split()))
ans = [0] * (n + 1)
for i in range(n, 0, -1):
    tmp = 0
    for j in range(i, n + 1, i):
        tmp ^= ans[j]
    if tmp != a[i]:
        ans[i] = 1

ans = [i for i in range(1, n + 1) if ans[i] == 1]
print(len(ans))
print(*ans)
