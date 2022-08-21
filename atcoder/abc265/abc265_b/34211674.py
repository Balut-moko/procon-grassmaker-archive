from sys import stdin

readline = stdin.readline
n, m, t = map(int, readline().split())
a = list(map(int, readline().split()))
xy = [tuple(map(int, readline().split())) for _ in [0] * m]
xy_di = {key: val for key, val in xy}

for i in range(1, n):
    t -= a[i - 1]
    if t <= 0:
        break
    t += xy_di.get(i + 1, 0)

if t > 0:
    ans = "Yes"
else:
    ans = "No"
print(ans)
