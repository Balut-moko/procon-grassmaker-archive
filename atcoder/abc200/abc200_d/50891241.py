N = int(input())
A = list(map(int, input().split()))


cnt = min(N, 8)
bk = [[] for _ in range(200)]
for n in range(1, 1 << cnt):
    cur = 0
    B = []
    for i in range(cnt):
        if n & (1 << i):
            B.append(i + 1)
            cur += A[i]
            cur %= 200
    if len(bk[cur]) != 0:
        print("Yes")
        print(len(bk[cur]), *bk[cur])
        print(len(B), *B)
        exit()
    else:
        bk[cur] = B[:]

print("No")
