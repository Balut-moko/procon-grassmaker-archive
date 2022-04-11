from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))
bc = [tuple(map(int, readline().split())) for _ in [0] * m]
a.sort(reverse=True)
bc.sort(reverse=True, key=lambda x: x[1])
now = 0
cnt = n
ans = 0
for b, c in bc:
    while now < n and c < a[now]:
        ans += a[now]
        now += 1
        cnt -= 1
    if b < cnt:
        ans += b * c
        cnt -= b
    else:
        ans += cnt * c
        cnt = 0
        break

for i in range(cnt):
    ans += a[now + i]
print(ans)
