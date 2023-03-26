from sys import stdin

readline = stdin.readline
a = [tuple(map(int, readline().split())) for _ in [0] * 3]
n = int(readline())
s = [int(readline()) for _ in [0] * n]

check = [[False] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if a[i][j] in s:
            check[i][j] = True

flag = False
for i in range(3):
    if check[i][0] and check[i][1] and check[i][2]:
        flag = True
    if check[0][i] and check[1][i] and check[2][i]:
        flag = True

if check[0][0] and check[1][1] and check[2][2]:
    flag = True
if check[0][2] and check[1][1] and check[2][0]:
    flag = True

print("Yes" if flag else "No")
