from sys import stdin

readline = stdin.readline
n = int(readline())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))
cnt = 0

for i in range(n):
    if a[i] == b[i]:
        cnt += 1
print(cnt)
print(len(set(a) & set(b)) - cnt)
