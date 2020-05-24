def resolve():
    N = int(input())
    X = list(map(int, input().split()))
    mean = sum(X) / N
    P = round(mean)
    result = 0
    for i in range(N):
        result += (X[i] - P)**2
    print(result)
resolve()