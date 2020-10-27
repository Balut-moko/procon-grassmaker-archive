#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    if a + b == c and a - b == c:
        ans = '?'
    else:
        if a + b == c:
            ans = '+'
        elif a - b == c:
            ans = '-'
        else:
            ans = '!'
    print(ans)


if __name__ == "__main__":
    main()
