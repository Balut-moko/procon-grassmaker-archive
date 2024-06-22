Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

if Sx > Tx:
    Sx, Tx = Tx, Sx
    Sy, Ty = Ty, Sy


if Sy % 2 == 0:
    if Sx % 2 == 1:
        Sx -= 1
else:
    if Sx % 2 == 0:
        Sx -= 1
if Ty % 2 == 0:
    if Tx % 2 == 0:
        Tx += 1
else:
    if Tx % 2 == 1:
        Tx += 1

dx = abs(Sx - Tx)
dy = abs(Sy - Ty)
ans = 0
if dx <= dy:
    ans += dx
    dy -= dx
    ans += dy
else:
    ans += dy
    dx -= dy
    ans += dx // 2
print(ans)
