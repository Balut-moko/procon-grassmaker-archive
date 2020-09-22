#!/usr/bin/env python3

def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    print(n * x - (x - y) * max(n - k, 0))


if __name__ == "__main__":
    main()
