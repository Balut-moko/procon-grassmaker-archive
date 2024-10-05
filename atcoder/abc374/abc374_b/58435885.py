S = input() + "S"
T = input() + "T"

if S[:-1] == T[:-1]:
    print(0)
    exit()

for i in range(min(len(S), len(T))):
    if S[i] != T[i]:
        print(i + 1)
        exit()
