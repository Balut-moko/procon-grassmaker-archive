#!/usr/bin/env python3


def main():
    x = int(input())
    n = 0
    i = 1
    while n < x:
        n += i
        i += 1
    print(i - 1)


if __name__ == "__main__":
    main()
