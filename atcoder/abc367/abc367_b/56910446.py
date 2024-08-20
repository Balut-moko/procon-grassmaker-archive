X = list(input())

for x in X[::-1]:
    if x == "0":
        X.pop()
    else:
        break

if X[-1] == ".":
    X.pop()

print(*X, sep="")
