A, B, D = map(int, input().split())
ans = []
while True:
    ans.append(A)
    if A == B:
        break
    A += D

print(*ans)
