#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    ans = (100 * (N - M) + M * 1900) * 2**M

    print(int(ans))


if __name__ == "__main__":
    main()
