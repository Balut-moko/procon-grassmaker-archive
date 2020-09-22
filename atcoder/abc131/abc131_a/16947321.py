#!/usr/bin/env python3

def main():
    a, b, c, d = input()
    print("Bad" if a == b or b == c or c == d else "Good")


if __name__ == "__main__":
    main()
