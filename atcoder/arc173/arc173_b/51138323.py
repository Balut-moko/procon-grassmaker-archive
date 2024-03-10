def check(P0, Q0, Q1):
    x1, y1 = P0
    x2, y2 = Q0
    x3, y3 = Q1
    a0 = x2 - x1
    b0 = y2 - y1
    a2 = x3 - x1
    b2 = y3 - y1

    return a0 * b2 - a2 * b0


N = int(input())
XY = [tuple(map(int, input().split())) for _ in [0] * N]
cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        tmp = 0
        for k in range(N):
            if check(XY[k], XY[i], XY[j]) == 0:
                tmp += 1
        cnt = max(cnt, tmp)
ans = N // 3
if cnt // 2 >= ans:
    ans = min(cnt // 2, N - cnt)
print(ans)
