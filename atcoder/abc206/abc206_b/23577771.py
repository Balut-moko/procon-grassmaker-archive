#!/usr/bin/env python3

def main():
    n = int(input())
    tmp = 0
    i = 1
    while tmp < n:
        tmp += i
        i += 1
    print(i - 1)


if __name__ == "__main__":
    main()
