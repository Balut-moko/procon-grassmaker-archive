S, T = input().split()
flag = False
for w in range(1, len(S)):
    lst = [S[i : i + w] for i in range(0, len(S), w)]
    for c in range(len(S)):
        tmp = ""
        for val in lst:
            if c < len(val):
                tmp += val[c]
        if tmp == T:
            flag = True

print("Yes" if flag else "No")
