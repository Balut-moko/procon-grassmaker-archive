N = int(input())
x, y = 0, 0
flag = False
while pow(2, x) <= N:
    while pow(3, y) <= N:
        if pow(2, x) * pow(3, y) == N:
            flag = True
        y += 1
    y = 0
    x += 1
print("Yes" if flag else "No")
