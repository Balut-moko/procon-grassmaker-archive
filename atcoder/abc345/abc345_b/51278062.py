def round_up0(p, q):
    if q < 0:
        p = -p
        q = -q
    return (p + q - 1) // q


X = int(input())

print(round_up0(X, 10))
