from sys import stdin

readline = stdin.readline
n, d = map(int, readline().split())
t = list(map(int, readline().split()))

pre = t[0]

for i in range(1,n):
    if t[i] - pre <=d:
        print(t[i])
        exit()
    pre = t[i]
print(-1)