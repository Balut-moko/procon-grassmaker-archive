A, B, C, K = map(int, input().split())

if A == B and B == C:
    print(0)
    exit()

ans = A - B

if K % 2 == 1:
    ans *= -1
print(ans)
