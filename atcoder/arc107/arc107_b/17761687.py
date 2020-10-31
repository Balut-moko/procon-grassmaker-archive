#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    k = abs(k)
    ans = 0
    for ab in range(2 + k, 2 * n + 1):
        cd = ab - k
        ans += (n - abs(n + 1 - ab)) * (n - abs(n + 1 - cd))

    print(ans)


if __name__ == "__main__":
    main()
