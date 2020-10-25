#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    print('Yes' if a < c < b or b < c < a else 'No')


if __name__ == "__main__":
    main()
