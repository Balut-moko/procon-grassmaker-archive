#!/usr/bin/env python3

def main():
    x = int(input())
    a, b = (int(input()) for i in range(2))
    print((x - a) % b)


if __name__ == "__main__":
    main()
