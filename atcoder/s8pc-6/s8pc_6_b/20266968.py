#!/usr/bin/env python3

def main():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    s = A[n // 2]
    g = B[n // 2]
    ans = 0
    for a, b in zip(A, B):
        ans += abs(a - s) + b - a + abs(b - g)
    print(ans)


if __name__ == "__main__":
    main()
