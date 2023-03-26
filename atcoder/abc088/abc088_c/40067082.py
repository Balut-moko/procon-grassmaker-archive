from sys import stdin

readline = stdin.readline
c = [tuple(map(int, readline().split())) for _ in [0] * 3]


for a1 in range(-100, 101):
    flag = True
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    a2 = c[1][0] - b1
    a3 = c[2][0] - b1

    if c[1][1] != a2 + b2:
        flag = False
    if c[1][2] != a2 + b3:
        flag = False
    if c[2][0] != a3 + b1:
        flag = False
    if c[2][1] != a3 + b2:
        flag = False
    if c[2][2] != a3 + b3:
        flag = False
    if flag:
        break

print("Yes" if flag else "No")
