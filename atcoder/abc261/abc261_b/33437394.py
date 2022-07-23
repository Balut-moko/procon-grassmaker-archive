from sys import stdin

readline = stdin.readline
n = int(readline())
a = [tuple(readline()[:-1]) for _ in [0] * n]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == "W" and a[j][i] == "L":
            continue
        if a[i][j] == "L" and a[j][i] == "W":
            continue
        if a[i][j] == "D" and a[j][i] == "D":
            continue
        print("incorrect")
        exit()
print("correct")
