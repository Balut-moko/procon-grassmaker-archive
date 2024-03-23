W, B = map(int, input().split())

S = "wbwbwwbwbwbw" * 200
flag = False
for i in range(len(S)):
    for j in range(len(S)):
        if S[i:j].count("w") == W and S[i:j].count("b") == B:
            flag = True
print("Yes" if flag else "No")
