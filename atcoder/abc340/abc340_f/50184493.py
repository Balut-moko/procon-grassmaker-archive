def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0


X, Y = map(int, input().split())
d, a, b = extgcd(Y, -X)
if abs(d) > 2:
    print(-1)
    exit()

A, B = a * 2 // d, b * 2 // d

print(A, B)
