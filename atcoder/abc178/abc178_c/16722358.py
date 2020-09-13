#!/usr/bin/env python3

def main():
    n = int(input())
    mod = 10**9 + 7
    if n == 1:
        ans = 0
    else:
        ans = 10**n % mod - 9**n % mod - 9**n % mod + 8**n % mod
    print(ans % mod)


if __name__ == "__main__":
    main()
