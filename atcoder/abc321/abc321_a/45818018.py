s = input()
tmp = 10
flag = True
for val in s:
    if tmp > int(val):
        tmp = int(val)
        continue
    flag = False

print("Yes" if flag else "No")
