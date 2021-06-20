#!/usr/bin/env python3

def main():
    n = int(input())
    a, b, c = sorted(map(int, input().split()), reverse=True)
    ans = 10000
    for i in range((n // a) + 1):
        bc = n - a * i
        for j in range((bc // b) + 1):
            tmp = n - a * i - b * j
            if 0 <= tmp and tmp % c == 0:
                ans = min(ans, i + j + tmp // c)
    print(ans)


if __name__ == "__main__":
    main()
