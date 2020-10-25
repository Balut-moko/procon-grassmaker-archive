#!/usr/bin/env python3

def main():
    s = sorted(input())
    t = sorted(input(), reverse=True)
    print('Yes' if s < t else 'No')


if __name__ == "__main__":
    main()
