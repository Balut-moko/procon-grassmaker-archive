#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    if a == b:
        ans = c
    elif b == c:
        ans = a
    elif c == a:
        ans = b
    else:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()
