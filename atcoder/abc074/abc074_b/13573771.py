def resolve():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))
    
    sum = 0
    for i in range(N):
        if K-x[i] > x[i]:
            sum += x[i]*2
        else:
            sum += (K-x[i])*2
    print(sum)
resolve()
