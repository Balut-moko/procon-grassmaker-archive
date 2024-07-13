xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

ab2 = (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)
bc2 = (xb - xc) * (xb - xc) + (yb - yc) * (yb - yc)
ca2 = (xa - xc) * (xa - xc) + (ya - yc) * (ya - yc)

flag = False
if max(ab2, bc2, ca2) == ab2 + bc2 + ca2 - max(ab2, bc2, ca2):
    flag = True

print("Yes" if flag else "No")
