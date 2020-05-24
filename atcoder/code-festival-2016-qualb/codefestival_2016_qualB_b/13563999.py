def resolve():
    N, A, B = map(int, input().split())
    S = input()
    Atmp = 0
    Btmp = 0
    for i in S:
        if i == 'a':
            if Atmp + Btmp < A+B:
                Atmp += 1
                print('Yes')
            else:
                print('No')
        elif i == 'b':
            if Btmp < B and Atmp + Btmp < A+B:
                Btmp += 1
                print('Yes')
            else:
                print('No')
        else:
            print('No')
resolve()
