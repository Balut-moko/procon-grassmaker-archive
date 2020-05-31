def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1
    if 0 in A:
        ans = 0
    else:
        for i in range(N):
            ans = ans * A[i]
            if ans > 10**18:
                ans = -1
                break
    print(ans)
resolve()