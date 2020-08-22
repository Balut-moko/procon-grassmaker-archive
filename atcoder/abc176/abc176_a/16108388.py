#!/usr/bin/env python3

def main():
    N, X, T = map(int, input().split())
    ans = (N // X) * T + (T if N % X != 0 else 0)
    print(ans)


if __name__ == "__main__":
    main()
