def resolve():
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    A3 = list(map(int, input().split()))
    N = int(input())
    b = [int(input()) for i in range(N)]
 
    A = A1 + A2 + A3
    checkA = [0]*9
    for i in range(N):
        if b[i] in A:
            checkA[A.index(b[i])] = 1
    if checkA[0] + checkA[1] + checkA[2] == 3:
        print('Yes')
    elif checkA[3] + checkA[4] + checkA[5] == 3:
        print('Yes')
    elif checkA[6] + checkA[7] + checkA[8] == 3:
        print('Yes')
    elif checkA[0] + checkA[3] + checkA[6] == 3:
        print('Yes')
    elif checkA[1] + checkA[4] + checkA[7] == 3:
        print('Yes')
    elif checkA[2] + checkA[5] + checkA[8] == 3:
        print('Yes')
    elif checkA[0] + checkA[4] + checkA[8] == 3:
        print('Yes')
    elif checkA[2] + checkA[4] + checkA[6] == 3:
        print('Yes')
    else:
        print('No')
resolve()