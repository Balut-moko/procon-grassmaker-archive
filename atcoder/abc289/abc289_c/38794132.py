from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
c = []
s = []

for i in range(m):
    ci = int(readline())
    c.append(ci)
    ai = set(map(int, readline().split()))
    s.append(ai)
ans = 0
for i in range(1, 2 ** m):
    tmp = set()
    for j in range(m):
        if (i >> j) & 1:
            tmp = tmp.union(s[j])
    for k in range(1, n + 1):
        if k not in tmp:
            break
    else:
        ans += 1
print(ans)
