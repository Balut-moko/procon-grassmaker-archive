#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    ans = 0
    if n == m:
        ans = 0
    elif m == 0:
        ans = 1
    else:
        a_lengths = [a[i + 1] - a[i] - 1 for i in range(m - 1) if a[i + 1] - a[i] - 1 != 0]
        if a[0] != 1:
            a_lengths = [a[0] - 1] + a_lengths
        if a[-1] != n:
            a_lengths = [n - a[-1]] + a_lengths
        k = min(a_lengths)
        for length in a_lengths:
            ans += (length - 1) // k + 1
    print(ans)


if __name__ == "__main__":
    main()
