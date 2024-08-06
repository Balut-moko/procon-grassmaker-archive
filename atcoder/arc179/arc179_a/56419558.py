from itertools import accumulate


N, K = map(int, input().split())
A = list(map(int, input().split()))

if 0 < K:
    A.sort()
else:
    A.sort(reverse=True)
Y = list(accumulate(A, initial=0))

flag = False

for y in Y:
    if K <= y:
        flag = True
    if flag:
        if y < K:
            print("No")
            exit()
    else:
        if K <= y:
            print("No")
            exit()
print("Yes")
print(*A)
