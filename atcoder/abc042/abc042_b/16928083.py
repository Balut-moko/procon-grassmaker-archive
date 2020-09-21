#!/usr/bin/env python3

def main():
    n, l = map(int, input().split())
    s = sorted([input() for i in range(n)])
    print("".join(s))


if __name__ == "__main__":
    main()
