from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
a.sort()
b.sort()
ans = 0
for i in range(n):
    ans += abs(a[i]- b[i])
print(ans)
