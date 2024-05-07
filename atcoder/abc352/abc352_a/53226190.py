N, X, Y, Z = map(int, input().split())
flag = False
if X <Y:
    if X<Z<Y:
        flag = True
else:
    if Y<Z<X:
        flag = True
print("Yes" if flag else "No")