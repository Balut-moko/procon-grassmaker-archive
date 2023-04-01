from sys import stdin

readline = stdin.readline
n = int(readline())
s = readline()[:-1]

flag = True

for i in range(n):
    if i%2 == 0 and s[i] == "M":
        continue
    elif i%2 == 1 and s[i] == "F":
        continue
    else:
        flag = False

if flag:
    print("Yes" if flag else "No")
    exit()

flag = True

for i in range(n):
    if i%2 == 0 and s[i] == "F":
        continue
    elif i%2 == 1 and s[i] == "M":
        continue
    else:
        flag = False

print("Yes" if flag else "No")
