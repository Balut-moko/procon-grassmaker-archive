from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = sorted(map(int, readline().split()))
b = sorted(map(int, readline().split()))
i = 0
j = 0
ans = 10 ** 9
while i < n and j < m:
    ans = min(ans, abs(a[i] - b[j]))
    if a[i] <= b[j]:
        i += 1
    else:
        j += 1

print(ans)
