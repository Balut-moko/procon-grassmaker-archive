from sys import stdin

readline = stdin.readline
n = int(readline())
A = sorted(map(int, readline().split()))
B = sorted(map(int, readline().split()))
C = sorted(map(int, readline().split()))
inf = 1 << 60
B_li = [inf] * n
i = 0
for b in B:
    if A[i] < b:
        B_li[i] = b
        i += 1
j = 0
for c in C:
    if B_li[j] < c:
        j += 1

print(j)
