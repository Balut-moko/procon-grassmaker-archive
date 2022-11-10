from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))

num = [0] * (m + 1)
for i in range(m):
    if a[i] <= m:
        num[a[i]] += 1
ans = 0
while num[ans]:
    ans += 1

for i in range(1, n - m + 1):
    if a[i + m - 1] <= m:
        num[a[i + m - 1]] += 1
        if num[a[i + m - 1]] == 1:
            tmp = a[i + m - 1]
            while num[tmp]:
                tmp += 1
                if ans <= tmp:
                    break
            ans = min(ans, tmp)
    if a[i - 1] <= m:
        num[a[i - 1]] -= 1
        if num[a[i - 1]] == 0:
            ans = min(ans, a[i - 1])

print(ans)
