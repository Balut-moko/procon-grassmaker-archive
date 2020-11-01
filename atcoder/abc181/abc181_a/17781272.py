#!/usr/bin/env python3

def main():
    n = int(input())
    print('White' if not n & 1 else 'Black')


if __name__ == "__main__":
    main()
