def resolve():
    import itertools
    
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    
    cnt = 0
    for i, j, k in itertools.product(range(A+1), range(B+1), range(C+1)):
        if 500*i + 100*j + 50*k == X:
            cnt += 1
    
    print(cnt)
resolve()