from collections import defaultdict


def check(p0, p1, q):
    p0x, p0y = p0
    p1x, p1y = p1
    qx, qy = q
    return (p0x - qx) * (p1y - qy) - (p1x - qx) * (p0y - qy)


N, K = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in [0] * N]

if K == 1:
    print("Infinity")
    exit()

di = defaultdict(int)
flag = [[False] * N for _ in [0] * N]
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        flag[i][j] = True
for i in range(N):
    for j in range(i + 1, N):
        if flag[i][j]:
            cnt = 2
            lst = [i, j]

            for k in range(j + 1, N):
                if check(XY[i], XY[j], XY[k]) == 0:
                    cnt += 1
                    lst.append(k)
            for ii in range(cnt):
                for jj in range(cnt):
                    flag[lst[ii]][lst[jj]] = False
            if cnt >= K:
                ans += 1

print(ans)
