N = int(input())
H = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(1, N + 1):
        pre = H[i]
        tmp = 0
        for k in range(0, N, j):
            if k < N and i + k < N and pre == H[i + k]:
                tmp += 1
            else:
                break
        ans = max(ans, tmp)

print(ans)
