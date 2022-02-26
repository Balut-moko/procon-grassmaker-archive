from sys import stdin

readline = stdin.readline
n = int(readline())
a = [tuple(readline()[:-1]) for _ in [0] * n]
a_inv = list(zip(*a))

for i in range(n):
    for j in range(n - 5):
        if a[i][j : j + 6].count("#") >= 4:
            print("Yes")
            exit()

for i in range(n):
    for j in range(n - 5):
        if a_inv[i][j : j + 6].count("#") >= 4:
            print("Yes")
            exit()

for i in range(n - 5):
    for j in range(n - 5):
        cnt = 0
        for k in range(6):
            if a[i + k][j + k] == "#":
                cnt += 1
        if cnt >= 4:
            print("Yes")
            exit()

for i in range(n - 5):
    for j in range(5, n):
        cnt = 0
        for k in range(6):
            if a[i + k][j - k] == "#":
                cnt += 1
        if cnt >= 4:
            print("Yes")
            exit()

print("No")
