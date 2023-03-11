from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

ans = [False] * n
for i in range(n):
    if not ans[i]:
        ans[a[i] - 1] = True

print(n-sum(ans))
nums = [i + 1 for i in range(n) if not ans[i]]
print(*nums)
