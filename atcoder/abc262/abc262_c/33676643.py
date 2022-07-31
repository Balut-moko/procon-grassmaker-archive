from sys import stdin


readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = 0
tmp = 0
for i in range(n):
    if a[i] == i + 1:
        tmp += 1
ans += tmp * (tmp - 1) // 2
for i in range(n):
    j = a[i] - 1
    if i == j:
        continue
    if min(a[i], a[j]) == i + 1 and max(a[i], a[j]) == j + 1:
        ans += 1

print(ans)
