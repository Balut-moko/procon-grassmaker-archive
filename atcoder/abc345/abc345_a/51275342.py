S = input()
flag = False
if S[0] == "<" and S[-1] == ">" and S.count("=") == len(S) - 2:
    flag = True

print("Yes" if flag else "No")
