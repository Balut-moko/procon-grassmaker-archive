def has_bit(n, i):
    return n & (1 << i) > 0


a, b, C = map(int, input().split())
A, B = a, b
x = 0
y = 0
for i in range(60):
    if has_bit(C, i):
        if a > b:
            x += 1 << i
            a -= 1
        else:
            y += 1 << i
            b -= 1
for i in range(60):
    if not has_bit(C, i):
        if a > 0 and b > 0:
            x += 1 << i
            a -= 1
            y += 1 << i
            b -= 1

if x.bit_count() == A and y.bit_count() == B and x ^ y == C:
    print(x, y)
else:
    print(-1)
