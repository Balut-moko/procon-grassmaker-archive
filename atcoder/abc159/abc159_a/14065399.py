def resolve():
    N, M = map(int, input().split())
    ans = 0
    if N == 1 and M == 1:
        pass
    else:
        if N != 0:
            ans += N*(N-1)/2
        if M != 0:
            ans += M*(M-1)/2
    print(int(ans))
resolve()