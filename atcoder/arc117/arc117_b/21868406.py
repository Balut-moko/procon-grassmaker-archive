#!/usr/bin/env python3

def main():
    n = int(input())
    a = sorted(map(int, input().split()))
    a_sa = [a[i + 1] - a[i] + 1 for i in range(n - 1)]
    ans = a[0] + 1
    for i in a_sa:
        ans *= i
        ans %= 10**9 + 7
    print(ans)


if __name__ == "__main__":
    main()
