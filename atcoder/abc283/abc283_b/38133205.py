from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
q = int(readline())
query = [tuple(map(int, readline().split())) for _ in [0] * q]

for que in query:
    num, *kx = que
    if num == 1:
        a[kx[0] - 1] = kx[1]
    else:
        print(a[kx[0] - 1])
