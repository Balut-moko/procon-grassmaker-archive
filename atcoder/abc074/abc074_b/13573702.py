def resolve():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))
    
    sum = 0
    for i in range(N):
        if abs(K-x[i]) > x[i]:
            sum += x[i]*2
        else:
            sum += abs(K-x[i])*2
    print(sum)
resolve()
