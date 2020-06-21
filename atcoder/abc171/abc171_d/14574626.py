#!/usr/bin/env python3

def main():
    from collections import Counter

    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    ans = [None] * Q
    Asum = sum(A)
    A_Counter = Counter(A)
    for q in range(Q):
        B, C = map(int, input().split())
        Asum = Asum + (C-B)*A_Counter[B]
        A_Counter[C] += A_Counter[B]
        A_Counter[B] = 0

        ans[q] = Asum

    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
