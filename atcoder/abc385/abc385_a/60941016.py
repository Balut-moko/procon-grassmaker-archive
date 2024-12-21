A, B, C = map(int, input().split())
flag = False
if A + B == C:
    flag = True
if A + C == B:
    flag = True
if B + C == A:
    flag = True
if A == B == C:
    flag = True

print("Yes" if flag else "No")