#!/usr/bin/env python3

def main():
    *a, = map(int, input().split())
    print(max(a) - min(a))


if __name__ == "__main__":
    main()
