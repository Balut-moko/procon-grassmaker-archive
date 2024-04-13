S = input()
T = input()

i = 0

for s in S:
    if i == 3:
        break
    if s.upper() == T[i]:
        i += 1
flag = False
if i == 3:
    flag = True
if i == 2 and T[2] == "X":
    flag = True

print("Yes" if flag else "No")
