#!/usr/bin/env python3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(a * d - b * c)


if __name__ == "__main__":
    main()
