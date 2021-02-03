#!/usr/bin/env python3

def main():
    n = int(input())
    a = 1
    ans = 0
    if n % 2 == 1:
        print(0)
        return
    while a*10 <= n:
        ans += n // (10 * a)
        a *= 5
    print(ans)


if __name__ == "__main__":
    main()
