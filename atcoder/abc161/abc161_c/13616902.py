def resolve():
    N, K = map(int, input().split())
    ans = N-(N//K)*K
    if ans > K/2:
        ans = abs(ans - K)
    print(ans)
resolve()