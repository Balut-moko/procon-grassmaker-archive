S = input()
flag = True
for i in range(1, len(S), 2):
    if S[i] != "0":
        flag = False

print("Yes" if flag else "No")
