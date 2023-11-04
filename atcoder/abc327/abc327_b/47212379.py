B = int(input())

A = 1

while pow(A, A) <= B:
    if pow(A, A) == B:
        print(A)
        exit()
    A += 1

print(-1)
