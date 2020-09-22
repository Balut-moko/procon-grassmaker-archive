#!/usr/bin/env python3

def main():
    a, b, c, d = input()
    print("Yes" if a == b == c or b == c == d else "No")


if __name__ == "__main__":
    main()
