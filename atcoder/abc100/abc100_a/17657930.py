#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    print('Yay!' if a <= 8 and b <= 8 else ':(')


if __name__ == "__main__":
    main()
