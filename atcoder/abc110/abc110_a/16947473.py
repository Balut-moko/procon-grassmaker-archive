#!/usr/bin/env python3

def main():
    abc = sorted(input().split())
    print(int(abc[2]) * 10 + int(abc[1]) + int(abc[0]))


if __name__ == "__main__":
    main()
