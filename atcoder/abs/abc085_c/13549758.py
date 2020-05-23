def resolve():
    import itertools
    
    N, Y = map(int, input().split())
    
    flag = False
    for x in reversed(range(N+1)):
        for y in range(N+1 -x):
            z = N-x-y
            if 10000*x + 5000*y + 1000*z == Y:
                print('{} {} {}'.format(x, y, z))
                flag = True
                break
        if flag:
            break
    else:
        print('-1 -1 -1')
resolve()