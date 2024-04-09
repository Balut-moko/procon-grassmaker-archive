N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
ans_li = []
x = A[0]
for i in range(1, N - 1):
    if A[i] < 0:
        ans_li.append((A[-1], A[i]))
        A[-1] -= A[i]
    else:
        ans_li.append((x, A[i]))
        x -= A[i]

ans_li.append((A[-1], x))
print(A[-1] - x)
for val in ans_li:
    print(*val)
