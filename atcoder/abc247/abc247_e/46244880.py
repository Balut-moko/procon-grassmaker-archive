N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

posX, posY = -1, -1
B = -1
ans = 0
for i in range(N):
    if A[i] == X:
        posX = i
    if A[i] == Y:
        posY = i
    if A[i] < Y or X < A[i]:
        B = i
    ans += max(0, min(posX, posY) - B)

print(ans)
