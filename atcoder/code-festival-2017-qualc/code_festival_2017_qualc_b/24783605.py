from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
ans = 3**n
tmp = 1
for i in range(n):
    if a[i] % 2 == 0:
        tmp *= 2
print(ans - tmp)
