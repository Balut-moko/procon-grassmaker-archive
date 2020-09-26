#!/usr/bin/env python3

def main():
    a, b, c, d = map(int, input().split())
    print('Yes' if a <= c <= b or c <= a <= d else 'No')


if __name__ == "__main__":
    main()
