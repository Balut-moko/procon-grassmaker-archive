from sys import stdin

readline = stdin.readline
n, m = map(int, readline().split())
b = [tuple(map(int, readline().split())) for _ in [0] * n]
tmp = b[0][0] % 7
if b[0][0] % 7 == 0:
    tmp += 7
if tmp + m - 1 >= 8:
    print('No')
    exit()

for i in range(n):
    for j in range(m):
        if b[i][j] != b[0][0] + i * 7 + j:
            print('No')
            exit()
print('Yes')
