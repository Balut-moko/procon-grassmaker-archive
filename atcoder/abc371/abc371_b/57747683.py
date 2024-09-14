N, M = map(int, input().split())

flag = [False] * N

for _ in range(M):
    A, B = input().split()
    A = int(A) - 1
    if not flag[A] and B == "M":
        print("Yes")
        flag[A] = True
    else:
        print("No")
