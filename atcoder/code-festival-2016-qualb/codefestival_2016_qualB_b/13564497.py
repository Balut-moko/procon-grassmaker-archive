def resolve():
    N, A, B = map(int, input().split())
    S = input()
    Atmp = 0
    Btmp = 0
    ans = []
    my_append = ans.append
    for i in S:
        if i == 'a':
            if Atmp + Btmp < A+B:
                Atmp += 1
                my_append('Yes')
            else:
                my_append('No')
        elif i == 'b':
            if Btmp < B and Atmp + Btmp < A+B:
                Btmp += 1
                my_append('Yes')
            else:
                my_append('No')
        else:
            my_append('No')
    print("\n".join(ans))
resolve()