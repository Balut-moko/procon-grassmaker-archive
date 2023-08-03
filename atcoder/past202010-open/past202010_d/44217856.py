from itertools import product
from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]
cnt = 100
ans = (0, 0)
for x, y in product(range(n), range(n)):
    li = list(s)
    for i in range(x):
        for j in range(1, n):
            if li[j] == "#":
                li[j - 1] = "#"
    for i in range(y):
        for j in range(n - 2, -1, -1):
            if li[j] == "#":
                li[j + 1] = "#"
    for val in li:
        if val != "#":
            break
    else:
        if x + y < cnt:
            ans = (x, y)
            cnt = x + y

print(*ans)
