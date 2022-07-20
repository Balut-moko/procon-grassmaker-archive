from sys import stdin

readline = stdin.readline
n, x, y, z = map(int, readline().split())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
c = [va + vb for va, vb in zip(a, b)]

a = [[-val, i] for i, val in enumerate(a)]
b = [[-val, i] for i, val in enumerate(b)]
c = [[-val, i] for i, val in enumerate(c)]

a.sort()
b.sort()
c.sort()

ans = [False] * n
i = 0
while x > 0:
    if not ans[a[i][1]]:
        ans[a[i][1]] = True
        x -= 1
    i += 1
i = 0
while y > 0:
    if not ans[b[i][1]]:
        ans[b[i][1]] = True
        y -= 1
    i += 1
i = 0
while z > 0:
    if not ans[c[i][1]]:
        ans[c[i][1]] = True
        z -= 1
    i += 1

for i in range(n):
    if ans[i]:
        print(i + 1)
