#!/usr/bin/env python3

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    Asum, Bsum = [0], [0]

    for i in range(N):
        Asum.append(Asum[i] + A[i])
    for i in range(M):
        Bsum.append(Bsum[i] + B[i])

    ans, j = 0, M

    for i in range(N + 1):
        if K < Asum[i]:
            break
        while Bsum[j] > K - Asum[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)


if __name__ == "__main__":
    main()
