N, M = map(int, input().split())
S = input()

for L in range(1001):
    tM = 0
    tL = 0
    for i in range(N):
        if S[i] == "0":
            tM, tL = 0, 0
            continue
        if S[i] == "1":
            if tM < M:
                tM += 1
            elif tL < L:
                tL += 1
            else:
                break
            continue
        if S[i] == "2":
            if tL < L:
                tL += 1
            else:
                break
    else:
        print(L)
        exit()
