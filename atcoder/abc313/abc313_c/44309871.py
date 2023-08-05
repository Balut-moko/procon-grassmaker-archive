from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))

s = sum(a)
a.sort()
b = [s // n for _ in range(n)]
for i in range(0, s % n):
    b[n - 1 - i] += 1
ans = 0
for i in range(0, n):
    ans += abs(a[i] - b[i])

print(ans // 2)
