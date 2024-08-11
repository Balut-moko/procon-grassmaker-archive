N, T, A = map(int, input().split())
flag = False
if N // 2 < T or N // 2 < A:
    flag = True
print("Yes" if flag else "No")
