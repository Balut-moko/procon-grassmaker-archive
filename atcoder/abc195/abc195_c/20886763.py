#!/usr/bin/env python3

def main():
    n = int(input())
    if n <= 999:
        ans = 0
    elif 999 < n <= 999999:
        ans = n - 999
    elif 999999 < n <= 999999999:
        ans = n - 999
        ans += n - 999999
    elif 999999999 < n <= 999999999999:
        ans = n - 999
        ans += n - 999999
        ans += n - 999999999
    elif 999999999999 < n <= 999999999999999:
        ans = n - 999
        ans += n - 999999
        ans += n - 999999999
        ans += n - 999999999999
    else:
        ans = n - 999
        ans += n - 999999
        ans += n - 999999999
        ans += n - 999999999999
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
