#!/usr/bin/env python3

def main():
    n = int(input())
    print(len(set([int(input()) for i in range(n)])))


if __name__ == "__main__":
    main()
