from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
tmp = 0
for i in range(1, n + 1):
    if i % k == 0:
        tmp += 1
ans = tmp**3

if k % 2 == 0:
    tmp = 0
    for i in range(1, n + 1):
        if i % k == k // 2:
            tmp += 1
    ans += tmp**3

print(ans)
