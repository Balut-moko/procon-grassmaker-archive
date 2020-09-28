#!/usr/bin/env python3

def main():
    a, d = map(int, input().split())
    print((min(a, d) + 1) * max(a, d))


if __name__ == "__main__":
    main()
