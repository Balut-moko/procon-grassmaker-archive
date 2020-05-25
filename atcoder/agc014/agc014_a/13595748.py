def resolve():
    A, B, C = map(int, input().split())
    cnt = 0
    while True:
        if A%2 == 1 or B%2 == 1 or C%2 == 1:
            break
        elif A==B and B==C:
            cnt = -1
            break
        Atmp = A
        Btmp = B
        Ctmp = C
        A = (Btmp+Ctmp)/2
        B = (Atmp+Ctmp)/2
        C = (Atmp+Btmp)/2
        cnt += 1
    print(cnt)
resolve()
