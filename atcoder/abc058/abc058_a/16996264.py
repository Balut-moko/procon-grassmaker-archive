#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    print("YES" if b - a == c - b else "NO")


if __name__ == "__main__":
    main()
