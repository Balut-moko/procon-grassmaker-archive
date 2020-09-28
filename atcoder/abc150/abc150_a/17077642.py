#!/usr/bin/env python3

def main():
    k, x = map(int, input().split())
    print("Yes" if 500 * k >= x else "No")


if __name__ == "__main__":
    main()
