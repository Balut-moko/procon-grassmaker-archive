def resolve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    
    ans = 0
    for i in range(N):
        calc =[0]*M
        for j in range(M):
            calc[j] = A[i][j]*B[j]
        if sum(calc) + C > 0:
            ans += 1
    
    print(ans)
resolve()