#!/usr/bin/env python3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = ['No'] * (N - K)
    for i in range(N - K):
        tmp = A[K + i] / A[i]
        if 1 < tmp:
            ans[i] = 'Yes'
    print("\n".join(ans))


if __name__ == "__main__":
    main()
