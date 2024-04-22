def solve(N, M, K):
    if M - K == 1:
        if N >= K - 1:
            return 0
        else:
            return pow(2, N, 10)
    else:
        v = N % (M - K)
        v += ((M - 1) - v) // (M - K) * (M - K)
        if N < M:
            v = N
        return pow(2, v, 10)


T = int(input())
for _ in range(T):
    print(solve(*map(int, input().split())))
