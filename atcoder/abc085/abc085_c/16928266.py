#!/usr/bin/env python3

def main():
    n, y = map(int, input().split())

    for i in range(n + 1):
        for j in range(n + 1):
            if n - i - j >= 0 and 10000 * i + 5000 * j + 1000 * (n - i - j) == y:
                print(i, j, n - i - j)
                exit()
    else:
        print("-1 -1 -1")


if __name__ == "__main__":
    main()
