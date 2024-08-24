N = int(input())
A = list(map(int, input().split()))
cnt = sum(True if a > 0 else False for a in A)
ans = 0
while cnt > 1:
    ans += 1
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    if A[0] <= 0:
        cnt -= 1
    if A[1] <= 0:
        cnt -= 1

print(ans)
