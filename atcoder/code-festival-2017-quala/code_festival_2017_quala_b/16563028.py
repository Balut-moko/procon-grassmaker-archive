#!/usr/bin/env python3

def main():
    n, m, k = map(int, input().split())
    ans = 'No'
    for i in range(n + 1):
        for j in range(m + 1):
            if (n - i) * j + (m - j) * i == k:
                ans = 'Yes'
    print(ans)


if __name__ == "__main__":
    main()
