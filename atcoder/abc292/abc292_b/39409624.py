from sys import stdin

readline = stdin.readline
n, q = map(int, readline().split())

member = [0] * n

for _ in range(q):
    a, x = map(int, readline().split())
    x -= 1
    if a == 1:
        member[x] += 1
    if a == 2:
        member[x] = 2
    if a == 3:
        print("Yes" if member[x] >= 2 else "No")
