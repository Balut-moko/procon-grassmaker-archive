#!/usr/bin/env python3

def main():
    a, b, x = map(int, input().split())
    ans = 'NO'
    if a + b >= x and a <= x:
        ans = 'YES'
    print(ans)


if __name__ == "__main__":
    main()
