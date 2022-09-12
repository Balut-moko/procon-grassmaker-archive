from sys import stdin

readline = stdin.readline
n = int(readline())
p = list(map(int, readline().split()))

cnt = [0] * n

for i in range(n):
    for j in range(3):
        cnt[(p[i] - 1 - i + j + n) % n] += 1

print(max(cnt))
