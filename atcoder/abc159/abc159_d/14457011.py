#!/usr/bin/env python3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    from collections import Counter

    C = Counter(A)

    sum = 0
    for val in list(C.values()):
        sum += val * (val - 1) // 2

    ans = [None] * N
    for i in range(N):
        p = C[A[i]]
        ans[i] = sum - p * (p - 1) // 2 + (p - 1) * (p - 2) // 2

    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
