from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
a = list(map(int, readline().split()))

vals = [[] for _ in [0] * (m + 1)]

for i, val in enumerate(a):
    if val >= n:
        continue
    if val >= 0:
        l = 1
    else:
        l = (-val + i) // (i + 1)
    r = min(m + 1, (n - val + i) // (i + 1))

    for j in range(l, r):
        vals[j].append(val + (i + 1) * j)

for i in range(1, m + 1):
    size = len(vals[i])
    num = [False] * (size + 1)
    for val in vals[i]:
        if val < size:
            num[val] = True
    res = 0
    while num[res]:
        res += 1
    print(res)
