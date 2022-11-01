from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

cnt = 0
for va, vb in zip(a, b):
    if va > vb:
        cnt -= va - vb
    if va < vb:
        cnt += (vb - va) // 2
print("Yes" if cnt >= 0 else "No")
