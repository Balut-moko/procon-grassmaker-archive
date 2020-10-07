#!/usr/bin/env python3

def main():
    n, m = map(int, input().split())
    ans = 0
    if 2 * n <= m:
        ans += n
        m -= 2 * n
        ans += m // 4
    else:
        ans += m // 2
    print(ans)


if __name__ == "__main__":
    main()
