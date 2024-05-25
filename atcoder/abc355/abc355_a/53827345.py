A, B = map(int, input().split())

if A == B:
    ans = -1
else:
    ans = {1, 2, 3}
    ans.discard(A)
    ans.discard(B)
    ans = ans.pop()
print(ans)
