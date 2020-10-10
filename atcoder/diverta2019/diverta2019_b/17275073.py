#!/usr/bin/env python3


def main():
    r, g, b, n = map(int, input().split())
    ans = 0
    for i in range(3001):
        for j in range(3001):
            if n - r * i - g * j >= 0 and (n - r * i - g * j) % b == 0:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
