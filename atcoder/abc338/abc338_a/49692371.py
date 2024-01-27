S = input()

for i in range(len(S)):
    if i == 0 and S[i].isupper():
        continue
    if i != 0 and S[i].islower():
        continue
    print("No")
    exit()
print("Yes")
