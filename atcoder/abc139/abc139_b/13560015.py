def resolve():
    A, B = map(int, input().split())
    useA = 0
    unuse = 1
    while True:
        if unuse >= B:
            print(useA)
            break
        else:
            useA += 1
            unuse += A-1
resolve()