S = list(input())
T = list(input())

X = []

for i in range(len(S)):
    if ord(S[i]) > ord(T[i]):
        S[i] = T[i]
        X.append("".join(S))

for i in range(len(S) - 1, -1, -1):
    if S[i] != T[i]:
        S[i] = T[i]
        X.append("".join(S))

print(len(X))
if X:
    print(*X, sep="\n")
