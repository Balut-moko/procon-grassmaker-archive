from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = 0
li = [0] * (10**5 + 1)
for i in range(n):
    li[a[i]] += 1
for i in range(10**5 - 1):
    ans = max(ans, li[i] + li[i + 1] + li[i + 2])
print(ans)
