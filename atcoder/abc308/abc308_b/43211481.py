from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
c = list(readline().split())
d = list(readline().split())
p = list(map(int, readline().split()))

di = dict()
for i in range(m):
    di[d[i]] = p[i + 1]
ans = 0
for val in c:
    ans += di.get(val, p[0])

print(ans)