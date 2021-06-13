#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    c %= 2
    c += 2
    if a**c == b**c:
        print('=')
    elif a**c < b**c:
        print('<')
    else:
        print('>')


if __name__ == "__main__":
    main()
