X, Y = map(int, input().split())
flag = False
if -2 <= X - Y <= 3:
    flag = True

print("Yes" if flag else "No")
