from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = [0] * n
for i in range(n - 1):
    if a[i] > a[i + 1]:
        ans[i] ^= 1
        ans[i + 1] ^= 1
print(*ans)
