from sys import stdin

readline = stdin.readline
n, k = map(int, readline().split())
a = list(map(int, readline().split()))
a_i = []
for i in range(n):
    a_i.append([i, a[i], k // n])
k %= n
a_i.sort(key=lambda x: x[1])
for i in range(k):
    a_i[i][2] += 1
a_i.sort()
for i in range(n):
    print(a_i[i][2])
