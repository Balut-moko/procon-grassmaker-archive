#!/usr/bin/env python3

def main():
    a = int(input())
    b = int(input())
    print(min(abs(b - a), 10 + b - a, 10 + a - b))


if __name__ == "__main__":
    main()
